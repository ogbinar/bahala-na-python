# PDF Quality Improvement Plan

**Status:** Draft — ready for implementation
**Date:** 2026-05-15
**Source:** PDF audit (15 recommendations)

---

## Overview

The PDF currently reads like "a website printed into a PDF" instead of "a professionally designed programming learning book." This plan converts it into a **Filipino Learning Operating System for Programming** — optimizing for emotional safety, momentum, identity, practical action, self-belief, community, and low-resource resilience.

---

## Phase 1: PDF CSS Overhaul (Highest ROI)

### P1.1: Code Block Readability
**Impact:** Critical — single most important thing for a programming book

**Problem:**
- Code wraps awkwardly
- Indentation sometimes collapses
- Long lines become hard to follow
- Code visually blends into text

**Fix:** Update `docs/overrides/assets/stylesheets/pdf.css`
- `font-size: 9pt` for code blocks
- `line-height: 1.45`
- `white-space: pre-wrap` with `overflow-wrap: break-word`
- `border-radius: 8px`
- `page-break-inside: avoid` on `.highlight` wrapper
- More padding around code blocks (visual rest)

### P1.2: Bullet List Fix
**Impact:** Critical — currently rendering as detached bullets

**Problem:** Bullets render as `• • •` detached from content

**Fix:** Update `pdf.css`
- `ul, ol`: `margin-left: 1.4rem`, `padding-left: 1rem`
- `li`: `margin-bottom: 0.35rem`, `line-height: 1.45`
- `li p`: `margin: 0`

### P1.3: Table Styling
**Impact:** High — tables flatten awkwardly

**Fix:** Update `pdf.css`
- `table`: `font-size: 9pt`, proper margins
- `th`: `background: #f5f5f5`, `font-weight: bold`
- `tr:nth-child(even)`: `background: #fafafa`
- `page-break-inside: avoid`

### P1.4: Footer Noise Reduction
**Impact:** High — current footer repeats "Copyright © 2026 Myk Ogbinar - 35/233 -" on every page

**Fix:** Update `mkdocs.yml` with-pdf config
- Remove `copyright` key (or set to empty)
- Keep page numbers only
- Add copyright to front matter only (cover page)
- Consider section title in footer for long chapters

### P1.5: Admonition Visual Hierarchy
**Impact:** High — Smart Kuya elements blend together

**Fix:** Update `pdf.css` with distinct left-border colors per admonition type:
- `tip` (Diskarte): `border-left: 5px solid #ff7043` (orange)
- `warning` (Boss Fight/Common Mistake): `border-left: 5px solid #d32f2f` (red)
- `success` (Level Up): `border-left: 5px solid #388e3c` (green)
- `note` (Portfolio Tip): `border-left: 5px solid #1976d2` (blue)
- `side-quest` (Side Quest): `border-left: 5px solid #7b1fa2` (purple)
- `badge` (Achievement): `border-left: 5px solid #ffd700` (gold)

### P1.6: Breathing Room
**Impact:** Medium — current PDF is dense

**Fix:** Update `pdf.css`
- More `margin-bottom` on headings
- More whitespace between sections
- `page-break-before: always` on chapter headings (h1)
- `page-break-inside: avoid` on code blocks, admonitions, tables
- Wider margins around code blocks

---

## Phase 2: Chapter Opener Cards

### P2.1: Standard Chapter Opener Template
**Impact:** High — chapters start abruptly

**What to add at the top of each chapter, after the Story Hook and before "What You'll Learn":**

```markdown
> **Difficulty:** ⭐ Beginner
> **Estimated Time:** 45 minutes
> **XP Reward:** +100 XP
```

Each chapter gets a difficulty/time/XP card matching its level:

| Part | Chapters | Difficulty | XP |
|------|----------|------------|-----|
| Part 0 (Welcome) | 1-2 | ⭐ | +25 XP |
| Part 1 (Fundamentals) | 3-8 | ⭐⭐ | +100 XP (chapters), +500 XP (boss) |
| Part 2 (Building Things) | 9-14 | ⭐⭐⭐ | +100 XP (chapters), +500 XP (boss) |
| Part 3 (Going Further) | 15-20 | ⭐⭐⭐⭐ | +150 XP (chapters), +500 XP (boss) |
| Part 4 (Capstone) | 21-26 | ⭐⭐⭐⭐⭐ | +200 XP (chapters), +1000 XP (final boss) |

**Files to modify:** All 26 chapter files in `docs/part-*/chapter-*.md`

**Approach:** Add a standardized `??? tip "Chapter Info"` block after the story hook.

---

## Phase 3: Study Companion Features

### P3.1: Chapter Reflection Sections
**Impact:** High — massively improves retention

**Add at the end of each chapter:**

```markdown
## 🧠 Reflection

- What confused me?
- What clicked today?
- What can I build with this?
```

**Files to modify:** All 26 chapter files (append to end)

### P3.2: Pause and Predict Prompts
**Impact:** High — increases active learning

**Add inline throughout chapters at key moments:**

```markdown
??? question "Pause and Predict"
    Before running this code, what do you think happens?
    
    ```python
    x = "10"
    print(x + 5)
    ```
    
    Write your prediction before scrolling down.
```

**Files to modify:** Key chapters (3, 4, 5, 6, 9, 10, 13) — where type confusion, control flow, or common bugs occur

### P3.3: Checklists
**Impact:** Medium — helps low-resource learners track progress

**Add at end of each chapter:**

```markdown
## ✅ Checklist

- [ ] I can define a variable
- [ ] I understand the difference between `int` and `str`
- [ ] I can create a list and a dictionary
- [ ] I ran the sari-sari store inventory program
```

**Files to modify:** All 26 chapter files (append before Reflection)

---

## Phase 4: Low-Resource Learner UX (Unique Differentiator)

### P4.1: "If You Only Have a Phone" Sections
**Impact:** High — huge differentiator globally

**Add to chapters with heavy IDE dependency:**
- Ch 1 (Hello World): Use Replit.com / Google Colab as alternatives
- Ch 7 (Files): Use phone-friendly editors
- Ch 11 (APIs): Use Postman mobile or online API testers
- Ch 15 (Discord Bots): Deploy to free hosting instead of local

**Format:**
```markdown
??? phone "If You Only Have a Phone"
    You don't need a laptop to learn Python. Here's how...
```

### P4.2: "If You Have Slow Internet" Sections
**Impact:** Medium — relevant for many Filipino learners

**Add to chapters that require pip install or large downloads:**
- Ch 11 (APIs): "You can read about APIs without installing anything"
- Ch 15 (Discord Bots): "Install once, use offline"
- Ch 16 (Data Viz): "Download datasets once, reuse"
- Ch 17 (NLP): "Use pre-downloaded models"

### P4.3: "If You Have a 4GB Laptop" Sections
**Impact:** Medium — many comshop setups

**Add to heavy chapters:**
- Ch 15-20: Memory-conscious alternatives
- Ch 16: Lightweight plotting alternatives
- Ch 17: Small models vs. large models

---

## Phase 5: Portfolio Mode Expansion

### P5.1: Portfolio Upgrade at End of Each Chapter
**Impact:** High — extremely differentiated

Already started in 10 chapters (R3). **Expand to ALL 26 chapters.**

**Template:**
```markdown
## 💼 Portfolio Upgrade

**GitHub Project:** Name this file `sarisari_inventory.py` and push to GitHub with a README explaining what it does.

**Resume Bullet:** "Built an inventory management system in Python using dictionaries and file I/O."

**LinkedIn Post:** "Just learned Python variables and built my first real program — a sari-sari store inventory tracker!"

**Interview Talking Point:** "I started learning Python by building tools that solve problems I see in my community..."
```

**Files already done:** Ch 3, 4, 6, 7, 9, 11, 12, 16, 23, 24
**Files to add:** Ch 1, 2, 5, 8, 10, 13, 14, 15, 17, 18, 19, 20, 21, 22, 25, 26

---

## Phase 6: Visual Polish

### P6.1: Improved TOC with Part Descriptions and Pacing
**Impact:** Medium — helps navigation

**Add to `docs/index.md`:**
- Emoji/icons per part
- Part descriptions (1-2 sentences)
- Recommended pacing timeline
  - Part 1: 1-2 weeks
  - Part 2: 2-4 weeks
  - Part 3: advanced, self-paced
  - Part 4: capstone, 1-2 weeks

### P6.2: Roadmap Visual / Skill Tree
**Impact:** Medium — readers need "where am I?"

**Add to `docs/index.md` or a dedicated `docs/roadmap.md`:**
- Mermaid diagram showing chapter progression
- XP milestones per part
- "You are here" markers per part index page

### P6.3: QR Codes / Links for Static PDF
**Impact:** Medium — useful for mobile-first learners

**Add to chapter footers or a dedicated section:**
- Links to GitHub repo for code
- Links to DEP Discord for help
- Links to datasets for data chapters
- Links to video tutorials (if available)

**Format:** Inline links in PDF (WeasyPrint supports href)

---

## Phase 7: Filipino Visual Identity

### P7.1: Warm Palette in PDF
**Impact:** Medium — "study notebook" vibes

**Already done:** Custom CSS has warm palette
**To improve in pdf.css:**
- Warm heading colors instead of default blue
- Orange accent for chapter numbers
- Subtle background tints for code blocks (warm gray instead of white)
- "Chaotic cozy tech" feel without being cringe

### P7.2: XP Cards and Game UI Motifs
**Impact:** Medium — reinforces gaming framing

**In pdf.css:**
- XP reward boxes with game-card styling
- Progress bar styling for "What You'll Learn" completion
- Badge styling for achievement blocks

---

## Implementation Order (ROI Priority)

| Priority | Phase | Effort | Impact |
|----------|-------|--------|--------|
| 1 | P1.1 Code Block Readability | 15 min | Critical |
| 2 | P1.2 Bullet List Fix | 10 min | Critical |
| 3 | P1.3 Table Styling | 10 min | High |
| 4 | P1.4 Footer Noise | 5 min | High |
| 5 | P1.5 Admonition Hierarchy | 20 min | High |
| 6 | P1.6 Breathing Room | 15 min | Medium |
| 7 | P2.1 Chapter Opener Cards | 2 hours (26 files) | High |
| 8 | P3.1 Reflection Sections | 1 hour (26 files) | High |
| 9 | P3.2 Pause and Predict | 2 hours (7 files) | High |
| 10 | P3.3 Checklists | 1.5 hours (26 files) | Medium |
| 11 | P4.1 Phone-Only Sections | 1 hour (4 files) | High |
| 12 | P4.2 Slow Internet | 30 min (4 files) | Medium |
| 13 | P4.3 4GB Laptop | 30 min (3 files) | Medium |
| 14 | P5.1 Portfolio Mode Expansion | 2 hours (16 files) | High |
| 15 | P6.1 TOC Improvement | 30 min | Medium |
| 16 | P6.2 Roadmap Visual | 30 min | Medium |
| 17 | P6.3 QR Codes / Links | 30 min | Medium |
| 18 | P7.1 Warm Palette PDF | 20 min | Medium |
| 19 | P7.2 XP Cards PDF | 20 min | Medium |

**Total estimated effort:** ~15 hours

---

## Files Affected

### CSS (Phase 1, 7)
- `docs/overrides/assets/stylesheets/pdf.css` — major overhaul
- `docs/overrides/assets/stylesheets/custom.css` — minor print additions

### Config
- `mkdocs.yml` — with-pdf footer config, optional new nav entries

### Chapter Files (Phases 2-5)
- All 26 chapter files: `docs/part-*/chapter-*.md`
- Priority files for Pause/Predict: Ch 3, 4, 5, 6, 9, 10, 13
- Priority files for Low-Resource: Ch 1, 7, 11, 15, 16, 17

### Navigation (Phase 6)
- `docs/index.md` — TOC improvements, roadmap
- Optional: `docs/roadmap.md` — dedicated skill tree page

---

## Verification

After implementation:
1. Run `mkdocs build` with `ENABLE_PDF_EXPORT=1`
2. Open `site/pdf/book.pdf` and verify:
   - [ ] Code blocks are readable with proper wrapping
   - [ ] Bullet lists render correctly
   - [ ] Tables have alternating row colors
   - [ ] Footer shows page number only
   - [ ] Admonitions have distinct border colors
   - [ ] Chapter openers have difficulty/time/XP cards
   - [ ] Reflection sections appear at chapter ends
   - [ ] Portfolio Upgrade sections in all chapters
   - [ ] Low-resource sections present where applicable
   - [ ] Overall feel: "professional learning book" not "printed website"
