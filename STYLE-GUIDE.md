# Style Guide for Bahala Na Python

Every chapter should sound like it was written by the same person: the **Smart Kuya** who's been through this, makes mistakes too, and speaks Taglish naturally.

## Voice and Tone

### The Smart Kuya

- Write like a knowledgeable older sibling, not a professor
- Use "kayo/ka" (you) directly -- address the reader personally
- Admit mistakes: *"Naiimutan ko pa rin kung paano..."*
- Celebrate small wins: *"Galing mo! Working na!"*
- Normalize struggle: *"Confused? Good. That means you're learning."*

### Taglish Guidelines

```markdown
# Good: Natural code-switching
Let's try it. Ibaril natin ang code:

```python
name = "Juan"
print(f"Kumusta, {name}!")
```

# Good: Taglish for explanation, English for code
Ang variable ay parang lalagyan. I-click mo lang:

# Avoid: Over-translating technical terms
Don't translate "variable," "function," "API" -- these are used in English
everywhere in Philippine tech.

# Good: Tagalog for emotional/cultural moments
Kaya mo 'yan. Hindi ka nag-iisa sa journey na 'to.
```

## Sentence Structure

- Keep paragraphs to 3-5 sentences max
- One idea per paragraph
- Front-load important information
- Use active voice: *"Python stores this in a variable"* not *"This is stored by Python"*

## Code Presentation

### Code Blocks

```markdown
Basic code block:
```python
x = 5
print(x)
```

With filename and line numbers:
```python title="hello.py" linenums="1"
x = 5
print(x)
```

Highlighted lines:
```python title="hello.py" linenums="1" hl_lines="2 3"
x = 5
y = x + 1  # This line is highlighted
print(y)   # This line is highlighted
```

Terminal output:
```bash
$ python hello.py
10
```
```

### Code Comments

Use Taglish for comments when it adds warmth:

```python
# Check kung valid ang input bago i-process
if age >= 18:
    print("Adult na!")
else:
    print("Bata pa, walang access")
```

## Callout Boxes

Material for MkDocs supports native callout blocks. Use them consistently:

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

??? success "Level Up!"
    You just completed your first program! Congratulations!
```

## Chapter Structure

Every chapter must follow this pattern:

```markdown
# Chapter N: Chapter Title

<!-- Story hook: 1-2 paragraph narrative -->
You're running a sari-sari store in your barangay...

## What You'll Learn

- Variable assignment and data types
- Working with dictionaries
- File I/O basics

## Tutorial Sections

Step-by-step code walkthrough with explanations.

## Boss Fight

??? warning "Boss Fight"
    Combine everything you've learned.

## Side Quests

??? note "Optional: Side Quest"
    Extra practice for curious minds.

## Summary

- Key concepts covered
- What to read next

## Further Reading

- Links to Python docs, related chapters
```

## Formatting Rules

### Headings

- One H1 per file: `# Chapter Title`
- H2 for sections: `## Section`
- H3 for subsections: `### Subsection`
- Never skip heading levels

### Tables

- Keep tables under 6 columns
- For wider tables, use a separate reference page

### Images

- Store in `docs/images/`
- Use descriptive filenames: `sari-sari-store.png` not `img1.png`
- Always include alt text: `![Sari-sari store illustration](images/sari-sari-store.png)`
- Use WebP format for better compression

### Links

- Internal: `[Next chapter](variables.md)`
- External with title: `[Python docs](https://docs.python.org/3/ "Python Documentation")`

## Filipino Vocabulary

Use these naturally throughout the book:

| English | Tagalog/Filipino | When to Use |
|---------|-----------------|-------------|
| Resourcefulness | Diskarte | Problem-solving situations |
| Courage | Lakas ng loob | Encouragement moments |
| Community | Bayanihan | Collaboration, open source |
| Let's try | Bahala na | Starting something new |
| You can do it | Kaya mo yan | Encouragement |
| Hang out / break | Tambay | Rest, pause, casual moments |
| Trust relationship | Suki | Mentorship, recurring patterns |
| Let's eat | Kain muna | Breaks, rewards |
| Amazing | Grabe | Amazement, praise |
| Forget it / whatever | Sige na lang | Giving up on perfection |
| Oh my | Ay nako | Surprise, frustration |

## What to Avoid

- **Academic tone**: No "the aforementioned" or "it is imperative to note"
- **Assuming prior knowledge**: Define every technical term on first use
- **Long paragraphs**: Break up text with code, callouts, and images
- **English-only**: Taglish is a feature, not a bug
- **Condescending tone**: Never talk down to beginners
- **Cultural stereotypes**: Be specific and authentic, not caricature
