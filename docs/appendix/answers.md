# Appendix: Answers to Practice Questions

> Here are the answers to the practice exercises throughout the book. Try the exercises yourself before looking at the answers -- that's where the real learning happens.

---

**Jump to a chapter:** [Ch 3](../part-1-fundamentals/chapter-03-variables.md) | [Ch 4](../part-1-fundamentals/chapter-04-conditionals.md) | [Ch 5](../part-1-fundamentals/chapter-05-loops.md) | [Ch 6](../part-1-fundamentals/chapter-06-functions.md) | [Ch 7](../part-1-fundamentals/chapter-07-files.md) | [Ch 9](../part-2-building-things/chapter-09-classes.md) | [Ch 10](../part-2-building-things/chapter-10-strings.md) | [Ch 11](../part-2-building-things/chapter-11-apis.md) | [Ch 12](../part-2-building-things/chapter-12-scraping.md) | [Ch 13](../part-2-building-things/chapter-13-errors.md) | [Ch 14](../part-2-building-things/chapter-14-boss-fight-2.md) | [Ch 15](../part-3-going-further/chapter-15-discord-bots.md) | [Ch 16](../part-3-going-further/chapter-16-dataviz.md) | [Ch 17](../part-3-going-further/chapter-17-nlp.md) | [Ch 18](../part-3-going-further/chapter-18-ai-coding.md) | [Ch 20](../part-3-going-further/chapter-20-boss-fight-3.md) | [Ch 21](../part-4-capstone/chapter-21-mobile.md) | [Ch 22](../part-4-capstone/chapter-22-bayanihan.md) | [Ch 23-24](../part-4-capstone/chapter-23-capstone-a.md) | [Ch 25](../part-4-capstone/chapter-25-final-boss.md) | [Ch 26](../part-4-capstone/chapter-26-whats-next.md)

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

## Chapter 11: APIs

### Mini-Project: GCash Transaction Tracker

```python
# gcash_tracker.py
# Sample solution for GCash Transaction Tracker

transactions = {
    "2024-01-15": [
        {"type": "sent", "amount": 200, "to": "Tita", "note": "pasaload"},
        {"type": "received", "amount": 500, "from": "Mom", "note": "allowance"},
    ]
}


def add_transaction(date, tx_type, amount, note="", to="", fr=""):
    """Add a new GCash transaction."""
    if date not in transactions:
        transactions[date] = []

    tx = {"type": tx_type, "amount": amount, "note": note}
    if tx_type == "sent":
        tx["to"] = to
    elif tx_type == "received":
        tx["from"] = fr

    transactions[date].append(tx)
    print(f"Added: {tx_type} ₱{amount:.2f} -- {note}")


def daily_balance(date):
    """Calculate net balance for a specific date."""
    if date not in transactions:
        return 0

    total = 0
    for tx in transactions[date]:
        if tx["type"] == "sent":
            total -= tx["amount"]
        else:
            total += tx["amount"]
    return total


def category_summary():
    """Show transaction summary by category (note field)."""
    categories = {}
    for date, tx_list in transactions.items():
        for tx in tx_list:
            cat = tx.get("note", "uncategorized")
            if cat not in categories:
                categories[cat] = {"sent": 0, "received": 0}
            if tx["type"] == "sent":
                categories[cat]["sent"] += tx["amount"]
            else:
                categories[cat]["received"] += tx["amount"]

    print("\n=== GCash Summary by Category ===")
    for cat, amounts in categories.items():
        net = amounts["received"] - amounts["sent"]
        print(f"  {cat}: Sent ₱{amounts['sent']:.2f} | Received ₱{amounts['received']:.2f} | Net: ₱{net:.2f}")


# Demo
add_transaction("2024-01-16", "sent", 150, "merienda", to="Barkada")
add_transaction("2024-01-16", "received", 300, "load top-up", fr="Tito")
print(f"\nDaily balance (2024-01-15): ₱{daily_balance('2024-01-15'):.2f}")
print(f"Daily balance (2024-01-16): ₱{daily_balance('2024-01-16'):.2f}")
category_summary()
```

### Mini-Project: Palengke Price Comparator

```python
# price_compare.py
# Sample solution: Compare prices across different markets

import random


def fetch_prices(source, item):
    """
    Simulate fetching prices from a source.
    In real code, replace with actual API call or web scraping.
    """
    # Simulated price ranges for demonstration
    price_ranges = {
        "palengke": (item * 0.8, item * 1.0),
        "supermarket": (item * 0.95, item * 1.15),
        "online": (item * 1.0, item * 1.3),
    }
    low, high = price_ranges[source]
    return round(random.uniform(low, high), 2)


def compare_prices(item, base_price):
    """Compare prices for an item across multiple markets."""
    sources = ["palengke", "supermarket", "online"]
    results = {}

    for source in sources:
        price = fetch_prices(source, base_price)
        savings = base_price - price
        results[source] = {"price": price, "savings": savings}

    # Find the best price
    best_source = min(results, key=lambda s: results[s]["price"])

    print(f"\n=== Price Comparison: {item} (Base: ₱{base_price:.2f}) ===")
    for source, data in results.items():
        flag = " <-- BEST" if source == best_source else ""
        savings_str = f"Save ₱{data['savings']:.2f}" if data["savings"] > 0 else f"Overpay ₱{abs(data['savings']):.2f}"
        print(f"  {source.capitalize()}: ₱{data['price']:.2f} ({savings_str}){flag}")

    return best_source, results


def alert_price(item, threshold, base_price):
    """Alert when a price drops below threshold."""
    best_source, results = compare_prices(item, base_price)
    best_price = results[best_source]["price"]

    if best_price < threshold:
        print(f"\n🔔 ALERT: {item} is below ₱{threshold:.2f} at {best_source.capitalize()}!")
    else:
        print(f"\nNo alert: best price ₱{best_price:.2f} is above ₱{threshold:.2f} threshold.")


# Demo
compare_prices("Gala bananas (1kg)", 80)
compare_prices("Laundry soap", 120)
alert_price("Instant noodles (pack of 5)", 50, 65)
```

## Chapter 12: Web Scraping

### Mini-Project: Facebook Marketplace Alert Bot

```python
# marketplace_alert.py
# Sample solution: Monitor Facebook Marketplace for specific items

import json
import os
import random
from datetime import datetime


LISTINGS_FILE = "seen_listings.json"
ALERT_THRESHOLD = 5000  # Only alert if price is below this


def load_seen_listings():
    """Load previously seen listings from file."""
    if os.path.exists(LISTINGS_FILE):
        with open(LISTINGS_FILE, "r") as f:
            return json.load(f)
    return {"listings": [], "alerts": []}


def save_listings(data):
    """Save listings data to file."""
    with open(LISTINGS_FILE, "w") as f:
        json.dump(data, f, indent=4)


def scrape_listings(search_term, max_results=10):
    """
    Simulate scraping listings.
    In real code, use requests + BeautifulSoup to parse Facebook Marketplace.
    """
    # Simulated scraped data
    sample_listings = [
        {"title": f"{search_term} - Like New", "price": random.randint(3000, 15000), "location": "Manila"},
        {"title": f"{search_term} - Used, Good Condition", "price": random.randint(2000, 8000), "location": "Quezon City"},
        {"title": f"{search_term} - Brand New Sealed", "price": random.randint(8000, 20000), "location": "Makati"},
    ]
    return sample_listings[:max_results]


def check_alerts(listings, seen_ids):
    """Check for new listings below threshold and send alerts."""
    alerts = []
    for listing in listings:
        # Use title + price as a simple unique identifier
        listing_id = f"{listing['title']}_{listing['price']}"
        if listing_id not in seen_ids and listing["price"] <= ALERT_THRESHOLD:
            alerts.append(listing)
            print(f"🔔 ALERT: '{listing['title']}' -- ₱{listing['price']} in {listing['location']}")
    return alerts


# Demo
data = load_seen_listings()
seen_ids = {l["id"] for l in data["listings"]}

print("=== Checking Facebook Marketplace ===")
listings = scrape_listings("iPhone 12")
alerts = check_alerts(listings, seen_ids)

# Save all listings
for i, listing in enumerate(listings):
    listing_id = f"{listing['title']}_{listing['price']}"
    listing["id"] = listing_id
    data["listings"].append(listing)

data["alerts"].extend([
    {"title": a["title"], "price": a["price"], "time": datetime.now().isoformat()}
    for a in alerts
])

save_listings(data)
print(f"\nTotal listings tracked: {len(data['listings'])}")
print(f"Alerts sent: {len(alerts)}")
```

### Mini-Project: Load Sharing Tracker

```python
# load_tracker.py
# Sample solution: Track shared load among barkada members

class LoadTracker:
    def __init__(self):
        self.members = {}  # name -> {"paid": amount, "used": amount}
        self.history = []  # list of transactions

    def add_member(self, name):
        """Add a barkada member."""
        if name not in self.members:
            self.members[name] = {"paid": 0, "used": 0}
            print(f"Added: {name}")

    def record_payment(self, name, amount):
        """Record who paid for shared load."""
        if name in self.members:
            self.members[name]["paid"] += amount
            self.history.append({"action": "pay", "member": name, "amount": amount})
            print(f"{name} paid ₱{amount:.2f} for load")

    def record_usage(self, name, amount):
        """Record how much load a member used."""
        if name in self.members:
            self.members[name]["used"] += amount
            self.history.append({"action": "use", "member": name, "amount": amount})

    def who_owes_whom(self):
        """Calculate who owes whom."""
        balances = {}
        for name, data in self.members.items():
            balances[name] = data["paid"] - data["used"]

        debtors = {n: b for n, b in balances.items() if b < 0}
        creditors = {n: b for n, b in balances.items() if b > 0}

        print("\n=== Load Balance ===")
        for name, balance in balances.items():
            status = f"OWES ₱{abs(balance):.2f}" if balance < 0 else f"CREDIT ₱{balance:.2f}"
            print(f"  {name}: {status}")

        return debtors, creditors

    def summary_report(self):
        """Generate a full summary report."""
        print("\n=== Load Sharing Summary ===")
        total_paid = sum(d["paid"] for d in self.members.values())
        total_used = sum(d["used"] for d in self.members.values())
        print(f"Total paid: ₱{total_paid:.2f}")
        print(f"Total used: ₱{total_used:.2f}")
        print(f"Discrepancy: ₱{total_paid - total_used:.2f}")
        self.who_owes_whom()


# Demo
tracker = LoadTracker()
tracker.add_member("Juan")
tracker.add_member("Maria")
tracker.add_member("Pedro")

tracker.record_payment("Juan", 200)
tracker.record_payment("Maria", 200)
tracker.record_payment("Pedro", 100)

tracker.record_usage("Juan", 150)
tracker.record_usage("Maria", 180)
tracker.record_usage("Pedro", 170)

tracker.summary_report()
```

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

**Approach:** Use `py-cord`'s `discord.Bot()` with slash commands. Key points:
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

## Chapter 16: Data Visualization

### Mini-Project: Typhoon Impact Visualizer

```python
# typhoon_viz.py
# Sample solution: Visualize typhoon data

import matplotlib.pyplot as plt
import pandas as pd


def load_typhoon_data():
    """
    Load typhoon track data.
    In real code, fetch from PAGASA API or NOAA HURDAT2.
    For this example, we use sample data.
    """
    data = {
        "typhoon": ["Amang", "Betty", "Chedeng", "Dindo", "Enteng"],
        "year": [2019, 2019, 2021, 2022, 2023],
        "max_wind_kph": [95, 130, 85, 110, 140],
        "affected_provinces": [5, 12, 3, 8, 15],
        "estimated_damage_m": [0.5, 2.3, 0.3, 1.2, 3.1],
    }
    return pd.DataFrame(data)


def plot_wind_speed(df):
    """Plot max wind speed per typhoon."""
    plt.figure(figsize=(10, 5))
    bars = plt.bar(df["typhoon"], df["max_wind_kph"], color=["#e74c3c", "#e67e22", "#f39c12", "#2ecc71", "#3498db"])

    plt.title("Max Wind Speed by Typhoon (km/h)")
    plt.xlabel("Typhoon Name")
    plt.ylabel("Wind Speed (km/h)")
    plt.axhline(y=120, color="red", linestyle="--", label="Typhoon (120+ kph)")
    plt.legend()

    # Add value labels on bars
    for bar, speed in zip(bars, df["max_wind_kph"]):
        plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 5,
                 f"{speed} kph", ha="center", fontsize=9)

    plt.tight_layout()
    plt.savefig("typhoon_wind_speed.png", dpi=150)
    plt.show()


def plot_provinces_affected(df):
    """Plot provinces affected per typhoon."""
    plt.figure(figsize=(10, 5))
    plt.bar(df["typhoon"], df["affected_provinces"], color="#9b59b6")
    plt.title("Provinces Affected by Typhoon")
    plt.xlabel("Typhoon Name")
    plt.ylabel("Number of Provinces")
    plt.tight_layout()
    plt.savefig("typhoon_provinces.png", dpi=150)
    plt.show()


# Demo
df = load_typhoon_data()
plot_wind_speed(df)
plot_provinces_affected(df)
print(f"Loaded {len(df)} typhoons")
print(df.to_string(index=False))
```

### Mini-Project: Personal Budget Dashboard

```python
# budget_dashboard.py
# Sample solution: Visualize spending habits

import matplotlib.pyplot as plt
import pandas as pd


def load_expense_data():
    """Load expense data from a dict (or CSV/JSON in real code)."""
    data = {
        "month": ["Jan", "Feb", "Mar", "Apr", "May"],
        "kain": [3000, 3200, 2800, 3500, 3100],
        "pamasahe": [800, 850, 800, 900, 850],
        "load": [500, 500, 600, 500, 500],
        "entertainment": [1000, 800, 1200, 900, 1100],
        "savings": [2000, 1500, 2500, 1800, 2200],
    }
    return pd.DataFrame(data)


def pie_chart_spending(df, month="Jan"):
    """Create a pie chart of spending by category for a specific month."""
    idx = df[df["month"] == month].index[0]
    categories = ["kain", "pamasahe", "load", "entertainment"]
    labels = ["Kain", "Pamasahe", "Load", "Entertainment"]
    values = [df.loc[idx, cat] for cat in categories]
    colors = ["#e74c3c", "#3498db", "#f39c12", "#9b59b6"]

    plt.figure(figsize=(8, 6))
    plt.pie(values, labels=labels, colors=colors, autopct="%1.1f%%")
    plt.title(f"Spending Breakdown - {month}")
    plt.tight_layout()
    plt.savefig(f"budget_pie_{month}.png", dpi=150)
    plt.show()


def bar_chart_monthly(df):
    """Create a bar chart of monthly totals."""
    df["total"] = df[["kain", "pamasahe", "load", "entertainment"]].sum(axis=1)
    df["savings"] = df["savings"]

    x = df["month"]
    plt.figure(figsize=(10, 5))
    plt.bar(x, df["total"], label="Spending", color="#e74c3c")
    plt.bar(x, df["savings"], label="Savings", color="#2ecc71", bottom=df["total"])
    plt.ylabel("Amount (₱)")
    plt.title("Monthly Spending vs Savings")
    plt.legend()
    plt.tight_layout()
    plt.savefig("budget_monthly.png", dpi=150)
    plt.show()


def line_chart_trends(df):
    """Create a line chart of spending trends over time."""
    categories = ["kain", "pamasahe", "load", "entertainment"]
    colors = ["#e74c3c", "#3498db", "#f39c12", "#9b59b6"]

    plt.figure(figsize=(10, 5))
    for cat, color in zip(categories, colors):
        plt.plot(df["month"], df[cat], marker="o", label=cat.capitalize(), color=color)

    plt.ylabel("Amount (₱)")
    plt.title("Spending Trends")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig("budget_trends.png", dpi=150)
    plt.show()


# Demo
df = load_expense_data()
pie_chart_spending(df, "Jan")
bar_chart_monthly(df)
line_chart_trends(df)
print(f"Monthly data loaded: {len(df)} months")
```

## Boss Fights: Part 3 (Chapters 17-20)

### Mini-Project: Tagalog Slang Dictionary

```python
# slang_dict.py
# Sample solution: Filipino internet slang dictionary

slang = {
    "lit": "maganda, exciting",
    "grabe": "wow, amazing",
    "charot": "joke lang",
    "pre": "friend, bro",
    "naimbis": "jealous",
    "kamote": "confused, out of touch",
    "tsismis": "gossip",
    "lambing": "affectionate behavior",
    "walaw": "feeling sorry for someone",
    "bes": "best friend, bro",
    "gen": "generated (by AI)",
    "sks": "seryos? (serious?)",
    "omg": "oh my god (used in Tagalog context too)",
    "crush": "crush (same as English)",
    "ghosting": "dating taong biglang hindi na sumasagot",
    "soft launch": "ipakita ang relationship nang dahan-dahan sa social media",
    "red flag": "tanda na may problema sa isang tao",
    "gaslighting": "manipulate someone into questioning their sanity",
    "sobrang": "extremely, very (used for emphasis)",
    "bingit": "excellent, awesome (originally Cebuano)",
    "ulil": "acting crazy, ridiculous",
    "tita/tito culture": "gossiping, judgmental behavior (usually from older women)",
    "chika": "gossip, casual chat",
    "padrino": "someone with connections who can help",
    "wingman": "tulong sa pag-approach ng crush",
}


def search_slang(query):
    """Search slang terms by keyword in definition."""
    results = []
    query_lower = query.lower()
    for term, definition in slang.items():
        if query_lower in definition.lower() or query_lower in term.lower():
            results.append((term, definition))
    return results


def show_definition(term):
    """Show definition for a specific slang term."""
    term_lower = term.lower()
    if term_lower in slang:
        print(f'"{term}" = {slang[term_lower]}')
    else:
        # Fuzzy match
        matches = [t for t in slang.keys() if term_lower in t]
        if matches:
            print(f'Did you mean: {", ".join(matches)}?')
        else:
            print(f'"{term}" not found in dictionary.')


def show_all():
    """Display all slang terms sorted alphabetically."""
    print("\n=== Tagalog/Internet Slang Dictionary ===")
    for term in sorted(slang.keys()):
        print(f"  {term}: {slang[term]}")


def suggest_similar(term):
    """Suggest similar terms based on shared keywords."""
    if term.lower() not in slang:
        return []

    target_def = slang[term.lower()]
    similar = []
    for other_term, other_def in slang.items():
        if other_term == term.lower():
            continue
        # Check for shared words in definitions
        target_words = set(target_def.lower().split())
        other_words = set(other_def.lower().split())
        shared = target_words & other_words
        if shared:
            similar.append((other_term, other_def, shared))

    similar.sort(key=lambda x: len(x[2]), reverse=True)
    return similar[:5]


# Demo
show_all()
print(f"\n--- Search: 'friend' ---")
for term, defn in search_slang("friend"):
    print(f"  {term}: {defn}")

print(f"\n--- Definition: 'pre' ---")
show_definition("pre")

print(f"\n--- Similar to 'ghosting' ---")
for term, defn, shared in suggest_similar("ghosting"):
    print(f"  {term}: {defn} (shared: {', '.join(shared)})")
```

### Mini-Project: Barkada Chat Analyzer

```python
# chat_analyzer.py
# Sample solution: Analyze barkada chat patterns

import re
from collections import Counter, defaultdict


class ChatAnalyzer:
    def __init__(self):
        self.messages = []
        self.member_counts = Counter()
        self.hourly_activity = Counter()
        self.tagalog_words = Counter()

    def add_message(self, member, message, hour=None):
        """Add a chat message for analysis."""
        self.messages.append({"member": member, "message": message, "hour": hour})
        self.member_counts[member] += 1

        # Track hourly activity
        if hour is not None:
            self.hourly_activity[hour] += 1

        # Count common Tagalog words
        msg_lower = message.lower()
        tagalog_keywords = ["kaya", "hindi", "sige", "nako", "grabe", "charot", "pre", "bes", "lodi", "diko"]
        for word in tagalog_keywords:
            if re.search(r'\b' + word + r'\b', msg_lower):
                self.tagalog_words[word] += 1

    def most_active_member(self):
        """Find the most chatty member."""
        return self.member_counts.most_common(1)[0] if self.member_counts else ("nobody", 0)

    def peak_hours(self, top_n=5):
        """Find the hours with most activity."""
        return self.hourly_activity.most_common(top_n)

    def word_frequency(self, top_n=10):
        """Show most frequent words in all messages."""
        all_words = []
        for msg in self.messages:
            words = re.findall(r'\b\w+\b', msg["message"].lower())
            all_words.extend(words)
        return Counter(all_words).most_common(top_n)

    def tagalog_ratio(self):
        """Estimate the ratio of Tagalog/Taglish messages."""
        tagalog_markers = ["ang", "ng", "sa", "ko", "mo", "kami", "silá", "diko", "hindi", "sige"]
        tagalog_count = 0
        for msg in self.messages:
            msg_lower = msg["message"].lower()
            if any(marker in msg_lower for marker in tagalog_markers):
                tagalog_count += 1
        total = len(self.messages)
        ratio = (tagalog_count / total * 100) if total > 0 else 0
        return ratio

    def summary(self):
        """Print a full analysis summary."""
        most_active = self.most_active_member()
        peak = self.peak_hours(3)
        ratio = self.tagalog_ratio()

        print("\n=== Barkada Chat Analysis ===")
        print(f"Total messages: {len(self.messages)}")
        print(f"Members: {len(self.member_counts)}")
        print(f"Most active: {most_active[0]} ({most_active[1]} messages)")
        print(f"\nPeak chat hours:")
        for hour, count in peak:
            print(f"  {hour:02d}:00 -- {count} messages")
        print(f"\nTagalog/Taglish ratio: {ratio:.0f}%")
        print(f"\nTop Tagalog words used:")
        for word, count in self.tagalog_words.most_common(5):
            print(f"  {word}: {count}")
        print(f"\nTop words overall:")
        for word, count in self.word_frequency(5):
            print(f"  {word}: {count}")


# Demo
analyzer = ChatAnalyzer()

# Simulated chat data
chat_data = [
    ("Juan", "Kumusta pre! Kaya mo 'yan!", 14),
    ("Maria", "Sige na! Charot 😂", 14),
    ("Pedro", "Grabe naman, nag-aral ba kayo?", 15),
    ("Juan", "Oo naman! Hindi kami nagpapabaya", 15),
    ("Maria", "Bes, may homework pa ako", 20),
    ("Pedro", "Charot! Diko rin gusto mag-study", 20),
    ("Juan", "Nako, exam bukas eh", 21),
    ("Maria", "Sige na, kaya natin 'to!", 21),
    ("Pedro", "Loddddd! Kaya natin! 💪", 21),
    ("Juan", "Kumusta na review ninyo?", 9),
]

for member, message, hour in chat_data:
    analyzer.add_message(member, message, hour)

analyzer.summary()
```

## Boss Fights: Part 3 (Chapters 17-20)

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

## Chapter 24: Capstone B — Barangay System (Part 2)

### Part 1: Certificate Generation

```python
# Certificate Generation
# Chapter 24 -- Part 2

from datetime import datetime, timedelta
import os


class CertificateGenerator:
    """Generates barangay certificates."""

    CERTIFICATE_TEMPLATES = {
        "clearance": """
╔══════════════════════════════════════════════╗
║           BARANGAY CERTIFICATE OF CLEARANCE  ║
║                                              ║
║   This certifies that                        ║
║   {name}                                     ║
║   {address}                                  ║
║   is a registered resident of this barangay  ║
║   with NO pending cases or obligations.      ║
║                                              ║
║   Issued on: {date}                          ║
║   Valid until: {expiry}                      ║
║                                              ║
║   {captain_name}                             ║
║   Barangay Captain                           ║
║   Barangay {barangay_name}                   ║
║   {municipality}, {province}                 ║
╚══════════════════════════════════════════════╝
        """,
        "indigency": """
╔══════════════════════════════════════════════╗
║        BARANGAY CERTIFICATE OF INDIGENCY     ║
║                                              ║
║   This certifies that                        ║
║   {name}                                     ║
║   {address}                                  ║
║   is a resident of this barangay and is      ║
║   financially indigent.                      ║
║                                              ║
║   This certificate is issued for the         ║
║   purpose of: {purpose}                      ║
║                                              ║
║   Issued on: {date}                          ║
║                                              ║
║   {captain_name}                             ║
║   Barangay Captain                           ║
║   Barangay {barangay_name}                   ║
║   {municipality}, {province}                 ║
╚══════════════════════════════════════════════╝
        """,
        "residency": """
╔══════════════════════════════════════════════╗
║     BARANGAY CERTIFICATE OF RESIDENCY        ║
║                                              ║
║   This certifies that                        ║
║   {name}                                     ║
║   has been a resident of this barangay       ║
║   since {residency_start}                    ║
║   at {address}                               ║
║                                              ║
║   This certificate is issued for the         ║
║   purpose of: {purpose}                      ║
║                                              ║
║   Issued on: {date}                          ║
║                                              ║
║   {captain_name}                             ║
║   Barangay Captain                           ║
║   Barangay {barangay_name}                   ║
║   {municipality}, {province}                 ║
╚══════════════════════════════════════════════╝
        """,
    }

    def __init__(self, barangay_name="Barangay San Isidro",
                 municipality="Municipality", province="Province",
                 captain_name="Hon. Juan Dela Cruz"):
        self.barangay_name = barangay_name
        self.municipality = municipality
        self.province = province
        self.captain_name = captain_name

    def generate(self, resident, cert_type, purpose=""):
        """Generate a certificate for a resident."""
        template = self.CERTIFICATE_TEMPLATES.get(cert_type)
        if not template:
            raise ValueError(
                f"Unknown certificate type: {cert_type}. "
                f"Choose from: {', '.join(self.CERTIFICATE_TEMPLATES.keys())}"
            )

        now = datetime.now()
        expiry = (now.replace(day=1) + timedelta(days=90)).strftime("%B %d, %Y")

        context = {
            "name": resident.full_name(),
            "address": resident.address,
            "date": now.strftime("%B %d, %Y"),
            "expiry": expiry,
            "purpose": purpose or "General Purpose",
            "barangay_name": self.barangay_name,
            "municipality": self.municipality,
            "province": self.province,
            "captain_name": self.captain_name,
            "residency_start": resident.registration_date.strftime("%B %d, %Y"),
        }

        certificate = template.format(**context)

        # Save to file
        filename = f"certificate_{resident.resident_id}_{cert_type}_{now.strftime('%Y%m%d')}.txt"
        with open(filename, "w") as f:
            f.write(certificate)

        print(f"Certificate generated: {filename}")
        print()
        print(certificate)

        return filename


# Usage
# cert_gen = CertificateGenerator()
# resident = manager.find_resident("juan")[0]
# cert_gen.generate(resident, "clearance")
# cert_gen.generate(resident, "indigency", "Court Requirement")
```

### Part 2: Advanced Reporting

```python
# Advanced Reporting
# Chapter 24 -- Part 2

from datetime import datetime
from collections import defaultdict


class ReportGenerator:
    """Generates advanced reports for barangay officials."""

    def __init__(self, fee_manager):
        self.fee_manager = fee_manager

    def monthly_summary(self, year=None, month=None):
        """Generate a monthly fee collection summary."""
        if not year:
            year = datetime.now().year
        if not month:
            month = datetime.now().month

        start = f"{year}-{month:02d}-01"
        if month == 12:
            end = f"{year + 1}-01-01"
        else:
            end = f"{year}-{month + 1:02d}-01"

        # Get all transactions for the month
        transactions = [
            t for t in self.fee_manager.transactions
            if start <= t["date"] < end
        ]

        total_collected = sum(t["amount"] for t in transactions)
        unique_payers = len(set(t["resident_id"] for t in transactions))
        total_residents = len(self.fee_manager.residents)

        # By fee type
        by_type = {}
        for t in transactions:
            fee = t["fee_type"]
            if fee not in by_type:
                by_type[fee] = {"count": 0, "total": 0}
            by_type[fee]["count"] += 1
            by_type[fee]["total"] += t["amount"]

        print(f"\n{'=' * 60}")
        print(f"  MONTHLY SUMMARY -- {datetime(year, month, 1).strftime('%B %Y')}")
        print(f"{'=' * 60}")
        print(f"  Residents: {total_residents}")
        print(f"  Paid this month: {unique_payers}")
        print(f"  Collection rate: {(unique_payers/total_residents*100):.1f}%")
        print(f"  Total collected: ₱{total_collected:.2f}")
        print(f"{'-' * 60}")
        print(f"  By Fee Type:")
        for fee_type, data in sorted(by_type.items()):
            bar = "█" * int(data['total'] / 100)
            print(f"    {fee_type:.<30} {bar} ₱{data['total']:>10.2f}")
        print(f"{'=' * 60}\n")

        return {
            "month": f"{year}-{month:02d}",
            "total_collected": total_collected,
            "unique_payers": unique_payers,
            "collection_rate": unique_payers / total_residents * 100,
            "by_type": by_type,
        }

    def resident_status_report(self, resident):
        """Generate a status report for a single resident."""
        print(f"\n{'=' * 60}")
        print(f"  RESIDENT STATUS REPORT")
        print(f"{'=' * 60}")
        print(f"  Name: {resident.full_name()}")
        print(f"  ID: {resident.resident_id}")
        print(f"  Address: {resident.address}")
        print(f"  Contact: {resident.contact}")
        print(f"  Age: {resident.age()}")
        print(f"  Senior: {'Yes' if resident.is_senior() else 'No'}")
        print(f"  Registered: {resident.registration_date}")
        print(f"{'-' * 60}")

        # Fee history
        if resident.fees:
            print(f"  Fee History:")
            for fee_date, fees in sorted(resident.fees.items()):
                print(f"    {fee_date}:")
                for fee_type, status in fees.items():
                    amount = FeeManager.FEE_AMOUNTS.get(fee_type, 500.00)
                    symbol = "✅" if status == PaymentStatus.PAID else "❌"
                    print(f"      {symbol} {fee_type}: ₱{amount:.2f} ({status.value})")
        else:
            print(f"  No fee records found.")

        # Certificates
        if resident.certificates:
            print(f"  Certificates issued:")
            for cert in resident.certificates:
                print(f"    - {cert['type']} ({cert['date']})")

        print(f"{'=' * 60}\n")

    def yearly_comparison(self, year=None):
        """Compare fee collection across months."""
        if not year:
            year = datetime.now().year

        print(f"\n{'=' * 60}")
        print(f"  YEARLY COMPARISON -- {year}")
        print(f"{'=' * 60}")

        monthly_data = []
        for month in range(1, 13):
            start = f"{year}-{month:02d}-01"
            if month == 12:
                end = f"{year + 1}-01-01"
            else:
                end = f"{year}-{month + 1:02d}-01"

            transactions = [
                t for t in self.fee_manager.transactions
                if start <= t["date"] < end
            ]
            total = sum(t["amount"] for t in transactions)
            monthly_data.append((month, total))

        # Display as bar chart (text-based)
        max_amount = max(t for _, t in monthly_data) if monthly_data else 1
        for month, total in monthly_data:
            bar_length = int((total / max_amount) * 40) if max_amount > 0 else 0
            bar = "█" * bar_length
            month_name = datetime(year, month, 1).strftime('%b')
            print(f"  {month_name:>3} | {bar:<40} ₱{total:>10.2f}")

        total_year = sum(t for _, t in monthly_data)
        print(f"{'─' * 60}")
        print(f"  {'TOTAL':>3} |{' ' * 40} ₱{total_year:>10.2f}")
        print(f"{'=' * 60}\n")

        return monthly_data
```

### Part 3: Custom Exceptions

```python
# Enhanced error handling with custom exceptions
# Chapter 24 -- Part 3

class BarangayError(Exception):
    """Base exception for barangay system errors."""
    pass


class ResidentNotFoundError(BarangayError):
    """Raised when a resident is not found."""
    def __init__(self, query):
        self.query = query
        super().__init__(f"Resident not found: '{query}'")


class InvalidFeeError(BarangayError):
    """Raised when a fee type is invalid."""
    def __init__(self, fee_type):
        self.fee_type = fee_type
        super().__init__(f"Invalid fee type: {fee_type}")


class CertificateError(BarangayError):
    """Raised when certificate generation fails."""
    pass


# Example with try/except
def safe_pay_fee(manager, resident_id, fee_type, amount=None):
    """Pay fee with proper error handling."""
    try:
        if resident_id not in manager.residents:
            raise ResidentNotFoundError(resident_id)

        if fee_type not in FeeManager.FEE_AMOUNTS:
            raise InvalidFeeError(fee_type)

        return manager.pay_fee(resident_id, fee_type, amount)

    except ResidentNotFoundError as e:
        print(f"Error: {e}")
        print("   Tip: Use 'Search resident' to find the correct ID.")
    except InvalidFeeError as e:
        print(f"Error: {e}")
        print(f"   Valid fee types: {', '.join(FeeManager.FEE_AMOUNTS.keys())}")
    except ValueError as e:
        print(f"Error: Invalid input: {e}")
    except Exception as e:
        print(f"Error: Unexpected error: {e}")
        print("   Please try again or contact the system admin.")
```

### Part 4: Flask Web Interface

```python
# Optional: Web Interface using Flask
# Chapter 24

# Install: pip install flask
# Run: python web_app.py
# Visit: http://localhost:5000

from flask import Flask, render_template_string, request, jsonify

app = Flask(__name__)

# Initialize the fee manager
manager = FeeManager()

HTML_PAGE = """
<!DOCTYPE html>
<html>
<head>
    <title>Barangay Management System</title>
    <style>
        body { font-family: Arial, sans-serif; max-width: 800px; margin: 0 auto; padding: 20px; }
        h1 { color: #2c3e50; }
        .form-group { margin: 15px 0; }
        label { display: block; margin-bottom: 5px; font-weight: bold; }
        input, select { width: 100%; padding: 8px; border: 1px solid #ddd; border-radius: 4px; }
        button { background: #3498db; color: white; padding: 10px 20px; border: none; border-radius: 4px; cursor: pointer; }
        button:hover { background: #2980b9; }
        .result { background: #f0f0f0; padding: 15px; margin: 15px 0; border-radius: 4px; }
        .success { color: #27ae60; }
        .error { color: #e74c3c; }
        table { width: 100%; border-collapse: collapse; margin: 15px 0; }
        th, td { padding: 8px; text-align: left; border-bottom: 1px solid #ddd; }
        th { background: #3498db; color: white; }
    </style>
</head>
<body>
    <h1>Barangay Management System</h1>

    <h2>Search Resident</h2>
    <div class="form-group">
        <input type="text" id="search" placeholder="Enter name, ID, or address...">
        <button onclick="searchResident()">Search</button>
    </div>
    <div id="results"></div>

    <h2>Register New Resident</h2>
    <div class="form-group">
        <input type="text" id="first_name" placeholder="First Name">
    </div>
    <div class="form-group">
        <input type="text" id="last_name" placeholder="Last Name">
    </div>
    <div class="form-group">
        <input type="text" id="address" placeholder="Address">
    </div>
    <div class="form-group">
        <input type="text" id="contact" placeholder="Contact Number">
    </div>
    <button onclick="registerResident()">Register</button>

    <script>
        async function searchResident() {
            const query = document.getElementById('search').value;
            const response = await fetch(`/api/residents?q=${encodeURIComponent(query)}`);
            const residents = await response.json();
            const results = document.getElementById('results');

            if (residents.length === 0) {
                results.innerHTML = '<div class="result error">No residents found.</div>';
                return;
            }

            let html = '<table><tr><th>ID</th><th>Name</th><th>Address</th><th>Contact</th></tr>';
            for (const r of residents) {
                html += `<tr><td>${r.resident_id}</td><td>${r.first_name} ${r.last_name}</td>
                         <td>${r.address}</td><td>${r.contact}</td></tr>`;
            }
            html += '</table>';
            results.innerHTML = html;
        }

        async function registerResident() {
            const data = {
                first_name: document.getElementById('first_name').value,
                last_name: document.getElementById('last_name').value,
                address: document.getElementById('address').value,
                contact: document.getElementById('contact').value,
            };
            const response = await fetch('/api/residents', {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify(data)
            });
            const result = await response.json();
            alert(result.message);
        }
    </script>
</body>
</html>
"""


@app.route("/")
def index():
    return render_template_string(HTML_PAGE)


@app.route("/api/residents")
def api_search():
    query = request.args.get("q", "")
    results = manager.find_resident(query)
    return jsonify([r.to_dict() for r in results])


@app.route("/api/residents", methods=["POST"])
def api_register():
    data = request.get_json()
    if not data:
        return jsonify({"error": "Invalid JSON"}), 400

    first_name = data.get("first_name", "").strip()
    last_name = data.get("last_name", "").strip()
    if not first_name or not last_name:
        return jsonify({"error": "first_name and last_name are required"}), 400

    resident = Resident(
        first_name=first_name,
        last_name=last_name,
        address=data.get("address", ""),
        contact=data.get("contact", ""),
    )
    manager.add_resident(resident)
    return jsonify({"message": "Resident registered!", "id": resident.resident_id}), 201


if __name__ == "__main__":
    app.run(debug=True, port=5000)
```

### Final Boss: Your Own Project (Chapter 25)

**Approach:** This is self-directed. Use the starter framework as a template. Key points:
- Pick a real problem you care about
- Start with the minimum working version
- Add features incrementally
- Use `json.dump(data, f, default=str)` for saving with date objects
- Don't get stuck -- bahala na!

---

*See the [troubleshooting appendix](troubleshooting.md) for common errors and their solutions.*

---

*Previous: [Chapter 26: What's Next](../part-4-capstone/chapter-26-whats-next.md) -- End of the book*

---

## Chapter 26: What's Next — Your Journey Continues

### Sample Reflection Responses

Here are sample responses to the reflection prompts in Chapter 26. Remember, your answers will be different -- and that's the point.

**What did you learn?**

> "From `print()` to building full applications with Flask, NLP, and APIs. The journey taught me that coding is about problem-solving, not memorization. I learned to break big problems into small pieces, and that asking for help is a strength, not weakness."

**How can you apply this?**

> "Join DEP Barkada, teach my siblings Python basics, build a tool for my sari-sari store using what I learned in Ch 23-24. I can automate my family's budget tracking and create reports for our barangay."

**What's next?**

> "Web development with Django. I want to build a barangay portal where residents can request certificates online. Or maybe data visualization -- I want to show typhoon patterns in the Visayas."

### 30-Day Challenge Template

Here's a sample project plan for the 30-Day Challenge:

```python
# Sample 30-Day Project Plan
# Project: Personal Finance Tracker

# Week 1: CLI version with categories and basic reporting
#   - Classes: Transaction, BudgetTracker
#   - File I/O: JSON persistence
#   - Features: Add income/expense, view summary

# Week 2: Add data persistence (SQLite) and charts
#   - Database: sqlite3 module
#   - Visualization: matplotlib bar charts
#   - Features: Monthly trends, category breakdown

# Week 3: Build Flask web interface
#   - Flask routes for CRUD operations
#   - HTML templates with Filipino context
#   - Features: Web dashboard, search/filter

# Week 4: Deploy to Render/Heroku, write README, share on GitHub
#   - Git workflow: commits, branches, PRs
#   - README with screenshots and setup instructions
#   - Share in PythonPH and DEP Barkada

# Success criteria:
# - Can track income/expenses
# - Shows monthly spending by category
# - Accessible via browser
# - Deployed and shareable
```

### Portfolio Project Examples

Here are projects from earlier chapters that make strong portfolio pieces:

| Project | Chapter | What It Shows |
|---------|---------|---------------|
| Sari-Sari Store Inventory System | Ch 8 | OOP, JSON, file I/O, CLI design |
| GCash Transaction Tracker | Ch 11 | Data modeling, aggregation, APIs |
| Typing Game Suite | Ch 10 | Classes, file persistence, algorithms |
| Facebook Marketplace Alert Bot | Ch 12 | Web scraping simulation, alerts |
| Personal Finance Dashboard | Ch 14 | Multi-concept integration, reporting |
| Barkada Chat Analyzer | Ch 16 | Data analysis, NLP basics |
| Tagalog Slang Dictionary | Ch 17 | Pattern matching, fuzzy search |
| Advanced Barkada Chatbot | Ch 17 | NLP, conversation memory, learning |
| Barangay Dashboard | Ch 20 | Async, data viz, NLP, data pipelines |
| Barangay Management System | Ch 23-24 | Full OOP system, certificates, reports |
| Flask Web Interface | Ch 24 | Web development, REST APIs, templates |

The full solution is embedded in [Chapter 8](../part-1-fundamentals/chapter-08-boss-fight-1.md). Below is a concise reference version showing the key methods that were implemented in the Boss Fight.

```python
# Complete Sari-Sari Store Inventory System
# Boss Fight 1 — Chapter 8

inventory = {
    "laundry soap": {"qty": 10, "price": 15.00},
    "cigarettes": {"qty": 50, "price": 5.00},
    "candy": {"qty": 25, "price": 3.00},
    "instant noodles": {"qty": 30, "price": 8.00},
    "softdrinks": {"qty": 20, "price": 15.00},
}


def display_inventory():
    """Show all items and their quantities."""
    print("\n=== Sari-Sari Store Inventory ===")
    for item, data in inventory.items():
        print(f"  {item}: {data['qty']} @ ₱{data['price']:.2f}")


def sell_item(name, qty):
    """Sell items and check low stock."""
    name = name.lower().strip()
    if name in inventory:
        if inventory[name]["qty"] >= qty:
            inventory[name]["qty"] -= qty
            print(f"Sold {qty}x {name}")
            # Check if stock is low (below 5)
            if inventory[name]["qty"] < 5:
                print(f"⚠️ Low stock: {name} ({inventory[name]['qty']} left)")
        else:
            print(f"Not enough stock! Only {inventory[name]['qty']} left.")
    else:
        print(f"'{name}' not found in inventory.")


def total_value():
    """Calculate total inventory value."""
    total = sum(data["qty"] * data["price"] for data in inventory.values())
    print(f"\nTotal inventory value: ₱{total:.2f}")


# Demo
display_inventory()
sell_item("candy", 3)
sell_item("laundry soap", 12)
total_value()
```

**Key concepts demonstrated:**
- Dictionaries as data structures for key-value pairs
- String methods (`.lower()`, `.strip()`) for input normalization
- Conditional logic for stock checking
- Low-stock alerts using nested `if` statements
- Generator expressions in `sum()` for concise calculations

---

## Chapter 10: Strings and the Tagalog Typing Game

### Boss Fight: Full Typing Game Suite

The Boss Fight asks you to extend the Typing Game with: multiple rounds, leaderboard with file persistence, custom word input, WPM calculation, and adaptive difficulty. Below is a complete implementation that addresses all five requirements.

```python
# Full Typing Game Suite
# Chapter 10 — Boss Fight Solution

import time
import random
import json
import os

# Word lists by difficulty
WORD_BANKS = {
    "easy": [
        "kumusta", "mabuti", "salamat", "oo", "hindi",
        "po", "tayo", "kami", "bahay", "kain", "tubig",
        "gatas", "tinapay", "silya", "mesa", "bintana",
    ],
    "medium": [
        "magandang", "gabi", "umaga", "hapon", "merienda",
        "pamasahe", "photocopy", "biskwit", "sigarilye",
        "barangay", "pamilya", "kaibigan", "barkada",
        "pagkain", "tubig-minsan", "silahis", "damdamin",
    ],
    "hard": [
        "pagpapahalaga", "pananampalataya", "pagpapakumbaba",
        "pakikisama", "pagkakaisa", "katarungan", "kalayaan",
        "karapatan", "pinagmulan", "pamamaraan", "pananaw",
        "pangarap", "tagumpay", "pag-asa", "lakas-loob",
    ],
}

LEADERBOARD_FILE = "typing_leaderboard.json"


class TypingGame:
    def __init__(self, difficulty="medium", word_count=10):
        self.difficulty = difficulty
        self.word_count = word_count
        self.words = []
        self.results = []
        self.leaderboard = self._load_leaderboard()

    def _load_leaderboard(self):
        """Load leaderboard from file, or start empty."""
        if os.path.exists(LEADERBOARD_FILE):
            with open(LEADERBOARD_FILE, "r") as f:
                return json.load(f)
        return {"best_wpm": [], "best_accuracy": []}

    def _save_leaderboard(self):
        """Save leaderboard to file."""
        with open(LEADERBOARD_FILE, "w") as f:
            json.dump(self.leaderboard, f, indent=4)

    def get_words(self):
        """Select random words, adapting difficulty based on past performance."""
        # Adaptive difficulty: if accuracy < 60%, drop difficulty
        if self.results and len(self.results) >= 5:
            accuracy = sum(1 for r in self.results if r["correct"]) / len(self.results) * 100
            if accuracy < 60 and self.difficulty != "easy":
                print("⚠️ Dropping to easier words. Ganap mo 'yan!")
                self.difficulty = "easy"
            elif accuracy > 90 and self.difficulty != "hard":
                print("🔥 Words getting harder! Heto na!")
                self.difficulty = "hard"
        self.words = random.sample(WORD_BANKS[self.difficulty], self.word_count)

    def play(self):
        """Run a single typing round."""
        self.get_words()
        print(f"\n=== Tagalog Typing Game ({self.difficulty.upper()}) ===")
        print(f"Type {self.word_count} words. Ganap mo 'yan!\n")

        times = []
        for i, word in enumerate(self.words, 1):
            print(f"\n{i}. {word}")
            print("   ", end="")

            start_time = time.time()
            typed = input()
            end_time = time.time()

            elapsed = end_time - start_time
            times.append(elapsed)

            correct = typed.strip().lower() == word.lower()
            self.results.append({
                "word": word,
                "typed": typed.strip(),
                "correct": correct,
                "time": elapsed,
            })

            status = "✅" if correct else "❌"
            print(f"   {status} {elapsed:.1f}s")

        return self._calculate_stats()

    def _calculate_stats(self):
        """Calculate typing statistics."""
        total_words = len(self.results)
        correct = sum(1 for r in self.results if r["correct"])
        accuracy = (correct / total_words) * 100 if total_words else 0
        avg_time = sum(r["time"] for r in self.results) / total_words if total_words else 0
        total_time = sum(r["time"] for r in self.results)
        wpm = (correct / total_time * 60) if total_time > 0 else 0

        # Save to leaderboard if it's a good score
        if wpm > 0 and accuracy >= 70:
            entry = {"wpm": round(wpm, 1), "accuracy": round(accuracy, 1),
                     "difficulty": self.difficulty, "words": total_words}
            self.leaderboard["best_wpm"].append(entry)
            self.leaderboard["best_wpm"].sort(key=lambda x: x["wpm"], reverse=True)
            self.leaderboard["best_wpm"] = self.leaderboard["best_wpm"][:10]  # Top 10
            self._save_leaderboard()

        print(f"\n=== Results ===")
        print(f"Accuracy: {accuracy:.0f}% ({correct}/{total_words})")
        print(f"Words/min: {wpm:.0f}")
        print(f"Average time: {avg_time:.1f}s per word")
        print(f"Total time: {total_time:.1f}s")

        if accuracy >= 90:
            print("🏅 Galing! Super fast!")
        elif accuracy >= 70:
            print("💪 Good job! Konti pa lang!")
        else:
            print("💪 Subok ulit! Practice makes perfect!")

        return {"accuracy": accuracy, "wpm": wpm, "avg_time": avg_time, "total_time": total_time}

    def show_custom_words(self):
        """Allow user to type custom words."""
        print("\n=== Custom Words Mode ===")
        print("Type words separated by commas (or press Enter to skip):")
        custom_input = input("  Your words: ").strip()
        if custom_input:
            self.words = [w.strip() for w in custom_input.split(",") if w.strip()]
            self.word_count = len(self.words)
            if self.word_count == 0:
                print("No words entered. Using default words.")
                self.get_words()

    def show_leaderboard(self):
        """Display the leaderboard."""
        print("\n=== 🏆 Leaderboard ===")
        if not self.leaderboard["best_wpm"]:
            print("No scores yet. Play a round first!")
            return
        print(f"{'Rank':<6} {'WPM':<8} {'Accuracy':<10} {'Difficulty':<10} {'Words':<6}")
        print("-" * 42)
        for i, entry in enumerate(self.leaderboard["best_wpm"][:5], 1):
            print(f"{i:<6} {entry['wpm']:<8} {entry['accuracy']:<10} {entry['difficulty']:<10} {entry['words']:<6}")


def main():
    game = TypingGame()
    print("=== Tagalog Typing Game Suite ===\n")

    while True:
        print("\nOptions: [P]lay [C]ustom words [L]eaderboard [Q]uit")
        choice = input("Choose: ").strip().lower()

        if choice == "p":
            difficulty = input("Difficulty (easy/medium/hard, default: medium): ").strip() or "medium"
            count = int(input("Number of words (default: 10): ") or "10")
            game.difficulty = difficulty
            game.word_count = count
            game.results = []
            game.play()
        elif choice == "c":
            game.results = []
            game.show_custom_words()
            game.play()
        elif choice == "l":
            game.show_leaderboard()
        elif choice == "q":
            print("Salamat for playing! Palagi kang pwede mag-improve.")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
```

**Key concepts demonstrated:**
- `json.load()` / `json.dump()` for file persistence (leaderboard)
- `os.path.exists()` to check if a file exists before reading
- String methods: `.strip()`, `.lower()`, `.split(",")` for input parsing
- List comprehensions for data transformation
- Sorting lists of dictionaries (leaderboard ranking)
- Adaptive difficulty based on performance metrics

---

## Chapter 17: NLP and the AI Barkada Chatbot

### Boss Fight: Advanced Barkada Bot

The Boss Fight asks you to extend the chatbot with conversation memory, learning mode, multi-language support, personality system, and Discord integration. Below is a complete implementation covering the first four requirements.

```python
# Advanced Barkada Chatbot
# Chapter 17 — Boss Fight Solution

import random
import re
from datetime import datetime


class AdvancedBarkadaChatbot:
    """Chatbot with memory, learning, personality, and multi-language support."""

    def __init__(self):
        self.responses = self._build_responses()
        self.conversation_history = []  # Conversation memory
        self.learned_patterns = {}       # Learning mode
        self.mood = "neutral"            # Personality system
        self.mood_history = []           # Track mood changes

    def _build_responses(self):
        """Build pattern-response pairs for Tagalog, English, and Taglish."""
        return {
            r"\b(kumusta|hello|hi|hey|morning|good\s+evening)\b": [
                "Kumusta ka! 😊", "Hey! Anong balita?",
                "Hi there! Ready ka na ba mag-code?", "Kumusta! Good day!",
            ],
            r"\b(paano\s+ka?|how\s+are\s+you|fine\s+ka?|anong\s+balita)\b": [
                "Good naman! Ready to help you code!",
                "Okay lang! Ikaw, kamusta?",
                "Live lang! Bahala na kung ano mangyari.",
            ],
            r"\b(tulong|help|paano|how\s+to|ano\s+ang)\b": [
                "Sige! I-explain ko sa'yo. Ano ang specific question mo?",
                "Diskarte! Let's figure this out together.",
                "Bahala na! Try mo first, then I'll help.",
            ],
            r"\b(code|python|programming|bug|error|function|variable)\b": [
                "Python is the best language for beginners! Kaya mo 'yan.",
                "Bug? Don't worry, debugging is just learning in disguise.",
                "Variable? Parang lalagyan. I-label mo lang.",
            ],
            r"\b(hirap|difficult|hard|can't\s+do|baka\s+ hindi|give\s+up)\b": [
                "Kaya mo 'yan! Every expert was once a beginner.",
                "Hirap is normal. If you're not struggling, you're not learning.",
                "Bahala na! Try it, see what breaks, fix it.",
            ],
            r"\b(jollibee|chickenjoy|kain|eat|merienda)\b": [
                "🐝 Jollibee knows what works. So does this code.",
                "Kain muna tayo! Brain needs fuel.",
                "Chickenjoy is the most reliable function I know. Never fails.",
            ],
            r"\b(bye|goodbye|see\s+you|slà|palà|dà)\b": [
                "Bye! Kaya mo 'yan! 💪",
                "See you! Palagi kang pwede mag-improve.",
                "Padala! Bahala na! 🚀",
            ],
        }

    def understand(self, text):
        """Analyze text with multi-language support."""
        text_lower = text.lower().strip()

        # Check learned patterns first (user corrections)
        for pattern, response in self.learned_patterns.items():
            if re.search(pattern, text_lower):
                return {"type": "learned", "response": response, "confidence": 1.0}

        # Check built-in patterns
        for pattern, responses in self.responses.items():
            if re.search(pattern, text_lower):
                return {
                    "type": "pattern_match",
                    "response": random.choice(responses),
                    "confidence": 0.8,
                }

        # No pattern matched — use memory for context
        return {
            "type": "unknown",
            "response": self._unknown_response(text_lower),
            "confidence": 0.3,
        }

    def _unknown_response(self, text):
        """Handle unknown input with context from conversation."""
        # If we have recent history, reference it
        if self.conversation_history:
            last_topic = self.conversation_history[-1]["input"]
            fallbacks = [
                f"Hindi ko gets 'yung '{text}', pero last time we talked about '{last_topic[:30]}'. Want to continue?",
                "Hmm, hindi ko fully na-understand. Baka maswerte tayo sa next topic?",
            ]
            return random.choice(fallbacks)

        fallbacks = [
            f"Hindi ko gets 'yung '{text}'. Pwede mo ba i-explain?",
            "Hmm, hindi ko fully na-understand. Maaari mo bang i-word ito differently?",
            "Diskarte! Let me try to understand... Can you rephrase that?",
        ]
        return random.choice(fallbacks)

    def chat(self, user_message):
        """Process a message, update memory, and return response."""
        understanding = self.understand(user_message)

        # Save to conversation history (keep last 10 messages for memory)
        self.conversation_history.append({
            "input": user_message,
            "response": understanding["response"],
            "timestamp": datetime.now().isoformat(),
        })
        if len(self.conversation_history) > 10:
            self.conversation_history.pop(0)

        # Update mood based on sentiment
        sentiment = self.analyze_sentiment(user_message)
        self._update_mood(sentiment)

        response = understanding["response"]
        if understanding["confidence"] < 0.5:
            response += " (🤔 low confidence)"

        return response

    def learn(self, pattern, response):
        """Learning mode: add new pattern-response pairs from user corrections."""
        # Convert user-friendly pattern to regex
        regex_pattern = pattern.replace("*", ".*").replace("?", ".")
        self.learned_patterns[regex_pattern] = response
        print(f"✅ Learned: '{pattern}' → '{response}'")
        print(f"   (Now matching {len(self.learned_patterns)} custom patterns)")

    def _update_mood(self, sentiment):
        """Update chatbot personality based on sentiment."""
        mood_map = {
            "positive": ["😊", "💪", "🎉", "✨"],
            "negative": ["😔", "🤔", "💭", "😤"],
            "neutral": ["😐", "👍", "🤓", "🙂"],
        }
        self.mood = sentiment
        self.mood_history.append(sentiment)

    def analyze_sentiment(self, text):
        """Simple sentiment analysis for Tagalog/English."""
        text_lower = text.lower()
        positive_words = ["maganda", "galing", "ganda", "awesome", "love", "great",
                          "salamat", "nice", "good", "happy", "excited", "gumagana"]
        negative_words = ["hirap", "sira", "error", "bad", "hate", "angry",
                          "frustrated", "nagugulu", "confused"]

        pos_count = sum(1 for word in positive_words if word in text_lower)
        neg_count = sum(1 for word in negative_words if word in text_lower)

        if pos_count > neg_count:
            return "positive"
        elif neg_count > pos_count:
            return "negative"
        return "neutral"

    def show_memory(self):
        """Show conversation history for debugging."""
        print(f"\n=== Conversation History ({len(self.conversation_history)} messages) ===")
        for i, msg in enumerate(self.conversation_history[-5:], 1):
            print(f"  {i}. You: {msg['input'][:50]}")
            print(f"     Bot: {msg['response'][:50]}")

    def show_personality(self):
        """Show current mood and personality state."""
        emojis = {"positive": "😊", "negative": "😔", "neutral": "😐"}
        emoji = emojis.get(self.mood, "😐")
        print(f"\n=== Personality ===")
        print(f"  Mood: {emoji} {self.mood}")
        print(f"  Learned patterns: {len(self.learned_patterns)}")
        print(f"  Total conversations: {len(self.conversation_history)}")


# Interactive chat
def main():
    bot = AdvancedBarkadaChatbot()
    print("=== Advanced AI Barkada Chatbot ===")
    print("Type 'quit' to exit, 'learn' to add patterns, 'memory' to see history\n")

    while True:
        message = input("You: ").strip()
        if message.lower() in ("quit", "exit", "bye"):
            print("Bot: Bye! Kaya mo 'yan! 💪")
            break

        if message.lower() == "learn":
            pattern = input("  Enter pattern (use * for wildcards): ").strip()
            response = input("  Enter response: ").strip()
            bot.learn(pattern, response)
            continue

        if message.lower() == "memory":
            bot.show_memory()
            continue

        if message.lower() == "personality":
            bot.show_personality()
            continue

        response = bot.chat(message)
        print(f"Bot: {response}")

        sentiment = bot.analyze_sentiment(message)
        print(f"   Sentiment: {sentiment} | Mood: {bot.mood}")


if __name__ == "__main__":
    main()
```

**Key concepts demonstrated:**
- `re.search()` with regex patterns for flexible matching
- Conversation history stored as a list of dictionaries
- Learning mode: user teaches the bot new patterns
- Mood/personality system driven by sentiment analysis
- String methods: `.lower()`, `.strip()`, slicing for context display

---

## Chapter 18: Coding with AI as a Partner

### Boss Fight: Build Without AI

The Boss Fight asks you to create a simple Python script that takes user input, processes it, displays meaningful output, and handles errors — **without using AI to write the code**. Below is one possible solution demonstrating a practical, Filipino-context example: a GCash-style transaction tracker.

```python
# GCash-Style Transaction Tracker
# Chapter 18 — Boss Fight Solution
# (Written without AI — just like the Boss Fight requires!)

from datetime import datetime


class TransactionTracker:
    """Track income and expenses with validation and error handling."""

    def __init__(self, name="My Budget"):
        self.name = name
        self.balance = 0.0
        self.transactions = []

    def add_income(self, amount, source, note=""):
        """Add income with validation."""
        if not isinstance(amount, (int, float)) or amount <= 0:
            print(f"❌ Invalid amount: {amount}. Must be a positive number.")
            return False

        txn = {
            "type": "income",
            "amount": amount,
            "source": source,
            "note": note,
            "date": datetime.now().isoformat(),
        }
        self.transactions.append(txn)
        self.balance += amount
        print(f"✅ +₱{amount:.2f} from {source} (Balance: ₱{self.balance:.2f})")
        return True

    def add_expense(self, amount, category, note=""):
        """Add expense with balance check."""
        if not isinstance(amount, (int, float)) or amount <= 0:
            print(f"❌ Invalid amount: {amount}. Must be a positive number.")
            return False

        if amount > self.balance:
            print(f"❌ Insufficient funds! Balance: ₱{self.balance:.2f}")
            return False

        txn = {
            "type": "expense",
            "amount": amount,
            "category": category,
            "note": note,
            "date": datetime.now().isoformat(),
        }
        self.transactions.append(txn)
        self.balance -= amount
        print(f"❌ -₱{amount:.2f} for {category} (Balance: ₱{self.balance:.2f})")
        return True

    def summary(self):
        """Print a full transaction summary."""
        total_income = sum(t["amount"] for t in self.transactions if t["type"] == "income")
        total_expense = sum(t["amount"] for t in self.transactions if t["type"] == "expense")

        print(f"\n=== {self.name} Summary ===")
        print(f"Total Income:  ₱{total_income:.2f}")
        print(f"Total Expenses: ₱{total_expense:.2f}")
        print(f"Balance:       ₱{self.balance:.2f}")

        # Category breakdown
        categories = {}
        for t in self.transactions:
            if t["type"] == "expense":
                cat = t["category"]
                categories[cat] = categories.get(cat, 0) + t["amount"]

        if categories:
            print(f"\nSpending by Category:")
            for cat, total in sorted(categories.items()):
                pct = (total / total_expense * 100) if total_expense else 0
                print(f"  {cat:<15} ₱{total:>8.2f} ({pct:.0f}%)")

    def history(self):
        """Show full transaction history."""
        print(f"\n=== Transaction History ({len(self.transactions)} entries) ===")
        for i, txn in enumerate(self.transactions, 1):
            arrow = "+" if txn["type"] == "income" else "-"
            detail = txn.get("source", txn.get("category", "unknown"))
            print(f"  {i}. {arrow}₱{txn['amount']:.2f} | {detail}")


def main():
    tracker = TransactionTracker("My Budget")

    print("=== GCash-Style Transaction Tracker ===\n")
    print("Commands: income, expense, summary, history, quit\n")

    while True:
        cmd = input("Command: ").strip().lower()

        if cmd == "income":
            try:
                amount = float(input("  Amount: "))
                source = input("  Source (e.g. allowance, salary): ").strip()
                note = input("  Note (optional): ").strip()
                tracker.add_income(amount, source, note)
            except ValueError:
                print("❌ Please enter a valid number.")

        elif cmd == "expense":
            try:
                amount = float(input("  Amount: "))
                category = input("  Category (pamasahe, kain, load): ").strip()
                note = input("  Note (optional): ").strip()
                tracker.add_expense(amount, category, note)
            except ValueError:
                print("❌ Please enter a valid number.")

        elif cmd == "summary":
            tracker.summary()

        elif cmd == "history":
            tracker.history()

        elif cmd in ("quit", "exit", "q"):
            tracker.summary()
            print("\nSalamat for tracking! Panatag ang budget mo! 💪")
            break

        else:
            print("Unknown command. Try: income, expense, summary, history, quit")


if __name__ == "__main__":
    main()
```

**Why this solution works:**
- **User input**: Takes commands and numeric/text values via `input()`
- **Processing**: Validates amounts, checks balance, categorizes expenses
- **Meaningful output**: Shows running balance, category breakdown with percentages
- **Error handling**: Catches `ValueError` for non-numeric input, prevents negative balance
- **No AI dependency**: Uses only basic Python constructs — types, conditionals, loops, dictionaries

**After finishing:** Try asking AI to review this code. You'll likely get suggestions like: add a `save/load` feature, add a `search` function, or refactor the summary formatting. Only implement suggestions you understand!
*Next: [Troubleshooting](troubleshooting.md) -- Common issues and fixes*
