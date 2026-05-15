# Chapter 19: Open Source and Your First Contribution

??? example "📋 Chapter Info"
    | | |
    |---|---|
    | **Difficulty** | ⭐⭐ Intermediate |
    | **Time** | 30 min |
    | **XP** | +100 XP |

> **Story Hook:** You've been using open-source software for months. Python itself is open source. The libraries you import (requests, pandas, matplotlib) are all open source. You've never contributed to one. Today, that changes. You make your first pull request. Your hands are sweating. You click "Submit." And then: the most beautiful thing in programming. A review comment: "Great first contribution! Could you add a test?" You smile. You belong here now.

---

## What You'll Learn

- What open source is and why it matters
- How GitHub works: forks, branches, pull requests
- Reading and understanding existing code
- Making your first contribution
- The open-source code of conduct

## What Is Open Source?

**Open source** means the code is publicly available for anyone to use, modify, and share. Python, Linux, VS Code, React -- all open source.

### Why Contribute?

- **Learn faster**: Reading other people's code teaches you more than any tutorial
- **Build a portfolio**: Your contributions become proof of your skills
- **Give back**: You've used open source; now contribute to it
- **Build community**: Connect with developers worldwide
- **Real impact**: Your code helps thousands (or millions) of people

## GitHub Basics

### Fork: Your Own Copy

A **fork** is a copy of someone else's repository. You make changes in your fork, then request to merge them into the original.

### Branch: A Parallel Line

A **branch** is a parallel version of the code. You create a branch for each feature or fix, so you don't break the main code.

### Pull Request: The Request to Merge

A **pull request (PR)** is your request to merge your changes into the original repository. It's also where code review happens.

## Your First Contribution: A Step-by-Step Guide

### Step 1: Find a Project

Look for projects with `good-first-issue` or `help-wanted` labels:

- [first-contributions](https://github.com/first-contributions/first-contributions) -- Designed for first-time contributors
- [good-first-issue](https://goodfirstissue.dev) -- Aggregates beginner-friendly issues

### Step 2: Fork the Repository

1. Go to the project's GitHub page
2. Click the "Fork" button (top right)
3. Clone your fork: `git clone <your-fork-url>`

??? note "🐌 Slow Internet?"

    Cloning large repositories can take a long time on slow connections:

    - **Download during off-peak hours**: Clone repos at night or early morning when your internet is less congested. Many Philippine ISPs have more bandwidth available during these hours.
    - **Shallow clones**: Use `git clone --depth 1 <url>` to download only the most recent commit instead of the full history. This can reduce download size by 90% for large projects.
    - **Sparse checkouts**: For very large repos, you can download only the specific folders you need:

    ```bash
    git clone --filter=blob:none --sparse <url>
    cd project-name
    git sparse-checkout set path/to/folder/you/need
    ```

    - **Pro tip**: Start with small projects for your first contributions. Look for repos under 10 MB — documentation fixes and typo corrections don't require downloading massive codebases.

### Step 3: Create a Branch

### Step 3: Create a Branch

```bash
git checkout -b feature/my-contribution
```

### Step 4: Make Your Changes

Edit files, add code, fix bugs. Test everything.

### Step 5: Commit Your Changes

```bash
git add .
git commit -m "Fix: correct typo in README"
```

### Step 6: Push and Create a Pull Request

```bash
git push origin feature/my-contribution
```

Then go to GitHub and click "Compare & pull request."

### Step 7: Respond to Review

Maintainers will review your PR. They might ask for changes. Make them, push again, and wait for approval.

## Understanding the Code of Conduct

Every serious open-source project has a Code of Conduct. It's not just rules -- it's a commitment to making the community welcoming:

- Be kind and patient
- Accept constructive criticism
- Focus on what's best for the community
- Show empathy towards others

**Remember**: No question is stupid. No contribution is too small.

## Contributing to This Book

This book IS an open-source project. Your contributions matter:

### What You Can Contribute

| Type | Examples |
|------|----------|
| **Typos** | Fix misspelled words, grammar errors |
| **Explanations** | Make confusing explanations clearer |
| **Examples** | Add new code examples with Filipino context |
| **Exercises** | Create new Boss Fights and side quests |
| **Translations** | Translate chapters to Tagalog, Cebuano, etc. |
| **Design** | Add illustrations, icons, diagrams |

### How to Contribute to This Book

1. Fork this repository
2. Create a branch: `git checkout -b fix/chapter-3-typos`
3. Edit the markdown files in `docs/`
4. Preview: `mkdocs serve`
5. Commit and push
6. Open a Pull Request

## Writing a Good Pull Request

### PR Title
```
Fix: correct typo in chapter 3 about variable types
```

### PR Description
```markdown
## What I Changed

Fixed a typo in chapter 3 where "dictionary" was spelled "dictinary" in the code example on line 45.

## Why This Matters

Typos in code examples can confuse beginners. This correction ensures the code runs correctly.

## Testing

- Ran `mkdocs serve` to verify the build works
- Checked that the corrected code example runs in Python
```

## Summary

- Open source means code is freely available to use and modify
- GitHub workflow: fork → branch → change → commit → push → PR
- Every contribution matters, no matter how small
- Code of conduct keeps communities welcoming
- You can contribute to this book right now

## Boss Fight

??? warning "Boss Fight: Your First Open-Source Contribution"

    Make a real contribution to an open-source project:

    1. Find a project with a `good-first-issue` label
    2. Fork the repository
    3. Create a branch and make your changes
    4. Open a pull request
    5. Respond to review comments

    **Bonus:** Contribute to this book! Fix a typo, add an example, or improve an explanation.

??? success "You did it! Level Up!"
    +150 XP. You made your first open-source contribution. Ang galing!

## Side Quests

??? note "Optional: Side Quest"
    - Contribute to 3 different open-source projects
    - Write your first documentation improvement
    - Help a beginner with their first PR
    - Start your own open-source project

## Further Reading

- [first-contributions tutorial](https://github.com/first-contributions/first-contributions)
- [GitHub's guide to pull requests](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request)
- [Open Source Guide](https://opensource.guide/)

---

??? example "Portfolio Tip"

    **GitHub README**: Your first open-source contribution is a badge of honor. Pin the PR on your GitHub profile. Add to your personal README: "Open source contributor. Fork → branch → commit → push → PR. I believe in bayanihan for developers."

    **LinkedIn**: Post a screenshot of your merged PR with the caption: "My first open-source contribution is merged! From reading other people's code to submitting a pull request -- this is what bayanihan looks like in the developer world. #OpenSource #Python". Link to the PR.

    **Interview Talking Point**: "I've contributed to open-source projects following the full GitHub workflow: forking, branching, making changes, and submitting pull requests. I understand code of conduct, write clear PR descriptions, and respond to review feedback. Open source taught me how to collaborate with developers I've never met."

??? example "🧠 Reflection — Open Source and Your First Contribution"

    - **What did you learn?** Open source is a collaborative model where anyone can fork, modify, and contribute to projects through pull requests.
    - **How can you apply this?** Contribute to Philippine-focused open-source projects like the PSGC API or help translate coding tutorials into Filipino languages.
    - **What's next?** How could you start your own open-source project that solves a problem in your community?

??? checkbox "✅ Chapter Checklist"

    - [ ] Understand the fork → branch → commit → push → PR workflow
    - [ ] Find a project with a `good-first-issue` label
    - [ ] Make your first pull request to an open-source project
    - [ ] Write a PR description explaining what, why, and how you tested
    - [ ] Follow a project's code of conduct and CONTRIBUTING guidelines

---

*Next: [Chapter 20: Boss Fight 3](chapter-20-boss-fight-3.md) -- The ultimate challenge.*
