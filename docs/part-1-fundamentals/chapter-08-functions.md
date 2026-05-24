# Chapter 8: Functions and Reusable Helpers

??? example "📋 Chapter Info"
    | | |
    |---|---|
    | **Difficulty** | ⭐⭐ Beginner |
    | **Time** | 35 min |
    | **XP** | +100 XP |

> **Story Hook:** By now, the sari-sari store keeps asking you the same kinds of questions: What is the total price? Is the stock low? What should the receipt say? Instead of writing the same logic again and again, you turn it into reusable helpers.

> **Output:** A small function toolkit for common store tasks like totals, summaries, and receipt messages.

---

## What You'll Learn

- What functions are and why they help
- How to define a function with `def`
- How to pass inputs using parameters
- How to send results back with `return`
- How default arguments and scope work

## What Functions Do

A function is a reusable block of code.

Write it once. Call it many times.

```python
def greet(name):
    print(f"Kumusta, {name}!")


greet("Juan")
greet("Maria")
```

## Why Functions Matter

Without functions, repeated code gets noisy.

```python
def line_total(price, qty):
    return price * qty


print(line_total(15, 2))
print(line_total(8, 3))
```

The repeated logic stays in one place.

??? tip "Diskarte"
    If you keep copying the same pattern, a function can usually clean it up.

## Parameters and Return Values

Parameters are the inputs a function receives. `return` is the answer it gives back.

```python
def calculate_change(paid, total):
    return paid - total


change = calculate_change(100, 72)
print(f"Change: ₱{change}")
```

## Default Arguments

You can set fallback values.

```python
def print_receipt(item, qty, unit_price, store_name="Lola's Store"):
    total = qty * unit_price
    print(f"{store_name} receipt")
    print(f"{item} x{qty} = ₱{total}")


print_receipt("candy", 3, 5)
print_receipt("rice", 2, 50, store_name="Tindahan ni Lola")
```

## Store Helper Functions

Here is a small helper toolkit for store tasks:

```python
def item_total(price, qty):
    return price * qty


def is_low_stock(qty, threshold=5):
    return qty <= threshold


def receipt_line(name, qty, price):
    total = item_total(price, qty)
    return f"{name} x{qty} = ₱{total}"


print(receipt_line("laundry soap", 2, 15))
print(is_low_stock(3))
```

## Scope: Where Variables Live

Variables inside a function are local.

```python
def add(a, b):
    total = a + b
    return total


result = add(5, 3)
print(result)
```

`total` exists only inside the function. That is local scope.

## Good Function Habits

- Keep functions focused on one job
- Pass data in instead of relying on globals
- Return a value when the result matters
- Use clear names that match the job

## Summary

- Functions are reusable blocks of code
- Parameters are inputs
- `return` sends a value back
- Default arguments provide fallback values
- Local variables stay inside the function

## Side Quest

??? note "Optional: Practice"
    Write three store helper functions:

    - one that calculates a subtotal
    - one that checks if an item is low stock
    - one that prints a receipt line

## Further Reading

- [Python's official tutorial on functions](https://docs.python.org/3/tutorial/controlflow.html#defining-functions)
- [Real Python: functions](https://realpython.com/defining-your-own-python-function/)

*Previous: [Chapter 7: Loops and Repeated Checks at the Store](chapter-07-loops.md) -- Repeating work*
*Next: [Chapter 9: Files and JSON for the Store](chapter-09-files.md) -- Saving data permanently.*
