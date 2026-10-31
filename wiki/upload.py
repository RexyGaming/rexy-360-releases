#!/usr/bin/env python3
"""Upload the Rexy 360 wiki pages to a MediaWiki wiki (e.g. Miraheze).

Pages live in wiki/pages/*.wiki; wiki/pages.json maps each file to its page title.

Needs a bot password (Special:BotPasswords on the wiki, with the
"Edit existing pages" and "Create, edit, and move pages" grants), passed as:

  MIRAHEZE_WIKI          the wiki's host, e.g. rexy360.miraheze.org
  MIRAHEZE_BOT_USER      the bot login, e.g. RobPortazier@wiki-upload
  MIRAHEZE_BOT_PASSWORD  the bot password

Any of these not set in the environment are read from ~/.config/rexy360-wiki.env
(KEY=value lines), so they stay on your computer and out of the repository.

Usage: python3 wiki/upload.py [--dry-run] [file.wiki ...]
"""
import http.cookiejar
import json
import os
import sys
import urllib.parse
import urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
SUMMARY = "Rexy 360 documentation (from rexy-360-releases/wiki)"
ENV_FILE = os.path.expanduser("~/.config/rexy360-wiki.env")


def load_env_file():
    if not os.path.exists(ENV_FILE):
        return
    with open(ENV_FILE, encoding="utf-8") as f:
        for line in f:
            key, sep, value = line.strip().partition("=")
            if sep and not key.startswith("#"):
                os.environ.setdefault(key.strip(), value.strip().strip("'\""))


def main():
    args = sys.argv[1:]
    dry_run = "--dry-run" in args
    only = [a for a in args if a != "--dry-run"]

    with open(os.path.join(HERE, "pages.json"), encoding="utf-8") as f:
        pages = json.load(f)
    if only:
        pages = {k: v for k, v in pages.items() if k in only}

    if dry_run:
        for name, title in pages.items():
            print(f"would upload {name} -> {title}")
        return

    load_env_file()
    host =os.environ["MIRAHEZE_WIKI"].removeprefix("https://").strip("/")
    api = f"https://{host}/w/api.php"
    opener = urllib.request.build_opener(
        urllib.request.HTTPCookieProcessor(http.cookiejar.CookieJar()))

    def call(params, post=False):
        params = {**params, "format": "json", "formatversion": "2"}
        data = urllib.parse.urlencode(params).encode()
        req = (urllib.request.Request(api, data=data) if post
               else urllib.request.Request(f"{api}?{data.decode()}"))
        req.add_header("User-Agent", "rexy-360-wiki-upload/1.0 (rob@realprogear.com)")
        with opener.open(req) as r:
            result = json.load(r)
        if "error" in result:
            raise SystemExit(f"API error: {result['error']}")
        return result

    login_token = call({"action": "query", "meta": "tokens", "type": "login"})["query"]["tokens"]["logintoken"]
    login = call({"action": "login", "lgname": os.environ["MIRAHEZE_BOT_USER"],
                  "lgpassword": os.environ["MIRAHEZE_BOT_PASSWORD"], "lgtoken": login_token}, post=True)
    if login["login"]["result"] != "Success":
        raise SystemExit(f"Login failed: {login['login']}")
    csrf = call({"action": "query", "meta": "tokens"})["query"]["tokens"]["csrftoken"]

    for name, title in pages.items():
        with open(os.path.join(HERE, "pages", name), encoding="utf-8") as f:
            text = f.read()
        result = call({"action": "edit", "title": title, "text": text, "summary": SUMMARY,
                       "bot": "1", "token": csrf}, post=True)["edit"]
        state = "unchanged" if result.get("nochange") else ("created" if result.get("new") else "updated")
        print(f"{state}: {title}")


if __name__ == "__main__":
    main()
