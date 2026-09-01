# mtyrolski.github.io

Source for [mtyrolski.github.io](https://mtyrolski.github.io), Michał Tyrolski's academic website.

## Content model

Publication metadata lives in `_publications/`. Both the homepage and the research archive render those records through `_includes/publication-card.html`; author lists and venue labels should be updated there rather than duplicated in page copy.

The homepage is `_pages/about.md`. Shared homepage and publication-list styles live in `_sass/layout/_home.scss`.

The only intentionally public file in `files/` is `cv.pdf`.

## Local build

```bash
bundle install
bundle exec jekyll serve
```

Or run it with Docker:

```bash
docker compose up --build
```

Then open <http://localhost:4000>. Use `Ctrl+C` to stop the foreground container.

The production build is compatible with GitHub Pages. `jekyll-sitemap` supplies the machine-readable sitemap; the site has no blog, public teaching/talk collections, or comments.
