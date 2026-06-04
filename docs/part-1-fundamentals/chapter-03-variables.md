# Chapter 3: Variables, Data Types, and the Sari-Sari Store

??? example "📋 Chapter Info"
    | | |
    |---|---|
    | **Difficulty** | ⭐⭐ Beginner |
    | **Time** | 30 min |
    | **XP** | +100 XP |

> **Story Hook:** It's 6 AM. Your Lola opens her sari-sari store for the day. She walks through the rows of shelves, checking what needs restocking. "Tatlong laundry soap, sampung biskwit, lima na lang sigarilyo," she mutters. She keeps track of everything in a small notebook -- items on the left, quantities on the right, prices in a column. It works, but sometimes she miscounts. You think: "Lola, let me help you with this."

> **Output:** A simple inventory script that stores item names, counts, and prices.

---

## What You'll Learn

- What variables are and why they're useful
- Basic data types: strings, integers, floats
- Lists: storing multiple items
- Dictionaries: storing key-value pairs (the sari-sari store's best friend)
- Basic input and output

## Variables: Lalagyan ng Impormasyon

A **variable** is like a labeled container. You put something inside, give it a name, and you can use that name later.

```python
# Creating variables
item = "laundry soap"
quantity = 10
price = 15.00
```

Think of it like the labels Lola puts on her shelves. "Laundry soap" is the label (variable name), and "10" is what's inside (value).

??? tip "Diskarte"
    Variable names should be descriptive. `quantity` is better than `q`. `item_price` is better than `x`. Good variable names are like good shelf labels -- they tell you what's inside without opening the container.

??? tip "⏸️ Pause and Predict"

    **Before reading the code below, predict: what do you think happens when you assign a string to a variable that previously held a number?**

    Take 30 seconds to think about your answer before reading on. This is how you build real understanding!

## Data Types: Kung Ano ang Iyong Tinatago

Python has different types for different kinds of data:

| Type | Example | What It Stores |
|------|---------|---------------|
| `str` (string) | `"laundry soap"` | Text |
| `int` (integer) | `10` | Whole numbers |
| `float` (float) | `15.00` | Decimal numbers |
| `bool` (boolean) | `True` / `False` | Yes/No values |

```python
# String: text
item = "laundry soap"

# Integer: whole number
quantity = 10

# Float: decimal number
price = 15.00

# Boolean: True or False
in_stock = True
```

??? bug "Common Mistake"
    `"10"` (with quotes) is a string, not a number. `10` (without quotes) is an integer. Mixing these up is the #1 beginner error.

    ```pycon
    >>> "10" + 5
    TypeError: can only concatenate str (not "int") to str

    >>> 10 + 5
    15
    ```

## Lists: Mga Item sa Shelb

A **list** stores multiple items in order. Think of it like a shelf with items lined up:

```python
# A list of inventory items
inventory = ["laundry soap", "cigarettes", "candy", "instant noodles", "softdrinks"]

# Access individual items (Python starts counting at 0!)
print(inventory[0])  # laundry soap
print(inventory[2])  # candy
```

??? note "Try It Yourself"
    Create a list of your favorite merienda items and print the first and last one.

### List Operations

```python
# Add an item
inventory.append("coffee")

# Remove an item
inventory.remove("candy")

# Check how many items
print(len(inventory))  # 5

# Check if an item is in the list
print("cigarettes" in inventory)  # True
```

## Dictionaries: Ang Puso ng Sari-Sari Store

A **dictionary** stores items as **key-value pairs**. This is the most important data structure for our sari-sari store project:

```python
# Inventory as a dictionary
inventory = {
    "laundry soap": 10,
    "cigarettes": 50,
    "candy": 25,
    "instant noodles": 30,
    "softdrinks": 20,
}
```

Each item has a **name** (key) and a **quantity** (value). It's like Lola's notebook but organized.

### Working with Dictionaries

```python
# Access a value by its key
print(inventory["laundry soap"])  # 10

# Add a new item
inventory["coffee"] = 15

# Update a quantity
inventory["candy"] = 20

# Check if an item exists
if "cigarettes" in inventory:
    print("Available: " + str(inventory["cigarettes"]))

# Loop through all items
for item, qty in inventory.items():
    print(f"{item}: {qty} left")
```

??? tip "Diskarte"
    Dictionaries are like real dictionaries: you look up a word (key) and get its definition (value). In our store, you look up an item name and get its quantity. Same pattern, different context.

## Input: Talking to Your Program

So far, our programs only do what we tell them to. But what if we want the **user** to decide what happens? That's where `input()` comes in:

```python
# Ask the user for their name
name = input("Ano ang pangalan mo? ")
print(f"Kumusta, {name}!")
```

??? note "Try It Yourself"
    Try this in the interpreter:

    ```pycon
    >>> name = input("Ano ang pangalan mo? ")
    Ano ang pangalan mo? Juan
    >>> print(f"Kumusta, {name}!")
    Kumusta, Juan!
    ```

## Building Your Sari-Sari Store Inventory

Let's put it all together. Here's a simple inventory system:

```python
# Sari-Sari Store Inventory System
# Chapter 3

# Store name
store_name = "Lola's Sari-Sari Store"

# Inventory dictionary
inventory = {
    "laundry soap": 10,
    "cigarettes": 50,
    "candy": 25,
    "instant noodles": 30,
    "softdrinks": 20,
}

# Display inventory
print(f"=== {store_name} ===")
print("Current Inventory:")
for item, qty in inventory.items():
    print(f"  {item}: {qty}")

# Add new item
new_item = input("\nAdd new item: ")
new_qty = int(input(f"Quantity of {new_item}: "))
inventory[new_item] = new_qty

# Display updated inventory
print(f"\nUpdated Inventory:")
for item, qty in inventory.items():
    print(f"  {item}: {qty}")
```

??? bug "Common Mistake"
    `input()` always returns a string. If you need a number, wrap it in `int()` or `float()`:

    ```pycon
    >>> quantity = input("Quantity: ")
    Quantity: 10
    >>> type(quantity)
    <class 'str'>

    >>> quantity = int(input("Quantity: "))
    Quantity: 10
    >>> type(quantity)
    <class 'int'>
    ```

??? example "Portfolio Tip: Show Your Foundation"
    Your sari-sari store inventory script is a great first project! Here's how to make it portfolio-ready:

    1. **Push to GitHub** -- Create a repo called `sari-sari-store-inventory` with a README that explains the problem you solved
    2. **Screenshot it** -- Take a screenshot of the program running and add it to your README
    3. **LinkedIn** -- You can add this to your About section: "Built a Python inventory management system for small businesses"
    4. **Interview talking point** -- "You can say: I started with Python fundamentals and applied them to build a real tool that helps track inventory for small stores like the ones in my community."

## Summary

- **Variables** are labeled containers for data
- **Data types** include strings (text), integers (whole numbers), floats (decimals), and booleans (True/False)
- **Lists** store ordered collections of items
- **Dictionaries** store key-value pairs -- perfect for inventory systems
- **`input()`** lets users interact with your program
- Python starts counting at 0 (not 1)

## Boss Fight

??? warning "Boss Fight: Complete Inventory System"

    Build a complete sari-sari store inventory system that can:

    1. Display all items and quantities
    2. Add new items
    3. Sell items (reduce quantity)
    4. Check if an item is in stock
    5. Show total inventory value (quantity × price)

    **Hint:** Use a dictionary with nested data. Each item should have both quantity and price:

    ```python
    inventory = {
        "laundry soap": {"qty": 10, "price": 15.00},
        "cigarettes": {"qty": 50, "price": 5.00},
    }
    ```

    **Side quest:** Add a "low stock" warning when quantity drops below 5.

??? note "Hint 1"
    To sell an item: `inventory[item]["qty"] -= amount` (subtract from quantity)

??? note "Hint 2"
    To calculate total value: sum up `qty * price` for all items

??? success "You did it! Level Up!"
    +150 XP. You built a real inventory system. Ang galing!

## Side Quests

??? note "Optional: Side Quest"
    - Add a feature to sort inventory by quantity (lowest first)
    - Create a "restock list" that shows items below a threshold
    - Add prices to your inventory and calculate total store value

## Further Reading

- [Python's official tutorial on data structures](https://docs.python.org/3/tutorial/datastructures.html)
- [Real Python: Dictionaries](https://realpython.com/python-dicts/)

??? example "🧠 Reflection — Variables and Data Types"

    - **What did you learn?** Variables store data, and Python has different types — strings, integers, floats, lists, and dictionaries — each suited for different kinds of information.
    - **How can you apply this?** Think of your lola's sari-sari store notebook: variables are the labeled shelves, lists are the rows of products, and dictionaries are the item-to-price lookup. You can use the same structures to organize any collection of data in your daily life.
    - **What's next?** Once you can store data, the next question is: how do you make decisions based on it?

??? checkbox "✅ Chapter Checklist"

    - [ ] I can create variables and assign values of different data types
    - [ ] I can tell the difference between a string `"10"` and an integer `10`
    - [ ] I can use lists to store and access collections of items
    - [ ] I can use dictionaries to store and retrieve key-value pairs
    - [ ] I can use `input()` to get user input and convert it to the right type

---

*Previous: [Chapter 2: Bahala Na](../part-0-welcome/chapter-02-bahala-na.md) -- Learning the philosophy*
*Next: [Chapter 4: Comparisons and Truth Values at the Store](chapter-04-conditionals.md) -- Checking what is true or false.*
