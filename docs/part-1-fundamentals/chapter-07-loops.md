# Chapter 7: Loops and Repeated Checks at the Store

??? example "📋 Chapter Info"
    | | |
    |---|---|
    | **Difficulty** | ⭐⭐ Beginner |
    | **Time** | 30 min |
    | **XP** | +100 XP |

> **Story Hook:** Lola does not check one item and stop. She checks every shelf, every morning. Some items need restocking. Some are okay. Some need to be skipped because they are not for sale right now. That is what loops do in Python too.

> **Output:** A small store checker that repeats work across many items and can stop or skip when needed.

---

## What You'll Learn

- How `for` loops repeat over a collection
- How `while` loops repeat until a condition changes
- How `break` stops a loop early
- How `continue` skips one pass and moves on
- How `range()` generates simple number sequences

## Why Loops Matter

If you have 20 store items, you do not want to write 20 separate print statements.

Loops help you repeat the same action without repeating the same code.

## `for` Loops

A `for` loop goes through each item in a list.

```python
items = ["laundry soap", "candy", "rice", "sardines"]

for item in items:
    print(f"Checking {item}")
```

That is the basic idea: one item at a time.

??? tip "Diskarte"
    Read a `for` loop as: "For each item, do this."

## `range()`

Use `range()` when you want to repeat something a set number of times.

```python
for i in range(5):
    print(f"Restock check #{i + 1}")
```

If you want to start at 1, you can use `range(1, 6)`.

## `while` Loops

A `while` loop keeps running while a condition stays true.

```python
restock_needed = True

while restock_needed:
    print("Checking inventory...")
    restock_needed = False
```

In real programs, `while` loops are useful when you do not know in advance how many times the program must repeat.

## `break` and `continue`

```python
items = ["laundry soap", "candy", "rice", "sardines"]

for item in items:
    if item == "rice":
        print("Found rice. Stop checking.")
        break
    print(f"Still checking {item}")
```

`break` stops the loop entirely.

```python
for item in items:
    if item == "candy":
        continue
    print(f"Processing {item}")
```

`continue` skips one item and moves to the next one.

## Store Example: Checking Stock

```python
inventory = {
    "laundry soap": 10,
    "candy": 3,
    "rice": 20,
    "sardines": 0,
}

for item, qty in inventory.items():
    if qty == 0:
        print(f"{item}: sold out")
        continue

    if qty <= 5:
        print(f"{item}: low stock ({qty} left)")
    else:
        print(f"{item}: okay ({qty} left)")
```

That is the kind of repeated check a store owner does every day.

## One Small Menu Loop

```python
while True:
    print("\n1. Check inventory")
    print("2. Exit")

    choice = input("Choose: ")

    if choice == "1":
        print("Checking the shelves...")
    elif choice == "2":
        print("Stopping the loop.")
        break
    else:
        print("Invalid choice.")
```

This is the first time a loop can keep asking for input until the user chooses to exit.

??? warning "Boss Fight Warning"
    Every `while` loop needs an exit path. If it never becomes `False` and you never `break`, it can run forever.

## Nested Loops

Sometimes you repeat inside a repeat.

```python
for shelf in range(1, 4):
    for slot in range(1, 4):
        print(f"Shelf {shelf}, Slot {slot}")
```

Use nested loops carefully. They can get hard to read fast.

## Summary

- `for` loops repeat over collections
- `while` loops repeat until a condition changes
- `break` stops the loop
- `continue` skips one pass
- `range()` creates simple number sequences

## Side Quest

??? note "Optional: Practice"
    Turn the stock checker into a nightly restock report. Mark items as `sold out`, `low stock`, or `okay`.

## Further Reading

- [Python's official tutorial on control flow](https://docs.python.org/3/tutorial/controlflow.html)
- [Real Python: for loops](https://realpython.com/python-for-loop/)

*Previous: [Chapter 6: And, Or, Not](chapter-06-boolean-logic.md) -- Combining conditions*
*Next: [Chapter 8: Functions and Reusable Helpers](chapter-08-functions.md) -- Reusing logic.*
