# Chapter 8: Boss Fight 1 -- The Complete Sari-Sari Store System

??? example "📋 Chapter Info"
    | | |
    |---|---|
    | **Difficulty** | ⭐⭐⭐ Boss Fight |
    | **Time** | 60 min |
    | **XP** | +500 XP |

??? warning "⚔️ Tier 1 — Fundamentals Boss"
    **Tier:** Elite Boss | **Concepts Combined:** 5 (Variables, Lists/Dicts, Conditionals, Loops, Functions, File I/O)
    **XP Reward:** 500 XP | **Badge:** "Sari-Sari Store Owner"

> **Story Hook:** It's been a few weeks since you started learning Python. Your Lola's notebook is getting full, and she keeps miscounting. You've learned variables, conditionals, loops, functions, and file handling. Now it's time to put it all together. "Lola," you say, "hayaan mo na 'to. Gagawan kita ng computer system." She looks at you skeptically. "Ah, oo nga? Kaya mo ba 'yan?" "Bahala na," you say. And you get to work.

---

## What You'll Do

This Boss Fight combines **everything** you've learned in Chapters 3-7:

- Variables and data types
- Lists and dictionaries
- Conditionals (if/elif/else)
- Loops (for and while)
- Functions with parameters and return values
- File I/O (saving and loading data)

Build a **complete sari-sari store management system** that can:

1. Add items to inventory
2. Sell items and track revenue
3. Check stock levels with low-stock warnings
4. Generate sales reports
5. Save and load data between sessions

## The Challenge

Build a system with these features:

### Feature 1: Inventory Management

- Add new items with name, quantity, and price
- Update quantities (restocking)
- Remove sold-out items
- Display full inventory

### Feature 2: Sales System

- Record a sale (item + quantity)
- Calculate total sale amount
- Update inventory after each sale
- Show change due (if customer pays with cash)

### Feature 3: Reports

- Daily sales summary
- Total revenue
- Low-stock warnings
- Profit calculation (if cost price is known)

### Feature 4: Data Persistence

- Save inventory to a JSON file
- Load inventory when the program starts
- Save sales history

## Starter Code

Here's a skeleton to get you started. Fill in the blanks:

```python
# Sari-Sari Store Management System
# Boss Fight 1 -- Combine everything!

import json
import os
from datetime import datetime

INVENTORY_FILE = "store_inventory.json"
SALES_FILE = "sales_history.json"


class SariSariStore:
    def __init__(self, name="Lola's Sari-Sari Store"):
        self.name = name
        self.inventory = {}
        self.sales = []
        self.load_data()

    def add_item(self, name, quantity, price, cost_price=None):
        """Add an item to inventory."""
        # YOUR CODE HERE
        pass

    def sell_item(self, name, quantity, customer_paid=None):
        """Sell items and record the transaction."""
        # YOUR CODE HERE
        pass

    def check_stock(self):
        """Check stock levels and show warnings."""
        # YOUR CODE HERE
        pass

    def daily_report(self):
        """Generate a daily sales report."""
        # YOUR CODE HERE
        pass

    def save_data(self):
        """Save inventory and sales to files."""
        # YOUR CODE HERE
        pass

    def load_data(self):
        """Load inventory and sales from files."""
        # YOUR CODE HERE
        pass


def main_menu(store):
    """Display the main menu."""
    while True:
        print(f"\n=== {store.name} ===")
        print("1. View inventory")
        print("2. Add item")
        print("3. Sell item")
        print("4. Check stock")
        print("5. Daily report")
        print("6. Exit")

        choice = input("\nChoose (1-6): ")

        if choice == "1":
            # YOUR CODE HERE
            pass
        elif choice == "2":
            # YOUR CODE HERE
            pass
        elif choice == "3":
            # YOUR CODE HERE
            pass
        elif choice == "4":
            store.check_stock()
        elif choice == "5":
            store.daily_report()
        elif choice == "6":
            store.save_data()
            print("Saving... See you tomorrow, Lola!")
            break
        else:
            print("Invalid choice. Subok ulit.")


if __name__ == "__main__":
    store = SariSariStore()
    main_menu(store)
```

## Hints

??? note "Hint 1: Data Structure"
    Use a dictionary for inventory. Each item should have name, quantity, price, and optionally cost_price:

    ```python
    self.inventory = {
        "laundry soap": {"qty": 10, "price": 15.00, "cost": 10.00},
        "cigarettes": {"qty": 50, "price": 5.00, "cost": 3.50},
    }
    ```

??? note "Hint 2: Selling Items"
    When selling, check if enough stock exists first:

    ```python
    if name in self.inventory:
        if self.inventory[name]["qty"] >= quantity:
            self.inventory[name]["qty"] -= quantity
            # Record sale
        else:
            print("Hindi sapat ang stock!")
    ```

??? note "Hint 3: Saving to JSON"
    ```python
    def save_data(self):
        with open(INVENTORY_FILE, "w") as f:
            json.dump(self.inventory, f, indent=4)
        with open(SALES_FILE, "w") as f:
            json.dump(self.sales, f, indent=4)
    ```

??? note "Hint 4: Daily Report"
    Loop through today's sales and calculate totals:

    ```python
    today_sales = [s for s in self.sales if s["date"].startswith(today)]
    total_revenue = sum(s["total"] for s in today_sales)
    total_profit = sum(s["profit"] for s in today_sales)
    ```

## Solution

??? success "Solution -- Click to reveal"
    <details>
    <summary>Click here to see the complete solution</summary>

    ```python
    import json
    import os
    from datetime import datetime

    INVENTORY_FILE = "store_inventory.json"
    SALES_FILE = "sales_history.json"


    class SariSariStore:
        def __init__(self, name="Lola's Sari-Sari Store"):
            self.name = name
            self.inventory = {}
            self.sales = []
            self.load_data()

        def add_item(self, name, quantity, price, cost_price=None):
            name = name.lower().strip()
            if name in self.inventory:
                self.inventory[name]["qty"] += quantity
                print(f"Updated {name}: +{quantity} (now {self.inventory[name]['qty']})")
            else:
                self.inventory[name] = {
                    "qty": quantity,
                    "price": price,
                    "cost": cost_price or price * 0.7,
                }
                print(f"Added {name}: {quantity} @ ₱{price}")

        def sell_item(self, name, quantity, customer_paid=None):
            name = name.lower().strip()
            if name not in self.inventory:
                print(f"'{name}' not found in inventory.")
                return

            item = self.inventory[name]
            if item["qty"] < quantity:
                print(f"Hindi sapat ang stock! Available: {item['qty']}")
                return

            item["qty"] -= quantity
            total = item["price"] * quantity
            profit = (item["price"] - item["cost"]) * quantity
            change = (customer_paid - total) if customer_paid and customer_paid >= total else 0

            sale = {
                "date": datetime.now().isoformat(),
                "item": name,
                "qty": quantity,
                "unit_price": item["price"],
                "total": total,
                "profit": profit,
                "paid": customer_paid or total,
                "change": change,
            }
            self.sales.append(sale)

            print(f"Sale: {quantity}x {name} = ₱{total:.2f}")
            if customer_paid:
                print(f"Paid: ₱{customer_paid:.2f}, Change: ₱{change:.2f}")

            if item["qty"] < 5:
                print(f"⚠️  Low stock: {name} ({item['qty']} left)")

        def check_stock(self):
            print(f"\n=== Stock Check: {self.name} ===")
            low_stock = []
            for name, data in sorted(self.inventory.items()):
                status = "✅" if data["qty"] >= 5 else "⚠️"
                print(f"  {status} {name}: {data['qty']} (₱{data['price']})")
                if data["qty"] < 5:
                    low_stock.append(name)

            if low_stock:
                print(f"\n⚠️  Restock needed: {', '.join(low_stock)}")
            else:
                print("\n✅ All items well-stocked!")

        def daily_report(self):
            today = datetime.now().strftime("%Y-%m-%d")
            today_sales = [s for s in self.sales if s["date"].startswith(today)]

            if not today_sales:
                print("No sales today. Walang benta.")
                return

            total_revenue = sum(s["total"] for s in today_sales)
            total_profit = sum(s["profit"] for s in today_sales)
            total_items = sum(s["qty"] for s in today_sales)

            print(f"\n=== Daily Report: {today} ===")
            print(f"Transactions: {len(today_sales)}")
            print(f"Items sold: {total_items}")
            print(f"Revenue: ₱{total_revenue:.2f}")
            print(f"Profit: ₱{total_profit:.2f}")
            print(f"Profit margin: {(total_profit/total_revenue*100):.1f}%")

        def save_data(self):
            with open(INVENTORY_FILE, "w") as f:
                json.dump(self.inventory, f, indent=4)
            with open(SALES_FILE, "w") as f:
                json.dump(self.sales, f, indent=4)
            print("Data saved.")

        def load_data(self):
            if os.path.exists(INVENTORY_FILE):
                with open(INVENTORY_FILE, "r") as f:
                    self.inventory = json.load(f)
            if os.path.exists(SALES_FILE):
                with open(SALES_FILE, "r") as f:
                    self.sales = json.load(f)


    def main():
        store = SariSariStore()

        while True:
            print(f"\n=== {store.name} ===")
            print("1. View inventory")
            print("2. Add item")
            print("3. Sell item")
            print("4. Check stock")
            print("5. Daily report")
            print("6. Exit")

            choice = input("\nChoose (1-6): ")

            if choice == "1":
                for name, data in store.inventory.items():
                    print(f"  {name}: {data['qty']} @ ₱{data['price']}")

            elif choice == "2":
                name = input("Item name: ")
                qty = int(input("Quantity: "))
                price = float(input("Selling price: "))
                cost = input("Cost price (optional, press Enter to skip): ")
                cost = float(cost) if cost else None
                store.add_item(name, qty, price, cost)

            elif choice == "3":
                name = input("Item name: ")
                qty = int(input("Quantity: "))
                paid = input("Amount paid (optional): ")
                paid = float(paid) if paid else None
                store.sell_item(name, qty, paid)

            elif choice == "4":
                store.check_stock()

            elif choice == "5":
                store.daily_report()

            elif choice == "6":
                store.save_data()
                print("See you tomorrow, Lola!")
                break

            else:
                print("Invalid choice.")


    if __name__ == "__main__":
        main()
    ```
    </details>

??? badge "🏆 Achievement Unlocked: Sari-Sari Store Owner"
    **Badge:** Sari-Sari Store Owner
    **XP Earned:** +500 XP
    **Description:** You built a complete inventory management system from scratch. Your Lola is proud, and so should you.

    > *"Ang unang hakbang ng developer ay ang unang linya ng code. Iyong pinatunayan na kaya mo."*

## Summary

- You combined variables, conditionals, loops, functions, and files into one working program
- Object-oriented programming (the `class` keyword) organizes related data and functions
- JSON is a practical format for saving and loading program data
- A "Boss Fight" tests your ability to connect all concepts

## Further Reading

- [Python's official tutorial -- Data Structures](https://docs.python.org/3/tutorial/datastructures.html)
- [Real Python -- Working with JSON](https://realpython.com/python-json/)
- [Automate the Boring Stuff -- Storing Data](https://automatetheboringstuff.com/2e/chapter10/)

## What's Next

In Part 2, you'll level up with **classes, APIs, web scraping, and error handling**. The projects get more ambitious, and so does your skill.

---

*Previous: [Chapter 7: Files](chapter-07-files.md) -- Saving data permanently*
*Next: [Part 2: Building Things](../part-2-building-things/index.md) -- Where things get real.*

---

??? example "Portfolio Tip"

    **GitHub README**: Your sari-sari store system is a STAR project. Write a README that explains: the problem (Lola's notebook), the solution (Python + JSON), and a screenshot of the menu. Add an `assets/` folder with a demo screenshot. This is the kind of project that gets interviews.

    **LinkedIn**: Post a detailed write-up: "I built a complete inventory management system for my Lola's sari-sari store using Python. It tracks stock, processes sales, calculates profit, and persists data to JSON. Real problem, real solution. #Python #SariSariStore". Include a short demo video if you can.

    **Interview Talking Point**: "I built a CRUD application from scratch -- a sari-sari store system with inventory management, sales tracking, and data persistence. It used classes, dictionaries, file I/O, and error handling. It taught me that the best projects solve problems for real people, not just tutorial exercises."

??? example "🧠 Reflection — Sari-Sari Store System Boss Fight"

    - **What did you learn?** You combined variables, lists, dictionaries, conditionals, loops, functions, and file I/O to build a complete, working application from scratch.
    - **How can you apply this?** The same patterns used in your sari-sari store system apply to real small-business tools: inventory tracking for a palengke vendor, grade calculators for students, or attendance systems for community organizations.
    - **What's next?** Now that you can build a full program, how would you organize larger projects with hundreds of lines of code?

??? checkbox "✅ Chapter Checklist"

    - [ ] I can add, update, and remove items from a dictionary-based inventory
    - [ ] I built a sales system that tracks revenue and updates stock levels
    - [ ] I implemented low-stock warnings using conditionals
    - [ ] I saved and loaded inventory data to/from a JSON file between sessions
    - [ ] I generated a sales report summarizing total revenue and items sold
