# Appendix: Python Reference

> Quick reference for Python keywords, built-in functions, and common patterns. Bookmark this page!

---

**Related chapters:** [Ch 3](../part-1-fundamentals/chapter-03-variables.md) (Variables & Data Types) | [Ch 4](../part-1-fundamentals/chapter-04-conditionals.md) (Conditionals) | [Ch 5](../part-1-fundamentals/chapter-05-loops.md) (Loops) | [Ch 6](../part-1-fundamentals/chapter-06-functions.md) (Functions) | [Ch 7](../part-1-fundamentals/chapter-07-files.md) (File I/O) | [Ch 9](../part-2-building-things/chapter-09-classes.md) (Classes) | [Ch 11](../part-2-building-things/chapter-11-apis.md) (APIs) | [Ch 13](../part-2-building-things/chapter-13-errors.md) (Errors) | [Ch 15](../part-3-going-further/chapter-15-discord-bots.md) (Async & Discord) | [Ch 16](../part-3-going-further/chapter-16-dataviz.md) (Data Viz)

---

## Python Keywords

These are reserved words you can't use as variable names:

```
and       as        assert    async     await
break     class     continue  def       del
elif      else      except    False     finally
for       from      global    if        import
in        is        lambda    None      nonlocal
not       or        pass      raise     return
True      try       while     with      yield
```

## Built-in Functions

### Data Type Functions

| Function | What It Does | Example |
|----------|-------------|---------|
| `int()` | Convert to integer | `int("42")` → `42` |
| `float()` | Convert to float | `float("3.14")` → `3.14` |
| `str()` | Convert to string | `str(42)` → `"42"` |
| `list()` | Convert to list | `list("hello")` → `['h','e','l','l','o']` |
| `dict()` | Convert to dict | `dict(a=1, b=2)` → `{'a': 1, 'b': 2}` |
| `tuple()` | Convert to tuple | `tuple([1, 2, 3])` → `(1, 2, 3)` |
| `set()` | Convert to set | `set([1, 1, 2])` → `{1, 2}` |
| `bool()` | Convert to boolean | `bool(0)` → `False`, `bool(1)` → `True` |

### Math Functions

| Function | What It Does | Example |
|----------|-------------|---------|
| `abs()` | Absolute value | `abs(-5)` → `5` |
| `round()` | Round to nearest | `round(3.14159, 2)` → `3.14` |
| `max()` | Maximum value | `max(1, 5, 3)` → `5` |
| `min()` | Minimum value | `min(1, 5, 3)` → `1` |
| `sum()` | Sum of list | `sum([1, 2, 3])` → `6` |
| `pow()` | Power | `pow(2, 3)` → `8` |

### Sequence Functions

| Function | What It Does | Example |
|----------|-------------|---------|
| `len()` | Length of sequence | `len("hello")` → `5` |
| `range()` | Number sequence | `range(5)` → `0, 1, 2, 3, 4` |
| `enumerate()` | Index + value | `enumerate(["a","b"])` → `(0,"a"), (1,"b")` |
| `zip()` | Combine lists | `zip([1,2], [3,4])` → `(1,3), (2,4)` |
| `sorted()` | Sort a sequence | `sorted([3,1,2])` → `[1,2,3]` |
| `reversed()` | Reverse a sequence | `reversed([1,2,3])` → `[3,2,1]` |
| `any()` | Any True? | `any([False, True])` → `True` |
| `all()` | All True? | `all([True, True])` → `True` |

### Input/Output

| Function | What It Does | Example |
|----------|-------------|---------|
| `print()` | Display output | `print("Hello")` |
| `input()` | Get user input | `name = input("Name: ")` |
| `open()` | Open a file | `f = open("data.txt", "r")` |

### Type Checking

| Function | What It Does | Example |
|----------|-------------|---------|
| `type()` | Get type | `type(42)` → `<class 'int'>` |
| `isinstance()` | Check type | `isinstance(42, int)` → `True` |
| `hasattr()` | Check attribute | `hasattr(obj, "name")` |
| `getattr()` | Get attribute | `getattr(obj, "name", default)` |
| `setattr()` | Set attribute | `setattr(obj, "name", value)` |

## String Methods

| Method | What It Does | Example |
|--------|-------------|---------|
| `.upper()` | All uppercase | `"hello".upper()` → `"HELLO"` |
| `.lower()` | All lowercase | `"HELLO".lower()` → `"hello"` |
| `.strip()` | Remove whitespace | `"  hello  ".strip()` → `"hello"` |
| `.replace()` | Replace text | `"hello".replace("l", "r")` → `"herro"` |
| `.split()` | Split into list | `"a,b,c".split(",")` → `["a","b","c"]` |
| `.join()` | Join list to string | `"-".join(["a","b"])` → `"a-b"` |
| `.startswith()` | Check prefix | `"hello".startswith("he")` → `True` |
| `.endswith()` | Check suffix | `"hello".endswith("lo")` → `True` |
| `.find()` | Find substring | `"hello".find("ll")` → `2` |
| `.count()` | Count occurrences | `"banana".count("a")` → `3` |
| `.isalpha()` | All letters? | `"hello".isalpha()` → `True` |
| `.isdigit()` | All digits? | `"123".isdigit()` → `True` |
| `.islower()` | All lowercase? | `"hello".islower()` → `True` |
| `.isupper()` | All uppercase? | `"HELLO".isupper()` → `True` |

## List Methods

| Method | What It Does | Example |
|--------|-------------|---------|
| `.append()` | Add to end | `lst.append(4)` |
| `.insert()` | Add at index | `lst.insert(0, "first")` |
| `.remove()` | Remove by value | `lst.remove("item")` |
| `.pop()` | Remove by index | `lst.pop(0)` |
| `.sort()` | Sort in place | `lst.sort()` |
| `.reverse()` | Reverse in place | `lst.reverse()` |
| `.index()` | Find index | `lst.index("item")` |
| `.count()` | Count occurrences | `lst.count("item")` |
| `.copy()` | Shallow copy | `new_lst = lst.copy()` |
| `.clear()` | Remove all items | `lst.clear()` |

## Dictionary Methods

| Method | What It Does | Example |
|--------|-------------|---------|
| `.keys()` | All keys | `d.keys()` |
| `.values()` | All values | `d.values()` |
| `.items()` | Key-value pairs | `d.items()` |
| `.get()` | Get with default | `d.get("key", "default")` |
| `.setdefault()` | Set if not exists | `d.setdefault("key", 0)` |
| `.update()` | Merge dicts | `d.update({"a": 1})` |
| `.pop()` | Remove and return | `d.pop("key")` |
| `.clear()` | Remove all items | `d.clear()` |

## File Operations

```python
# Reading files
with open("file.txt", "r") as f:
    content = f.read()        # Read entire file
    lines = f.readlines()     # Read as list of lines
    for line in f:             # Read line by line
        print(line.rstrip())

# Writing files
with open("file.txt", "w") as f:
    f.write("Hello")          # Write (overwrites)

with open("file.txt", "a") as f:
    f.write("Hello")          # Append (adds to end)

# File modes
# "r" = read (default)
# "w" = write (overwrites)
# "a" = append
# "r+" = read and write
# "b" = binary mode (e.g., "rb", "wb")
```

## Common Patterns

### F-strings

```python
name = "Juan"
age = 25
print(f"My name is {name} and I'm {age} years old")
print(f"Next year I'll be {age + 1}")
print(f"Price: ₱{15.00:.2f}")  # Format with 2 decimal places
```

### List Comprehensions

```python
# Basic
squares = [x**2 for x in range(10)]

# With condition
evens = [x for x in range(20) if x % 2 == 0]

# Nested
matrix = [[i*j for j in range(1, 4)] for i in range(1, 4)]
```

### Try/Except

```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Can't divide by zero!")
except TypeError as e:
    print(f"Type error: {e}")
except Exception as e:
    print(f"Unexpected error: {e}")
else:
    print("No errors!")
finally:
    print("This always runs")
```

### Working with JSON

```python
import json

# Read JSON file
with open("data.json", "r") as f:
    data = json.load(f)

# Write JSON file
with open("data.json", "w") as f:
    json.dump(data, f, indent=4)

# JSON string to dict
data = json.loads('{"name": "Juan"}')

# Dict to JSON string
json_str = json.dumps({"name": "Juan"}, indent=4)
```

### Working with Dates

```python
from datetime import datetime, date, timedelta

now = datetime.now()
today = date.today()

# Format dates
print(now.strftime("%Y-%m-%d %H:%M:%S"))  # 2025-01-15 14:30:00

# Parse dates
dt = datetime.strptime("2025-01-15", "%Y-%m-%d")

# Date arithmetic
tomorrow = today + timedelta(days=1)
last_week = today - timedelta(weeks=1)
```

## Virtual Environments

```bash
# Create
python -m venv venv

# Activate
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# Install packages
pip install requests

# Save requirements
pip freeze > requirements.txt

# Install from requirements
pip install -r requirements.txt

# Deactivate
deactivate
```

## Asyncio Quick Reference

```python
import asyncio

# Basic async function
async def greet(name):
    await asyncio.sleep(1)
    return f"Kumusta, {name}!"

# Run a single coroutine
result = asyncio.run(greet("Juan"))

# Run multiple coroutines concurrently
async def main():
    tasks = [greet("Juan"), greet("Maria"), greet("Pedro")]
    results = await asyncio.gather(*tasks)
    for r in results:
        print(r)

asyncio.run(main())

# Common patterns
asyncio.sleep(1)          # Non-blocking sleep
asyncio.gather(*tasks)    # Run all tasks concurrently
asyncio.create_task(coro) # Schedule a task in background
asyncio.wait_for(coro, timeout=5)  # Timeout after 5 seconds
```

## discord.py Quick Reference

```python
import discord
from discord.ext import commands

# Bot setup
intents = discord.Intents.default()
intents.message_content = True
bot = discord.Bot(intents=intents)

# Events
@bot.event
async def on_ready():
    print(f"Bot is ready! {bot.user}")

# Slash commands
@bot.slash_command(description="Say hello")
async def hello(ctx, name: str = "World"):
    await ctx.respond(f"Kumusta, {name}!")

# Message commands
@bot.slash_command(description="Remind me later")
async def remind(ctx, minutes: int, message: str):
    await ctx.respond(f"Will remind you in {minutes} minutes!")

# Run
bot.run("YOUR_TOKEN")
```

## Matplotlib Quick Reference

```python
import matplotlib.pyplot as plt

# Line chart
plt.plot([1, 2, 3], [4, 5, 6])
plt.title("Trend")
plt.xlabel("Time")
plt.ylabel("Value")

# Bar chart
plt.bar(["A", "B", "C"], [10, 20, 15])
plt.title("Comparison")

# Horizontal bar chart
plt.barh(["A", "B", "C"], [10, 20, 15])

# Pie chart
plt.pie([30, 50, 20], labels=["A", "B", "C"], autopct="%1.1f%%")

# Multiple subplots
fig, axes = plt.subplots(2, 2, figsize=(12, 8))
axes[0, 0].plot([1, 2, 3], [4, 5, 6])
axes[0, 1].bar(["A", "B"], [10, 20])

# Save and show
plt.tight_layout()
plt.savefig("chart.png", dpi=150, bbox_inches="tight")
plt.show()

# Non-interactive backend (for servers/cron)
import matplotlib
matplotlib.use("Agg")
```

## Pandas Quick Reference

```python
import pandas as pd

# Create DataFrame
df = pd.DataFrame({
    "name": ["Juan", "Maria", "Pedro"],
    "age": [25, 30, 35],
    "amount": [1000, 2000, 1500],
})

# Read CSV
df = pd.read_csv("data.csv")

# Basic operations
df.columns              # Column names
df.head(5)              # First 5 rows
df.describe()           # Statistics
df["age"].mean()        # Mean of column
df[df["age"] > 25]      # Filter rows
df.sort_values("age")   # Sort by column
df.groupby("name")["amount"].sum()  # Group and aggregate

# Date handling
df["date"] = pd.to_datetime(df["date"])
df["date"].dt.strftime("%m/%d")     # Format date
df.set_index("date").resample("M").sum()  # Monthly aggregation

# Save
df.to_csv("output.csv", index=False)
df.to_json("output.json", indent=2)
```

## Regex Quick Reference

```python
import re

# Common patterns
re.search(r"\d+", "Age 25")           # Find digits: "25"
re.findall(r"\w+", "Hello World")     # Find words: ["Hello", "World"]
re.sub(r"\d+", "XXX", "Call 911")     # Replace: "Call XXX"
re.match(r"^Hi", "Hi there")          # Match at start

# Useful patterns
r"\d+"              # One or more digits
r"\w+"              # One or more word characters
r"\s+"              # One or more whitespace
r"[A-Z]"            # Uppercase letter
r"[a-z]"            # Lowercase letter
r"\b\w+\b"          # Whole word
r".*"               # Any characters (greedy)
r".*?"              # Any characters (lazy)
r"(?i)pattern"      # Case insensitive

# Common use cases
re.sub(r"\s+", " ", text)           # Collapse whitespace
re.findall(r"[^\s]+", text)         # Split into words
re.match(r"^\d{3}-\d{4}$", "123-4567")  # Validate format
```

---

*Keep this reference handy. You'll use these patterns again and again.*

---

*Previous: [Troubleshooting](troubleshooting.md) -- Common issues and fixes*
*Next: [Glossary](glossary.md) -- Key terms*
