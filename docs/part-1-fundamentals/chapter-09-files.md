# Chapter 9: Files and JSON for the Store

??? example "📋 Chapter Info"
    | | |
    |---|---|
    | **Difficulty** | ⭐⭐ Beginner |
    | **Time** | 30 min |
    | **XP** | +100 XP |

> **Story Hook:** Lola closes the store at night, but the work is not really done. Tomorrow she still needs the same inventory, the same prices, and the same records. If the program forgets everything when it closes, it is not very useful. Files fix that.

> **Output:** A small store saver that can write inventory data to a file and load it again later.

---

## What You'll Learn

- Why files matter for long-term data
- How to use `with open(...)`
- The difference between text files, CSV, and JSON
- How to save and load store inventory data

## Why Save Data?

Variables live in memory. When the program ends, memory disappears.

Files let the program remember things between sessions.

## The `with` Statement

Use `with` so Python handles closing the file for you.

```python
with open("notes.txt", "w") as file:
    file.write("Lola's store inventory\n")
    file.write("laundry soap: 10\n")

with open("notes.txt", "r") as file:
    content = file.read()
    print(content)
```

??? tip "Diskarte"
    `with` is the safe default. You do not need to remember to close the file manually.

## File Modes

| Mode | Meaning | Creates file? |
|------|---------|---------------|
| `"r"` | Read | No |
| `"w"` | Write, overwrite | Yes |
| `"a"` | Append to end | Yes |
| `"r+"` | Read and write | No |

## CSV

CSV is good for simple table-like data.

```csv
item,qty,price
laundry soap,10,15.00
candy,25,5.00
rice,8,55.00
```

CSV is useful when your data looks like rows and columns.

## JSON

JSON is better for nested store data because it matches Python dictionaries closely.

```json
{
  "store_name": "Lola's Store",
  "inventory": {
    "laundry soap": {"qty": 10, "price": 15.0},
    "candy": {"qty": 25, "price": 5.0}
  }
}
```

## Saving Store Data

```python
import json

inventory = {
    "laundry soap": {"qty": 10, "price": 15.0},
    "candy": {"qty": 25, "price": 5.0},
}

with open("store.json", "w") as file:
    json.dump(inventory, file, indent=2)
```

## Loading Store Data

```python
import json
import os

if os.path.exists("store.json"):
    with open("store.json", "r") as file:
        inventory = json.load(file)
else:
    inventory = {}

print(inventory)
```

## Why JSON Fits This Book

Earlier chapters already use dictionaries for inventory.

JSON is a natural next step because it keeps the same shape when written to a file and loaded back later.

## A Tiny Store Backup Example

```python
import json


def save_inventory(filename, inventory):
    with open(filename, "w") as file:
        json.dump(inventory, file, indent=2)


def load_inventory(filename):
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}


store = {
    "laundry soap": {"qty": 10, "price": 15.0},
    "candy": {"qty": 25, "price": 5.0},
}

save_inventory("store.json", store)
loaded_store = load_inventory("store.json")
print(loaded_store)
```

## Summary

- Files let programs remember data after they close
- `with open(...)` is the safe way to handle files
- CSV is good for rows and columns
- JSON is great for nested dictionaries
- Saving and loading data makes small tools much more useful

## Side Quest

??? note "Optional: Practice"
    Save your own small inventory dictionary to a JSON file, then load it back and print it.

## Further Reading

- [Python's official tutorial on file I/O](https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files)
- [Real Python: JSON](https://realpython.com/python-json/)

*Previous: [Chapter 8: Functions and Reusable Helpers](chapter-08-functions.md) -- Reusing logic*
*Next: [Chapter 10: Boss Fight 1 -- The Complete Sari-Sari Store System](chapter-10-boss-fight-1.md) -- Combining everything.*
