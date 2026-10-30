# Rexy 360 wiki

Source for the Rexy 360 pages on the Miraheze wiki, written in MediaWiki wikitext.

- `pages/*.wiki` — one file per page.
- `pages.json` — maps each file to its page title on the wiki.
- `upload.py` — creates or updates every page through the wiki's API (see the top of the file for the bot-password setup).

Edit the files here and run `python3 wiki/upload.py` to publish; `--dry-run` lists what would be uploaded.
