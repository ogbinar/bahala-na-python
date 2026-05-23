# Book Improvement Todo

This file is the active execution list for the book.
Treat the longer review/report files as historical reference unless this file says otherwise.

Priority buckets:
- `Critical` items should be fixed before any release or broader polish.
- `Pareto` items are the highest-leverage improvements after the critical fixes.
- `Nice to Have` items improve polish and consistency, but should not block shipping.

## Critical

- [ ] Fix all broken or non-runnable code examples in the main book
  - [ ] Repair the Discord bot example in `docs/part-3-going-further/chapter-15-discord-bots.md`
    - [x] Remove the leading indentation before `intents = ...`
    - [x] Verify the code matches the installed Discord library API
    - [x] Make sure the install command and example code are aligned
  - [ ] Repair the NLP chatbot indentation bug in `docs/part-3-going-further/chapter-17-nlp.md`
    - [x] Fix the indentation mismatch around `negative_words`
    - [x] Rebuild the chapter to confirm it renders cleanly
  - [ ] Audit remaining code fences for syntax/runtime errors
    - [ ] Check all tutorial code in the book, especially examples that readers are likely to copy
    - [ ] Prioritize chapters with external dependencies, async code, or stateful sample logic
    - [ ] Fix any code blocks that do not parse or run as written

- [x] Fix the packaging/build contract so a clean install works
  - [x] Support `pip install .` as the canonical setup path
  - [x] Add the MkDocs plugins used by `mkdocs.yml` to the main dependencies in `pyproject.toml`
    - [x] Include `mkdocs-macros-plugin` in the main dependency list
    - [x] Keep `mkdocs-with-pdf` available for normal docs builds, even if PDF export stays optional
  - [x] Keep `pyproject.toml` and `requirements.txt` aligned on purpose
    - [x] Remove accidental dependency drift between the two files
    - [x] Document any intentional difference clearly
  - [x] Verify that `pip install . && mkdocs build` succeeds in a clean environment

- [x] Harden CI so broken docs or packaging issues fail early
  - [x] Add a clean-environment `pip install .` validation step
  - [x] Add a strict docs build gate
    - [x] Decide whether strict mode should be required in CI or only in a separate job
    - [x] Ensure warnings that matter become visible before merge
  - [x] Fix or isolate the PDF export path
    - [x] Make `ENABLE_PDF_EXPORT=1 mkdocs build --strict` pass cleanly, or move PDF generation to a separate non-strict job
    - [x] Keep PDF-only failures from blocking the main docs build
  - [x] Add a validation pass for chapter code fences
    - [x] Compile or execute code blocks where feasible
    - [x] At minimum, detect syntax errors in Python snippets
  - [x] Keep the current docs build, but do not rely on it alone

- [x] Fix onboarding friction for first-time readers
  - [x] Keep the README clone/setup instructions correct
    - [x] Verify the repository URL matches the actual repo
    - [x] Verify the clone directory name matches the cloned repo
  - [x] Keep the top-level source-code CTA functional
    - [x] Confirm the GitHub badge link points to the correct repo
  - [x] Make the first five minutes of setup frictionless
    - [x] Ensure a reader can go from README to `mkdocs serve` without guessing

- [x] Fix sample logic that recomputes state after the decision is already made
  - [x] Repair the Palengke Price Comparator sample in `docs/appendix/answers.md`
    - [x] Stop recomputing random prices after `compare_prices(...)` has already selected the best source
    - [x] Make the alert decision use the same state that was compared
    - [x] Keep the sample deterministic or clearly controlled where possible

## Pareto

- [x] Add a lightweight validation layer for the book itself
  - [x] Create a markdown/code-fence validation script
    - [x] Detect broken Python syntax in fenced code blocks
    - [ ] Optionally run a subset of examples that are meant to be executable
  - [x] Add link checking for internal and external references
  - [x] Run the validator before publishing or merging

- [x] Reduce planning noise by consolidating historical review docs
  - [x] Keep this file as the single active task list
  - [x] Move `REVISION-PLAN.md`, `PARETO-PLAN.md`, `PARETO-POLISH-PLAN.md`, `COMPLETENESS-REPORT.md`, and `IMPLEMENTATION-REPORT.md` into `archive/`
  - [x] Remove duplicated guidance from the historical docs instead of letting them compete with this file

- [x] Keep the author identity consistent with the ogbinar profile site
  - [x] Use `ogbinar.github.io` as the source of truth for author identity and bio
  - [x] Keep the book voice accessible, but treat `Smart Kuya` as delivery style only
  - [x] Avoid introducing new anecdotes that create a separate persona
  - [x] Keep chapter interview prompts learner-facing, not author-facing
  - [x] Review guidance docs and remaining chapter prompt phrasing against the profile-site identity rule

- [x] Standardize chapter structure and chapter-level prompts
  - [x] Keep the repeated pattern consistent across chapters:
    - [x] Story hook
    - [x] Output cue near the opening
    - [x] What You'll Learn
    - [x] Tutorial sections
    - [x] Reflection / summary
    - [x] Portfolio / interview prompt
  - [x] Make portfolio/interview prompts explicitly learner-facing
    - [x] Prefer wording such as `You can write`, `You can post`, `You can say`, or `Example talking point`
    - [x] Avoid first-person phrasing that sounds like the author claiming the project
  - [x] Keep reflections short and actionable

- [x] Sync the guidance docs so future edits do not drift
  - [x] Keep `STYLE-GUIDE.md` aligned with the current author voice rule
  - [x] Keep `CONTRIBUTING.md` aligned with the current tone and identity rule
  - [x] Keep `DESIGN.md` aligned with the current visual and storytelling direction
  - [x] Keep `AGENT-BEST-PRACTICES.md` aligned with the current book direction
  - [x] Keep `docs/index-alphabetical.md` aligned with the same voice terminology

- [x] Broaden and vary the recurring motifs without losing Filipino context
  - [x] Keep the Filipino grounding
    - [x] Retain familiar references like sari-sari stores, jeepneys, GCash, OFW, and barangays
  - [x] Avoid overusing any one origin story or anecdotal motif
    - [x] Prefer broader low-resource or shared-setup framing when discussing the author story
    - [x] Keep the examples lived-in, not repetitive
  - [x] Make sure the motifs support learning rather than distracting from it
  - [x] Files changed: `docs/part-0-welcome/chapter-01-hello-world.md`, `docs/part-1-fundamentals/chapter-05-loops.md`, `docs/part-1-fundamentals/chapter-07-files.md`, `docs/part-3-going-further/chapter-16-dataviz.md`, `docs/part-3-going-further/chapter-20-boss-fight-3.md`, `docs/part-4-capstone/chapter-22-bayanihan.md`, `docs/part-4-capstone/chapter-23-capstone-a.md`, `docs/part-4-capstone/chapter-25-final-boss.md`
  - [x] Verification: manual review of edited prose sections, targeted motif search with `rg`, and `git diff --check`

- [x] Clean up prose where the teaching is correct but the flow could be tighter
  - [x] Trim repetitive phrasing in intros and reflections
  - [x] Keep examples vivid, but not overlong
  - [x] Tighten places where the same idea is explained multiple times in slightly different words
  - [x] Files changed: `docs/part-0-welcome/chapter-01-hello-world.md`, `docs/part-1-fundamentals/chapter-05-loops.md`, `docs/part-1-fundamentals/chapter-07-files.md`, `docs/part-3-going-further/chapter-16-dataviz.md`, `docs/part-3-going-further/chapter-20-boss-fight-3.md`, `docs/part-4-capstone/chapter-22-bayanihan.md`, `docs/part-4-capstone/chapter-23-capstone-a.md`, `docs/part-4-capstone/chapter-25-final-boss.md`
  - [x] Verification: manual review for unchanged teaching content and `git diff --check`

## Nice to Have

- [x] Improve the reader-facing polish of reflection and portfolio sections
  - [x] Make portfolio prompts more actionable
  - [x] Give the reader better guidance on how to present the project in GitHub or interviews
  - [x] Keep the prompts realistic and beginner-friendly
  - [x] Applied in the same chapter-file pass listed above

- [ ] Add more explicit low-resource and mobile-first guidance
  - [ ] Highlight phone-friendly alternatives where useful
  - [ ] Keep the low-resource setup advice visible in early chapters
  - [ ] Add small notes that help readers with limited hardware or limited data

- [x] Vary the Filipino examples where repetition starts to feel heavy
  - [x] Keep the core examples, but add a few alternate analogies where it helps
  - [x] Make sure the same context does not appear in back-to-back explanations too often
  - [x] Applied in the same chapter-file pass listed above

- [ ] Add optional quality-of-life checks for maintainers
  - [ ] Add a single command to validate docs, links, and chapter code snippets locally
  - [ ] Add a quick release checklist for maintainers
  - [ ] Add a short note explaining which checks are required vs optional

## Suggested Execution Order

1. Fix the confirmed code and packaging issues.
2. Harden CI and the validation layer.
3. Consolidate the historical planning docs into one active source of truth.
4. Standardize chapter prompts and identity rules.
5. Clean up recurring motifs and prose repetition.
6. Polish the nice-to-have reader experience items.

## Exit Criteria

- [ ] All critical code examples parse and run as written
- [ ] A clean install/build path works from the published metadata
- [ ] CI catches packaging, docs, and code-fence regressions early
- [ ] The author identity stays consistent with the ogbinar profile site
- [ ] The teaching voice remains accessible and beginner-friendly
- [ ] The book still feels distinctly Filipino without leaning on one repeated anecdotal motif
