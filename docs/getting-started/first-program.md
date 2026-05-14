# Your First Program

> Before we install anything, let's understand what Python actually does.

---

## What Is Python?

Python is a **programming language** -- a way to give instructions to a computer. You write code (in Python), and Python translates it into things the computer can do: calculate numbers, display text, manipulate files, connect to the internet, and much more.

Python is special because:

- It reads almost like English
- It's used everywhere: websites, data science, AI, automation, games
- It has one of the most welcoming communities in tech
- **It runs on any device**, even cheap ones

## The Interpreter: Your Python Playground

The Python interpreter is an interactive program that lets you type Python code and see results immediately. Think of it as a conversation:

You type something in Python, and Python responds.

```python
>>> 1 + 1
2
>>> print("Kumusta!")
Kumusta!
```

This is the fastest way to experiment and learn. No saving, no running, no waiting. Just type and see.

## Your First Program: Hello, World!

Every programmer's first program is called "Hello, World!" -- you write code that makes the computer display that message. It's a tradition that goes back to 1978.

Open your terminal and type:

```bash
python3
```

Then type this at the `>>>` prompt:

```python
>>> print("Hello, World!")
```

You should see:

```
Hello, World!
```

That's it. That's your first program. `print()` is a **built-in function** that tells Python to display text on the screen.

??? tip "Diskarte"
    The `print()` function is your best friend. Use it to see what's happening inside your code. It's the Python equivalent of "hindi ko gets, let me check."

## What's Inside `print()`?

```python
print("Hello, World!")
```

- `print` is the **function name** -- it tells Python what to do (display text)
- `()` are **parentheses** -- everything inside them is the "input" to the function
- `"Hello, World!"` is **text** (called a "string" in Python) -- the thing you want to display
- The `""` quotes tell Python: "this is text, not code"

## Try It Yourself

??? note "Try It Yourself"
    Change the text inside the quotes and try again:

    ```python
    >>> print("Ang galing ko sa Python!")
    >>> print(2 + 2)
    >>> print("P10/Hour, parang sa comshop!")
    ```

    Notice that `print(2 + 2)` outputs `4` -- Python can do math too!

## Your First Python File

The interpreter is great for quick experiments. But for real programs, we write code in a file and run it.

Create a file called `hello.py` and type:

```python
print("Hello, World!")
print("I'm learning Python!")
print("Kaya ko 'to!")
```

Save it, then run it from your terminal:

```bash
python3 hello.py
```

You should see all three lines printed out. The `.py` extension tells Python: "this is a Python file."

??? tip "Diskarte"
    The file extension `.py` is Python's way of knowing "this is my language." Just like `.jpg` means image and `.mp3` means audio, `.py` means "Python code."

---

*Next: [Installing Python](../getting-started/install-python.md) -- Let's set up Python on your computer.*
