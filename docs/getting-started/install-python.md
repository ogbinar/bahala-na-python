# Installing Python

> Let's get Python on your computer. This takes about 10 minutes. **Kaya mo yan.**

Kung medyo nakaka-intimidate sa simula, okay lang. Isang setup lang 'to, hindi mo kailangan maging expert muna.

---

## Step 1: Download Python

Go to **[python.org/downloads](https://www.python.org/downloads/)** and click the big yellow button that says "Download Python 3.x.x".

### If You're on Windows

1. Click the download button above
2. Run the `.exe` file you just downloaded
3. **IMPORTANT**: Check the box that says **"Add Python to PATH"** before clicking "Install Now"
4. Wait for the installation to complete

### If You're on macOS

1. Click the download button above
2. Open the `.pkg` file
3. Follow the installation wizard
4. You may need to enter your password

### If You're on Linux (Ubuntu/Debian)

Open your terminal and run:

```bash
sudo apt update
sudo apt install python3 python3-pip python3-venv
```

## Step 2: Verify Installation

Open a terminal (Command Prompt on Windows, Terminal on macOS/Linux) and type:

```bash
python3 --version
```

or on Windows:

```bash
python --version
```

You should see something like:

```
Python 3.12.x
```

If you see a version number, **congratulations! Python is installed!** 🎉

??? tip "Diskarte"
    If `python3` doesn't work but `python` does, that's fine. Just use `python` instead of `python3` throughout this book. They're the same thing.

??? bug "Common Mistake"
    If you get "command not found" or "is not recognized," make sure you checked the "Add Python to PATH" box during installation. Try reinstalling and double-check that box.

## Step 3: Try the Interactive Interpreter

The Python interpreter is like a playground. Type Python code and see the result immediately.

In your terminal, type:

```bash
python3
```

You should see:

```pycon
Python 3.12.x (main, ... )
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

That `>>>` is Python waiting for you. It's like a conversation:

```pycon
>>> 2 + 2
4
>>> print("Kumusta, World!")
Kumusta, World!
>>> exit()
```

Type `exit()` and press Enter to leave the interpreter.

## Step 4: Create Your First Python File

Let's create a real Python file. Open any text editor (VS Code, Sublime Text, or even Notepad) and type:

```python
print("Hello, World!")
print("I'm learning Python!")
print("Kaya ko 'to!")
```

Save the file as `hello.py` in a folder you'll remember (like `Python` or `Code`).

Now open your terminal, navigate to that folder, and run:

```bash
python3 hello.py
```

You should see:

```
Hello, World!
I'm learning Python!
Kaya ko 'to!
```

??? success "Level Up!"
    You just installed Python and ran your first program. Every programmer ever has done this exact thing. You're part of the club now.

---

*Previous: [Getting Started](index.md) -- Setting up your environment*
*Next: [Your First Program](first-program.md) -- Verify everything works.*
