# Chapter 18: AI-Assisted Coding and Vibecoding

??? example "📋 Chapter Info"
    | | |
    |---|---|
    | **Difficulty** | ⭐⭐ Intermediate |
    | **Time** | 25 min |
    | **XP** | +100 XP |

> **Story Hook:** You're stuck on a bug for 3 hours. You've tried everything: print debugging, rubber duck debugging, even a nap. The error message makes no sense. You think about asking in the Python Discord, but it's 2 AM. Then you remember: you have AI. You paste the code, describe the problem, and within seconds, the AI suggests a fix. It works. You think: "This is either amazing or terrifying. Probably both."

---

## What You'll Learn

- What AI-assisted coding is and how it works
- Prompt engineering for Python
- Using AI as a learning tool (not a crutch)
- Auditing AI-generated code
- The "vibecoding" workflow

## AI as a Creative Partner

AI tools like GitHub Copilot, ChatGPT, and Claude are **partners**, not replacements. They're like having a senior developer looking over your shoulder -- helpful, but they make mistakes too.

### When to Use AI

| Use AI For | Don't Use AI For |
|-----------|-----------------|
| Understanding error messages | Writing code you won't read |
| Brainstorming approaches | Avoiding learning fundamentals |
| Code review and suggestions | Cheating on assignments |
| Learning new concepts | Replacing critical thinking |

??? note "💻 Low-Spec Laptop?"

    You don't need a powerful machine to be a great coder:

    - **Offline editors**: Lightweight editors like VS Code (with minimal extensions) or Sublime Text run well on older laptops. They provide syntax highlighting and auto-completion without the overhead of heavy IDEs.
    - **Keep extensions minimal**: Each VS Code extension uses memory. Stick to essentials like Python, Pylance, and one linter. You can always add more later.
    - **Use the terminal**: Learn to run Python from the command line (`python script.py`). It uses almost no resources compared to running a full IDE.
    - **Pro tip**: The best coders aren't the ones with the fastest machines — they're the ones who understand their tools deeply. A simple editor + strong fundamentals beats a fancy setup every time.

## Prompt Engineering for Python

The quality of AI output depends on the quality of your prompt:

### Bad Prompt
```
Fix my code
```

### Good Prompt
```
I'm getting a TypeError on line 15 of my Python script.
The error says: "can only concatenate str (not 'int') to str"
Here's the code:

```python
name = "Juan"
age = 25
print("Age: " + age)
```

What's wrong and how do I fix it?
```

### Best Prompt
```
I'm a beginner learning Python. I'm getting this error:
TypeError: can only concatenate str (not 'int') to str

Here's my code:
```python
name = "Juan"
age = 25
print("Age: " + age)
```

Please explain:
1. What the error means (in simple terms)
2. How to fix it
3. Why the fix works
4. One similar exercise for practice
```

## The Vibecoding Workflow

Andrej Karpathy's "vibecoding" is a workflow where you describe what you want in natural language and AI generates the code:

1. **Describe** what you want in plain language
2. **Generate** the code with AI
3. **Read** the generated code carefully
4. **Test** it and see if it works
5. **Modify** based on results
6. **Repeat** until it's right

```
You: "Write a function that calculates jeepney fare"
AI: [generates code]
You: [reads and tests]
You: "Make it handle peak hour surcharges"
AI: [updates code]
You: [tests again]
...
```

## Auditing AI-Generated Code

AI can make mistakes. Always audit the code:

```python
# AI-generated code (potentially buggy)
def calculate_fare(distance, passengers):
    fare = 13 + (distance - 4) * 1.5  # Bug: doesn't handle distance <= 4
    fare += (passengers - 1) * 1  # Bug: doesn't handle 1 passenger
    return fare

# Audited and fixed
def calculate_fare(distance, passengers):
    base = 13.0
    if distance > 4:
        base += (distance - 4) * 1.5
    if passengers > 1:
        base += (passengers - 1) * 1.0
    return base
```

## Building an AI-Powered Code Assistant

Let's build a simple tool that uses AI concepts:

```python
# Simple Code Assistant
# Chapter 18

import re


class CodeAssistant:
    """A simple code analysis assistant (simulating AI-like features)."""

    def __init__(self):
        self.patterns = self._load_patterns()

    def _load_patterns(self):
        """Common code patterns and suggestions."""
        return {
            "missing_colon": {
                "pattern": r"if\s+.*(?<!:)\s*$",
                "message": "Missing colon (:) at the end of this line.",
                "fix": "Add ':' at the end of the if/for/while/def line.",
            },
            "missing_quote": {
                "pattern": r'print\([^)]*$',
                "message": "Possibly missing closing quote or parenthesis.",
                "fix": "Check that all strings have matching quotes.",
            },
            "f_string_missing_brace": {
                "pattern": r'f["\'].*\{[^}]*$',
                "message": "Possibly missing closing brace in f-string.",
                "fix": "Ensure all { have matching }.",
            },
        }

    def analyze(self, code):
        """Analyze code for common issues."""
        issues = []
        lines = code.split("\n")

        for i, line in enumerate(lines, 1):
            for name, info in self.patterns.items():
                if re.search(info["pattern"], line.strip()):
                    issues.append({
                        "line": i,
                        "type": name,
                        "message": info["message"],
                        "fix": info["fix"],
                    })

        return issues

    def suggest_improvements(self, code):
        """Suggest code improvements."""
        suggestions = []

        # Check for long lines
        for i, line in enumerate(code.split("\n"), 1):
            if len(line) > 80:
                suggestions.append({
                    "line": i,
                    "type": "style",
                    "message": f"Line is {len(line)} characters (max 80).",
                    "fix": "Break the line into multiple lines.",
                })

        # Check for missing docstrings
        if "def " in code and '"""' not in code and "'''" not in code:
            suggestions.append({
                "line": 0,
                "type": "documentation",
                "message": "Functions missing docstrings.",
                "fix": "Add a docstring (\"\"\"...\"\"\") to each function.",
            })

        return suggestions


# Usage
assistant = CodeAssistant()

code = """
def calculate_fare(distance passengers):
    fare = 13 + (distance - 4) * 1.5
    fare += (passengers - 1) * 1
    return fare

result = calculate_fare(5 3)
print("Fare: " + result)
"""

issues = assistant.analyze(code)
if issues:
    print("Issues found:")
    for issue in issues:
        print(f"  Line {issue['line']}: {issue['message']}")
        print(f"    Fix: {issue['fix']}")
else:
    print("No issues found!")

suggestions = assistant.suggest_improvements(code)
if suggestions:
    print("\nSuggestions:")
    for s in suggestions:
        print(f"  {s['message']}")
```

## Summary

- AI is a partner, not a replacement for learning
- Good prompts produce good results
- Always read and audit AI-generated code
- The vibecoding workflow: describe, generate, read, test, modify
- AI tools accelerate learning when used correctly

## Boss Fight

??? warning "Boss Fight: AI Code Review Tool"

    Build a comprehensive code review tool that:

    1. Checks for common Python errors
    2. Enforces PEP 8 style guidelines
    3. Suggests improvements for readability
    4. Detects potential security issues
    5. Generates a review report

    **Hint:** Use Python's `ast` module for parsing code structure.

??? success "You did it! Level Up!"
    +150 XP. You built an AI-assisted tool. Ang galing!

## Side Quests

??? note "Optional: Side Quest"
    - Create a "code explanation" tool that explains any Python code in Tagalog
    - Build a "best practices" checker specific to Filipino coding communities
    - Add a "difficulty estimator" that predicts how hard a problem is

## Further Reading

- [Andrej Karpathy on Vibecoding](https://twitter.com/karpathy/status/1748414944097391413)
- [Real Python: Prompt engineering](https://realpython.com/prompt-engineering/)

---

??? example "Portfolio Tip"

    **GitHub README**: Include your code assistant tool with a note: "I use AI as a partner, not a crutch. Every AI-generated line of code is audited, tested, and understood before I use it." This shows you're a responsible developer, not just a prompt typist.

    **LinkedIn**: Post: "Learned to code WITH AI, not INSTEAD of learning. Built a code analysis tool that checks for common Python errors, enforces PEP 8, and suggests improvements. The vibecoding workflow: describe, generate, read, test, modify. #Python #AICoding". This is a hot topic that shows you're current.

    **Interview Talking Point**: "I use AI as a creative partner -- for understanding error messages, brainstorming approaches, and code review. But I always audit AI-generated code for bugs, test it thoroughly, and understand every line. I know the difference between using AI to learn and using AI to replace thinking."

??? example "🧠 Reflection — AI-Assisted Coding and Vibecoding"

    - **What did you learn?** AI is a creative partner that accelerates coding when you write good prompts and always audit the generated code.
    - **How can you apply this?** Use AI to debug your programs at 2 AM when no one in your barkada is online, or to explain error messages in Tagalog.
    - **What's next?** How do you balance using AI for help while still building your own problem-solving skills?

??? checkbox "✅ Chapter Checklist"

    - [ ] Write effective prompts that include context, errors, and code samples
    - [ ] Follow the vibecoding workflow: describe, generate, read, test, modify
    - [ ] Audit AI-generated code for bugs and edge cases
    - [ ] Know when to use AI and when to think through a problem yourself
    - [ ] Build a simple code analysis tool with pattern matching

---

*Next: [Chapter 19: Open Source](chapter-19-open-source.md) -- Contributing to the community.*
