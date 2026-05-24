# Chapter 4: Comparisons and Truth Values at the Store

??? example "📋 Chapter Info"
    | | |
    |---|---|
    | **Difficulty** | ⭐⭐ Beginner |
    | **Time** | 25 min |
    | **XP** | +100 XP |

> **Story Hook:** Lola checks the shelves before opening the sari-sari store. Some items are running low. Some are still fine. Some prices match what she expected, and some do not. Before she decides what to do, she first needs to know one thing: is this statement true or false?

> **Output:** A small set of store checks that returns `True` or `False` for common inventory questions.

---

## What You'll Learn

- What `True` and `False` mean in Python
- Comparison operators: `==`, `!=`, `<`, `>`, `<=`, `>=`
- How to read a comparison as a question
- The difference between assignment (`=`) and comparison (`==`)

## Truth Values: The Two Answers

Python uses a special data type called **boolean**. A boolean has only two possible values:

- `True`
- `False`

You will use booleans constantly when checking store data.

```python
is_open = True
is_sold_out = False

print(is_open)
print(is_sold_out)
```

Booleans are not text. They are not numbers. They are a yes-or-no answer stored in the program.

??? tip "Diskarte"
    If a question can only be answered with yes or no, a boolean is often the right choice.

## Comparison Operators

Comparison operators ask whether two values have a certain relationship.

| Operator | Meaning | Example | Result |
|----------|---------|---------|--------|
| `==` | Equal to | `5 == 5` | `True` |
| `!=` | Not equal to | `5 != 3` | `True` |
| `<` | Less than | `3 < 5` | `True` |
| `>` | Greater than | `5 > 3` | `True` |
| `<=` | Less than or equal | `5 <= 5` | `True` |
| `>=` | Greater than or equal | `5 >= 3` | `True` |

```python
stock = 12
price = 15

print(stock > 10)     # True
print(stock <= 5)     # False
print(price == 15)    # True
print(price != 20)    # True
```

??? bug "Common Mistake"
    `=` assigns a value. `==` compares two values.

    ```pycon
    >>> stock = 12
    >>> stock == 12
    True
    ```

## Reading Comparisons

Think of every comparison as a question:

- `stock < 5` means "Is stock less than 5?"
- `price == 15` means "Is the price exactly 15?"
- `qty >= 3` means "Is the quantity at least 3?"

This habit matters because it makes later branching easier to understand.

```python
stock = 4

print(stock < 5)   # Low stock?
print(stock >= 5)  # Enough stock?
```

??? tip "⏸️ Pause and Predict"

    Before running the code, predict the answers:

    ```python
    items_left = 2
    print(items_left == 0)
    print(items_left < 5)
    print(items_left >= 3)
    ```

## Store Examples

Here are some useful store checks:

```python
price = 18.00
cost = 12.00
stock = 3

print(price > cost)      # Is this item sold above cost?
print(stock == 0)        # Is the item sold out?
print(stock <= 5)        # Is it low stock?
print(price >= 15)       # Is it at or above the target price?
```

These checks do not make decisions yet. They only tell us what is true.

## Why This Chapter Comes First

Before Python can choose what to do, it needs a way to answer questions correctly.

Comparisons give you the answer.
Branching will use that answer.

That is why this chapter stays simple.

## Summary

- Booleans have only two values: `True` and `False`
- Comparison operators ask questions about values
- `=` assigns, `==` compares
- Comparisons are the foundation for later decisions

## Side Quest

??? note "Optional: Practice"
    Write five comparisons for your own small store or personal budget. Try to make each one return either `True` or `False`.

## Further Reading

- [Python's official tutorial on data structures and comparisons](https://docs.python.org/3/tutorial/datastructures.html)
- [Python's official tutorial on booleans](https://docs.python.org/3/library/stdtypes.html#boolean-operations-and-or-not)

*Previous: [Chapter 3: Variables, Data Types, and the Sari-Sari Store](chapter-03-variables.md) -- Storing information*
*Next: [Chapter 5: If, Else, and Simple Branching](chapter-05-branching.md) -- Making simple decisions.*
