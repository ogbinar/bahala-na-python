# Chapter 1: Hello, World!

> **Story Hook:** You're sitting at a comshop. The monitor is a CRT from 2008, the keyboard has sticky keys, and the "P10/HOUR" sign is flickering above you. On the screen, someone has left Python open -- the cursor blinking at a `>>>` prompt. You've never coded before. Your fingers hover over the keyboard. What do you type?

---

## What You'll Learn

- What Python is and what it can do
- How to use the Python interactive interpreter
- Your first `print()` statement
- Why making mistakes is part of learning

## What Is Python?

Python is a **programming language** -- a way to give instructions to a computer. You write code, Python reads it, and the computer does what you told it to do.

Python is special because:

- It reads almost like English (easy to learn, hard to master)
- It's used everywhere: websites, data science, AI, automation, games, robotics
- It has one of the most welcoming communities in all of tech
- It runs on **any** device -- even a cheap ₱8,000 laptop

Think of Python like a recipe. You write the instructions (code), and Python follows them (runs your program). The difference? With Python, you're the chef.

## The Interpreter: Your Playground

The Python interpreter is like a conversation with a computer. You type something, and Python responds immediately.

```python
>>> 2 + 2
4
>>> print("Kumusta, World!")
Kumusta, World!
```

That `>>>` is Python saying: *"I'm ready. Try me."*

## Your First Line of Code

Type this at the `>>>` prompt:

```python
>>> print("Hello, World!")
```

You should see:

```
Hello, World!
```

**That's your first program.** Every programmer who has ever lived has done this exact thing. You're now part of a community that stretches back decades.

??? success "Level Up!"
    +100 XP. You wrote your first line of Python. Ang ganda!

## Breaking Down `print()`

```python
print("Hello, World!")
```

| Part | What It Is |
|------|-----------|
| `print` | The **function name** -- tells Python to display text |
| `()` | **Parentheses** -- everything inside is the "input" |
| `"Hello, World!"` | **Text** (called a "string") -- what gets displayed |
| `""` | **Quotes** -- tell Python "this is text, not code" |

## Try It Yourself

??? note "Try It Yourself"
    Change the text inside the quotes and try again:

    ```python
    >>> print("Ang galing ko sa Python!")
    >>> print("P10/Hour lang, pero free if my diskarte!")
    >>> print(100 + 200)
    ```

    Notice that `print(100 + 200)` outputs `300` -- Python can do math too!

## Common Errors: Don't Panic

Errors are not failures. They're **data**. Every programmer sees errors -- the best ones just know how to read them.

### Error 1: Missing quotes

```python
>>> print(Hello)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'Hello' is not defined
```

**What happened?** Python thinks `Hello` is a variable name, not text. You forgot the quotes.

**Fix:** `print("Hello")`

### Error 2: Missing parentheses

```python
>>> print "Hello"
  File "<stdin>", line 1
    print "Hello"
          ^
SyntaxError: Missing parentheses in call to 'print'.
```

**What happened?** Python 3 requires parentheses. Python 2 didn't. You're using Python 3, so you need them.

**Fix:** `print("Hello")`

??? tip "Diskarte"
    When you see an error, read it from **bottom to top**. The last line tells you what went wrong. The lines above tell you where. It's like reading a receipt -- the total is at the bottom, but the details are above it.

## The Sari-Sari Store Connection

Every great learning journey starts with something familiar. For us Filipinos, that's the **sari-sari store**.

Imagine you're helping your lola manage her sari-sari store. She needs to:

- Track what items she has in stock
- Calculate the total price for a customer
- Remember who owes her money

All of these require the same thing: **the ability to store and process information**. That's what programming is. Python is just the tool that helps you do it.

In the chapters ahead, you'll build a sari-sari store inventory system from scratch. But first, let's master the absolute basics.

## Summary

- Python is a programming language that reads like English
- The interpreter lets you type code and see results immediately
- `print()` displays text on the screen
- Errors are normal and informative -- read them carefully
- Every programmer started with `print("Hello, World!")`

## Further Reading

- [Python's official tutorial](https://docs.python.org/3/tutorial/)
- [Automate the Boring Stuff with Python](https://automatetheboringstuff.com/)
- [Real Python tutorials](https://realpython.com/)

## What's Next

In the next chapter, we'll install Python on your computer and write your first real Python file. Until then, play around with the interpreter. Type random things. Break things. Fix them.

**That's the Bahala Na way.**

---

*Next: [Chapter 2: Bahala Na, Let's Try It](chapter-02-bahala-na.md) -- Installing Python and running your first file.*
