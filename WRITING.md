# Writing guide

How to write posts in Google Docs so they move to the site cleanly, plus a few style habits that make long posts easier to read.

## Workflow

1. Write in Google Docs.
2. Share → General access → **Anyone with the link → Viewer**.
3. From the site folder, run:

   ```
   python3 scripts/import_gdoc.py "<doc link>" --tag Research --description "One sentence on what this post is about."
   ```

4. Preview with `jekyll serve`, then commit and push.
5. Edited the doc later? Re-run the same command with `--force`. The post is regenerated and keeps its description.

The post automatically gets a reading time and a "Read the original" link back to the doc.

## Formatting in Google Docs (so it converts cleanly)

| Do | Avoid |
|---|---|
| Put the title as the first line, styled **Heading 1** or **Heading 2** (or pass `--title`). | A cover page, or the title in a text box. |
| Use **Heading 2/3/4** styles for sections. | Bold normal text pretending to be a heading. |
| Use real bulleted/numbered lists. | Typing "-" or "1." by hand. |
| Insert images inline, then put `Figure 1: …` on the line right below. It becomes a centered caption. | Floating/wrapped images, drawings, or screenshots of text. |
| Use ordinary links. Links to your other Google Doc posts are automatically pointed at the site versions. | Footnotes and comments (they don't export). |
| Keep tables simple: one header row, no merged cells. | Merged cells, colored cells, multi-column layouts. |
| Start optional extras like **Disclaimer:** or **TL;DR:** in bold at the start of a paragraph. | Colored text or highlighting for emphasis (lost on export). |

A byline of "Rohan Pandey" plus the date right under the title is removed automatically. The site shows the date already.

## Style habits for posts

- **Lead with the point.** The first paragraph should tell readers what they'll get and who it's for. It shows up in previews.
- **Write a one-line description.** It appears on the blog index and in link previews. Aim for under ~20 words.
- **Use headings every few screens.** A heading every 300–500 words lets people skim and come back.
- **Keep paragraphs short.** 2–5 sentences. One idea per paragraph reads well on phones.
- **Use lists for steps and parallel items**, and prose for arguments.
- **Make link text descriptive.** "my [literature review process](…)", not "click [here](…)".
- **Caption every figure** with what the reader should notice, not only what it is.
- **Pick one tag** from the existing set (Research, Reflection, Personal) unless a new topic will have several posts. Tags become the filters on the blog page.
- **No need for a table of contents.** The site builds an outline from your headings automatically (any post with 3+ headings), and a Docs table of contents is removed on import. Your Heading 2/3 structure *is* the outline, so name headings so they make sense on their own.
- **End with something:** a takeaway, what's next, or an invitation to reach out.
