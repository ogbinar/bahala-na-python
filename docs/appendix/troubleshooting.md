# Appendix: Troubleshooting Common Issues

> Things go wrong. That's normal. Every programmer sees errors -- the best ones just know how to read them and fix them. This appendix covers the most common issues you'll encounter.

---

## Installation Issues

### "Python is not recognized" (Windows)

**Problem:** You installed Python but can't run it from the command line.

**Cause:** You didn't check "Add Python to PATH" during installation.

**Fix:**
1. Go to [python.org/downloads](https://www.python.org/downloads/)
2. Download the installer again
3. Run it and choose "Modify"
4. Check ✅ "Add Python to PATH"
5. Click "Modify"

**Alternative:** Add Python to PATH manually:
```
1. Search "Environment Variables" in Windows
2. Find "Path" in System Variables
3. Click "Edit" → "New"
4. Add: C:\Users\YourName\AppData\Local\Programs\Python\Python3xx\
5. Restart your terminal
```

### "command not found: python3" (macOS/Linux)

**Problem:** Python 3 isn't installed or isn't in your PATH.

**Fix:**
```bash
# Check if Python is installed
which python3

# If not found, install it:
# macOS:
brew install python3

# Ubuntu/Debian:
sudo apt update
sudo apt install python3 python3-pip python3-venv

# Fedora:
sudo dnf install python3
```

### Not enough disk space

**Problem:** Your laptop is nearly full.

**Fix:** Python needs about 200-400MB. Clear space by:
- Deleting old downloads
- Clearing browser cache
- Removing unused apps
- Using cloud storage

**Alternative:** Use [Google Colab](https://colab.research.google.com) -- free Python in the browser, no installation needed.

## Common Python Errors

### SyntaxError

```python
>>> print "Hello"
  File "<stdin>", line 1
    print "Hello"
          ^
SyntaxError: Missing parentheses in call to 'print'.
```

**Cause:** Python 3 requires parentheses for `print()`.

**Fix:** `print("Hello")`

### NameError

```python
>>> print(name)
NameError: name 'name' is not defined
```

**Cause:** You're trying to use a variable that doesn't exist.

**Fix:** Define it first: `name = "Juan"`

### TypeError

```python
>>> "Hello" + 5
TypeError: can only concatenate str (not "int") to str
```

**Cause:** You're trying to combine different data types.

**Fix:** Convert the type: `str(5)` or `int("5")`

### IndexError

```python
>>> my_list = [1, 2, 3]
>>> my_list[5]
IndexError: list index out of range
```

**Cause:** You're trying to access an index that doesn't exist.

**Fix:** Python uses 0-based indexing. Valid indices are 0, 1, 2 for a 3-item list.

### KeyError

```python
>>> my_dict = {"name": "Juan"}
>>> my_dict["age"]
KeyError: 'age'
```

**Cause:** You're trying to access a dictionary key that doesn't exist.

**Fix:** Check if the key exists first:
```python
if "age" in my_dict:
    print(my_dict["age"])
# Or use .get():
print(my_dict.get("age", "Not found"))
```

### IndentationError

```python
>>> def hello():
... print("Hi")
  File "<stdin>", line 2
    print("Hi")
    ^
IndentationError: expected an indented block.
```

**Cause:** Python uses indentation to define code blocks. The code inside a function must be indented.

**Fix:**
```python
def hello():
    print("Hi")  # Indented!
```

## File Issues

### "FileNotFoundError"

```python
>>> with open("data.txt", "r") as f:
...     print(f.read())
FileNotFoundError: [Errno 2] No such file or directory: 'data.txt'
```

**Cause:** The file doesn't exist at the specified path.

**Fix:**
```python
import os
if os.path.exists("data.txt"):
    with open("data.txt", "r") as f:
        print(f.read())
else:
    print("File not found. Creating it...")
    with open("data.txt", "w") as f:
        f.write("")
```

### "Permission denied" (Linux/macOS)

**Cause:** The file isn't writable or you don't have permission.

**Fix:**
```bash
# Check permissions
ls -la data.txt

# Add write permission
chmod u+w data.txt
```

## Package Issues

### "ModuleNotFoundError"

```python
>>> import requests
ModuleNotFoundError: No module named 'requests'
```

**Cause:** The package isn't installed.

**Fix:**
```bash
pip install requests
```

### "pip is not recognized" (Windows)

**Cause:** pip isn't in your PATH.

**Fix:**
```bash
# Try using python -m pip instead:
python -m pip install requests

# Or add pip to PATH:
# C:\Users\YourName\AppData\Local\Programs\Python\Python3xx\Scripts\
```

### Conflicting package versions

```python
>>> import some_package
ImportError: some_package requires version X, but Y is installed.
```

**Fix:** Use a virtual environment:
```bash
# Create a virtual environment
python -m venv venv

# Activate it
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# Install packages
pip install requests
```

## Network Issues

### API requests failing

**Possible causes:**
1. No internet connection
2. API key is invalid or expired
3. Rate limit exceeded
4. API endpoint changed

**Fix:**
```python
import requests

try:
    response = requests.get("https://api.example.com/data", timeout=10)
    response.raise_for_status()  # Raise error for bad status codes
    data = response.json()
except requests.exceptions.ConnectionError:
    print("Connection error. Check your internet.")
except requests.exceptions.Timeout:
    print("Request timed out. Try again.")
except requests.exceptions.HTTPError as e:
    print(f"HTTP error: {e}")
except requests.exceptions.RequestException as e:
    print(f"Request failed: {e}")
```

## Performance Issues

### Program is too slow

**Possible causes:**
1. Infinite loop
2. Processing too much data at once
3. Repeatedly reading from disk

**Fix:**
```python
# Use generators for large datasets
def read_lines(filename):
    with open(filename, "r") as f:
        for line in f:  # Generator -- reads one line at a time
            yield line

# Use caching for repeated calculations
from functools import lru_cache

@lru_cache(maxsize=128)
def expensive_computation(x):
    return x * x * x  # cached for repeated calls
```

### Program uses too much memory

**Fix:**
```python
# Process data in chunks instead of loading everything
CHUNK_SIZE = 1000

def process_large_file(filename):
    with open(filename, "r") as f:
        chunk = []
        for line in f:
            chunk.append(line)
            if len(chunk) >= CHUNK_SIZE:
                process(chunk)  # Process the chunk
                chunk = []  # Free memory
        if chunk:
            process(chunk)  # Process remaining lines
```

## Terminal/Command Line Issues

### "Tab completion not working"

**Fix:** Make sure your terminal emulator supports tab completion. In Termux:
```bash
pkg install bash
```

### "Terminal is too narrow for my output"

**Fix:** Format output for narrow screens:
```python
def compact_print(data, max_width=40):
    for key, value in data.items():
        display_key = str(key)[:max_width - 15]
        print(f"  {str(display_key):.<20} {value}")
```

## Discord.py Troubleshooting

### "Privileged Intents" error

**Problem:** Your bot can't read messages.

**Fix:**
1. Go to [Discord Developer Portal](https://discord.com/developers/applications)
2. Select your bot → Bot
3. Enable "Message Content Intent" under Privileged Gateway Intents
4. Update your code:
```python
intents = discord.Intents.default()
intents.message_content = True
bot = discord.Bot(intents=intents)
```

### "Invalid token" error

**Problem:** Your bot token is wrong or expired.

**Fix:**
1. Go to Discord Developer Portal → Your Bot
2. Click "Reset Token" and copy the new token
3. Never share your token publicly
4. Use environment variables:
```python
import os
bot.run(os.environ["DISCORD_TOKEN"])
```

### Bot not responding to commands

**Common causes:**
1. Bot doesn't have permission to send messages in the channel
2. Intents not configured properly
3. Bot is offline (check `on_ready()` prints)

## Asyncio Troubleshooting

### "RuntimeWarning: coroutine was never awaited"

**Problem:** You forgot to `await` an async function.

**Fix:**
```python
# Wrong:
async def hello():
    return "hi"
hello()  # Never awaited!

# Correct:
result = asyncio.run(hello())
# or inside another async function:
result = await hello()
```

### "This event loop is already running"

**Problem:** You called `asyncio.run()` inside an async function.

**Fix:** Use `await` instead of `asyncio.run()`:
```python
# Wrong inside async def:
async def main():
    asyncio.run(something())  # Error!

# Correct:
async def main():
    await something()
```

### "Task exception was never retrieved"

**Problem:** An async task raised an error but nobody caught it.

**Fix:** Add error handling:
```python
async def safe_task():
    try:
        await risky_operation()
    except Exception as e:
        print(f"Error: {e}")
```

## Matplotlib Troubleshooting

### Charts don't show up

**Problem:** `plt.show()` doesn't work in Jupyter, cron jobs, or remote servers.

**Fix:** Use `plt.savefig()` instead:
```python
plt.savefig("chart.png", dpi=150, bbox_inches="tight")
```

### "Agg backend" warning

**Problem:** Running matplotlib without a display (SSH, cron, Docker).

**Fix:** Set non-interactive backend before importing pyplot:
```python
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
```

### Charts look blurry

**Fix:** Increase DPI:
```python
plt.savefig("chart.png", dpi=300, bbox_inches="tight")
```

## Pandas Troubleshooting

### "SettingWithCopyWarning"

**Problem:** Modifying a slice of a DataFrame.

**Fix:** Use `.copy()` or `.loc[]`:
```python
# Wrong:
df[df["age"] > 25]["name"] = "Adult"  # Warning!

# Correct:
df.loc[df["age"] > 25, "name"] = "Adult"
# or:
subset = df[df["age"] > 25].copy()
subset["name"] = "Adult"
```

### "None of [columns] are in the columns"

**Problem:** Column name doesn't exist (typo or whitespace issue).

**Fix:**
```python
print(df.columns)  # Check exact column names
# Strip whitespace from column names:
df.columns = df.columns.str.strip()
```

## Kivy Troubleshooting

### App crashes on launch

**Problem:** `__init__` override conflicts with Kivy's App class.

**Fix:** Initialize your data before calling `super().__init__()`:
```python
class MyApp(App):
    def __init__(self):
        self.data = []  # Init your data first
        super().__init__()  # Then call parent

    def build(self):
        # Build UI here
        return BoxLayout()
```

### Kivy not found on Android (Termux)

**Fix:**
```bash
# Termux:
pkg install python kivy

# Or use pip:
pip install kivy
```

### Kivy app too slow on low-end device

**Fix:** Reduce window size and complexity:
```python
from kivy.core.window import Window
Window.size = (360, 640)  # Phone size
```

## Getting Help

When you're stuck:

1. **Read the error message carefully** -- It usually tells you exactly what's wrong
2. **Google the error** -- "Python [error message]" usually has solutions
3. **Ask AI** -- Paste the error and your code, ask for help
4. **Ask your barkada** -- Bayanihan!
5. **Take a break** -- Sometimes the answer comes when you're not looking at the code

### Useful Resources

| Resource | URL |
|----------|-----|
| Python docs | https://docs.python.org/3/ |
| Stack Overflow | https://stackoverflow.com/ |
| r/learnpython | https://reddit.com/r/learnpython |
| Python Discord | https://pythondiscord.com/ |
| Real Python | https://realpython.com/ |

---

*Remember: errors are data. Every error you read makes you a better programmer.*
