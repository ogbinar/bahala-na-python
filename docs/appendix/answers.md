# Appendix: Answers to Practice Questions

> Here are the answers to the practice exercises throughout the book. Try the exercises yourself before looking at the answers -- that's where the real learning happens.

---

## Chapter 3: Variables, Data Types, and the Sari-Sari Store

### Exercise 1: Variables

```python
# Create variables for a sari-sari store item
item = "laundry soap"
quantity = 10
price = 15.00
in_stock = True

print(f"{item}: {quantity} in stock @ ₱{price}")
```

### Exercise 2: Lists

```python
# Create a list of merienda items
merienda = ["pan de sal", "banana cue", "fishball", "kikiam", "camote cue"]

# Print first and last
print(f"First: {merienda[0]}")
print(f"Last: {merienda[-1]}")

# Add a new item
merienda.append("fishball with spicy sauce")
print(f"Updated: {merienda}")
```

### Exercise 3: Dictionaries

```python
# Sari-sari store inventory
inventory = {
    "laundry soap": {"qty": 10, "price": 15.00},
    "cigarettes": {"qty": 50, "price": 5.00},
    "candy": {"qty": 25, "price": 3.00},
}

# Sell 3 candies
inventory["candy"]["qty"] -= 3
print(f"Candy left: {inventory['candy']['qty']}")

# Add coffee
inventory["coffee"] = {"qty": 15, "price": 12.00}
```

### Boss Fight: Complete Inventory System

```python
# Complete sari-sari store inventory system

inventory = {
    "laundry soap": {"qty": 10, "price": 15.00},
    "cigarettes": {"qty": 50, "price": 5.00},
    "candy": {"qty": 25, "price": 3.00},
    "instant noodles": {"qty": 30, "price": 8.00},
    "softdrinks": {"qty": 20, "price": 15.00},
}

def display_inventory():
    print("\n=== Sari-Sari Store Inventory ===")
    for item, data in inventory.items():
        print(f"  {item}: {data['qty']} @ ₱{data['price']:.2f}")

def sell_item(name, qty):
    name = name.lower().strip()
    if name in inventory:
        if inventory[name]["qty"] >= qty:
            inventory[name]["qty"] -= qty
            print(f"Sold {qty}x {name}")
            if inventory[name]["qty"] < 5:
                print(f"⚠️ Low stock: {name} ({inventory[name]['qty']} left)")
        else:
            print(f"Not enough stock! Only {inventory[name]['qty']} left.")
    else:
        print(f"'{name}' not found in inventory.")

def total_value():
    total = sum(data["qty"] * data["price"] for data in inventory.values())
    print(f"\nTotal inventory value: ₱{total:.2f}")

# Demo
display_inventory()
sell_item("candy", 3)
sell_item("laundry soap", 12)
total_value()
```

## Chapter 4: Conditionals

### Exercise 1: Jeepney Fare

```python
def calculate_fare(distance_km):
    base_fare = 13.00
    additional_per_km = 0.00  # Simplified -- actual rates vary
    if distance_km <= 4:
        return base_fare
    else:
        return base_fare + (distance_km - 4) * 1.00

print(f"Fare for 7km: ₱{calculate_fare(7):.2f}")
```

### Exercise 2: GCash Transaction

```python
balance = 500.00

def gcash_transaction(action, amount):
    global balance
    if action == "send":
        if amount <= balance:
            balance -= amount
            print(f"Sent ₱{amount:.2f}. Balance: ₱{balance:.2f}")
        else:
            print("Insufficient funds!")
    elif action == "receive":
        balance += amount
        print(f"Received ₱{amount:.2f}. Balance: ₱{balance:.2f}")

gcash_transaction("send", 100)
gcash_transaction("receive", 200)
gcash_transaction("send", 600)  # Should fail
```

## Chapter 5: Loops

### Exercise 1: Merienda Counter

```python
# Track merienda purchases for a week
merienda_items = ["pan de sal", "banana cue", "fishball", "kikiam"]
daily_budget = 50.00
item_price = 10.00

for day in range(1, 8):  # Monday to Sunday
    items_bought = 0
    spent = 0

    while spent + item_price <= daily_budget:
        item = merienda_items[(day - 1 + items_bought) % len(merienda_items)]
        spent += item_price
        items_bought += 1
        print(f"Day {day}: Bought {item} (spent: ₱{spent:.2f})")

    print(f"Day {day} complete! Budget used: ₱{spent:.2f}/{daily_budget}\n")
```

### Boss Fight: Number Guessing Game

```python
import random

secret = random.randint(1, 100)
attempts = 0
max_attempts = 7

print(f"Guess the number (1-100). You have {max_attempts} attempts!")

for attempt in range(1, max_attempts + 1):
    guess = int(input(f"Attempt {attempt}/{max_attempts}: "))
    attempts += 1

    if guess == secret:
        print(f"🎉 Correct! You got it in {attempts} attempts!")
        break
    elif guess < secret:
        print("Too low! Try higher.")
    else:
        print("Too high! Try lower.")
else:
    print(f"😢 Game over! The number was {secret}.")
```

## Chapter 6: Functions

### Exercise 1: Budget Calculator

```python
def calculate_budget(allowance, fixed_costs, variable_costs=None):
    if variable_costs is None:
        variable_costs = []

    total_fixed = sum(fixed_costs.values())
    total_variable = sum(variable_costs)
    remaining = allowance - total_fixed - total_variable

    return {
        "allowance": allowance,
        "fixed_costs": total_fixed,
        "variable_costs": total_variable,
        "remaining": remaining,
        "daily_budget": remaining / 30 if remaining > 0 else 0,
    }

budget = calculate_budget(
    allowance=500,
    fixed_costs={"pamasahe": 30, "load": 50},
    variable_costs=[50, 80, 30]  # Merienda, photocopy, etc.
)

for key, value in budget.items():
    print(f"{key}: ₱{value:.2f}")
```

## Chapter 7: Files

### Boss Fight: Recipe Organizer

```python
import json
import os

RECIPES_FILE = "recipes.json"


def load_recipes():
    if os.path.exists(RECIPES_FILE):
        with open(RECIPES_FILE, "r") as f:
            return json.load(f)
    return []


def save_recipes(recipes):
    with open(RECIPES_FILE, "w") as f:
        json.dump(recipes, f, indent=4)


def add_recipe(recipes):
    name = input("Recipe name: ")
    ingredients = input("Ingredients (comma-separated): ").split(",")
    instructions = input("Instructions: ")

    recipe = {
        "name": name,
        "ingredients": [i.strip() for i in ingredients],
        "instructions": instructions,
    }
    recipes.append(recipe)
    save_recipes(recipes)
    print(f"Added: {name}")


def search_recipes(recipes, search_term):
    results = [r for r in recipes if search_term.lower() in r["name"].lower()]
    if results:
        print(f"Found {len(results)} recipe(s):")
        for r in results:
            print(f"  - {r['name']}")
    else:
        print("No recipes found.")


# Main
recipes = load_recipes()
add_recipe(recipes)
search_recipes(recipes, "adobo")
```

## Chapter 9: Classes

### Boss Fight: Extended Budget Manager

```python
from datetime import date, timedelta


class Expense:
    def __init__(self, category, amount, description=""):
        self.category = category
        self.amount = amount
        self.description = description


class Budget:
    def __init__(self, allowance, category_limits=None):
        self.allowance = allowance
        self.category_limits = category_limits or {}
        self.expenses = []

    def add_expense(self, category, amount, description=""):
        self.expenses.append(Expense(category, amount, description))

    def remaining(self):
        return self.allowance - sum(e.amount for e in self.expenses)

    def category_totals(self):
        totals = {}
        for e in self.expenses:
            totals[e.category] = totals.get(e.category, 0) + e.amount
        return totals

    def get_alerts(self):
        alerts = []
        for cat, total in self.category_totals().items():
            if cat in self.category_limits:
                pct = (total / self.category_limits[cat]) * 100
                if pct >= 80:
                    alerts.append(
                        f"⚠️ {cat}: {pct:.0f}% of limit used ({total}/{self.category_limits[cat]})"
                    )
        return alerts

    def recommendations(self):
        cat_totals = self.category_totals()
        recommendations = []
        for cat, total in cat_totals.items():
            if cat in self.category_limits and total > self.category_limits[cat] * 0.8:
                over = total - self.category_limits[cat]
                recommendations.append(
                    f"💡 Consider reducing {cat} spending by ₱{over:.2f}"
                )
        return recommendations


class Savings(Budget):
    def __init__(self, allowance, goal, category_limits=None):
        super().__init__(allowance, category_limits)
        self.goal = goal
        self.savings = 0

    def save(self, amount):
        self.savings += amount
        print(f"Saved ₱{amount:.2f}. Goal progress: {self.savings}/{self.goal}")

    def progress(self):
        return (self.savings / self.goal) * 100 if self.goal > 0 else 0


class WeeklyBudget(Budget):
    def __init__(self, daily_allowance):
        super().__init__(daily_allowance * 7)
        self.daily_allowance = daily_allowance
        self.days = list(range(1, 8))
        self.daily_spending = {day: 0 for day in self.days}

    def spend_today(self, day, category, amount):
        self.daily_spending[day] += amount
        super().add_expense(category, amount)
        remaining_today = self.daily_allowance - self.daily_spending[day]
        if remaining_today < 0:
            print(f"⚠️ Over daily budget by ₱{abs(remaining_today):.2f}!")
        return remaining_today


# Usage
budget = Budget(500, {"kain": 200, "pamasahe": 100})
budget.add_expense("kain", 150, "Jollibee")
budget.add_expense("kain", 80, "Merienda")
budget.add_expense("pamasahe", 30, "UD")

print("Alerts:", budget.get_alerts())
print("Recommendations:", budget.recommendations())

savings = Savings(500, goal=1000)
savings.save(200)
print(f"Progress: {savings.progress():.0f}%")
```

## Chapter 13: Errors

### Boss Fight: Debugging Challenge

The code below has 5 bugs. Can you find them all?

```python
# BUGGY CODE -- Find and fix the errors!

def calculate_discount(price, discount_percent):
    discount = price * discount_percent / 100
    return price - discount

def apply_discounts(items):
    total = 0
    for item in items:
        if item["discount"] > 0:
            price = calculate_discount(item["price"], item["discount"])
        else:
            price = item["price"]
        total += price
    return total

# Test data
items = [
    {"name": "Shirts", "price": 299, "discount": 20},
    {"name": "Pants", "price": 499, "discount": 10},
    {"name": "Shoes", "price": 899, "discount": 0},
]

print(f"Total: ₱{apply_discounts(items):.2f}")
```

**Answers:**
1. `price` should be `item["price"]` in the loop (variable name mismatch)
2. Need to handle empty items list
3. Discount calculation is correct but needs input validation
4. No error handling for non-numeric values
5. The `calculate_discount` function doesn't handle negative discounts

## Boss Fights: Part 2 (Chapters 14-16)

### Boss Fight: Error Handling Patterns (Chapter 14)

```python
def safe_divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("❌ Hindi pwedeng mag-divide ng zero!")
        return None
    except TypeError:
        print("❌ Mga number lang!")
        return None
    else:
        return result

# Test all cases
print(safe_divide(10, 2))     # 5.0
print(safe_divide(10, 0))     # Error message, None
print(safe_divide("10", 2))   # Error message, None
```

### Boss Fight: Discord Bot Challenge (Chapter 15)

**Approach:** Use `discord.Bot()` with slash commands. Key points:
- Use `@bot.slash_command` for slash commands
- Use `ctx.respond()` for initial response, `ctx.send()` follow-ups
- Store reminders in memory or a JSON file
- Use `asyncio.create_task()` for background tasks

### Boss Fight: Barangay Dashboard (Chapter 16)

**Approach:** Use `matplotlib` to create charts. Key points:
- Use `plt.subplots()` for multi-chart layouts
- Handle empty data with `if data:` guards
- Use `pd.DataFrame()` for data aggregation
- Save with `plt.savefig()` instead of `plt.show()` for non-interactive use

## Boss Fights: Part 3 (Chapters 17-20)

### Boss Fight: AI Barkada Chatbot (Chapter 17)

**Approach:** Build pattern-response matching with regex. Key points:
- Use `re.search()` for pattern matching
- Handle Taglish with flexible regex patterns
- Maintain conversation state with a dict
- Use sentiment analysis to adjust responses

### Boss Fight: Boss Fight 3 -- Barangay Dashboard Complete (Chapter 20)

**Approach:** Combine all Part 3 concepts. Key points:
- Use `asyncio` for concurrent API calls
- Use `matplotlib` for visualization with error handling
- Use `pandas` for data aggregation
- Structure code into classes: `DataCollector`, `DashboardVisualizer`, `ChatAnalyzer`

## Boss Fights: Part 4 (Chapters 21-25)

### Boss Fight: Mobile App Challenge (Chapter 21)

**Approach:** Use Kivy for cross-platform mobile UI. Key points:
- Don't override `__init__` before `super().__init__()`
- Use JSON for offline data storage
- Design for small screens (360x640 aspect ratio)

### Boss Fight: Bayanihan Toolkit (Chapter 22)

**Approach:** Use GitHub search API. Key points:
- Query: `https://api.github.com/search/repositories?q=good+first+issue+{keyword}`
- Parse JSON response for `stargazers_count`, `language`, `open_issues_count`
- Use `random.choice()` for random project feature

### Boss Fight: Barangay Management System (Chapter 23-24)

**Approach:** Full OOP system with CLI and optional web interface. Key points:
- Use classes for `Resident`, `FeeManager`, `CertificateGenerator`
- Use `json` for data persistence with `default=str` for dates
- Use `Flask` for web API endpoints with input validation

### Final Boss: Your Own Project (Chapter 25)

**Approach:** This is self-directed. Use the starter framework as a template. Key points:
- Pick a real problem you care about
- Start with the minimum working version
- Add features incrementally
- Use `json.dump(data, f, default=str)` for saving with date objects
- Don't get stuck -- bahala na!

---

*See the [troubleshooting appendix](troubleshooting.md) for common errors and their solutions.*
