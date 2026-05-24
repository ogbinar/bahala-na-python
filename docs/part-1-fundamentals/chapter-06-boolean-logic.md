# Chapter 6: And, Or, Not

??? example "📋 Chapter Info"
    | | |
    |---|---|
    | **Difficulty** | ⭐⭐ Beginner |
    | **Time** | 25 min |
    | **XP** | +100 XP |

> **Story Hook:** Sometimes one question is not enough. A discount might depend on membership and total spending. A warning might depend on low stock or a bad price. A decision might fail because not enough conditions were met. That is when boolean logic helps.

> **Output:** Small store rules that combine conditions using `and`, `or`, and `not`.

---

## What You'll Learn

- How `and` requires both conditions to be true
- How `or` allows either condition to be true
- How `not` flips a condition
- Why parentheses help when combining conditions

## `and`: Both Must Be True

Use `and` when both conditions must pass.

```python
is_member = True
subtotal = 150

if is_member and subtotal >= 100:
    print("Member discount applied.")
else:
    print("Regular price.")
```

Both sides must be true before the branch runs.

## `or`: One Is Enough

Use `or` when either condition is enough.

```python
low_stock = True
expired = False

if low_stock or expired:
    print("Check this item before selling.")
```

If either side is true, the whole expression is true.

## `not`: Flip the Result

Use `not` when you want the opposite answer.

```python
is_open = False

if not is_open:
    print("The store is closed.")
```

`not True` becomes `False`, and `not False` becomes `True`.

## Combining Conditions in Store Rules

```python
is_member = True
subtotal = 250
stock = 3

if is_member and subtotal >= 200:
    print("Special member discount.")

if stock <= 5 or subtotal >= 500:
    print("Review this sale carefully.")
```

## Parentheses Help

Parentheses make the order of logic easier to read.

```python
is_member = True
subtotal = 120
has_coupon = False

if is_member and (subtotal >= 100 or has_coupon):
    print("Discount approved.")
```

Without parentheses, beginners can easily lose track of what the program checks first.

??? tip "Diskarte"
    Read boolean logic slowly from left to right. If the sentence feels confusing, add parentheses or split the condition into smaller pieces.

## A Small Truth Check

Try to predict these before running them:

```python
print(True and False)
print(True or False)
print(not True)
```

## About `xor`

`xor` means "exclusive or." It is useful in some technical problems, but it is not part of the main beginner path here.

If you ever need it later, you can learn it as an optional topic.

## Summary

- `and` needs both conditions to be true
- `or` needs only one condition to be true
- `not` flips a boolean value
- Parentheses help keep combined conditions readable

## Side Quest

??? note "Optional: Practice"
    Write three store rules using `and`, `or`, and `not`. Keep each rule to one line first, then try adding parentheses.

## Further Reading

- [Python's official boolean operations reference](https://docs.python.org/3/library/stdtypes.html#boolean-operations-and-or-not)
- [Real Python: boolean logic](https://realpython.com/python-boolean/)

*Previous: [Chapter 5: If, Else, and Simple Branching at the Store](chapter-05-branching.md) -- Simple decisions*
*Next: [Chapter 7: Loops and Repeated Checks](chapter-07-loops.md) -- Repeating work.*
