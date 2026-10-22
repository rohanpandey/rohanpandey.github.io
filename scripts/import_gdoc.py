#!/usr/bin/env python3
"""Turn a Google Doc into a blog post.

Usage:
  python3 scripts/import_gdoc.py <google-doc-url> --tag Research
  python3 scripts/import_gdoc.py <url> --tag Personal --title "My title" --date 2026-11-02 --slug my-title

The doc must be shared as "Anyone with the link can view".
Re-running with --force updates an existing post (handy after editing the doc).
"""
import argparse
import base64
import datetime as dt
import glob
import os
import re
import sys
import urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def doc_id(url):
    m = re.search(r"/document/d/([A-Za-z0-9_-]+)", url) or re.fullmatch(r"([A-Za-z0-9_-]{20,})", url)
    if not m:
        sys.exit(f"Couldn't find a Google Doc ID in: {url}")
    return m.group(1)


def fetch_markdown(did):
    url = f"https://docs.google.com/document/d/{did}/export?format=md"
    with urllib.request.urlopen(url) as r:
        body = r.read().decode("utf-8")
        if "markdown" not in r.headers.get("Content-Type", ""):
            sys.exit("Google didn't return Markdown. Is the doc shared as 'Anyone with the link can view'?")
    return body


def slugify(text):
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")


def existing_posts():
    """Map Google Doc ID -> post slug, from `original:` in existing posts."""
    out = {}
    for p in glob.glob(os.path.join(ROOT, "_posts", "*.md")):
        m = re.search(r"^original:\s*\S*/document/d/([A-Za-z0-9_-]+)", open(p, encoding="utf-8").read(), re.M)
        if m:
            out[m.group(1)] = re.sub(r"^\d{4}-\d{2}-\d{2}-", "", os.path.basename(p)[:-3])
    return out


def convert(md, slug, title):
    # 1. Embedded images -> files in images/blog/<slug>/
    imgs = {m.group(1): (m.group(2), m.group(3)) for m in
            re.finditer(r"^\[(image\d+)\]: <data:image/(\w+);base64,([^>]+)>", md, re.M)}
    md = re.sub(r"^\[image\d+\]: <data:image/[^>]+>\s*$", "", md, flags=re.M)
    if imgs:
        os.makedirs(os.path.join(ROOT, "images", "blog", slug), exist_ok=True)
    for name, (ext, data) in imgs.items():
        n = name.replace("image", "")
        rel = f"/images/blog/{slug}/fig{n}.{ext}"
        with open(ROOT + rel, "wb") as f:
            f.write(base64.b64decode(data))
        md = md.replace(f"![][{name}]", f"![Figure {n}]({{{{ '{rel}' | relative_url }}}})")

    # 2. Drop a title heading + "Rohan Pandey / <date>" byline at the top
    md = md.lstrip()
    first = re.match(r"#{1,3} (.*)\n", md)
    if first and slugify(first.group(1).replace("*", "")) == slugify(title):
        md = md[first.end():].lstrip()
    md = re.sub(r"\ARohan Pandey\s*\n[^\n]*\d{4}[^\n]*\n+", "", md)

    # 3. Headings: no bold, no trailing colon; doc title "#" becomes "##"
    def clean_heading(m):
        level, h = m.group(1), m.group(2).replace("**", "").strip()
        attr = ""
        am = re.search(r"\s*(\{#[^}]*\})\s*$", h)
        if am:
            attr, h = am.group(1), h[:am.start()].strip()
        level = "##" if level == "#" else level
        return f"{level} {h.rstrip(':').strip()}" + (f" {attr}" if attr else "")
    md = re.sub(r"^(#{1,6})\s+(.*)$", clean_heading, md, flags=re.M)

    # 4. Google's heading ids contain characters Markdown can't handle; simplify them (and TOC links)
    for old in set(re.findall(r"\{#([^}]*)\}", md)):
        new = slugify(old)
        md = md.replace("{#" + old + "}", "{#" + new + "}").replace("(#" + old + ")", "(#" + new + ")")

    # 5. Links to other docs that are already posts -> link to the post
    for did, other in existing_posts().items():
        md = re.sub(r"https://docs\.google\.com/document/d/" + re.escape(did) + r"[^)\s]*",
                    "{{ '/blog/" + other + "/' | relative_url }}", md)

    # 6. Drop a Docs table of contents (lines that are only a link to a heading); the site builds its own outline
    md = re.sub(r"^\[[^\]]*\]\(#[^)]*\)\s*\n", "", md, flags=re.M)

    # 7. "Figure N: ..." lines become captions
    md = re.sub(r"^(\*{0,3}Figure \d+[:.].*?)\s*$", r"\1\n{: .caption}", md, flags=re.M)

    return re.sub(r"\n{3,}", "\n\n", md).strip() + "\n"


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("url")
    ap.add_argument("--tag", required=True, help="Research, Reflection, Personal, ...")
    ap.add_argument("--title", help="defaults to the first heading in the doc")
    ap.add_argument("--date", default=dt.date.today().isoformat(), help="YYYY-MM-DD (default: today)")
    ap.add_argument("--slug", help="URL name, e.g. phd-year-2 (default: from the title)")
    ap.add_argument("--description", default="", help="one-line summary shown on the blog index")
    ap.add_argument("--force", action="store_true", help="overwrite an existing post with the same slug")
    a = ap.parse_args()

    did = doc_id(a.url)
    md = fetch_markdown(did)

    title = a.title
    if not title:
        m = re.match(r"\s*#{1,3} (.*)\n", md)
        if not m:
            sys.exit("The doc doesn't start with a heading. Pass --title \"...\".")
        title = m.group(1).replace("*", "").strip()
    slug = a.slug or slugify(title)[:60].strip("-")

    clash = [p for p in glob.glob(os.path.join(ROOT, "_posts", f"*-{slug}.md"))]
    if clash and not a.force:
        sys.exit(f"{os.path.relpath(clash[0], ROOT)} already exists. Use --force to update it.")
    description = a.description
    for p in clash:
        old = re.search(r'^description: "(.*)"$', open(p, encoding="utf-8").read(), re.M)
        if old and not description:
            description = old.group(1).replace('\\"', '"')  # keep the summary you already wrote
        os.remove(p)

    body = convert(md, slug, title)
    esc = lambda s: s.replace('"', '\\"')
    front = (f'---\nlayout: post\ntitle: "{esc(title)}"\ndate: {a.date}\ntag: {a.tag}\n'
             f'description: "{esc(description)}"\n'
             f"original: https://docs.google.com/document/d/{did}/edit\n---\n\n")
    path = os.path.join(ROOT, "_posts", f"{a.date}-{slug}.md")
    with open(path, "w", encoding="utf-8") as f:
        f.write(front + body)
    print(f"Wrote {os.path.relpath(path, ROOT)}  ->  /blog/{slug}/")
    if not description:
        print("Tip: add a one-line `description:` to the front matter for the blog index.")


if __name__ == "__main__":
    main()
