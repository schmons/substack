# Substack: ideas & research

Every article lives in its own folder under `articles/`. Ideas that aren't ready for a folder go in `ideas.md`.

## Structure

```
.
├── README.md            # this file
├── ideas.md             # backlog of rough ideas (one line each)
├── new-article.sh       # creates a new article folder from the template
├── requirements.txt     # Python packages for the visualisation scripts
├── _template/           # copied for every new article — don't write in it
└── articles/
    └── YYYY-MM-short-slug/
        ├── draft.md                 # the article itself (status in the header)
        ├── research-summary.md      # everything we've learned, in one place
        └── assets/
            ├── sources.csv          # every link + summary of its content
            ├── data/
            │   ├── raw/             # data exactly as collected (never edited)
            │   ├── processed/       # cleaned data, made from raw/ by scripts
            │   └── README.md        # where each dataset came from
            ├── scripts/             # visualisation & analysis scripts
            ├── figures/             # charts produced by scripts/
            └── images/              # other images (screenshots, photos, cover)
```

## Starting a new article

```bash
./new-article.sh my-article-slug
```

This creates `articles/YYYY-MM-my-article-slug/` from `_template/`.

## Conventions

- **Folder names:** `YYYY-MM-short-slug` (month the folder was created), lowercase, hyphens.
- **Status:** set in the header of `draft.md`: `idea` → `researching` → `drafting` → `editing` → `published`.
- **Sources:** every link we read goes in `sources.csv`, even ones we end up not using.
- **Data:** never edit files in `data/raw/`. Cleaning happens in a script that writes to `data/processed/`.
- **Figures:** produced by scripts, so they can be regenerated. Don't hand-edit them.
- **Research summary:** the single source of truth for what we know. If it's not there, we don't know it.

## Scripts

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python articles/<folder>/assets/scripts/plot.py
```
