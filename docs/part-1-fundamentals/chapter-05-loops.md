# Chapter 5: Loops and the Merienda Reminder

??? example "📋 Chapter Info"
    | | |
    |---|---|
    | **Difficulty** | ⭐⭐ Beginner |
    | **Time** | 30 min |
    | **XP** | +100 XP |

> **Story Hook:** You're studying for exams. Your phone keeps buzzing -- notifications from your barkada, reminders about deadlines, ads for "50% off at Jollibee." You want to focus, but every notification pulls your attention away. So you write a program: a timer that tells you when to study and when to take a break. "Pomodoro" is what the cool kids call it. You call it "merienda mode."

---

## What You'll Learn

- `for` loops: iterating over sequences
- `while` loops: repeating until a condition changes
- `break` and `continue`: controlling loop flow
- `range()`: generating number sequences
- Nested loops

## Why Loops?

Imagine you have 50 items in your sari-sari store inventory. Without loops, you'd write 50 lines of code to print each one. With a loop, you write 3.

Loops let you **repeat actions automatically**. They're the difference between doing something once and doing it a thousand times without getting bored.

## `for` Loops: The Workhorse

A `for` loop goes through each item in a collection:

```python
# List of merienda items
merienda = ["pancit canton", "chocolate drink", "banana cue", "fishballs", "kikiam"]

for item in merienda:
    print(f"I love {item}!")
```

Output:

```
I love pancit canton!
I love chocolate drink!
I love banana cue!
I love fishballs!
I love kikiam!
```

### How It Works

```python
for item in merienda:
    # 'item' takes the value of each element, one at a time
    print(item)
```

## `range()`: Numbers on Demand

Need to repeat something a specific number of times? `range()` generates a sequence:

```python
# Count from 0 to 4
for i in range(5):
    print(f"Study session #{i + 1}")
```

Output:

```
Study session #1
Study session #2
Study session #3
Study session #4
Study session #5
```

??? tip "Diskarte"
    `range(5)` gives you 0, 1, 2, 3, 4 -- that's 5 numbers, but it starts at 0. If you want to count from 1, use `range(1, 6)` or add 1 inside the loop.

??? tip "⏸️ Pause and Predict"

    **Pause: Can you think of a situation where a `for` loop would be better than a `while` loop? What about the opposite?**

    Take 30 seconds to think about your answer before reading on. This is how you build real understanding!

### `range()` with Steps

```python
# Even numbers from 0 to 10
for i in range(0, 11, 2):
    print(i)  # 0, 2, 4, 6, 8, 10

# Counting backwards
for i in range(10, 0, -1):
    print(f"{i}... ")
print("Lakas ng loob!")
```

## `while` Loops: Keep Going Until...

A `while` loop repeats as long as a condition is true:

```python
import random

# Simulate rolling a 6
roll = 0
attempts = 0

while roll != 6:
    roll = random.randint(1, 6)
    attempts += 1
    print(f"Rolled: {roll}")

print(f"Got a 6 after {attempts} attempts!")
```

### Infinite Loops: Be Careful!

```python
# DANGEROUS -- this never stops!
while True:
    print("I will never stop!")
```

To stop it, press `Ctrl+C` in the terminal.

??? warning "Boss Fight Warning"
    Always make sure your `while` loop has a way to exit. Add a condition that eventually becomes False, or use `break`.

## `break` and `continue`

- **`break`**: Exit the loop entirely
- **`continue`**: Skip to the next iteration

```python
# break: Stop when we find what we want
inventory = ["laundry soap", "cigarettes", "candy", "instant noodles"]

for item in inventory:
    if item == "candy":
        print(f"Found candy! We have {item} in stock.")
        break  # Stop searching
    print(f"Checking {item}...")

# continue: Skip items we don't want
for i in range(10):
    if i % 2 == 0:
        continue  # Skip even numbers
    print(i)  # Only odd numbers: 1, 3, 5, 7, 9
```

## Building a Merienda Reminder Timer

Let's build a Pomodoro-style timer with Filipino twists:

```python
import time

def merienda_timer(work_minutes=25, break_minutes=5, sessions=4):
    """Pomodoro timer with Filipino merienda breaks."""

    print("=== Merienda Timer ===")
    print(f"Work: {work_minutes} min | Break: {break_minutes} min")
    print(f"Sessions: {sessions}\n")

    for session in range(1, sessions + 1):
        print(f"--- Session {session}/{sessions} ---")

        # Work period
        print(f"Kumikita! Focus for {work_minutes} minutes...")
        for minute in range(work_minutes, 0, -1):
            print(f"  {minute} min left...")
            time.sleep(1)  # In real code, this would be 1 second

        # Break period (except after the last session)
        if session < sessions:
            print(f"\nKain muna tayo! {break_minutes} minute break.")
            for minute in range(break_minutes, 0, -1):
                print(f"  {minute} min left...")
                time.sleep(1)

    print("\n🎉 All sessions complete! Merienda time!")
    print("Jollibee knows what works -- so does this timer.")
```

??? note "Try It Yourself"
    Try running this with shorter times to test it:

    ```python
    merienda_timer(work_minutes=1, break_minutes=1, sessions=3)
    ```

## Nested Loops: Loops Inside Loops

You can put loops inside loops. This is useful for things like printing a grid or checking all combinations:

```python
# Print a multiplication table
for i in range(1, 6):
    for j in range(1, 6):
        print(f"{i * j:3}", end="")  # :3 means width of 3
    print()  # New line after each row
```

Output:

```
  1  2  3  4  5
  2  4  6  8 10
  3  6  9 12 15
  4  8 12 16 20
  5 10 15 20 25
```

## Summary

- `for` loops iterate over collections
- `while` loops repeat until a condition is False
- `range()` generates number sequences
- `break` exits a loop; `continue` skips to the next iteration
- Nested loops go inside other loops

## Boss Fight

??? warning "Boss Fight: Study Session Manager"

    Build a study session manager that:

    1. Asks how many subjects you have
    2. Assigns time slots to each subject using a loop
    3. Shows a schedule summary
    4. Runs a countdown timer for each session
    5. Includes automatic break reminders

    **Hint:** Use a list of subjects and loop through them.

??? success "You did it! Level Up!"
    +100 XP. You mastered loops. Ang galing!

## Side Quests

??? note "Optional: Side Quest"
    - Create a "tambay mode" that randomly inserts break times
    - Add a streak counter for consecutive completed sessions
    - Build a "kain break" that randomly suggests merienda items

## Further Reading

- [Python's official tutorial on control flow](https://docs.python.org/3/tutorial/controlflow.html)
- [Real Python: for loops](https://realpython.com/python-for-loop/)

??? example "Portfolio Tip"

    **GitHub README**: Add your merienda timer script to a repo called `merienda-timer`. Include a GIF or screenshot of the countdown in action. Mention: "Built to help Filipino students stay focused with Pomodoro-style breaks -- because merienda time is sacred."

    **LinkedIn**: Post: "Built a Pomodoro-style study timer in Python with Filipino merienda breaks. Because productivity culture should include time for banana cue. #Python #Productivity". Tag friends who need a study tool.

    **Interview Talking Point**: "I understand loops deeply -- `for` loops for known iterations, `while` loops for conditions, and `break`/`continue` for flow control. I've used them to build practical tools like automated timers and batch processors that save repetitive manual work."

??? example "🧠 Reflection — Loops"

    - **What did you learn?** `for` and `while` loops let you repeat actions automatically, with `break` and `continue` to control the flow and `range()` to generate number sequences.
    - **How can you apply this?** Whether you're processing 50 items in your sari-sari store inventory or running a study timer through multiple subjects, loops save you from writing the same code over and over — just like how a street vendor sells the same merienda to a line of customers without getting tired.
    - **What's next?** What if you want to package a whole loop (or any block of logic) into something you can reuse anywhere?

??? checkbox "✅ Chapter Checklist"

    - [ ] I can use `for` loops to iterate over lists and other collections
    - [ ] I can use `while` loops to repeat until a condition is met
    - [ ] I can use `range()` to generate number sequences
    - [ ] I can use `break` to exit a loop and `continue` to skip iterations
    - [ ] I can write nested loops for tasks like multiplication tables

---

*Previous: [Chapter 4: Conditionals](chapter-04-conditionals.md) -- Making decisions*
*Next: [Chapter 6: Functions](chapter-06-functions.md) -- Reusable code blocks.*
