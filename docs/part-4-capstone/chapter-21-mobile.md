# Chapter 21: Mobile Python

> **Story Hook:** Your Lola doesn't have a laptop. She has a ₱5,000 Infinix phone with 32GB of storage and a cracked screen. She uses WhatsApp to talk to her sisters in another barangay and GCash to receive money from her children abroad. She's never heard of Python. But she tracks her sari-sari store inventory in a notebook, just like before. You think: "What if she could use her phone to track everything? What if Python could run on that phone?"

---

## What You'll Learn

- How to run Python on Android
- Mobile-friendly Python frameworks
- Building simple tools for phones
- Offline-first design for data-conscious users

## Python on Your Phone

Yes, you can run Python on your phone. It's not ideal for everything, but for simple tools, scripts, and learning, it's surprisingly capable.

### Termux (Android)

[Termux](https://termux.dev/) is a terminal emulator for Android that gives you a full Linux environment:

```bash
# Install Termux from F-Droid (not Play Store -- F-Droid has the updated version)
# Then in Termux:
pkg update && pkg upgrade
pkg install python
python --version
```

Now you have Python on your phone. Real Python. With pip, with packages, with everything.

```bash
pip install requests
pip install beautifulsoup4
pip install kivy
```

### Pydroid 3 (Android)

If Termux feels too complex, [Pydroid 3](https://pydroid.app/) is a simpler Python IDE for Android with a visual editor:

- Works out of the box
- Comes with pip
- Has a built-in editor
- Supports matplotlib, pygame, and more

### Pythonista (iOS)

If you have an iPhone or iPad, [Pythonista](https://omz-software.com/pythonista/) is the best Python IDE for iOS. It's not free, but it's powerful and beautifully designed.

## Building Mobile-Friendly Tools

### CLI Tools That Work on Phone Terminals

Most phone terminals are narrow (30-40 characters wide). Keep your output compact:

```python
# Mobile-friendly CLI output
# Chapter 21

def print_inventory(inventory, max_width=35):
    """Print inventory in a compact, mobile-friendly format."""
    print("📦 INVENTORY")
    print("-" * max_width)
    for name, data in inventory.items():
        # Truncate long names
        display_name = name[:max_width - 15]
        print(f"  {display_name:.<20} {data['qty']:>3} @ ₱{data['price']}")
    print("-" * max_width)


inventory = {
    "laundry soap": {"qty": 10, "price": 15.00},
    "cigarettes": {"qty": 50, "price": 5.00},
    "candy": {"qty": 25, "price": 3.00},
    "instant noodles": {"qty": 30, "price": 8.00},
    "softdrinks": {"qty": 20, "price": 15.00},
    "coffee": {"qty": 15, "price": 12.00},
}

print_inventory(inventory)
```

Output on a narrow screen:

```
📦 INVENTORY
-----------------------------------
  laundry soap.......  10 @ ₱15.0
  cigarettes.........  50 @ ₱5.00
  candy..............  25 @ ₱3.00
  instant noodles....  30 @ ₱8.00
  softdrinks.........  20 @ ₱15.0
  coffee.............  15 @ ₱12.0
-----------------------------------
```

### Kivy: Building Real Mobile Apps

[Kivy](https://kivy.org/) is a Python framework for building cross-platform mobile apps:

```bash
pip install kivy
```

```python
# Simple GCash Tracker
# Chapter 21
# Run on: Android (Termux/Pydroid), desktop, or web

import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.window import Window


class GCashTrackerApp(App):
    def __init__(self):
        self.balance = 0.0
        self.transactions = []
        super().__init__()

    def build(self):
        Window.size = (360, 640)  # Phone aspect ratio
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # Title
        title = Label(text="💰 GCash Tracker", font_size=24)
        layout.add_widget(title)

        # Balance display
        self.balance_label = Label(
            text=f"₱{self.balance:.2f}",
            font_size=32,
            bold=True
        )
        layout.add_widget(self.balance_label)

        # Amount input
        self.amount_input = TextInput(
            hint_text="Amount (₱)",
            multiline=False,
            keyboard_type="number"
        )
        layout.add_widget(self.amount_input)

        # Description input
        self.desc_input = TextInput(
            hint_text="Description (e.g., 'Load', 'Merienda')",
            multiline=False
        )
        layout.add_widget(self.desc_input)

        # Buttons
        btn_layout = BoxLayout(spacing=10)
        send_btn = Button(text="💸 Send (₱)", size_hint=(0.5, 1))
        receive_btn = Button(text="📥 Receive (₱)", size_hint=(0.5, 1))

        send_btn.bind(on_press=self.send_money)
        receive_btn.bind(on_press=self.receive_money)

        btn_layout.add_widget(send_btn)
        btn_layout.add_widget(receive_btn)
        layout.add_widget(btn_layout)

        # Transaction list
        self.tx_label = Label(text="No transactions yet", halign="center")
        layout.add_widget(self.tx_label)

        return layout

    def send_money(self, instance):
        try:
            amount = float(self.amount_input.text)
            desc = self.desc_input.text or "Sent"
            if amount > self.balance:
                self.tx_label.text = "⚠️ Sufficient funds lang!"
                return
            self.balance -= amount
            self.transactions.append(f"-₱{amount:.2f} {desc}")
        except ValueError:
            self.tx_label.text = "⚠️ Number lang, please"
            return

        self.update_display()

    def receive_money(self, instance):
        try:
            amount = float(self.amount_input.text)
            desc = self.desc_input.text or "Received"
            self.balance += amount
            self.transactions.append(f"+₱{amount:.2f} {desc}")
        except ValueError:
            self.tx_label.text = "⚠️ Number lang, please"
            return

        self.update_display()

    def update_display(self):
        self.balance_label.text = f"₱{self.balance:.2f}"
        if self.transactions:
            recent = self.transactions[-5:]  # Show last 5
            self.tx_label.text = "\n".join(reversed(recent))
        else:
            self.tx_label.text = "No transactions yet"


if __name__ == "__main__":
    GCashTrackerApp().run()
```

??? tip "Diskarte"
    If Kivy feels complex for your needs, start with CLI tools in Termux. They're simpler, work everywhere, and you can always add a GUI later.

## Offline-First Design

Filipino users often have limited or intermittent internet. Design for offline:

```python
# Offline-first data storage
# Chapter 21

import json
import os
from datetime import datetime


class OfflineStore:
    """Stores data locally, syncs when online."""

    def __init__(self, filename="data.json"):
        self.filename = filename
        self.data = self.load()

    def load(self):
        """Load data from file. Return empty dict if file doesn't exist."""
        if os.path.exists(self.filename):
            with open(self.filename, "r") as f:
                return json.load(f)
        return {}

    def save(self):
        """Save data to file."""
        with open(self.filename, "w") as f:
            json.dump(self.data, f, indent=4)

    def add_transaction(self, amount, description):
        """Add a transaction and save immediately."""
        transaction = {
            "amount": amount,
            "description": description,
            "timestamp": datetime.now().isoformat(),
        }
        if "transactions" not in self.data:
            self.data["transactions"] = []
        self.data["transactions"].append(transaction)
        self.save()  # Save immediately -- works offline

    def get_balance(self):
        """Calculate balance from stored transactions."""
        total = 0
        for tx in self.data.get("transactions", []):
            total += tx["amount"]
        return total

    def export_csv(self, filename="transactions.csv"):
        """Export transactions to CSV for sharing."""
        with open(filename, "w") as f:
            f.write("Date,Amount,Description\n")
            for tx in self.data.get("transactions", []):
                date = tx["timestamp"][:10]
                f.write(f"{date},{tx['amount']},{tx['description']}\n")
        print(f"Exported to {filename}")


# Usage on phone
tracker = OfflineStore("gcash_tracker.json")
tracker.add_transaction(-50.00, "Jollibee merienda")
tracker.add_transaction(200.00, "Receive from abuela")
tracker.add_transaction(-30.00, "Smart load")
print(f"Balance: ₱{tracker.get_balance():.2f}")
tracker.export_csv()
```

## Google Colab for Mobile

When you need more power than your phone can handle, [Google Colab](https://colab.research.google.com) runs in your mobile browser:

```python
# Colab notebook -- works on any device with a browser
# Just open colab.research.google.com in your phone's browser

import pandas as pd
import matplotlib.pyplot as plt

# Your data
data = {
    "month": ["Jan", "Feb", "Mar", "Apr", "May"],
    "sales": [15000, 18000, 16500, 20000, 22000],
    "expenses": [12000, 14000, 13000, 15000, 16000],
}

df = pd.DataFrame(data)
df["profit"] = df["sales"] - df["expenses"]
print(df)

# Plot on mobile -- use this magic command in Colab
# %matplotlib inline
# df.plot(x="month", y="profit", kind="bar")
# plt.show()
```

## Building a Sari-Sari Store SMS Tool

For users without smartphones, you can send data via SMS using APIs:

```python
# SMS notification for sari-sari store
# Uses a free SMS API (Twilio, or Philippine SMS gateways)

import json

LOW_STOCK_THRESHOLD = 5


def check_and_alert(inventory_file, phone_number):
    """Check inventory and send SMS alert for low stock."""
    with open(inventory_file, "r") as f:
        inventory = json.load(f)

    low_stock = []
    for item, data in inventory.items():
        if data["qty"] < LOW_STOCK_THRESHOLD:
            low_stock.append(f"{item}: {data['qty']} left")

    if low_stock:
        message = "⚠️ Low stock alert!\n" + "\n".join(low_stock)
        # Send SMS via your preferred API
        # send_sms(phone_number, message)
        print(f"Would send SMS to {phone_number}:\n{message}")
    else:
        print("✅ All items well-stocked. Walang alert.")


# Example usage
inventory = {
    "laundry soap": {"qty": 3, "price": 15.00},
    "cigarettes": {"qty": 50, "price": 5.00},
    "candy": {"qty": 2, "price": 3.00},
    "instant noodles": {"qty": 30, "price": 8.00},
}

check_and_alert("inventory.json", "09171234567")
```

## Summary

- Python runs on Android via Termux and Pydroid 3
- Kivy lets you build real mobile apps in Python
- Design for offline: save data locally first
- Keep CLI output compact for narrow phone screens
- Google Colab works in mobile browsers for heavier computation

## Boss Fight

??? warning "Boss Fight: Complete Mobile Inventory"

    Build a sari-sari store inventory app that:

    1. Runs on Android (Termux or Pydroid 3)
    2. Stores data offline in JSON
    3. Has a text-based menu optimized for narrow screens
    4. Can add, sell, and view inventory
    5. Sends low-stock alerts
    6. Exports data to CSV for sharing

    **Bonus:** Add a simple Kivy GUI if you want to go further.

??? success "You did it! Level Up!"
    +150 XP. You built a mobile Python app. Ang galing!

## Side Quests

??? note "Optional: Side Quest"
    - Deploy your app to a Raspberry Pi as a kiosk inventory system
    - Build a Telegram bot that lets customers check inventory via chat
    - Create a web version using Flask that works on any browser

## Further Reading

- [Termux documentation](https://termux.dev/)
- [Kivy documentation](https://kivy.org/doc/stable/)
- [Google Colab guide](https://colab.research.google.com/notebooks/intro.ipynb)

---

*Next: [Chapter 22: Bayanihan & Open Source](chapter-22-bayanihan.md) -- Giving back to the community.*
