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

    return best_source


def alert_price(item, threshold, base_price):
    """Alert when a price drops below threshold."""
    best_source = compare_prices(item, base_price)
    best_price = next(d for s, d in {
        s: {"price": fetch_prices(s, base_price), "savings": base_price - fetch_prices(s, base_price)}
        for s in ["palengke", "supermarket", "online"]
    }.items() if s == best_source)["price"]

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
    ("Juan", "Kumusta na review ninyo?", 09),
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

### Final Boss: Your Own Project (Chapter 25)

**Approach:** This is self-directed. Use the starter framework as a template. Key points:
- Pick a real problem you care about
- Start with the minimum working version
- Add features incrementally
- Use `json.dump(data, f, default=str)` for saving with date objects
- Don't get stuck -- bahala na!

---

*See the [troubleshooting appendix](troubleshooting.md) for common errors and their solutions.*
