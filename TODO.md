# Book Improvement Todo

This file is the active execution list for the book.
Completed migration plans and longer implementation notes live in `archive/`.

## Current Status

- Part 1 has been rewritten into the sari-sari-store arc and the reader-facing docs have been synchronized to that structure.
- Parts 2-4 now use matching chapter filenames, so the on-disk paths follow the visible numbering.
- `mkdocs build` passes.
- `python3 scripts/validate_book.py` passes.
- The remaining work is maintainer-facing cleanup, not chapter-flow rewrites.

## Critical

- [ ] Make `mkdocs build --strict` pass without warnings
  - [ ] Resolve the remaining `without generate PDF` warning from the optional PDF plugin path
  - [ ] Decide whether that warning should be suppressed, documented differently, or isolated from strict builds

## Nice to Have

- [ ] Add a short maintainer release checklist here once the strict-build warnings are resolved
  - [ ] Include the exact required commands
  - [ ] Separate required checks from optional PDF/export checks
