# Chapter 10: Boss Fight 1 -- The Complete Sari-Sari Store System

??? example "📋 Chapter Info"
    | | |
    |---|---|
    | **Difficulty** | ⭐⭐⭐ Boss Fight |
    | **Time** | 60 min |
    | **XP** | +500 XP |

??? warning "⚔️ Tier 1 -- Fundamentals Boss"
    **Tier:** Elite Boss | **Concepts Combined:** 7 (Variables, Comparisons, Branching, Boolean Logic, Loops, Functions, Files)
    **XP Reward:** 500 XP | **Badge:** "Sari-Sari Store Owner"

> **Story Hook:** Lola’s store is no longer just a notebook. It can now check stock, handle sales, calculate totals, and save the results for tomorrow. You are not learning a new concept here. You are combining the same tools into one complete system.

> **Output:** A CLI sari-sari store manager with inventory, sales, warnings, summaries, and saved records.

---

## What You'll Do

This Boss Fight combines **everything** you learned in Chapters 3 to 9:

- Variables and data types
- Comparisons and booleans
- Branching with `if`, `elif`, and `else`
- Boolean logic with `and`, `or`, and `not`
- Loops for menus and repeated checks
- Functions for reusable helpers
- Files and JSON for saving data

Build a store system that can:

1. View inventory
2. Add or restock items
3. Sell items and update stock
4. Warn about low stock
5. Save and load inventory data

## Starter Code

Fill in the missing pieces.

```python
import json
import os
from datetime import datetime

INVENTORY_FILE = "store_inventory.json"
SALES_FILE = "sales_history.json"


def load_json(filename, default):
    if os.path.exists(filename):
        with open(filename, "r") as file:
            return json.load(file)
    return default


def save_json(filename, data):
    with open(filename, "w") as file:
        json.dump(data, file, indent=2)


def load_data():
    inventory = load_json(INVENTORY_FILE, {})
    sales = load_json(SALES_FILE, [])
    return inventory, sales


def save_data(inventory, sales):
    save_json(INVENTORY_FILE, inventory)
    save_json(SALES_FILE, sales)


def view_inventory(inventory):
    if not inventory:
        print("Walang items sa inventory.")
        return

    print("\n=== Inventory ===")
    for name, data in inventory.items():
        print(f"{name}: {data['qty']} pcs @ ₱{data['price']:.2f}")


def add_item(inventory):
    name = input("Item name: ").strip().lower()
    qty = int(input("Quantity: "))
    price = float(input("Price: "))
    cost_input = input("Cost price (optional): ").strip()
    cost = float(cost_input) if cost_input else price * 0.7

    if name in inventory:
        inventory[name]["qty"] += qty
        inventory[name]["price"] = price
        inventory[name]["cost"] = cost
        print(f"Updated {name}.")
    else:
        inventory[name] = {"qty": qty, "price": price, "cost": cost}
        print(f"Added {name}.")


def sell_item(inventory, sales):
    name = input("Item name: ").strip().lower()
    qty = int(input("Quantity: "))

    if name not in inventory:
        print("Item not found.")
        return

    item = inventory[name]
    if item["qty"] < qty:
        print(f"Hindi sapat ang stock. Available: {item['qty']}")
        return

    total = item["price"] * qty
    item["qty"] -= qty

    sale = {
        "date": datetime.now().isoformat(),
        "item": name,
        "qty": qty,
        "total": total,
    }
    sales.append(sale)

    print(f"Sold {qty} x {name} = ₱{total:.2f}")

    paid_input = input("Amount paid (optional): ").strip()
    if paid_input:
        paid = float(paid_input)
        if paid >= total:
            print(f"Change: ₱{paid - total:.2f}")
        else:
            print("Kulang ang bayad.")


def check_stock(inventory):
    print("\n=== Stock Check ===")
    for name, data in inventory.items():
        if data["qty"] <= 5:
            print(f"⚠️  {name}: low stock ({data['qty']})")
        else:
            print(f"✅ {name}: okay ({data['qty']})")


def daily_report(sales):
    today = datetime.now().strftime("%Y-%m-%d")
    today_sales = [sale for sale in sales if sale["date"].startswith(today)]

    if not today_sales:
        print("Walang sales today.")
        return

    total_sales = sum(sale["total"] for sale in today_sales)
    total_items = sum(sale["qty"] for sale in today_sales)

    print(f"\n=== Daily Report ({today}) ===")
    print(f"Transactions: {len(today_sales)}")
    print(f"Items sold: {total_items}")
    print(f"Revenue: ₱{total_sales:.2f}")


def main_menu():
    inventory, sales = load_data()

    while True:
        print("\n=== Lola's Sari-Sari Store ===")
        print("1. View inventory")
        print("2. Add item")
        print("3. Sell item")
        print("4. Check stock")
        print("5. Daily report")
        print("6. Exit")

        choice = input("Choose (1-6): ").strip()

        if choice == "1":
            view_inventory(inventory)
        elif choice == "2":
            add_item(inventory)
        elif choice == "3":
            sell_item(inventory, sales)
        elif choice == "4":
            check_stock(inventory)
        elif choice == "5":
            daily_report(sales)
        elif choice == "6":
            save_data(inventory, sales)
            print("Saving... See you tomorrow.")
            break
        else:
            print("Invalid choice. Subok ulit.")


if __name__ == "__main__":
    main_menu()
```

## Hints

??? note "Hint 1: Inventory Data"
    Keep inventory as a dictionary of dictionaries:

    ```python
    inventory = {
        "laundry soap": {"qty": 10, "price": 15.0, "cost": 10.0},
        "candy": {"qty": 25, "price": 5.0, "cost": 3.0},
    }
    ```

??? note "Hint 2: Low Stock"
    Check stock with a simple condition:

    ```python
    if item["qty"] <= 5:
        print("Low stock")
    ```

??? note "Hint 3: Saving Data"
    Use JSON so the program can load the same inventory next time.

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


    def load_json(filename, default):
        if os.path.exists(filename):
            with open(filename, "r") as file:
                return json.load(file)
        return default


    def save_json(filename, data):
        with open(filename, "w") as file:
            json.dump(data, file, indent=2)


    def load_data():
        return load_json(INVENTORY_FILE, {}), load_json(SALES_FILE, [])


    def save_data(inventory, sales):
        save_json(INVENTORY_FILE, inventory)
        save_json(SALES_FILE, sales)


    def view_inventory(inventory):
        if not inventory:
            print("Walang items sa inventory.")
            return

        print("\n=== Inventory ===")
        for name, data in inventory.items():
            print(f"{name}: {data['qty']} pcs @ ₱{data['price']:.2f}")


    def add_item(inventory):
        name = input("Item name: ").strip().lower()
        qty = int(input("Quantity: "))
        price = float(input("Price: "))
        cost_input = input("Cost price (optional): ").strip()
        cost = float(cost_input) if cost_input else price * 0.7

        if name in inventory:
            inventory[name]["qty"] += qty
            inventory[name]["price"] = price
            inventory[name]["cost"] = cost
            print(f"Updated {name}.")
        else:
            inventory[name] = {"qty": qty, "price": price, "cost": cost}
            print(f"Added {name}.")


    def sell_item(inventory, sales):
        name = input("Item name: ").strip().lower()
        qty = int(input("Quantity: "))

        if name not in inventory:
            print("Item not found.")
            return

        item = inventory[name]
        if item["qty"] < qty:
            print(f"Hindi sapat ang stock. Available: {item['qty']}")
            return

        total = item["price"] * qty
        item["qty"] -= qty

        sales.append({
            "date": datetime.now().isoformat(),
            "item": name,
            "qty": qty,
            "total": total,
        })

        print(f"Sold {qty} x {name} = ₱{total:.2f}")


    def check_stock(inventory):
        print("\n=== Stock Check ===")
        for name, data in inventory.items():
            if data["qty"] <= 5:
                print(f"⚠️  {name}: low stock ({data['qty']})")
            else:
                print(f"✅ {name}: okay ({data['qty']})")


    def daily_report(sales):
        today = datetime.now().strftime("%Y-%m-%d")
        today_sales = [sale for sale in sales if sale["date"].startswith(today)]

        if not today_sales:
            print("Walang sales today.")
            return

        total_sales = sum(sale["total"] for sale in today_sales)
        total_items = sum(sale["qty"] for sale in today_sales)

        print(f"\n=== Daily Report ({today}) ===")
        print(f"Transactions: {len(today_sales)}")
        print(f"Items sold: {total_items}")
        print(f"Revenue: ₱{total_sales:.2f}")


    def main_menu():
        inventory, sales = load_data()

        while True:
            print("\n=== Lola's Sari-Sari Store ===")
            print("1. View inventory")
            print("2. Add item")
            print("3. Sell item")
            print("4. Check stock")
            print("5. Daily report")
            print("6. Exit")

            choice = input("Choose (1-6): ").strip()

            if choice == "1":
                view_inventory(inventory)
            elif choice == "2":
                add_item(inventory)
            elif choice == "3":
                sell_item(inventory, sales)
            elif choice == "4":
                check_stock(inventory)
            elif choice == "5":
                daily_report(sales)
            elif choice == "6":
                save_data(inventory, sales)
                print("Saving... See you tomorrow.")
                break
            else:
                print("Invalid choice. Subok ulit.")


    if __name__ == "__main__":
        main_menu()
    ```
    </details>

??? badge "🏆 Achievement Unlocked: Sari-Sari Store Owner"
    **Badge:** Sari-Sari Store Owner
    **XP Earned:** +500 XP
    **Description:** You combined the core fundamentals into one working store system.

## Summary

- You combined variables, comparisons, branching, boolean logic, loops, functions, and files into one program
- Functions and JSON make a small CLI tool much easier to maintain
- A boss fight should reuse learned concepts, not introduce a new one

## Further Reading

- [Python's official tutorial -- Data Structures](https://docs.python.org/3/tutorial/datastructures.html)
- [Real Python -- Working with JSON](https://realpython.com/python-json/)

## What's Next

In Part 2, you'll level up with **classes**, so the same kind of store logic can be organized into larger objects.

*Previous: [Chapter 9: Files and JSON for the Store](chapter-09-files.md) -- Saving data permanently*
*Next: [Part 2: Building Things](../part-2-building-things/index.md) -- Where things get real.*

??? example "Portfolio Tip"

    **GitHub README**: Explain the problem, the store system, and include a screenshot of the menu. Show the data file format too.

    **LinkedIn**: Post a short demo or summary of how you built a complete inventory manager with Python, JSON, and functions.

    **Interview Talking Point**: Example talking point: "I built a full CLI inventory system using dictionaries, functions, loops, conditionals, and JSON persistence. It helped me connect multiple beginner concepts into one practical tool."

??? example "🧠 Reflection — Sari-Sari Store System Boss Fight"

    - **What did you learn?** You combined the core fundamentals into one working store system.
    - **How can you apply this?** The same patterns can power a simple inventory tracker, a club supply list, or a home budget helper.
    - **What's next?** Now that you can build a complete small program, how would you organize larger projects into classes?

??? checkbox "✅ Chapter Checklist"

    - [ ] I can add, update, and display inventory using a dictionary
    - [ ] I can sell items while checking for available stock
    - [ ] I can use loops and functions to organize repeated work
    - [ ] I can save and load inventory data using JSON
    - [ ] I built a working store menu from start to finish
