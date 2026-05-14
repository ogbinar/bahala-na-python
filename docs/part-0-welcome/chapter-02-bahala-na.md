# Chapter 2: Bahala Na, Let's Try It

> **Story Hook:** Your friend from Manila just sent you a Python script. "Run this," they said. You have no idea what a script is. Your laptop is a second-hand ThinkPad from 2015 with 4GB of RAM. You have 200MB of data left. But you're curious. You click the file. Nothing happens. "Huh," you think. "Ibaril ko na lang."

---

## What You'll Learn

- How to install Python on your computer
- How to create and run Python files
- How to use the interactive interpreter
- What to do when installation goes wrong

## Installing Python

### Step 1: Download Python

Go to **[python.org/downloads](https://www.python.org/downloads/)** and click the big yellow button.

### Step 2: Install It

#### Windows

1. Run the `.exe` file
2. **CRITICAL**: Check ✅ **"Add Python to PATH"** before clicking "Install Now"
3. Wait for it to finish

??? warning "Boss Fight Warning"
    If you forget to check "Add Python to PATH," Python will be installed but you won't be able to run it from the command line. You'll need to reinstall and check that box.

#### macOS

1. Open the `.pkg` file
2. Follow the wizard
3. Enter your password if asked

#### Linux (Ubuntu/Debian)

```bash
sudo apt update
sudo apt install python3 python3-pip python3-venv
```

### Step 3: Verify It Worked

Open your terminal (Command Prompt on Windows) and type:

```bash
python3 --version
```

or on Windows:

```bash
python --version
```

You should see:

```
Python 3.12.x
```

??? bug "Common Mistake"
    If you get "command not found," restart your terminal. Sometimes the PATH changes don't take effect until you close and reopen it.

## The Interactive Interpreter

The interpreter is Python's conversation mode. Type code, get answers.

```bash
python3
```

You'll see:

```python
Python 3.12.x (...)
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

That `>>>` means Python is waiting for you. Try:

```python
>>> print("Hello from my computer!")
Hello from my computer!
>>> 50 * 75
3750
>>> exit()
```

Type `exit()` to leave.

## Your First Python File

Open any text editor and type:

```python
# My first Python file!
print("Hello, World!")
print("I'm learning Python!")
print("Kaya ko 'to!")
```

Save it as `hello.py` (make sure the extension is `.py`, not `.py.txt`).

Run it from your terminal:

```bash
python3 hello.py
```

Output:

```
Hello, World!
I'm learning Python!
Kaya ko 'to!
```

??? success "Level Up!"
    +100 XP. You created and ran your first Python file.

## What Is a `.py` File?

A `.py` file is just a text file with Python code in it. Think of it like a recipe:

1. You write the instructions in a file (the recipe)
2. Python reads the file and follows the instructions (cooking the dish)
3. You get the result (the meal)

The file extension `.py` is Python's way of knowing "this is my language."

## Common Installation Problems

### "Python is not recognized" (Windows)

**Cause:** You didn't check "Add Python to PATH" during installation.

**Fix:** Reinstall Python and check that box. Or add Python to PATH manually:
1. Search "Environment Variables" in Windows
2. Add Python's install path to your PATH variable
3. Restart your terminal

### "Permission denied" (macOS/Linux)

**Cause:** Python isn't installed or isn't in your PATH.

**Fix:**
```bash
# Check if Python is installed
which python3

# If not found, install it
# macOS:
brew install python3

# Ubuntu/Debian:
sudo apt install python3
```

### Not enough disk space

If your laptop is nearly full, Python needs about 200-400MB. Clear some space first.

??? tip "Diskarte"
    If you really can't install Python locally, use [Google Colab](https://colab.research.google.com) -- it's a free Python environment that runs in your browser. No installation needed.

## The Comshop Reflection

Remember that comshop from Chapter 1? The one with the flickering "P10/HOUR" sign?

That comshop is where millions of Filipinos learned their first computer skills. You learned to type, to browse the internet, to open files -- all because someone sat down at that comshop and clicked something.

Installing Python is the same. It's just a different kind of comshop. Instead of paying ₱10/hour, you're paying with curiosity. And unlike the comshop, this one is yours forever. No time limit. No one kicking you out.

**Bahala na. Let's try it.**

## Summary

- Python needs to be installed on your computer (or used online)
- The interpreter is a conversation mode: type code, get answers
- Python files have a `.py` extension and contain your code
- Run files with `python3 filename.py`
- Installation problems are normal and fixable

## Further Reading

- [Python's official tutorial](https://docs.python.org/3/tutorial/)
- [Python for Beginners (freeCodeCamp)](https://youtube.com/playlist?list=PLWKjhJtqVAbkArMiSqQ8m8XWKtzITUvXM2H)

---

*Next: [Part 1: Fundamentals](../part-1-fundamentals/index.md) -- Let's start building real things.*
