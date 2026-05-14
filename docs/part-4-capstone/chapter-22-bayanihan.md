# Chapter 22: Bayanihan & Open Source

> **Story Hook:** You've built your sari-sari store system. Your Lola uses it every day. Your tito asks if you can build something similar for his hardware store. Your barkada wants their own versions. You realize: "I'm not the only one who needs this. What if we built it together?" That's the spirit of bayanihan. That's open source.

---

## What You'll Learn

- How open source works in practice
- How to contribute to existing projects
- How to collaborate on projects with others
- How to license your own work
- The Filipino values behind open source

## What Is Open Source?

Open source means the code is **free for anyone to use, modify, and share**. It's not just about the price -- it's about the philosophy:

> "Given enough eyeballs, all bugs are shallow." -- Linus's Law

In the Filipino context, open source is pure bayanihan:

- **Bayanihan** = neighbors lifting a bahay kubo together
- **Open source** = developers building software together
- Same spirit. Different tools.

## Why Open Source Matters for Filipino Developers

### 1. It's Free

Most Filipino developers don't have budgets for expensive software. Open source tools are free forever.

### 2. It's Community-Driven

Open source projects are built by people who care about solving real problems. Filipino developers contribute to projects that matter to the Philippines:

- **Philippine Statistics Authority API** -- Community-maintained data
- **Bayanihan** -- Open-source disaster relief coordination
- **Edukasyon.ph** -- Open educational resources

### 3. It Builds Your Portfolio

Your GitHub profile is your resume. Every contribution -- even fixing a typo -- shows that you can collaborate, write clean code, and give back.

## How to Contribute to Existing Projects

### Step 1: Find a Project You Care About

Look for projects that solve problems you've experienced:

| Platform | How to Find Projects |
|----------|---------------------|
| **GitHub Explore** | github.com/explore -- trending repos |
| **Good First Issue** | github.com/contributegood/first-contributions |
| **First Contributions** | github.com/firstcontributions/first-contributions |
| **Hacktoberfest** | hacktoberfest.com -- October events |

### Step 2: Read the CONTRIBUTING.md

Every good project has a `CONTRIBUTING.md` file. It tells you:

- How to set up the project
- Coding standards
- How to submit changes
- Code of conduct

### Step 3: Start Small

Don't try to rewrite the whole project. Start with:

1. **Documentation fixes** -- typos, broken links, unclear explanations
2. **Bug reports** -- open an issue describing the problem
3. **Small features** -- one function, one test
4. **Tests** -- writing tests is one of the most valuable contributions

### Step 4: Make Your First Pull Request

```bash
# Fork the repository (create your own copy)
# Clone your fork
git clone https://github.com/your-username/project.git
cd project

# Create a branch for your change
git checkout -b feature/fix-typo-in-readme

# Make your changes
# (edit files with your text editor)

# Commit your changes
git add .
git commit -m "fix: fix typo in README installation steps"

# Push to your fork
git push origin feature/fix-typo-in-readme

# Open a Pull Request on GitHub
```

## Writing a Good Pull Request

A PR is a **conversation**, not a transaction. Here's how to make it good:

```markdown
## What does this PR do?
Fixes the broken link in the installation section. The old link
pointed to python.org/downloads/2.7 which no longer exists.

## Why?
Beginners following the tutorial get a 404 error. This breaks
the learning flow and causes frustration.

## How did you test it?
Clicked the link manually. Verified it points to the correct
Python 3 download page.

## Screenshots (if applicable)
[Before: 404 error]
[After: correct download page]
```

??? tip "Diskarte"
    Small, focused PRs get reviewed faster. One change per PR. Not ten. One. If you want to make ten changes, make ten PRs.

## Creating Your Own Open-Source Project

### Step 1: Start With a Problem

The best open-source projects solve problems the creator has experienced:

```python
# Example: A simple library for Filipino phone numbers
# Chapter 22

def validate_phonenumber(number: str) -> bool:
    """Validate a Philippine phone number.

    Accepts formats:
    - 09171234567
    - +639171234567
    - 639171234567
    """
    # Remove common separators
    cleaned = number.replace(" ", "").replace("-", "")

    # Add country code if missing
    if cleaned.startswith("09"):
        cleaned = "63" + cleaned[1:]
    elif not cleaned.startswith("+63") and not cleaned.startswith("63"):
        return False

    # Must be 11 digits after country code
    digits = cleaned.lstrip("+")
    return digits.startswith("63") and len(digits) == 13


def format_phonenumber(number: str) -> str:
    """Format a Philippine phone number for display."""
    if validate_phonenumber(number):
        cleaned = number.replace(" ", "").replace("-", "")
        if cleaned.startswith("09"):
            return f"+63{cleaned[1:]}"
        return cleaned
    raise ValueError(f"Invalid Philippine phone number: {number}")


# Usage
print(validate_phonenumber("09171234567"))     # True
print(format_phonenumber("09171234567"))       # +639171234567
print(format_phonenumber("+639171234567"))     # +639171234567
```

### Step 2: Write Good Documentation

Your `README.md` is your project's front page. It should answer:

1. **What does this project do?**
2. **Why was it built?**
3. **How do I install it?**
4. **How do I use it?** (with examples)
5. **How do I contribute?**

### Step 3: License It

Use [choosealicense.com](https://choosealicense.com/) to pick a license. For this book, we use **CC BY 4.0**. For code, common choices:

| License | What It Allows | Best For |
|---------|---------------|----------|
| **MIT** | Almost anything | Permissive, popular |
| **Apache 2.0** | Almost anything + patent protection | Larger projects |
| **GPL** | Must share modifications | Copyleft, free software |
| **CC BY 4.0** | Share and adapt with credit | Documentation, non-code |

### Step 4: Invite Contributions

```markdown
## Contributing

We welcome contributions! Here's how:

1. Fork this repo
2. Create a branch: `git checkout -b feature/my-feature`
3. Make your changes
4. Submit a Pull Request

**Good first issues:** Look for labels like `good-first-issue` or `help-wanted`.
```

## Filipino Open-Source Projects to Study

### Community-Driven Projects

- **[first-contributions](https://github.com/firstcontributions/first-contributions)** -- The project designed to help you make your first contribution. Over 100,000 first-time contributors.
- **[freeCodeCamp](https://github.com/freeCodeCamp/freeCodeCamp)** -- 40,000+ developers got jobs through this open-source platform.
- **[The Odin Project](https://github.com/TheOdinProject)** -- Free, open-source full-stack curriculum.

### Philippine-Focused Projects

- **[PSGC API](https://github.com/OSSPhilippines/psgc-api)** -- Philippine Standard Geographic Codes API. Community-maintained geographic data.
- **[Edukasyon.ph](https://edukasyon.ph/)** -- Open educational resources for Filipino students.
- **Various Discord servers** -- Filipino tech communities on Discord are informal open-source spaces.

## The Open-Source Mindset

Open source isn't just about code. It's about a mindset:

1. **Share what you learn** -- Write tutorials, answer questions, help beginners
2. **Give credit** -- Cite sources, credit inspiration, link to originals
3. **Be patient** -- Code review takes time. Feedback is a gift.
4. **Be kind** -- Everyone was a beginner once. The Python community is welcoming for a reason.
5. **Give back** -- When you're ready, contribute to the projects you use.

## Boss Fight

??? warning "Boss Fight: Bayanihan Toolkit"
    Build a command-line utility that helps Filipino developers find open-source projects to contribute to. Your tool should:

    - Search GitHub for repositories with "good first issue" label
    - Filter by Filipino-related keywords (e.g., "philippines", "tagalog", "filipino")
    - Display results with stars, language, and issue count
    - Save favorite projects to a local JSON file
    - Include a "random project" feature for when you can't decide

    **XP Reward:** 50 XP | **Hint cost:** 10 XP per hint

    ??? hint "Hint 1 (10 XP)"
        Use the GitHub search API: `https://api.github.com/search/repositories?q=good+first+issue+{keyword}`

    ??? hint "Hint 2 (20 XP)"
        Use `requests.get()` with JSON parsing. Each result has `stargazers_count`, `language`, and `open_issues_count`.

    ??? hint "Hint 3 (30 XP)"
        For the random feature, import `random.choice()` from your filtered results list.

## Summary

- Open source is bayanihan for developers
- Start contributing with small changes: docs, bugs, tests
- Write good PRs: describe what, why, and how you tested
- License your projects so others know how to use them
- The Filipino values of bayanihan and diskarte are the spirit of open source

## Side Quests

??? note "Optional: Side Quest"
    - Make your first open-source contribution (even a typo fix counts!)
    - Create a GitHub profile and pin your best projects
    - Write a tutorial for something you just learned and share it
    - Join a Filipino tech Discord server and help someone

## Further Reading

- [First Contributions tutorial](https://github.com/firstcontributions/first-contributions)
- [Open Source Guide](https://opensource.guide/)
- [choosealicense.com](https://choosealicense.com/)

---

*Next: [Chapter 23: Capstone A](chapter-23-capstone-a.md) -- Building the Barangay Management System.*
