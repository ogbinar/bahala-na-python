# Chapter 5: If, Else, and Simple Branching at the Store

??? example "📋 Chapter Info"
    | | |
    |---|---|
    | **Difficulty** | ⭐⭐ Beginner |
    | **Time** | 25 min |
    | **XP** | +100 XP |

> **Story Hook:** A customer walks into the sari-sari store and asks for an item. Lola checks the shelf. If the item is there, she can sell it. If not, she has to tell the customer to come back later. That is the first real decision your program needs to make.

> **Output:** A simple store checker that chooses between two or three outcomes using `if`, `elif`, and `else`.

---

## What You'll Learn

- How `if` makes a program choose a path
- How `else` handles the fallback case
- How `elif` adds one more possible branch
- How indentation controls what runs inside each branch

## The `if` Statement

`if` means: if this condition is true, run this block.

```python
stock = 4

if stock > 0:
    print("May stock pa.")
```

If the condition is false, the indented block is skipped.

## `if` and `else`

`else` gives the program a second choice.

```python
stock = 0

if stock > 0:
    print("Pwede ibenta.")
else:
    print("Sold out muna.")
```

This is the simplest kind of branching: one question, two answers.

??? tip "Diskarte"
    The program does not guess. It checks the condition, then follows the matching path.

## `elif`: One More Choice

`elif` means "else if." Use it when there is more than one possible outcome.

```python
stock = 2

if stock == 0:
    print("Sold out.")
elif stock <= 3:
    print("Low stock. Restock soon.")
else:
    print("Stock is healthy.")
```

That is still simple branching. The program checks one path at a time from top to bottom.

## Store Examples

```python
price = 15
cash = 20

if cash >= price:
    print("Sale approved.")
else:
    print("Kulang ang bayad.")
```

```python
member = True

if member:
    print("Member price applied.")
else:
    print("Regular price.")
```

Notice that these examples use only one condition at a time. That is the goal of this chapter.

## Indentation Matters

Python uses indentation to know which lines belong to a branch.

```python
stock = 1

if stock > 0:
    print("May stock.")
    print("Proceed with sale.")
else:
    print("Out of stock.")
```

If the indentation is wrong, the logic becomes wrong too.

??? bug "Common Mistake"
    Forgetting the colon or the indentation is one of the most common beginner mistakes.

    ```pycon
    if stock > 0
        print("May stock.")
    ```

## Simple Decision Flow

The best way to think about branching is:

1. Ask one question.
2. If the answer is yes, do one thing.
3. If the answer is no, do another thing.

Keep it small for now. Do not add extra logic yet.

## Summary

- `if` runs code only when a condition is true
- `else` handles the fallback path
- `elif` adds a second or third choice
- Indentation shows which lines belong to each branch

## Side Quest

??? note "Optional: Practice"
    Write a store checker that prints one of three messages:

    - "Sold out"
    - "Low stock"
    - "Stock is healthy"

## Further Reading

- [Python's official tutorial on control flow](https://docs.python.org/3/tutorial/controlflow.html)
- [Real Python: if/else statements](https://realpython.com/python-conditional-statements/)

*Previous: [Chapter 4: Comparisons and Truth Values at the Store](chapter-04-conditionals.md) -- Comparing values*
*Next: [Chapter 6: And, Or, Not](chapter-06-boolean-logic.md) -- Combining conditions.*
