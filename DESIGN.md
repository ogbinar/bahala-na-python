# DESIGN: A Filipino's Guide to Python

**The Bahala Na Approach to Learning Code**

> **Status:** Living document — all planning, design, reviews, fixes, and research consolidated here.
> **Last Updated:** 2026-05-15 (Alignment Audit)
> **Replaces:** PLAN.md, IMPROVEMENT-PLAN.md, FIX-PLAN.md, REVIEW-IMPROVEMENT-PLAN.md, PDF-IMPROVEMENT-PLAN.md, PLAN-REVIEW.md

---

## TABLE OF CONTENTS

- [1. Book Identity](#1-book-identity)
- [2. Core Philosophies](#2-core-philosophies)
- [3. Book Structure](#3-book-structure)
- [4. Style Guide](#4-style-guide)
- [5. Voice and Tone](#5-voice-and-tone)
- [6. Gamification System](#6-gamification-system)
- [7. Pedagogical Principles](#7-pedagogical-principles)
- [8. Implementation Status](#8-implementation-status)
- [9. Fixes Applied](#9-fixes-applied)
- [10. Pending Fixes](#10-pending-fixes)
- [11. Experience Improvements](#11-experience-improvements)
- [12. PDF Quality](#12-pdf-quality)
- [13. Review Findings](#13-review-findings)
- [14. Research Reference](#14-research-reference)
- [15. Infrastructure](#15-infrastructure)
- [16. Alignment Audit (2026-05-15)](#16-alignment-audit-2026-05-15)

---

## 1. Book Identity

**Title:** A Filipino's Guide to Python: The Bahala Na Approach
**Format:** Open-source, free-to-read programming book (26 chapters, 4 parts)
**Stack:** MkDocs + Material for MkDocs, GitHub Pages, Markdown-first
**Audience:** Filipino beginners with zero prior programming experience, low-resource learners

### What Makes This Book Different

- **Filipino-first context:** Every example, analogy, and story grounded in Filipino life (sari-sari store, jeepney, comshop, GCash, OFW)
- **Gaming-inspired pedagogy:** XP, Boss Fights, Side Quests, Level Up, Achievement Badges as learning structure
- **Smart Kuya voice:** Taglish, older-sibling mentorship tone, not professor
- **Anti-gatekeeping:** Works on a P8,000 laptop with slow internet. No CS degree needed.
- **AI as creative partner:** Light-touch philosophy — AI accelerates learning, doesn't replace it

### Core Design Principles

1. **Emotionally Safe Learning** — "You belong here." Mistakes are expected and normal.
2. **Anti-Gatekeeping** — No "real programmers," no "you need math," no "get a better computer."
3. **Filipino Context** — Not a translated book; written from Filipino experience.
4. **Practical Building** — Theory serves practice. Build something in every chapter.
5. **Cozy Chaotic Tech Energy** — Warm, lived-in, comshop-at-2AM energy. Not corporate, not sterile.
6. **Mentorship Over Authority** — Smart Kuya, not Professor.
7. **Progression Over Perfection** — XP, Boss Fights, levels exist to show learning is a journey with milestones.
8. **PDF-First Parity** — PDF is not a byproduct. Primary reading format for Filipino learners.
9. **Community as Continuation, Not Dependency** — DEP is the "what's next." Book stands alone.
10. **Progression in Content, Not in Chrome** — Learning journey visible in chapter structure, not floating widgets.

---

## 2. Core Philosophies

### 2.1 Curiosity Over Credentials

Self-directed learning beats formal credentials. GitHub contribution graphs are becoming credentials themselves. 58.5% of career shifters into tech have no computing degree.

**Book implication:** The book assumes zero prerequisites. No "you should know X first."

### 2.2 Build First, Understand Deeper Later

Constructionism (Papert): learning happens most effectively when building publicly shareable things. "You can understand a thing more deeply when you can build it."

**Book implication:** Every chapter has hands-on code. Readers type code before full theory explanation.

### 2.3 Anti-Gatekeeping Education

Rejects the "banking model" of education (Freire). 85% of developers experience imposter syndrome regardless of credentials.

**Book implication:** Taglish explanations. Assumes zero prior knowledge. Normalizes struggle.

### 2.4 AI as a Creative Partner

AI augments rather than replaces human creativity. Centaur model: human + AI together beats either alone. AI pair programming: 55% faster completion, 45% fewer bugs (Microsoft, 2022).

**Integration (2026-05-15):**
- **Ch 1:** "Diskarte: When Stuck" tip box normalizes AI as one debugging tool among others
- **Ch 18:** Reframed as "Coding with AI as a Partner" with "The Trap" warning against copy-paste dependency
- **Ch 26:** "AI Will Keep Evolving" closing section on AI vs. human skills

### 2.5 Filipino Adaptive Resilience

Based on Sikolohiyang Pilipino (Enriquez): *Pakikipagkapwa*, *Diskarte*, *Bahala na* (courage in uncertainty, not fatalism), *Lakas ng Loob*.

**Book implication:** "Bahala na" = try it, see what happens, fix it later. "Diskarte" = resourcefulness, street-smart problem-solving.

---

## 3. Book Structure

### 3.1 Overall Structure

```
Front Matter
  - Homepage (index.md)
  - Preface (preface.md)
  - Getting Started (3 files: overview, install, first program)

Part 0: Welcome (Ch 1-2)
  - Ch 1: Hello World
  - Ch 2: Bahala Na

Part 1: Fundamentals (Ch 3-8)
  - Ch 3: Variables
  - Ch 4: Conditionals
  - Ch 5: Loops
  - Ch 6: Functions
  - Ch 7: Files
  - Ch 8: Boss Fight 1

Part 2: Building Things (Ch 9-14)
  - Ch 9: Classes
  - Ch 10: Strings
  - Ch 11: APIs
  - Ch 12: Scraping
  - Ch 13: Errors
  - Ch 14: Boss Fight 2

Part 3: Level Up (Ch 15-20)
  - Ch 15: Discord Bots
  - Ch 16: Data Visualization
  - Ch 17: NLP
  - Ch 18: Coding with AI as a Partner
  - Ch 19: Open Source
  - Ch 20: Boss Fight 3

Part 4: Capstone (Ch 21-26)
  - Ch 21: Mobile Python
  - Ch 22: Bayanihan
  - Ch 23: Capstone A
  - Ch 24: Capstone B
  - Ch 25: Final Boss
  - Ch 26: What's Next

Appendix
  - Answers
  - Troubleshooting
  - Reference
  - Glossary
```

**Total:** 40 .md files across 8 sections. All files present and containing substantial content.

### 3.2 Chapter Template

Every chapter follows this structure:

1. **Story Hook** — Filipino cultural narrative
2. **Chapter Opener Card** — `??? example "📋 Chapter Info"` with Difficulty / Time / XP
3. **What You'll Learn** — Learning objectives
4. **Tutorial** — Concept explanation + hands-on code
5. **Boss Fight** (select chapters) — Cumulative synthesis challenge
6. **Side Quests** — Optional extra challenges
7. **Portfolio Tip** — GitHub/LinkedIn/interview guidance
8. **Checklist** — Self-assessment
9. **Reflection** — Deeper thinking prompts
10. **Further Reading** — Next steps

### 3.3 Chapter Length

- 20-40 pages equivalent per chapter
- Shorter is better for beginners
- Clear sense of completion per chapter

---

## 4. Style Guide

### Code Presentation

- Syntax-highlighted code blocks with ` ```python `
- Show both code AND expected output
- Line-by-line explanation for important code
- Include intentional errors and debugging walkthroughs

### Callout Types (Admonitions)

| Type | Icon | Purpose |
|------|------|---------|
| `tip` / `diskarte` | 💡 | Practical shortcuts, workarounds |
| `warning` / `boss-fight` | ⚔️ | Boss fights, common mistakes |
| `success` / `level-up` | ⭐ | Milestone markers |
| `note` / `portfolio-tip` | 💼 | Career guidance |
| `side-quest` | 🗺️ | Optional challenges |
| `badge` | 🏆 | Achievement markers |

### Terminology

- Define terms on first use
- Don't translate technical terms ("variable," "function," "API")
- Use Tagalog for emotional/cultural moments
- Consistent terminology throughout

---

## 5. Voice and Tone

### The Smart Kuya

- Knowledgeable older sibling, not a professor
- Uses "kayo/ka" (you) directly
- Admits mistakes: *"Naiimutan ko pa rin kung paano..."*
- Celebrates wins: *"Galing mo! Working na!"*
- Normalizes struggle: *"Confused? Good. That means you're learning."*

### Taglish Guidelines

- Taglish for explanation and emotional moments
- English for code and technical terms
- Natural code-switching, not forced
- Don't over-translate technical terms

### Sentence Structure

- 3-5 sentences max per paragraph
- One idea per paragraph
- Front-load important information
- Active voice

---

## 6. Gamification System

### XP System

| Chapter Type | XP |
|-------------|-----|
| Regular chapter | +100 XP |
| Capstone chapter (23-24) | +200 XP |
| Boss Fight (8, 14, 20) | +500 XP |
| Final Boss (25) | +1000 XP |
| **Total** | **4,900 XP** |

### Level Progression

| Level | Filipino Name | Cumulative XP | Chapters |
|-------|--------------|---------------|----------|
| 1 | Tambay | 0 | Ch 1-2 |
| 2 | Albano | 500 | Ch 3-7 |
| 3 | Karera | 1,000 | Ch 8 |
| 4 | Devel | 2,000 | Ch 14 |
| 5 | Master | 2,500-3,100 | Ch 20-23 |
| 6 | Legend | 4,900 | Ch 25 |

### Current State

XP exists as **content-embedded motivational framing only** — in chapter opener cards, TOC tables, skill tree, Boss Fight callouts, badges. No JavaScript tracking widget (removed per experience improvement plan).

### What Was Removed

- Floating XP tracker HUD widget
- Toast notifications ("+100 XP!")
- localStorage-based XP tracking
- Level-up animations
- HP/MP bar CSS classes
- Pixel border CSS class
- `fadeIn` heading animations

### What Remains

- XP values in chapter opener cards
- XP table on homepage
- Boss Fight tier labels
- Side Quest blocks with XP rewards
- Achievement Badge blocks
- Level Up blocks
- TOC with XP column
- Skill Tree ASCII diagram
- "Total XP to complete" summary

---

## 7. Pedagogical Principles

### From Book Structuring Research

1. **Two-Part Model:** Basics + Projects (Python Crash Course pattern)
2. **Exercise-First:** Code before theory (Learn Python Hard Way pattern)
3. **Project-Driven:** Immediate practical value (Automate the Boring Stuff pattern)
4. **Playful Introduction:** Humor, relatable examples (Python for Kids pattern)

### Active Learning

- Every concept paired with hands-on practice
- "Pause and Predict" prompts at key moments
- Readers must write code, not just read it
- Exercises require modification, not just copying

### Scaffolding

- Start simple, increase complexity gradually
- Each concept builds on previously learned material
- Revisit earlier concepts in new contexts (spaced repetition)

### Progressive Disclosure

- Don't overwhelm with advanced concepts upfront
- Mark advanced sections clearly for skipping
- "Quick start" path vs. "deep dive" path

### Immediate Feedback

- Expected output shown for every code example
- "Try It" sections for experimentation
- Answer keys in appendix
- Common error patterns and debugging tips

---

## 8. Implementation Status

### Completion Summary

| Dimension | Status |
|-----------|--------|
| Chapter coverage (26 chapters) | Complete |
| Chapter structure (7-section template) | Complete |
| Voice & tone (Smart Kuya, Taglish) | Complete |
| Code quality (14 bugs fixed, CI validates) | Complete |
| Appendix (4 types) | Partial — answers missing Ch 8, 10, 17, 18, 24, 26 |
| CI/CD (syntax, build, deploy) | Complete |
| MkDocs build (`--strict`) | Passing, 40 HTML files |
| Gamification content (XP, Boss Fights, etc.) | Complete as content-embedded framing |
| AI as Creative Partner integration | Complete (Ch 1, 18, 26) |
| Experience improvements (T1-T15) | Complete, 15/15 tasks done |
| Checklists | Complete, 26/26 chapters |
| Reflections | Complete, 26/26 chapters |
| Portfolio tips | Complete, 26/26 chapters |
| Side quests | Partial, 20/26 chapters (missing Ch 1, 2, 8, 14, 25, 26) |

### Remaining Gaps (Non-Blocking)

| Gap | Priority | Notes |
|-----|----------|-------|
| `images/` has 3 files (favicon, 2 poring SVGs) | Low | Placeholder references only |
| `exercises/` directory empty | Low | Code embedded in chapters |
| No community Discord configured | Low | Out of scope for code |
| No PDF build pipeline | Low | `mkdocs-with-pdf` in optional deps |
| No translation infrastructure | Low | `mkdocs-static-i18n` not set up |
| No analytics | Low | Plausible not configured |
| No companion video content | Medium | YouTube/TikTok planned |
| `answers.md` missing 6 chapters | Medium | Ch 8, 10, 17, 18, 24, 26 |
| Side quests missing from 6 chapters | Low | Ch 1, 2, 8, 14, 25, 26 |
| Broken PDF download link in index.md | Medium | `pdf/book.pdf` does not exist |
| Ch 18 title mismatch in master TOC | Medium | index.md says old title |

---

## 9. Fixes Applied

### Critical Code Bugs Fixed (8)

| File | Issue | Fix |
|------|-------|-----|
| Ch 15 Discord Bots | `ctx.send()` missing `ephemeral=True` | Updated |
| Ch 17 NLP | Regex `kka?` should be `ka?` | Fixed |
| Ch 17 NLP | "sulit" (positive) in negative_words | Removed |
| Ch 20 Boss Fight | Missing `import os` | Added |
| Ch 22 Bayanihan | Phone validation `len(digits) == 14` | Changed to `13` |
| Ch 23 Capstone A | `_generate_id()` always same ID | Uses class counter |
| Ch 23 Capstone A | `to_dict()` serialization bug | Fixed for nested fee dicts |
| Answers | Missing `f` prefix on f-string | Added |

### Non-Critical Code Issues Fixed (6)

| File | Issue | Fix |
|------|-------|-----|
| Ch 15 | `pytz` import not in pip install | Added to install section |
| Ch 16 | `df` variable scoping NameError | Separate `df_pie` variable |
| Ch 20 | Division by zero when amounts empty | Added guard |
| Ch 21 | Kivy `__init__` order conflict | Data init before `super().__init__()` |
| Ch 24 | Flask missing input validation | Added validation |
| Ch 25 | `json.dump()` crashes on date objects | Added `default=str` |

### Structural Fixes

| File | Issue | Fix |
|------|-------|-----|
| Ch 22 | Missing Boss Fight section | Added challenge + hint system |
| Ch 23, Ch 24 | DILG URL typo `dils.gov.ph` | Corrected to `dilg.gov.ph` |
| Ch 23 | "The Project" header | Changed to "What You'll Learn" |
| Ch 25 | No callout boxes | Added warning, info, tip, success |
| Ch 16 | `from_dict()` not handling nested fees | Fixed restoration logic |

### MkDocs Config Fixes

| Issue | Fix |
|-------|-----|
| YAML colons in nav titles broke parsing | Quoted all nav section titles |
| `repo_actions_ignored` unrecognized | Commented out |
| RSS plugin `match_url` deprecated | Changed to `categories` config |
| `docs/overrides/` missing | Created |

### Appendix Expansions

| File | Added |
|------|-------|
| answers.md | Boss Fight answers for Ch 14-25 |
| glossary.md | Removed duplicate "Variable", added: asyncio, Flask, Kivy, NLP, pandas, Termux, Tokenization, Vibecoding |
| reference.md | Quick refs: asyncio, discord.py, matplotlib, pandas, regex |
| troubleshooting.md | Sections: discord.py, asyncio, matplotlib, pandas, Kivy |

---

## 10. Pending Fixes

### Resolved Since Last Audit (2026-05-15)

The following items were previously listed as pending but have since been fixed in the codebase:

| ID | Issue | Resolution |
|----|-------|------------|
| C3 | Ch 5 `inventory[item]` bug | Fixed — code no longer present |
| C4 | Ch 5 XP inconsistency (100 vs 150) | Fixed — both say +100 XP |
| C2 | Ch 25 XP conflict (100 vs 1000) | Fixed — all references say 1000 XP |
| H3 | Glossary duplicate "Variable" | Fixed — single V section entry |
| H4 | Part 3 nav label mismatch | Fixed — heading says "Level Up" |
| H6 | Ch 25 "No hints" contradiction | Fixed — reframed to "diskarte" language |
| L1 | Ch 25 "Too Simple" undermines motivation | Fixed — reframed to "Maybe Too Small" |
| M1 | Getting Started not in nav | Verified — present in mkdocs.yml |
| P3.2 | Pause and Predict prompts | Done — 7 chapters have prompts |
| P5.1 | Portfolio tips expansion | Done — all 26 chapters have portfolio tips |
| L2 | Part 0 index missing XP table | Fixed — XP table present at line 45-52 |

### Critical (Unresolved)

#### C1: XP Value Inconsistency — Master Total Is Wrong

**Locations:** `DESIGN.md` §6, `index.md:174`

The stated total of **3,950 XP** is incorrect. The actual sum from the TOC tables is:
- Part 0: 200 XP (Ch 1 + Ch 2)
- Part 1: 1,000 XP (Ch 3-7 @ 100 + Ch 8 @ 500)
- Part 2: 1,000 XP (Ch 9-13 @ 100 + Ch 14 @ 500)
- Part 3: 1,000 XP (Ch 15-19 @ 100 + Ch 20 @ 500)
- Part 4: 1,700 XP (Ch 21 @ 100 + Ch 22 @ 100 + Ch 23 @ 200 + Ch 24 @ 200 + Ch 25 @ 1000 + Ch 26 @ 100)
- **Actual total: 4,900 XP**

**Fix:** Update `index.md:174` to `**Total XP to complete: 4,900 XP**`. Update DESIGN.md §6 XP table total to 4,900. Update Level Progression table to match.

### High Priority

#### H1: Getting Started Flow — Ordering Is Correct Now

`first-program.md` now says "Now that you have Python installed" and is correctly ordered after `install-python.md`. **This item was resolved.**

#### H2: Getting Started vs. Part 0 — Minor Content Overlap

`first-program.md` covers a simple `print("Kumusta!")` verification. Ch 1 covers `print()` with full story hook and cultural context. The overlap is small and intentional (setup verification vs. first real lesson). **Acceptable as-is.**

#### H5: Ch 18 Title Mismatch in Master TOC

**Location:** `index.md:159`

Master TOC lists Ch 18 as "AI-Assisted Coding & Vibecoding" but the chapter title is "Coding with AI as a Partner". The chapter's Reflection block also still says "AI-Assisted Coding and Vibecoding".

**Fix:** Update `index.md:159` to match chapter title. Update Ch 18 Reflection block title.

### Medium Priority

| Issue | Location | Status | Fix |
|-------|----------|--------|-----|
| M2 | Ch 25 Resources | **Resolved** | Ch 25 now references Ch 21-24 including mobile, open source, capstone |
| M3 | Appendix answers coverage | **Partial** | 20/26 chapters covered. Missing: Ch 8, 10, 17, 18, 24, 26 |
| M4 | Projects table in index.md | **Resolved** | 8 projects + "and more" note present |
| M5 | Ch 23 `to_dict` complexity | **Pending** | No explanatory comment on `to_dict()` method |
| M6 | Ch 24 Flask security | **Resolved** | Warning callout present at line 490 |
| M7 | Broken PDF link in index.md | **Pending** | `pdf/book.pdf` link targets non-existent file |
| M8 | Ch 18 Reflection title | **Pending** | Still says "AI-Assisted Coding and Vibecoding" |

### Low Priority

| Issue | Status | Fix |
|-------|--------|-----|
| L2 | Part 0 index missing XP table | **Resolved** — XP table present |
| L3 | Part 3 directory named `part-3-going-further` despite "Level Up" label | **Pending** — directory rename requires mkdocs.yml + all link updates |
| L4 | Skill tree level names don't match XP progression | **Pending** — cosmetic only |

---

## 11. Experience Improvements

### Completed (T1-T15, 15/15)

All tasks from the experience improvement plan have been implemented and verified:

- T1: Floating XP tracker widget removed
- T2: Unused CSS removed (HP/MP bars, pixel borders, fadeIn)
- T3: Typography + spacing improvements added
- T4: Smart Kuya icons standardized
- T5: "Discord" → "Barkada" language updated
- T6: Hero promise + quick bullets added
- T7: "What You'll Build" project cards added
- T8: "Why This Exists" emotional section added
- T9: 4-button download area implemented
- T10: "Low Resource Friendly" callout added
- T11: "Continue With DEP" section added
- T12: Linear learning path + folded skill tree
- T13: Nav label "Going Further" → "Level Up"
- T14: QR code note updated
- T15: Build verification passed

### Long-Term (Future Iterations)

| Task | Impact |
|------|--------|
| L1: DEP roadmap integration | Ecosystem lock-in |
| L2: CSS-only progress markers | Subtle progression |
| L3: PDF cover page redesign | Brand consistency |
| L4: Print-only tracking pages | Workbook feel |

---

## 12. PDF Quality

### Phase 1: PDF CSS Overhaul (Completed)

Code block readability, bullet list fix, table styling, footer noise reduction, admonition visual hierarchy, and breathing room — all implemented in `pdf.css`.

### Phase 2-7: Outstanding Improvements

| Phase | What | Effort | Priority |
|-------|------|--------|----------|
| P2.1 | Standard chapter opener cards (26 files) | 2 hours | High |
| P3.1 | Reflection sections (26 files) | 1 hour | High |
| P3.2 | Pause and Predict prompts (7 key files) | 2 hours | High |
| P3.3 | Checklists (26 files) | 1.5 hours | Medium |
| P4.1 | "If You Only Have a Phone" sections (4 files) | 1 hour | High |
| P4.2 | "If You Have Slow Internet" sections (4 files) | 30 min | Medium |
| P4.3 | "If You Have a 4GB Laptop" sections (3 files) | 30 min | Medium |
| P5.1 | Portfolio Mode expansion to all 26 chapters | 2 hours | High |
| P6.1 | TOC improvement with pacing | 30 min | Medium |
| P6.2 | Roadmap visual / skill tree | 30 min | Medium |
| P6.3 | QR codes / links for static PDF | 30 min | Medium |
| P7.1 | Warm palette in PDF | 20 min | Medium |
| P7.2 | XP cards and game UI motifs in PDF | 20 min | Medium |

**Total estimated effort for remaining PDF work: ~12 hours**

---

## 13. Review Findings

### What Matches the Plan Well

| Area | Status |
|------|--------|
| 26 chapters, all files present, correct nav | Aligned |
| Chapter template followed faithfully | Aligned |
| Smart Kuya voice consistent | Aligned |
| Filipino cultural context pervasive | Aligned |
| Five core philosophies woven in | Aligned |
| 4 Boss Fights with starter code + hints | Aligned |
| 14 code bugs fixed, CI validates | Aligned |
| Appendix complete (4 types) | Aligned |
| CI/CD functional | Aligned |

### Key Misalignments (Plan vs. Implementation)

| Area | Plan | Reality | Gap |
|------|------|---------|-----|
| **Gamification mechanics** | XP tracking, stats system, skill trees, achievement badges | XP as flavor text only | Large (by design) |
| **Visual design** | 12 aesthetic themes, mascot, custom theme | Default Material theme | Large (by design) |
| **Community** | Discord, YouTube, TikTok | None built | Large (out of scope) |
| **Portfolio guidance** | Explicit per-project | All 26 chapters have portfolio tips | **Resolved** |
| **Mini-project density** | 3:1 mini:major ratio | ~1:1 ratio | Medium |
| **Boss fight tiers** | 4-tier escalation with labels | 4 boss fights, unlabeled | Medium |
| **Side quest types** | 4 categorized types | 20/26 chapters have side quests, uncategorized | Medium |
| **Publishing** | PDF, translation, analytics | None configured | Medium |
| **XP totals** | 3,950 XP | Actual: 4,900 XP | **Bug: numbers were wrong** |
| **Ch 18 title** | "Coding with AI as a Partner" | index.md still says old title | **Bug: stale reference** |

### Strengths to Preserve

- Voice consistency across all 37 chapters
- Authentic, lived-in cultural specificity
- Code quality with CI validation
- Satisfying reading rhythm (Story Hook → Tutorial → Boss Fight)
- Offline-first accessibility (Colab/Replit alternatives)
- Substantive appendices

---

## 14. Research Reference

The research documents have been consolidated into this file. Key research areas covered:

### Gaming + Learning
- Flow Theory (Csikszentmihalyi)
- Self-Determination Theory (Deci & Ryan)
- Gamification in education
- Deliberate practice
- Failure as productive learning
- Social learning and multiplayer gaming
- Systems thinking via game design
- Gaming mechanics → programming concepts mapping (16 parallels)

### Filipino Context
- Comshop history and role in digital literacy
- Gaming culture (MLBB, Free Fire, Ragnarok Online, esports)
- OFW family dynamics and "tech manager" children
- Meme culture, Facebook culture, Taglish
- Barangay systems and bayanihan
- Side hustle and freelancer culture
- Educational inequality and low-end hardware reality
- Filipino tech communities

### Open Source + Community
- Cathedral vs. Bazaar development models
- GitHub culture (PRs, issues, code review)
- Linux communities
- Collaborative learning (pair programming, Feynman technique)
- Mentorship models ("Kuya" model, reverse mentoring)
- Online learning tribes (Discord, Reddit, forums)

### Emotional + Human Themes
- Fear of programming and math anxiety
- Tutorial hell and information overwhelm
- Burnout prevention (bayanihan as buffer)
- Growth mindset and confidence building
- Identity ("Am I a programmer?")
- Shame vs. guilt in learning
- Belonging and community

### Project Design
- Career advancement motivation (₱35k to ₱100k+ jump)
- Job search competitiveness (LinkedIn + GitHub)
- Career shifting (58.5% no computing degree)
- Automation of mundane tasks
- AI augmentation
- Community and belonging

### Book Structuring Best Practices
- Two-part model (Basics + Projects)
- Exercise-first approach
- Project-driven learning
- Chapter architecture (6-section template)
- Scaffolding, progressive disclosure, active learning
- Writing and presentation best practices
- Common pitfalls to avoid

---

## 15. Infrastructure

### Build and Deploy

| Component | Status |
|-----------|--------|
| MkDocs + Material theme | Active, `mkdocs build --strict` passes |
| CI/CD (`.github/workflows/ci.yml`) | Python syntax validation, MkDocs build, GitHub Pages deploy |
| Issue templates | bug_report.md, content_contribution.md, chapter_proposal.md |
| Build output | 40 HTML files, all nav sections rendered |
| Sitemap + RSS | Generated successfully |

### Override Files

| File | Purpose |
|------|---------|
| `docs/overrides/main.html` | Minimal: dark mode palette only (13 lines) |
| `docs/overrides/assets/stylesheets/custom.css` | Custom CSS: typography, spacing, admonition icons |
| `docs/overrides/assets/stylesheets/pdf.css` | PDF-specific styling |

### What's in `docs/overrides/`

After XP tracker removal, `main.html` is minimal — only `block libs` and `block analytics`. No inline styles, no JavaScript, no HTML widgets.

---

## Appendix: File Inventory

### Administrative Files

| File | Status |
|------|--------|
| `DESIGN.md` | **This file** — consolidated design document |
| `STYLE-GUIDE.md` | Active — voice, tone, code presentation rules |
| `AGENT-BEST-PRACTICES.md` | Active — repo structure, workflow, tooling |
| `PLAN.md` | **ARCHIVED** — content merged into DESIGN.md |
| `IMPROVEMENT-PLAN.md` | **ARCHIVED** — content merged into DESIGN.md |
| `FIX-PLAN.md` | **ARCHIVED** — content merged into DESIGN.md |
| `REVIEW-IMPROVEMENT-PLAN.md` | **ARCHIVED** — content merged into DESIGN.md |
| `PDF-IMPROVEMENT-PLAN.md` | **ARCHIVED** — content merged into DESIGN.md |
| `PLAN-REVIEW.md` | **ARCHIVED** — content merged into DESIGN.md |
| `RESEARCH-MASTER.md` | **ARCHIVED** — content merged into DESIGN.md |
| `research-5-philosophies.md` | **ARCHIVED** — content merged into DESIGN.md |
| `research-filipino-context.md` | **ARCHIVED** — content merged into DESIGN.md |
| `research-gaming-learning.md` | **ARCHIVED** — content merged into DESIGN.md |
| `research-open-source-emotional.md` | **ARCHIVED** — content merged into DESIGN.md |
| `research-projects-design-structure.md` | **ARCHIVED** — content merged into DESIGN.md |
| `design.md` | **ARCHIVED** — content merged into DESIGN.md |

### Content Files (Active)

| Path | Purpose |
|------|---------|
| `docs/index.md` | Homepage, TOC, skill tree |
| `docs/preface.md` | Front matter |
| `docs/getting-started/` | Setup guide (3 files) |
| `docs/part-*/` | 26 chapter files across 4 parts |
| `docs/appendix/` | Answers, troubleshooting, reference, glossary |

---

## 16. Alignment Audit (2026-05-15)

### Purpose

This section records the results of a full codebase verification against DESIGN.md, STYLE-GUIDE.md, and AGENT-BEST-PRACTICES.md. Goal: alignment and integrity between what the plan files say and what exists in the code.

### Audit Method

Each pending fix in §10 was verified against the actual source files. Each claim in §8 Implementation Status was checked against the codebase. Cross-references between plan files were checked for consistency.

### Summary

| Category | Count | Details |
|----------|-------|---------|
| **Resolved since last update** | 11 | C3, C4, C2, H3, H4, H6, L1, M1, P3.2, P5.1, L2 |
| **Still pending — Critical** | 1 | C1: XP total wrong (3,950 vs 4,900) |
| **Still pending — High** | 2 | H5: Ch 18 title in TOC, H2: minor overlap (acceptable) |
| **Still pending — Medium** | 5 | M3, M5, M7, M8 |
| **Still pending — Low** | 2 | L3, L4 |
| **New findings** | 3 | Broken PDF link, side quest gaps, answers gaps |

### Cross-File Consistency

| Check | Status | Notes |
|-------|--------|-------|
| DESIGN.md §6 XP total vs index.md TOC sum | **Fixed** | Both now say 4,900 XP |
| DESIGN.md §6 Level table vs XP total | **Fixed** | Legend level now 4,900 |
| Ch 18 title in index.md vs chapter file | **Fixed** | Both now "Coding with AI as a Partner" |
| Ch 18 Reflection title vs chapter title | **Fixed** | Reflection updated |
| Part 4 index XP total vs master | **Fixed** | Part 4 index now says 4,900 |
| Part 3 nav label vs directory name | **Misaligned** | Nav says "Level Up", directory is `part-3-going-further` |
| AGENT-BEST-PRACTICES.md directory layout vs actual | **Minor** | References `part-3-going-further/` (matches current) |
| STYLE-GUIDE.md chapter template vs actual chapters | **Aligned** | All 26 chapters follow template |
| STYLE-GUIDE.md callout types vs DESIGN.md §4 | **Aligned** | Same 6 types |
| STYLE-GUIDE.md voice guidelines vs DESIGN.md §5 | **Aligned** | Same Smart Kuya guidelines |

### Codebase Facts Verified

| Fact | Value |
|------|-------|
| Total chapters | 26, all present |
| Chapters with checklists | 26/26 |
| Chapters with reflections | 26/26 |
| Chapters with portfolio tips | 26/26 |
| Chapters with side quests | 20/26 (missing: Ch 1, 2, 8, 14, 25, 26) |
| Chapters with "Pause and Predict" | 7 |
| Answers.md coverage | 20/26 chapters (missing: Ch 8, 10, 17, 18, 24, 26) |
| MkDocs build status | `--strict` passes, 40 HTML files |
| Images directory | 3 files (favicon, 2 poring SVGs) |
| Exercises directory | Empty |
| Get Started flow ordering | Correct: overview → install → first program |
