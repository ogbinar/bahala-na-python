# Manuscript Revision Plan

**Generated:** 2026-05-18  
**Based on:** Full audit against DESIGN.md, STYLE-GUIDE.md, AGENT-BEST-PRACTICES.md  
**Status:** Historical reference only; use `TODO.md` for the active checklist

---

## Phase 1 — Critical Fixes (Do First)

These are the few changes that resolve the largest coherence gaps.

### T1. Clean Up Stale "3,950 XP" References in DESIGN.md

**Problem:** The XP total (3,950 → 4,900) was fixed in `index.md` and the XP table, but DESIGN.md itself still contains stale "3,950 XP" references in its audit/history sections. These create confusion when reading DESIGN.md as the source of truth.

**Files:**
- `DESIGN.md` lines 441, 580, 730

**Action:**
- Line 441 (§10 Critical → C1): Rewrite to reflect the fix is resolved. Change `The stated total of **3,950 XP** is incorrect.` → `**Resolved:** XP total was 3,950, corrected to 4,900.`
- Line 580 (§13 Key Misalignments table): Change `| **XP totals** | 3,950 XP | Actual: 4,900 XP | **Bug: numbers were wrong** |` → `| **XP totals** | 4,900 XP | 4,900 XP | **Resolved** |`
- Line 730 (§16 Alignment Audit): Change `| **Still pending — Critical** | 1 | C1: XP total wrong (3,950 vs 4,900) |` → `| **Resolved — Critical** | 1 | C1: XP total (was 3,950, fixed to 4,900) |`
- Move C1 from "Still pending" to "Resolved Since Last Audit" table at line 419

**Verification:** No remaining "3,950" in DESIGN.md except in historical context.

---

### T2. Fix Preface — Stale XP Tracker Reference

**Problem:** `preface.md:31` says "Track your progress using the XP tracker in the bottom-right corner." The floating XP tracker widget was removed (DESIGN.md §6, T1). Readers will not find this feature.

**File:** `docs/preface.md` lines 29-31

**Action:** Replace the "Use the XP System" section:
```markdown
### Use the XP System

Track your progress using the XP values in each chapter's opener card.
Earn XP by completing exercises, Side Quests, and Boss Fights.
Level up from Tambay to Legend!

Want to keep a manual tally? Grab a notebook or make a simple
spreadsheet — just log your XP as you go.
```

**Verification:** No reference to "bottom-right corner" or "tracker" remains.

---

## Phase 2 — High Priority (Substantive Gaps)

### T3. Add Missing Answers — Chapter 8 (Boss Fight 1)

**Problem:** Ch 8 Boss Fight (Sari-Sari Store System) has no answer in `answers.md`. This is the first major Boss Fight — readers need verification.

**File:** `docs/appendix/answers.md`

**Action:** Insert a new section `## Chapter 8: Boss Fight 1 — Sari-Sari Store System` after the Ch 7 section (after line 270). Include:
- Complete implementation of `SariSariStore` class with all methods filled in
- The solution already exists in the chapter itself (lines 209-372) — copy the key methods into answers.md with explanatory comments
- Add brief walkthrough of how each method works

**Note:** The chapter already contains a full solution in a collapsible block. The answers.md entry should be a concise reference version.

---

### T4. Add Missing Answers — Chapter 10 (Strings)

**Problem:** Ch 10 (Strings & Tagalog Typing Game) has no answer in `answers.md`.

**File:** `docs/appendix/answers.md`

**Action:** Read `chapter-10-strings.md` to identify the practice exercises and Boss Fight. Add section `## Chapter 10: Strings and the Tagalog Typing Game` with:
- Solutions to string manipulation exercises
- Complete Tagalog Typing Game implementation
- Explanation of key string methods used

---

### T5. Add Missing Answers — Chapter 17 (NLP)

**Problem:** Ch 17 (NLP & AI Barkada Chatbot) has only high-level "Approach" notes in answers.md (line 1107), not a full solution.

**File:** `docs/appendix/answers.md`

**Action:** Read `chapter-17-nlp.md` to identify exercises. Add detailed section with:
- Complete chatbot implementation using pattern-response matching
- Sentiment analysis solution
- Tokenization exercise answer
- Regex patterns for Taglish processing

---

### T6. Add Missing Answers — Chapter 18 (AI Coding)

**Problem:** Ch 18 Boss Fight requires building something without AI. No answer key exists.

**File:** `docs/appendix/answers.md`

**Action:** Read `chapter-18-ai-coding.md` Boss Fight (lines 170-186). Add section with:
- A sample solution: a simple Python script that takes user input, processes it, displays output, handles errors
- Emphasize this is one possible solution — the point is self-directed building
- Include a "code explanation tool" as Side Quest answer

---

### T7. Add Missing Answers — Chapter 24 (Capstone B)

**Problem:** Ch 24 (Capstone B: Barangay System Part 2) has no dedicated answer. answers.md only has a high-level "Approach" for Ch 23-24 combined.

**File:** `docs/appendix/answers.md`

**Action:** Read `chapter-24-capstone-b.md` to identify advanced features. Add section with:
- Certificate generation implementation
- API integration example (PSA/DILG)
- Flask web interface skeleton
- Advanced reporting with charts

---

### T8. Add Missing Answers — Chapter 26 (What's Next)

**Problem:** Ch 26 has no answers. While this is a closing chapter, it has reflection prompts and a 30-Day Challenge that could use sample responses.

**File:** `docs/appendix/answers.md`

**Action:** Add section `## Chapter 26: What's Next` with:
- Sample responses to reflection prompts
- A template for the 30-Day Challenge plan
- Example portfolio project descriptions

---

## Phase 3 — Medium Priority (Template Consistency)

### T9. Add Side Quests to Missing Chapters

**Problem:** 6 chapters lack Side Quest blocks, breaking the chapter template (STYLE-GUIDE.md). Missing: Ch 1, 2, 8, 14, 25, 26.

**Files:**
- `docs/part-0-welcome/chapter-01-hello-world.md`
- `docs/part-0-welcome/chapter-02-bahala-na.md`
- `docs/part-1-fundamentals/chapter-08-boss-fight-1.md`
- `docs/part-2-building-things/chapter-14-boss-fight-2.md`
- `docs/part-4-capstone/chapter-25-final-boss.md`
- `docs/part-4-capstone/chapter-26-whats-next.md`

**Action per file:** Add a `## Side Quests` section before `## Further Reading` with 2-3 optional challenges relevant to the chapter topic.

**Side Quest Ideas:**
- **Ch 1:** Modify `print()` to display different Filipino greetings; create a multi-line poem using print
- **Ch 2:** Research one Filipino programmer and write a short bio; try a different code editor
- **Ch 8:** Add a "loyalty card" feature to the store system; add barcode scanning simulation
- **Ch 14:** Refactor a previous Boss Fight with better error handling; add logging
- **Ch 25:** Build a second project; share your project with a non-programmer friend
- **Ch 26:** Write a tutorial for a beginner; contribute to an open-source project

---

## Phase 4 — Low Priority (Polish)

### T10. Consolidate Duplicate DEP Community Section in index.md

**Problem:** `index.md` has two separate DEP community sections:
- Lines 241-255: "Continue With DEP" section
- Lines 257-269: "Join the Data Engineering Pilipinas Community" section

Both contain overlapping content and CTA links.

**File:** `docs/index.md`

**Action:** Merge into one consolidated section. Keep the rich content from the second block, remove the redundant first table.

---

### T11. Standardize Boss Fight Tier Labels

**Problem:** Boss Fights use inconsistent tier labels across chapters. DESIGN.md §13 notes "4 boss fights, unlabeled."

**Files:** All 4 Boss Fight chapters (8, 14, 20, 25)

**Action:** Add consistent tier labels to the Boss Fight warning callouts:
- Ch 8: "Tier 1 — Fundamentals Boss" (already has "Elite Boss")
- Ch 14: "Tier 2 — Midpoint Boss" (check current label)
- Ch 20: "Tier 3 — Advanced Boss" (check current label)
- Ch 25: "Tier 4 — Final Boss" (already has "FINAL BOSS FIGHT")

---

### T12. Add Explanatory Comment to Ch 23 `to_dict()` Method

**Problem:** The `to_dict()` method at `chapter-23-capstone-a.md:107-121` contains a complex nested dict comprehension that beginners will struggle with.

**File:** `docs/part-4-capstone/chapter-23-capstone-a.md`

**Action:** Add inline comments to explain the nested dict comprehension that converts Enum keys/values to strings. Add a `??? tip "Diskarte"` callout explaining why serialization is needed.

---

### T13. Expand Pause and Predict Prompts

**Problem:** Only 7 chapters have "Pause and Predict" prompts. DESIGN.md §7 recommends active learning in key moments.

**Action:** Add 1-2 "Pause and Predict" prompts to these high-value chapters that lack them:
- Ch 3 (Variables) — before revealing data types
- Ch 4 (Conditionals) — before revealing if/elif/else syntax
- Ch 5 (Loops) — before revealing for/while difference
- Ch 6 (Functions) — before revealing return vs print
- Ch 7 (Files) — before revealing read/write modes

---

## Execution Order Summary

| Order | Task ID | Description | Effort | Priority |
|-------|---------|-------------|--------|----------|
| 1 | T1 | Clean up stale 3,950 XP refs in DESIGN.md | 15 min | Critical |
| 2 | T2 | Fix preface XP tracker reference | 5 min | Critical |
| 3 | T3 | Add Ch 8 Boss Fight answers | 30 min | High |
| 4 | T4 | Add Ch 10 answers | 30 min | High |
| 5 | T5 | Add Ch 17 NLP answers | 45 min | High |
| 6 | T6 | Add Ch 18 AI Coding answers | 20 min | High |
| 7 | T7 | Add Ch 24 Capstone B answers | 45 min | High |
| 8 | T8 | Add Ch 26 answers | 15 min | High |
| 9 | T9 | Add Side Quests to 6 chapters | 45 min | Medium |
| 10 | T10 | Consolidate DEP community section | 10 min | Low |
| 11 | T11 | Standardize Boss Fight tier labels | 10 min | Low |
| 12 | T12 | Add explanatory comment to Ch 23 to_dict | 10 min | Low |
| 13 | T13 | Expand Pause and Predict prompts | 30 min | Low |

**Total estimated effort: ~4.5 hours**

---

## Verification Checklist

After execution, verify:
- [ ] `grep "3,950" DESIGN.md` returns only historical context lines
- [ ] `grep "bottom-right" preface.md` returns nothing
- [ ] `answers.md` has sections for Ch 8, 10, 17, 18, 24, 26
- [ ] All 26 chapters have a Side Quest section
- [ ] `mkdocs build --strict` passes
- [ ] Boss Fight tier labels consistent across Ch 8, 14, 20, 25
- [ ] Ch 23 `to_dict()` has explanatory comment
- [ ] Pause and Predict present in 12+ chapters
