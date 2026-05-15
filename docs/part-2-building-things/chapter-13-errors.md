# Chapter 13: Errors, Debugging, and the Boss Fight

??? example "📋 Chapter Info"
    | | |
    |---|---|
    | **Difficulty** | ⭐⭐ Intermediate |
    | **Time** | 30 min |
    | **XP** | +100 XP |

> **Story Hook:** You've been coding for weeks. Your programs work -- sometimes. Then you hit a wall. A program that worked yesterday crashes with a cryptic error message. You stare at the screen. "What does this even mean?" Your first instinct is to panic. But then you remember: errors are data. Every error is a clue. And you're a detective now.

---

## What You'll Learn

- Common Python errors and what they mean
- Reading error messages (from bottom to top!)
- `try/except` for graceful error handling
- Debugging strategies and techniques
- Using `print()` and `pdb` for debugging

## Types of Errors

### Syntax Errors: Breaking the Rules

```python
>>> print("Hello
  File "<stdin>", line 1
    print("Hello
          ^
SyntaxError: EOL while scanning string literal
```

**What happened?** You forgot the closing quote. Python couldn't parse the line.

**Fix:** `print("Hello")`

### Name Errors: Unknown Variables

```python
>>> print(name)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'name' is not defined
```

**What happened?** You used a variable that doesn't exist.

**Fix:** Define it first: `name = "Juan"`

### Type Errors: Wrong Data Type

```python
>>> "Age: " + 25
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can only concatenate str (not "int") to str
```

**What happened?** You tried to add a string and a number.

**Fix:** Convert the number: `f"Age: {25}"` or `"Age: " + str(25)`

### Index Errors: Out of Bounds

```python
>>> fruits = ["apple", "banana"]
>>> fruits[5]
IndexError: list index out of range
```

**What happened?** Python lists start at index 0. Index 5 doesn't exist in a 2-element list.

**Fix:** Use valid indices: `fruits[0]`, `fruits[1]`, or `len(fruits) - 1`

## Reading Error Messages

Error messages are your friends. Read them **from bottom to top**:

```
Traceback (most recent call last):    ← How we got here (stack trace)
  File "program.py", line 10, in <module>  ← Where it happened
    result = divide(10, 0)              ← The line with the error
ZeroDivisionError: division by zero     ← WHAT went wrong (most important!)
```

1. **Bottom line**: What error? (ZeroDivisionError)
2. **Line above**: Where? (File, line number, function)
3. **Top lines**: How did we get here? (Call stack)

??? tip "⏸️ Pause and Predict"

    **Think about the last error you got. What information did it give you? Could you have predicted what went wrong before running the code?**

    Take 30 seconds to think about your answer before reading on. This is how you build real understanding!

??? note "🐌 Slow Internet?"

    Error handling is especially important when your internet connection is unreliable:

    - **Graceful fallbacks**: Programs with good error handling keep working when the internet drops. Instead of crashing, they show a cached result or a friendly message. This is the difference between an app that frustrates users and one they can rely on.
    - **Timeout handling**: Always set timeouts on network requests so your program doesn't hang forever waiting for a response that may never come.
    - **Retry logic**: Learn to build programs that automatically retry a failed request a few times before giving up. Many Filipino developers build this into their apps because they know how spotty connections can be.

    The `try/except` patterns in this chapter are your toolkit for building resilient programs that work in the real world — not just in perfect lab conditions.

## `try/except`: Catching Errors

Instead of letting your program crash, catch errors gracefully:

```python
try:
    # Code that might fail
    result = 10 / 0
except ZeroDivisionError:
    # What to do if it fails
    print("Hindi mo pwedeng i-divide ang zero! Subok ulit.")
```

### Multiple Except Blocks

```python
try:
    number = int(input("Enter a number: "))
    result = 100 / number
except ValueError:
    print("Number lang po! Text hindi pwede.")
except ZeroDivisionError:
    print("Hindi mo pwedeng i-divide ang zero!")
except Exception as e:
    print(f"Unknown error: {e}")
else:
    # Runs only if NO error occurred
    print(f"Result: {result}")
finally:
    # Always runs, whether error or not
    print("Done.")
```

## Debugging Strategies

### 1. Print Debugging

The simplest and most powerful debugging technique:

```python
def calculate_budget(allowance, expenses):
    print(f"DEBUG: allowance={allowance}, expenses={expenses}")  # Add this
    total = sum(expenses)
    print(f"DEBUG: total_spent={total}")  # And this
    return allowance - total
```

### 2. Rubber Duck Debugging

Explain your code line by line to a rubber duck (or a patient friend). You'll often find the bug just by talking through it.

### 3. The Socratic Method

Ask yourself:
- What am I trying to do?
- What is the code actually doing?
- Where do they differ?
- Why do they differ?

### 4. Binary Search Debugging

If a bug appears somewhere in a 100-line function, test the middle. Is the bug before or after line 50? Cut the search space in half. Repeat.

## Building an Error-Resilient Program

Let's build a program that handles errors gracefully -- the "Bahala Na" way:

```python
# Error-Resilient Program
# Chapter 13

import sys


def get_valid_input(prompt, data_type=float, min_val=None, max_val=None):
    """Get validated user input with error handling."""
    while True:
        try:
            value = data_type(input(prompt))

            if min_val is not None and value < min_val:
                print(f"Minimum is {min_val}. Subok ulit.")
                continue
            if max_val is not None and value > max_val:
                print(f"Maximum is {max_val}. Subok ulit.")
                continue

            return value

        except ValueError:
            print(f"Invalid input. {data_type.__name__} lang po.")


def safe_divide(a, b):
    """Divide two numbers, handling division by zero."""
    try:
        return a / b
    except ZeroDivisionError:
        print("⚠️  Division by zero! Returning 0.")
        return 0
    except TypeError:
        print("⚠️  Invalid types! Please use numbers.")
        return 0


def main():
    """Budget calculator with full error handling."""
    print("=== Budget Calculator ===\n")

    # Get input with validation
    allowance = get_valid_input("Monthly allowance (₱): ", min_val=0)
    num_expenses = get_valid_input("Number of expense categories: ",
                                   data_type=int, min_val=1, max_val=20)

    expenses = []
    for i in range(num_expenses):
        print(f"\nCategory {i + 1}:")
        name = input(f"  Name: ")
        amount = get_valid_input(f"  Amount (₱): ", min_val=0)
        expenses.append({"name": name, "amount": amount})

    # Calculate
    total_expenses = sum(e["amount"] for e in expenses)
    remaining = safe_divide(allowance - total_expenses, 1)  # Safe
    daily_budget = safe_divide(remaining, 30)

    # Display
    print(f"\n=== Budget Summary ===")
    print(f"Allowance: ₱{allowance:.2f}")
    print(f"Total expenses: ₱{total_expenses:.2f}")
    print(f"Remaining: ₱{remaining:.2f}")
    print(f"Daily budget: ₱{daily_budget:.2f}")

    if remaining < 0:
        print("\n⚠️  Warning: You're spending more than you earn!")
        print("   Diskarte: Find where you can cut back.")
    elif remaining < allowance * 0.1:
        print("\n⚠️  Tight budget. Only {:.1f}% remaining.".format(
            (remaining / allowance) * 100))
    else:
        print("\n✅ Healthy budget! Mag-iipon ka na!")


if __name__ == "__main__":
    main()
```

## Debugging Checklist

- [ ] Read the error message from bottom to top
- [ ] Check for typos in variable names
- [ ] Verify data types match what's expected
- [ ] Print values before the error line
- [ ] Check loop bounds (off-by-one errors)
- [ ] Verify file paths are correct
- [ ] Test with simple inputs first
- [ ] Break complex problems into smaller pieces

## Summary

- Python has different error types: SyntaxError, NameError, TypeError, IndexError, etc.
- Error messages tell you exactly what went wrong -- read them carefully
- `try/except` catches errors gracefully
- Debugging is a systematic process, not magic
- Print debugging is your best friend

## Boss Fight

??? warning "Boss Fight: Bug Hunt!"

    Below is a program with **5 hidden bugs**. Find and fix them all:

    ```python
    # Budget Tracker with bugs
    def calculate_budget(allowance, expenses):
        total = 0
        for i in range(len(expenses)):
            total += expenses[i]
        return allowance - total

    def main():
        allowance = input("Allowance: ")
        expenses = [50, 30, 20]
        remaining = calculate_budget(allowance, expenses)
        print(f"Remaining: {remaining}")

    main()
    ```

    **Hints:**
    1. The input isn't converted to a number
    2. The expenses contain strings, not numbers
    3. Something else...

    Click to reveal the solution:

    ??? success "Solution"
        <details>
        <summary>Click to see all 5 bugs</summary>

        1. `allowance = input("Allowance: ")` -- Not converted to `float()`
        2. Total is initialized as `0` (int) instead of `0.0` (float) -- minor but good practice
        3. No error handling for invalid input
        4. Expenses list might contain strings if loaded from a file
        5. No check for negative allowance or expenses

        Fixed version:
        ```python
        def calculate_budget(allowance, expenses):
            total = 0.0  # Bug 2 fix
            for expense in expenses:  # Bug 3 fix: simpler loop
                total += expense
            return allowance - total

        def main():
            try:
                allowance = float(input("Allowance: "))  # Bug 1 fix
                if allowance < 0:
                    print("Allowance cannot be negative!")
                    return
            except ValueError:
                print("Invalid input! Number lang.")
                return

            expenses = [50, 30, 20]
            remaining = calculate_budget(allowance, expenses)

            if remaining < 0:  # Bug 4 fix: check for overspending
                print(f"⚠️ Over budget by ₱{abs(remaining):.2f}")
            else:
                print(f"Remaining: ₱{remaining:.2f}")

        main()
        ```
        </details>

??? success "You found all the bugs! Level Up!"
    +150 XP. You're now a debugging master. Ang galing!

## Side Quests

??? note "Optional: Side Quest"
    - Write a program that intentionally raises different errors and catches them
    - Create a "debug log" that records all errors for later review
    - Build a "crash recovery" system that saves state before operations

## Further Reading

- [Python's error hierarchy](https://docs.python.org/3/tutorial/errors.html)
- [Real Python: Debugging](https://realpython.com/python-debugging-pdb/)

---

*Next: [Chapter 14: Boss Fight 2](chapter-14-boss-fight-2.md) -- The midpoint boss battle.*

---

??? example "Portfolio Tip"

    **GitHub README**: Add your error-resilient budget calculator to your portfolio with a README that highlights: "Built with defensive programming -- every user input is validated, every division is protected. Filipino students deserve tools that don't crash."

    **LinkedIn**: Post: "Learned to stop panicking at error messages. Python errors are data, not failures. Built a budget calculator with full error handling -- try/except, input validation, graceful fallbacks. Subok ulit lang. #Python #Debugging". This shows maturity as a developer.

    **Interview Talking Point**: "I read tracebacks from bottom to top, use try/except for graceful error handling, and apply systematic debugging strategies like print debugging and binary search. I don't fear errors -- I treat them as clues that tell me exactly where to look."

??? example "🧠 Reflection — Error Handling and Debugging"

    - **What did you learn?** You learned to read and interpret Python error messages, use `try/except` blocks to handle errors gracefully, and apply systematic debugging strategies to find and fix bugs.
    - **How can you apply this?** Instead of panicking when a program crashes, you now treat errors as clues -- a mindset shift that helps whether you're fixing a school project, debugging a store system for Lola, or troubleshooting code at work.
    - **What's next?** How do you write automated tests to catch bugs before they reach users, and what debugging tools do professional developers use?

??? checkbox "✅ Chapter Checklist"

    - [ ] I can read a Python traceback and identify where the error occurred
    - [ ] I understand the difference between syntax errors, runtime errors, and logical errors
    - [ ] I can use `try/except` blocks to catch and handle specific exception types
    - [ ] I know debugging strategies: reading error messages, using `print()`, and stepping through code
    - [ ] I practiced turning a crashing program into one that handles errors gracefully
