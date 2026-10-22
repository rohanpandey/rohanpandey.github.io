# rohanpandey.github.io

Personal site, built with Jekyll and published automatically by GitHub Pages on every push to `main`.

## Updating the homepage

Most homepage content lives in small YAML lists in `_data/`. Add an entry to the top and push:

- `_data/publications.yml`: papers, with links and BibTeX

## Writing a new blog post

Write in Google Docs, then import it:

```
python3 scripts/import_gdoc.py "<google doc link>" --tag Research --description "One-line summary."
```

See [WRITING.md](WRITING.md) for the full workflow, formatting tips, and style guidelines.

To write a post directly in Markdown instead, create `_posts/YYYY-MM-DD-short-slug.md` starting with:

```
---
layout: post
title: "Your title here"
date: 2026-11-02
tag: Reflection
description: "One-line summary."
---
```

## Previewing locally

```
/opt/homebrew/lib/ruby/gems/4.0.0/bin/jekyll serve
```

Then open http://localhost:4000.
