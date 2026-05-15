# Chapter 6: Functions and the Budget Tracker

??? example "📋 Chapter Info"
    | | |
    |---|---|
    | **Difficulty** | ⭐⭐ Beginner |
    | **Time** | 35 min |
    | **XP** | +100 XP |

> **Story Hook:** Every week, your parents send you allowance. Every week, you spend it on three things: pamasahe (transport), kain (food), and photocopy (school supplies). By Wednesday, you're already broke. You think: "Kailangan ko ng system. Parang budget tracker sa GCash, pero para sa akin." So you write one -- with functions.

---

## What You'll Learn

- What functions are and why they're useful
- Defining functions with `def`
- Parameters and return values
- Default arguments
- Scope: local vs. global variables

## What Are Functions?

A **function** is a reusable block of code. Instead of writing the same logic over and over, you write it once in a function and call it whenever you need it.

Think of it like a **recipe**:

1. You write the recipe once
2. Whenever you want to cook, you follow the recipe
3. Different ingredients (inputs) → different results (outputs)

```python
# Defining a function
def greet(name):
    print(f"Kumusta, {name}!")

# Calling the function
greet("Juan")
greet("Maria")
greet("Pedro")
```

Output:

```
Kumusta, Juan!
Kumusta, Maria!
Kumusta, Pedro!
```

## Why Functions Matter

Without functions, your code gets long and repetitive:

```python
# Without functions: repetitive
print("Week 1 budget:")
print(f"  Allowance: 500")
print(f"  Spent: 450")
print(f"  Remaining: 50")

print("Week 2 budget:")
print(f"  Allowance: 500")
print(f"  Spent: 380")
print(f"  Remaining: 120")

# With functions: clean and reusable
def print_budget(week, allowance, spent):
    remaining = allowance - spent
    print(f"Week {week} budget:")
    print(f"  Allowance: {allowance}")
    print(f"  Spent: {spent}")
    print(f"  Remaining: {remaining}")

print_budget(1, 500, 450)
print_budget(2, 500, 380)
```

??? tip "Diskarte"
    If you find yourself copying and pasting code, you probably need a function. Functions make code readable, reusable, and easier to fix.

??? note "📱 Phone-Only? No Problem!"

    Coding functions on a phone screen feels cramped, but it's totally doable:

    - **Split-screen approach** — Open this book on one half of your screen and Replit or Pydroid 3 on the other. Most phones support split-screen multitasking.
    - **Voice typing for boilerplate** — Use your phone's voice-to-text to type out function skeletons like `def my_function():` — it's faster than tapping a tiny keyboard.
    - **Pro tip**: Practice writing functions during your commute. Functions are short enough to code on a small screen. Save the longer projects for when you have a bigger screen!

??? tip "⏸️ Pause and Predict"

    **Predict: what happens when you call a function that expects 2 arguments but you only pass 1?**

    Take 30 seconds to think about your answer before reading on. This is how you build real understanding!

## Parameters and Return Values

Functions can take **inputs** (parameters) and produce **outputs** (return values):

```python
def calculate_budget(allowance, expenses):
    """Calculate remaining budget."""
    remaining = allowance - expenses
    return remaining

# Using the function
remaining = calculate_budget(500, 450)
print(f"Remaining: ₱{remaining}")
```

### Multiple Parameters

```python
def calculate_budget(allowance, pamasahe, kain, photocopy):
    """Calculate budget after expenses."""
    total_spent = pamasahe + kain + photocopy
    remaining = allowance - total_spent
    return remaining, total_spent

# Unpack multiple return values
remaining, spent = calculate_budget(500, 100, 200, 50)
print(f"Spent: ₱{spent}, Remaining: ₱{remaining}")
```

## Default Arguments

You can set default values for parameters:

```python
def track_expense(category, amount, budget=500):
    """Track an expense with a default budget."""
    spent = budget - amount
    print(f"{category}: -₱{amount} | Remaining budget: ₱{spent}")

track_expense("Pamasahe", 15)          # Uses default budget of 500
track_expense("Kain", 50, budget=300)  # Custom budget of 300
```

## Building a Budget Tracker

Let's build a complete budget tracker using functions:

```python
# Budget Tracker for Students
# Chapter 6

def create_budget(allowance, categories=None):
    """Create a new budget with spending categories."""
    if categories is None:
        categories = ["pamasahe", "kain", "photocopy", "tambay", "other"]

    budget = {
        "allowance": allowance,
        "categories": {cat: {"allocated": 0, "spent": 0} for cat in categories},
    }
    return budget


def allocate(budget, category, amount):
    """Allocate money to a category."""
    if category not in budget["categories"]:
        print(f"Category '{category}' not found. Add it first.")
        return

    budget["categories"][category]["allocated"] += amount
    print(f"Allocated ₱{amount} to {category}")


def spend(budget, category, amount):
    """Record an expense."""
    if category not in budget["categories"]:
        print("Category not found!")
        return

    if amount > budget["categories"][category]["allocated"]:
        print(f"⚠️  Warning: You only allocated ₱{budget['categories'][category]['allocated']} to {category}")
        print(f"   You're trying to spend ₱{amount}. Diskarte mo na lang.")

    budget["categories"][category]["spent"] += amount
    remaining = budget["categories"][category]["allocated"] - budget["categories"][category]["spent"]
    print(f"Spent ₱{amount} on {category}. Remaining: ₱{remaining}")


def summary(budget):
    """Show a budget summary."""
    total_allocated = sum(cat["allocated"] for cat in budget["categories"].values())
    total_spent = sum(cat["spent"] for cat in budget["categories"].values())

    print(f"\n=== Budget Summary ===")
    print(f"Allowance: ₱{budget['allowance']}")
    print(f"Total allocated: ₱{total_allocated}")
    print(f"Total spent: ₱{total_spent}")
    print(f"Unallocated: ₱{total_allocated - total_spent}\n")

    for category, data in budget["categories"].items():
        if data["allocated"] > 0:
            remaining = data["allocated"] - data["spent"]
            print(f"  {category}: ₱{data['allocated']} allocated, "
                  f"₱{data['spent']} spent, ₱{remaining} left")


# Usage
budget = create_budget(500)
allocate(budget, "pamasahe", 100)
allocate(budget, "kain", 200)
allocate(budget, "photocopy", 50)
allocate(budget, "tambay", 50)

spend(budget, "pamasahe", 30)
spend(budget, "kain", 80)
spend(budget, "tambay", 60)  # Overspend!

summary(budget)
```

Output:

```
Allocated ₱100 to pamasahe
Allocated ₱200 to kain
Allocated ₱50 to photocopy
Allocated ₱50 to tambay
Spent ₱30 on pamasahe. Remaining: ₱70
Spent ₱80 on kain. Remaining: ₱120
⚠️  Warning: You only allocated ₱50 to tambay
   You're trying to spend ₱60. Diskarte mo na lang.
Spent ₱60 on tambay. Remaining: -₱10

=== Budget Summary ===
Allowance: ₱500
Total allocated: ₱400
Total spent: ₱170
Unallocated: ₱230

  pamasahe: ₱100 allocated, ₱30 spent, ₱70 left
  kain: ₱200 allocated, ₱80 spent, ₱120 left
  tambay: ₱50 allocated, ₱60 spent, -₱10 left
```

??? tip "Diskarte"
    Notice how `summary()` calculates everything from the budget dictionary. It doesn't need any extra variables -- it just reads what's stored. This is the power of functions: they work with data, not hardcoded values.

## Scope: Where Variables Live

Variables inside a function are **local** -- they don't exist outside the function:

```python
def add(a, b):
    total = a + b
    return total

result = add(5, 3)
print(result)  # 8
print(total)   # Error! 'total' doesn't exist outside the function
```

Global variables (defined outside functions) can be read inside functions, but it's better to pass them as parameters:

```python
# Bad: relying on global variables
budget = 500

def spend(amount):
    global budget
    budget -= amount
    print(f"Remaining: ₱{budget}")

# Good: passing data explicitly
def spend(allowance, amount):
    return allowance - amount

remaining = spend(500, 100)
```

??? example "Portfolio Tip: Modular Code"
    Your budget tracker using functions shows you understand code organization -- a key skill for any developer:

    1. **GitHub README** -- Highlight how your code uses functions to avoid repetition. Employers love seeing modular code!
    2. **LinkedIn headline** -- "Student Developer | Built a budget tracker with Python that tracks spending patterns"
    3. **Interview talking point** -- "I wrote my budget tracker using functions to keep the code clean and reusable. Each function handles one responsibility, like how a real codebase is structured."

## Summary

- Functions are reusable blocks of code
- Parameters are inputs; `return` is the output
- Default arguments let you set fallback values
- Local variables only exist inside their function
- Functions make code cleaner and easier to maintain

## Boss Fight

??? warning "Boss Fight: Complete Budget Tracker"

    Extend the budget tracker to include:

    1. Weekly tracking (multiple weeks of data)
    2. Category alerts when spending exceeds 80% of allocation
    3. A "savings" category that automatically saves 10% of allowance
    4. A weekly report showing trends

    **Hint:** Use a list of budgets (one per week) and loop through them for the report.

??? success "You did it! Level Up!"
    +150 XP. You built a complete budget tracker. Ang galing!

## Side Quests

??? note "Optional: Side Quest"
    - Add a "Jollibee fund" category that tracks savings for Jollibee trips
    - Create a "budget vs. actual" comparison chart
    - Export the budget to a CSV file

## Further Reading

- [Python's official tutorial on functions](https://docs.python.org/3/tutorial/controlflow.html#defining-functions)
- [Real Python: functions](https://realpython.com/defining-your-own-python-function/)

??? example "🧠 Reflection — Functions"

    - **What did you learn?** Functions are reusable blocks of code that take inputs (parameters), do work, and return outputs, keeping your code clean and organized.
    - **How can you apply this?** Think of a function like a trusted taga-load — you give them instructions (parameters), they handle the delivery, and you get your package (return value). Whether you're tracking your weekly allowance or building a bigger project, functions let you write code once and reuse it everywhere.
    - **What's next?** Functions keep your code organized, but what happens when you close the program — how do you save your data for next time?

??? checkbox "✅ Chapter Checklist"

    - [ ] I can define and call functions using `def`
    - [ ] I can pass parameters to functions and return values
    - [ ] I can use default arguments to set fallback values
    - [ ] I understand the difference between local and global variable scope
    - [ ] I can break a problem into multiple functions for cleaner code

---

*Next: [Chapter 7: Files](chapter-07-files.md) -- Saving data permanently.*
