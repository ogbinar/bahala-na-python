# Open Source Python Book: Best Practices for Formatting, Structure, Workflow & Approach

Research compiled from successful open-source books, documentation frameworks, and technical writing communities.

---

## 1. BOOK BUILDING TOOLS

### Recommended: MkDocs + Material for MkDocs

**Why MkDocs over alternatives:**

| Tool | Best For | Pros | Cons |
|------|----------|------|------|
| **MkDocs + Material** | Books, docs, tutorials | Python-native, Markdown-first, Material theme, plugins, GitHub Pages ready | Less flexible than mdBook for complex customization |
| **mdBook** (Rust Book) | Programming language docs | Rust-based, fast, simple, excellent for code-heavy books | Smaller ecosystem, fewer themes, Rust dependency |
| **Sphinx** | Python library docs | Python-native, autodoc, extensive extensions | reStructuredText learning curve, complex config |
| **Docusaurus** (React) | Modern docs sites | Fast, versioning, i18n, blog, React ecosystem | JavaScript/React dependency, heavier |
| **Hugo / Jekyll** | General websites | Fast, mature | Not optimized for book structure |

**Recommendation: MkDocs + Material for MkDocs**

- Python-native (fits the book's Python focus)
- 50,000+ organizations use it (OpenAI, Microsoft, Google, Netflix)
- Material theme is the most polished documentation theme available
- Extensive plugin ecosystem
- GitHub Pages integration is trivial
- Markdown-first (no reStructuredText learning curve)

### Alternative: mdBook

If the team prefers Rust or wants the exact structure of The Rust Book:

- Used by The Rust Programming Language (17.8k stars)
- `book.toml` for structure (similar to `mkdocs.yml`)
- Excellent for code-heavy books with exercises
- mdBook has plugins for Mermaid diagrams, copy buttons, etc.

---

## 2. REPOSITORY STRUCTURE BEST PRACTICES

### Recommended File Layout

```
book-python/
├── .github/
│   ├── workflows/
│   │   └── deploy.yml          # GitHub Actions CI/CD
│   └── PULL_REQUEST_TEMPLATE.md
│   └── ISSUE_TEMPLATE/
│       ├── bug_report.md
│       └── chapter_proposal.md
├── docs/
│   ├── index.md                # Book landing page
│   ├── getting-started/
│   │   ├── index.md
│   │   ├── install-python.md
│   │   └── first-program.md
│   ├── part-1-fundamentals/
│   │   ├── index.md
│   │   ├── variables.md
│   │   ├── conditionals.md
│   │   └── loops.md
│   ├── part-2-building-things/
│   │   ├── index.md
│   │   └── ...
│   ├── part-3-going-further/
│   │   ├── index.md
│   │   └── ...
│   ├── part-4-capstone/
│   │   ├── index.md
│   │   └── ...
│   ├── images/                 # All book images/illustrations
│   │   ├── comshop-retro.png
│   │   ├── poring-mascot.png
│   │   └── ...
│   └── exercises/              # Exercise code files (referenced from MD)
│       ├── ch03-sari-sari/
│       │   ├── main.py
│       │   └── solution.py
│       └── ...
├── src/                        # Alternative: raw MD files here
│   └── ...
├── mkdocs.yml                  # Book configuration
├── pyproject.toml              # Python dependencies (MkDocs, plugins)
├── requirements.txt            # Simpler dependency listing
├── CONTRIBUTING.md             # How to contribute to the book
├── CODE_OF_CONDUCT.md
├── LICENSE.md                  # CC BY 4.0 recommended
├── README.md                   # Book landing page (also shown on GitHub)
├── STYLE-GUIDE.md              # Writing & formatting rules for contributors
└── AGENT-BEST-PRACTICES.md     # This file
```

### Key Structural Decisions

1. **`docs/` vs `src/`**: MkDocs uses `docs/` by default. Rust Book uses `src/`. Either works -- `docs/` is more conventional for MkDocs.

2. **Exercise code in separate folders**: Keep code files alongside (not embedded in) MD files. This makes them:
   - Runnable by readers
   - Testable by CI
   - Easier to update independently

3. **Part-level index pages**: Each part should have an `index.md` that:
   - Explains the part's theme
   - Links to all chapters
   - Sets expectations

---

## 3. MARKDOWN FORMATTING STANDARDS

### Headings Hierarchy

```markdown
# Chapter Title              (H1 -- one per file)
## Section                   (H2 -- main sections within chapter)
### Subsection               (H3 -- sub-sections)
#### Sub-subsection          (H4 -- rarely needed)
```

**Rule**: One H1 per file. Use H2/H3 for structure. Never skip heading levels.

### Code Blocks

```markdown
Basic code block:
```python
x = 5
print(x)
```

Code block with line numbers:
```python title="hello.py" linenums="1"
x = 5
print(x)
```

Code block with highlighted lines:
```python title="hello.py" linenums="1" hl_lines="2 3"
x = 5
y = x + 1  # This line is highlighted
print(y)   # This line is highlighted
```

Terminal/command output:
```bash
$ python hello.py
10
```

Code blocks with diff highlighting (for showing changes):
```diff
- print("Hello, World!")
+ print("Kumusta, World!")
```

### Callout Boxes (Material for MkDocs)

Material theme supports native callout blocks:

```markdown
??? note "Try It Yourself"
    Modify the code above. Change the name to your own.

??? tip "Diskarte"
    Filipino resourcefulness in programming: use what you have.

??? warning "Boss Fight Warning"
    This challenge combines 4 concepts. Take a deep breath first.

??? info "Bahala Na Philosophy"
    "Bahala na" doesn't mean give up -- it means try, learn, adapt.

??? bug "Common Mistake"
    Beginners often forget the colon after `if` statements.

??? example "Real-World Example"
    The GCash app uses similar logic for transaction validation.
```

### Admonition Shortcuts

| Syntax | Type | Use Case |
|--------|------|----------|
| `??? note` | Note | Additional context |
| `??? tip` | Hint | Helpful suggestions |
| `??? warning` | Warning | Important cautions |
| `??? info` | Info | Background knowledge |
| `??? bug` | Caution | Common mistakes |
| `??? example` | Example | Real-world connections |
| `??? success` | Success | Completed milestones |
| `??? question` | Question | Self-assessment |
| `??? abstract` | Todo | Work-in-progress notes |

### Tables

```markdown
| Concept | Python Syntax | Filipino Analogy |
|---------|--------------|------------------|
| Variable | `x = 5` | Like a labeled container in a sari-sari store |
| List | `[1, 2, 3]` | Like shelves with items in order |
| Dict | `{"item": "price"}` | Like a price tag list |
```

**Rule**: Keep tables under 6 columns. For wider tables, use a separate reference page.

### Images

```markdown
![Sari-sari store illustration](images/sari-sari-store.png)

![Comshop retro aesthetic](images/comshop-retro.png){ width="600" }

![Diagram showing data flow](images/data-flow.png){ .center }
```

**Best practices**:
- Store all images in `docs/images/` (or `static/`)
- Use descriptive filenames (not `image1.png`)
- Provide alt text for every image
- Use WebP format for better compression (convert with `cwebp`)
- Include SVG for diagrams/icons
- Maximum width: 800px for inline images

### Links

```markdown
Internal link: [Next chapter](variables.md)
Internal link with anchor: [Loops section](loops.md#while-loops)
External link: [Python docs](https://docs.python.org/3/)
External link with title: [PEP 8](https://peps.python.org/pep-0008/ "Style Guide for Python Code")
```

**Rule**: Use relative paths for internal links. Always include titles for external links.

### Lists and Spacing

- One blank line between list items when items are long
- Use ordered lists for steps, unordered for options
- Never mix ordered and unordered lists without clear separation

---

## 4. CHAPTER TEMPLATE

Every chapter should follow this consistent structure:

```markdown
# Chapter N: Chapter Title

<!-- Story hook: 1-2 paragraph narrative -->
You're running a sari-sari store in your barangay...

<!-- What you'll learn -->
## What You'll Learn

- Variable assignment and data types
- Working with dictionaries
- File I/O basics

<!-- Tutorial sections -->
## Variables and Data Types

The simplest way to store information...

```python
inventory = {"merienda": 50, "candy": 30}
```

??? tip "Diskarte"
    ...

## Boss Fight

??? warning "Boss Fight"
    Combine everything you've learned.

## Side Quests

??? note "Optional: Side Quest"
    ...

## Summary

- Key concepts covered
- What to read next

## Further Reading

- Links to Python docs, related chapters
```

---

## 5. WRITING STYLE GUIDELINES

### Voice and Tone

- **The "Smart Kuya" voice**: A big sibling figure who's been through this. Not a professor.
- **Taglish naturally**: Code comments and explanations mix English and Tagalog organically.
- **Conversational, not academic**: Write like you're explaining to a friend at a comshop.
- **Admit mistakes**: "Naiimutan ko pa rin kung paano..." makes the writer relatable.

### Sentence Structure

- Keep paragraphs to 3-5 sentences max
- One idea per paragraph
- Front-load important information
- Use active voice: "Python stores this in a variable" not "This is stored by Python"

### Technical Writing Best Practices

- **Define terms on first use**: "A **dictionary** (like a real dictionary that maps words to definitions)..."
- **Show, don't just tell**: Always include code examples for programming concepts
- **Repeat key concepts**: Spiral curriculum -- revisit concepts at higher complexity
- **Use consistent terminology**: Pick one term and stick with it per chapter. Don't swap between "function" and "subroutine."
- **Number your code examples**: Reference them by number ("as shown in Example 3.1")

### Taglish Guidelines

```markdown
# Good: Natural code-switching
Let's try it. Ibaril natin ang code:

```python
name = "Juan"
print(f"Kumusta, {name}!")
```

# Avoid: Over-translating technical terms
Don't translate "variable," "function," "API" -- these are technical terms used
in English everywhere in Philippine tech.

# Good: Taglish for explanation, English for code
Ang variable ay parang lalagyan. I-click mo lang:
```

---

## 6. WORKFLOW & CONTRIBUTION MODEL

### Docs-as-Code Approach

Treat the book like software:

| Practice | Implementation |
|----------|---------------|
| **Version control** | Git + GitHub for all content |
| **Branching** | `main` (published) + feature branches for chapters |
| **Pull Requests** | Every change goes through PR review |
| **Code of Conduct** | Adopt Contributor Covenant |
| **Issue templates** | Bug reports, chapter proposals, translation requests |
| **CI/CD** | GitHub Actions to build and deploy on merge |
| **Spell checking** | GitHub Action that runs `cspell` on PR |
| **Link checking** | GitHub Action that checks broken links |
| **Formatting** | `markdownlint` or `dprint` for consistent formatting |

### GitHub Actions CI/CD Pipeline

```yaml
# .github/workflows/deploy.yml
name: Deploy Book
on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: 3.x
      - run: pip install -r requirements.txt
      - run: mkdocs build --strict  # Fail on errors
      - run: markdownlint "**/*.md" --ignore docs/images/

  deploy:
    needs: build
    if: github.event_name == 'push' && github.ref == 'refs/heads/main'
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: 3.x
      - run: pip install -r requirements.txt
      - run: mkdocs gh-deploy --force
```

### Contribution Workflow

```
1. Contributor opens Issue proposing a change
2. Maintainer assigns / approves
3. Contributor creates branch: `feature/chapter-5-loops`
4. Contributor writes content on branch
5. Contributor opens Pull Request with clear description
6. Maintainer reviews (checks formatting, accuracy, tone)
7. Changes requested if needed
8. Once approved, maintainer merges to main
9. GitHub Actions builds and deploys automatically
```

### Review Checklist for PRs

- [ ] Formatting follows STYLE-GUIDE.md
- [ ] All code examples are valid Python (runnable)
- [ ] Headings follow hierarchy rules
- [ ] Images have alt text
- [ ] Links work (internal and external)
- [ ] Tone matches "Smart Kuya" voice
- [ ] Technical accuracy verified
- [ ] No plagiarism or copyright issues
- [ ] Spell check passes

### Local Development Setup

```bash
# Install dependencies
pip install mkdocs mkdocs-material

# Start local server
mkdocs serve

# Build the book
mkdocs build

# Check for broken links
mkdocs build --strict
```

Visit `http://localhost:8000` to preview.

---

## 7. ESSENTIAL PLUGINS

### mkdocs-material (Theme)
- The Material for MkDocs theme
- Built-in search, dark mode, copy buttons, callouts
- **Required**

### mkdocs-simple-plug
- Simple plugin system

### mkdocs-with-pdf
- Export book to PDF
- `pip install mkdocs-with-pdf`

### mkdocs-minify-plugin
- Minify CSS/JS for faster page loads
- Important for readers with slow internet (Filipino context)

### mkdocs-rss-plugin
- Generate RSS feed for new chapters
- Helps community stay updated

### mkdocs-redirects
- Handle URL redirects (important when restructuring)

### mkdocs-jupyter
- Embed Jupyter notebooks directly in the book
- For chapters with data science/ML content

### mkdocs-awesome-pages-plugin
- Auto-generate navigation from file structure
- Supports custom ordering and grouping

### mkdocs-glightbox
- Lightbox for images
- Click to zoom

---

## 8. GITHUB PAGES DEPLOYMENT

### Basic Setup

1. Repository settings → Pages → Source: `GitHub Actions` (recommended) or `Deploy from a branch`
2. If using GitHub Actions: Deploy from the `gh-pages` branch (auto-created by `mkdocs gh-deploy`)
3. Custom domain: Add `CNAME` file to `docs/`

### Publishing Strategy

| Strategy | How | Pros |
|----------|-----|------|
| **`gh-deploy`** | `mkdocs gh-deploy` pushes to `gh-pages` branch | Simple, automatic, one-command deploy |
| **GitHub Actions** | Workflow builds and deploys on push | Full control, CI checks before deploy |
| **Manual** | Build locally, push `site/` to branch | Most control, no automation |

**Recommendation**: GitHub Actions (Option 2) -- gives you CI checks + automatic deploy.

---

## 9. OPEN-SOURCE BOOK COMMUNITY PATTERNS

### Successful Models to Study

| Book | Tool | Stars | Key Lesson |
|------|------|-------|------------|
| **The Rust Book** | mdBook | 17.8k | Consistent chapter structure, `ci/` for spellchecking, `listings/` for code examples |
| **Automate the Boring Stuff** | Markdown + custom | 10k+ | Free online, print version available, exercises with solutions |
| **The Odin Project** | Markdown + custom | 12.5k | Community-driven, PR-based contributions, clear contribution guide |
| **FastAPI Docs** | MkDocs + Material | -- | Best-in-class MkDocs example, embedded code examples with syntax highlighting |
| **Pydantic Docs** | MkDocs + Material | -- | Excellent callout/admonition usage, search functionality |
| **Ruff Docs** | MkDocs + Material | -- | Clean, minimal, fast |

### Community Engagement Strategies

1. **Discord/Slack server**: `#help`, `#show-your-work`, `#boss-fight`, `#side-quests` channels
2. **Weekly rhythm**: New chapter draft every week, community review every month
3. **Gamification**: XP system, badges, achievements (as planned in the book)
4. **Companion content**: YouTube walkthroughs, TikTok clips, Twitter/Reddit engagement
5. **First-time contributor friendly**: Label issues as `good-first-issue`, `welcome-contribution`
6. **Celebration**: Merge PRs with celebratory messages, feature contributors

---

## 10. ACCESSIBILITY & PERFORMANCE

### Accessibility (WCAG 2.1 AA)

- **Alt text**: Every image needs descriptive alt text
- **Color contrast**: Ensure text meets 4.5:1 contrast ratio
- **Keyboard navigation**: Material theme supports this by default
- **Screen readers**: Use semantic HTML (headings, lists, tables)
- **Language attribute**: Set `site_language` in `mkdocs.yml` for proper lang attribute
- **Skip links**: Material theme includes "Skip to content" link

### Performance (Critical for Filipino Context)

- **Image optimization**: Use WebP format, compress with `cwebp` or `sharp`
- **Lazy loading**: Material theme lazy-loads images by default
- **Minification**: Use `mkdocs-minify-plugin`
- **CDN**: GitHub Pages is fast globally; consider Cloudflare in front
- **Offline support**: Consider service worker for cached chapters
- **Data-conscious design**: Keep pages under 1MB where possible (data pack mentality)

---

## 11. VERSIONING & RELEASE STRATEGY

### Versioning Model

```
v0.1.0 -- First 5 chapters (early access)
v0.2.0 -- 10 chapters + community review
v0.3.0 -- 15 chapters
v0.4.0 -- 20 chapters
v1.0.0 -- Complete book (first edition)
v1.1.0 -- Post-launch corrections
v2.0.0 -- Second edition (major updates)
```

### Pre-release Checklist

- [ ] All code examples tested and runnable
- [ ] Broken links fixed
- [ ] Spell check passes
- [ ] Community review period complete (2-4 weeks)
- [ ] Accessibility audit
- [ ] Mobile responsive testing
- [ ] PDF export tested (if applicable)
- [ ] SEO metadata reviewed
- [ ] Analytics tracking set up

---

## 12. SEO & DISCOVERABILITY

### On-Page SEO

- **Meta descriptions**: Set `site_description` in `mkdocs.yml`
- **Open Graph tags**: Material theme includes OG tags by default
- **Sitemap**: `mkdocs.yml` enables `sitemap` plugin automatically
- **Canonical URLs**: Set `site_url` in `mkdocs.yml`
- **Heading structure**: Clear H1/H2/H3 hierarchy helps search engines

### Content SEO

- Include target keywords naturally in chapter titles and first paragraphs
- Use descriptive file names (not `chapter1.md` -- use `variables-and-data-types.md`)
- Internal linking between related chapters
- External links to authoritative sources (Python docs, PEPs, academic papers)

---

## 13. LICENSE & CREDIT

### Recommended License: CC BY 4.0

- **Attribution required**: Anyone can use, share, adapt -- but must credit the authors
- **Open and permissive**: Encourages translations, adaptations, and community contributions
- **Compatible with GitHub**: Widely understood and supported

### Additional Files Needed

- `LICENSE.md` -- Full CC BY 4.0 text
- `CREDITS.md` -- List of all contributors, translators, reviewers
- `CONTRIBUTING.md` -- How to contribute (code of conduct, workflow, guidelines)
- `CODE_OF_CONDUCT.md` -- Adopt [Contributor Covenant](https://www.contributor-covenant.org/)

---

## 14. LOCAL DEVELOPMENT REFERENCE

### Quick Start

```bash
# Clone the repo
git clone <repo-url>
cd book-python

# Install dependencies
pip install -r requirements.txt

# Start local server (hot-reload enabled)
mkdocs serve

# Open in browser
# http://localhost:8000
```

### Requirements File

```txt
mkdocs>=1.5.0
mkdocs-material>=9.5.0
mkdocs-simple-plug
mkdocs-minify-plugin
mkdocs-rss-plugin
mkdocs-redirects
mkdocs-glightbox
```

### mkdocs.yml Template

```yaml
site_name: A Filipino's Guide to Python
site_description: Learn Python the "Bahala Na" way
site_url: https://your-username.github.io/book-python
repo_url: https://github.com/your-username/book-python
repo_name: book-python

theme:
  name: material
  palette:
    # Light mode
    - media: "(prefers-color-scheme: light)"
      scheme: default
      primary: indigo
      accent: indigo
      toggle:
        icon: material/toggle-switch-off-outline
        name: Switch to dark mode
    # Dark mode
    - media: "(prefers-color-scheme: dark)"
      scheme: slate
      primary: indigo
      accent: indigo
      toggle:
        icon: material/toggle-switch
        name: Switch to light mode
  features:
    - navigation.instant
    - navigation.instant.progress
    - navigation.tracking
    - navigation.sections
    - navigation.top
    - search.highlight
    - search.share
    - search.suggest
    - content.code.copy
  icon:
    repo: fontawesome/brands/github
  language: en

plugins:
  - search
  - minify:
      minify_html: true
  - rss:
      match_url: blog/*

markdown_extensions:
  - toc:
      permalink: true
  - pymdownx.highlight:
      anchor_linenums: true
  - pymdownx.inlinehilite
  - pymdownx.snippets
  - pymdownx.superfences
  - attr_list
  - md_in_html
  - pymdownx.emoji:
      emoji_index: !!python/name:material.extensions.emoji.twemoji
      emoji_generator: !!python/name:material.extensions.emoji.to_svg

nav:
  - Home: index.md
  - Getting Started:
      - getting-started/index.md
      - getting-started/install-python.md
  - Part 1: Fundamentals:
      - part-1-fundamentals/index.md
      - part-1-fundamentals/variables.md
  # ... etc
```

---

## 15. COMMON PITFALLS AVOIDED BY SUCCESSFUL OPEN-SOURCE BOOKS

| Pitfall | How to Avoid |
|---------|-------------|
| **Tutorial hell** (endless tutorials, no original work) | Include "Boss Fight" challenges that require original thinking |
| **Outdated content** | CI checks that verify code examples still run; regular update schedule |
| **Inconsistent tone** | STYLE-GUIDE.md + PR review checklist |
| **No community involvement** | `good-first-issue` labels, Discord server, transparent roadmap |
| **Poor navigation** | Part-level index pages, clear breadcrumb trails, search enabled |
| **Broken links** | GitHub Action that runs `linkchecker` or similar on every PR |
| **No mobile support** | Material theme is responsive by default; test on mobile |
| **Ignoring accessibility** | WCAG checklist in PR review; alt text for all images |
| **Slow page loads** | Image optimization, minification, WebP format |
| **No offline reading** | Consider PDF export via `mkdocs-with-pdf` |

---

*This file was compiled from research on The Rust Book, MkDocs Material, Write the Docs community, and successful open-source documentation projects. Updated for the "A Filipino's Guide to Python" project.*
