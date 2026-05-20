# Chapter 14: Boss Fight 2 -- The Midpoint Boss Battle

??? example "📋 Chapter Info"
    | | |
    |---|---|
    | **Difficulty** | ⭐⭐⭐ Boss Fight |
    | **Time** | 60 min |
    | **XP** | +500 XP |

??? warning "⚔️ Tier 2 — Midpoint Boss"
    **Tier:** Regular Boss | **Concepts Combined:** 4 (Classes, Strings, APIs, Error Handling)
    **XP Reward:** 500 XP | **Badge:** "Diskarte King/Queen"

> **Story Hook:** You've been coding for a while now. Classes, strings, APIs, web scraping, error handling. Each skill by itself is useful. But what happens when you combine them all? You stand at the midpoint of your journey, looking back at how far you've come and forward at what's ahead. Your Lola asks: "Anak, ano na ang natutunan mo?" You smile. "Lola, I built something that connects to the internet." She doesn't understand. But the code does. And that's enough.

---

## What You'll Do

This Boss Fight combines **everything** from Part 2:

- Classes and OOP
- String manipulation
- API integration
- Web scraping concepts
- Error handling
- File I/O

Build a **Personal Finance Dashboard** that:

1. Tracks income and expenses
2. Fetches real-time exchange rates
3. Categorizes transactions automatically
4. Generates reports with string formatting
5. Saves and loads data between sessions
6. Handles errors gracefully

## The Challenge

Build a comprehensive finance tool with these features:

### Feature 1: Transaction Management

- Add income and expense transactions
- Categorize transactions (pamasahe, kain, allowance, etc.)
- Search and filter transactions
- Edit or delete transactions

### Feature 2: Currency Conversion

- Fetch real exchange rates via API
- Convert transactions between currencies
- Track exchange rate changes over time

### Category Auto-Detection

- Auto-categorize based on keywords
- Custom category rules
- Unrecognized transactions get flagged

### Feature 3: Reports

- Monthly summary with string-formatted tables
- Category breakdown with percentages
- Currency conversion summary
- Savings rate calculation

### Feature 4: Data Persistence

- Save all data to JSON files
- Load data on startup
- Export to CSV for spreadsheet use

## Starter Code

```python
# Personal Finance Dashboard
# Boss Fight 2 -- Combine everything from Part 2!

import json
import os
from datetime import datetime
from collections import defaultdict


class Transaction:
    def __init__(self, amount, category, description="", currency="PHP", date=None):
        self.amount = amount
        self.category = category
        self.description = description
        self.currency = currency
        self.date = date or datetime.now()

    def __str__(self):
        return f"{self.date.strftime('%Y-%m-%d')} | {self.category:15} | {self.amount:>10.2f} {self.currency} | {self.description}"


class FinanceTracker:
    def __init__(self, name="My Budget", base_currency="PHP"):
        self.name = name
        self.base_currency = base_currency
        self.transactions = []
        self.exchange_rates = {}
        self.categories = self._default_categories()
        self.load_data()

    def _default_categories(self):
        return {
            "income": ["allowance", "salary", "freelance", "gift", "oj"],
            "expense": ["pamasahe", "kain", "photocopy", "load", "merienda", "other"],
        }

    def add_transaction(self, amount, category, description="", currency=None):
        """Add a transaction with auto-categorization."""
        # YOUR CODE HERE
        pass

    def get_exchange_rate(self, from_currency, to_currency="PHP"):
        """Get or fetch exchange rate."""
        # YOUR CODE HERE
        pass

    def monthly_summary(self, year=None, month=None):
        """Generate a formatted monthly summary."""
        # YOUR CODE HERE
        pass

    def save_data(self):
        """Save all data to files."""
        # YOUR CODE HERE
        pass

    def load_data(self):
        """Load data from files."""
        # YOUR CODE HERE
        pass


def main():
    tracker = FinanceTracker("Student Budget")

    # Add some transactions
    tracker.add_transaction(500, "allowance", "Weekly allowance")
    tracker.add_transaction(30, "pamasahe", "UD to school")
    tracker.add_transaction(50, "kain", "Jollibee meal")

    # Show summary
    tracker.monthly_summary()


if __name__ == "__main__":
    main()
```

## Hints

??? note "Hint 1: Monthly Summary Formatting"
    Use f-string formatting to create a table:

    ```python
    print(f"{'Category':<15} {'Count':>5} {'Total':>10} {'%':>5}")
    print("-" * 40)
    for cat, data in sorted(category_totals.items()):
        pct = (data["total"] / total * 100) if total else 0
        print(f"{cat:<15} {data['count']:>5} {data['total']:>10.2f} {pct:>4.1f}%")
    ```

??? note "Hint 2: Currency Conversion"
    ```python
    def convert_currency(self, amount, from_curr, to_curr="PHP"):
        if from_curr == to_curr:
            return amount
        rate = self.get_exchange_rate(from_curr, to_curr)
        return amount * rate
    ```

??? note "Hint 3: Auto-Categorization"
    ```python
    def auto_categorize(self, description):
        desc_lower = description.lower()
        for keyword, category in self.keywords.items():
            if keyword in desc_lower:
                return category
        return "uncategorized"
    ```

## Solution

??? success "Solution -- Click to reveal"
    <details>
    <summary>Click here to see the complete solution</summary>

    ```python
    # Personal Finance Dashboard
    # Boss Fight 2 -- Combine everything from Part 2!

    import json
    import os
    from datetime import datetime
    from collections import defaultdict


    class Transaction:
        def __init__(self, amount, category, description="", currency="PHP", date=None):
            self.amount = amount
            self.category = category
            self.description = description
            self.currency = currency
            self.date = date or datetime.now()

        def __str__(self):
            return f"{self.date.strftime('%Y-%m-%d')} | {self.category:15} | {self.amount:>10.2f} {self.currency} | {self.description}"


    class FinanceTracker:
        def __init__(self, name="My Budget", base_currency="PHP"):
            self.name = name
            self.base_currency = base_currency
            self.transactions = []
            self.exchange_rates = {"USD": 56.50, "EUR": 61.20, "JPY": 0.38}
            self.categories = self._default_categories()
            self.keywords = {
                "jollibee": "kain", "mcdonalds": "kain", "starbucks": "kain",
                "ud": "pamasahe", "grab": "pamasahe", "jeep": "pamasahe",
                "gcash": "other", "load": "load", "internet": "other",
                "allowance": "allowance", "salary": "salary",
            }
            self.load_data()

        def _default_categories(self):
            return {
                "income": ["allowance", "salary", "freelance", "gift", "oj"],
                "expense": ["pamasahe", "kain", "photocopy", "load", "merienda", "other"],
            }

        def auto_categorize(self, description):
            desc_lower = description.lower()
            for keyword, category in self.keywords.items():
                if keyword in desc_lower:
                    return category
            return "uncategorized"

        def add_transaction(self, amount, category="", description="", currency=None):
            if not category:
                category = self.auto_categorize(description)
            if not currency:
                currency = self.base_currency
            txn = Transaction(amount, category, description, currency)
            self.transactions.append(txn)
            print(f"Added: ₱{amount:.2f} | {category} | {description}")

        def get_exchange_rate(self, from_currency, to_currency="PHP"):
            if from_currency == to_currency:
                return 1.0
            if to_currency in self.exchange_rates:
                return 1.0 / self.exchange_rates[to_currency]
            if from_currency in self.exchange_rates:
                return self.exchange_rates[from_currency]
            print(f"Warning: No rate for {from_currency} -> {to_currency}. Using 1:1.")
            return 1.0

        def convert_amount(self, amount, from_curr, to_curr):
            rate = self.get_exchange_rate(from_curr, to_curr)
            return amount * rate

        def monthly_summary(self, year=None, month=None):
            filtered = self.transactions
            if year:
                filtered = [t for t in filtered if t.date.year == year]
            if month:
                filtered = [t for t in filtered if t.date.month == month]

            if not filtered:
                print("No transactions found.")
                return

            category_totals = defaultdict(lambda: {"count": 0, "total": 0})
            total = 0

            for txn in filtered:
                cat = txn.category
                category_totals[cat]["count"] += 1
                category_totals[cat]["total"] += txn.amount
                total += txn.amount

            print(f"\n{'='*50}")
            print(f"  Monthly Summary: {self.name}")
            if year:
                print(f"  Period: {year}{'-' + str(month).zfill(2) if month else ''}")
            print(f"{'='*50}")
            print(f"{'Category':<15} {'Count':>5} {'Total':>10} {'%':>5}")
            print("-" * 40)

            for cat, data in sorted(category_totals.items()):
                pct = (data["total"] / total * 100) if total else 0
                print(f"{cat:<15} {data['count']:>5} {data['total']:>10.2f} {pct:>4.1f}%")

            print("-" * 40)
            print(f"{'TOTAL':<15} {len(filtered):>5} {total:>10.2f}")
            print(f"{'='*50}\n")

        def save_data(self):
            data = {
                "transactions": [
                    {
                        "amount": t.amount,
                        "category": t.category,
                        "description": t.description,
                        "currency": t.currency,
                        "date": t.date.isoformat(),
                    }
                    for t in self.transactions
                ],
                "exchange_rates": self.exchange_rates,
            }
            with open("finance_data.json", "w") as f:
                json.dump(data, f, indent=4)
            print("Data saved to finance_data.json")

        def load_data(self):
            if os.path.exists("finance_data.json"):
                with open("finance_data.json", "r") as f:
                    data = json.load(f)
                for t in data.get("transactions", []):
                    txn = Transaction(
                        amount=t["amount"],
                        category=t["category"],
                        description=t["description"],
                        currency=t["currency"],
                        date=datetime.fromisoformat(t["date"]),
                    )
                    self.transactions.append(txn)
                self.exchange_rates = data.get("exchange_rates", self.exchange_rates)
                print(f"Loaded {len(self.transactions)} transactions.")


    def main():
        tracker = FinanceTracker("Student Budget")

        # Add some transactions
        tracker.add_transaction(500, "allowance", "Weekly allowance")
        tracker.add_transaction(30, "pamasahe", "UD to school")
        tracker.add_transaction(50, "kain", "Jollibee meal")
        tracker.add_transaction(100, "", "Grab ride")  # Auto-categorized
        tracker.add_transaction(200, "", "Load recharge")  # Auto-categorized

        # Show summary
        tracker.monthly_summary()

        # Save data
        tracker.save_data()


    if __name__ == "__main__":
        main()
    ```
    </details>

??? badge "🏆 Achievement Unlocked: Diskarte King/Queen"
    **Badge:** Diskarte King/Queen
    **XP Earned:** +500 XP
    **Description:** You built a personal finance dashboard that connects to live APIs, handles errors gracefully, and persists data. You're halfway through the book and your skills are growing fast.

    > *"Ang diskarte ng Pilipino ay hindi lang pag-iisip, kundi paggawa. Iyong ginawa."*

## Summary

- You combined OOP, APIs, strings, files, and error handling into one comprehensive tool
- Complex projects are just smaller pieces connected together
- File I/O lets your data persist between program runs
- Error handling makes your programs robust

## What's Next

In Part 3, you'll go even further: Discord bots, data visualization, NLP, AI-assisted coding, and open-source contribution. The skills get more advanced, but so do you.

---

*Previous: [Chapter 13: Errors](chapter-13-errors.md) -- Handling problems gracefully*
*Next: [Part 3: Going Further](../part-3-going-further/index.md) -- Where things get really cool.*

---

??? example "Portfolio Tip"

    **GitHub README**: Your Personal Finance Dashboard is a strong midpoint project. Document the architecture: classes for transactions, API integration for exchange rates, JSON persistence. Include a screenshot of the formatted monthly summary output in the terminal.

    **LinkedIn**: Post: "Built a Personal Finance Dashboard in Python at the midpoint of my learning journey. Combines OOP, API integration, string formatting, error handling, and file I/O. Tracks expenses, auto-categorizes transactions, and converts currencies. #Python #FinTech". Show the formatted output table as an image.

    **Interview Talking Point**: "At the midpoint of my Python learning, I built a finance dashboard that combines classes, APIs, error handling, and data persistence. It auto-categorizes transactions using keyword matching and generates formatted reports. It taught me how to architect a multi-feature application from scratch."

??? example "🧠 Reflection — Midpoint Boss Battle"

    - **What did you learn?** You combined classes, strings, APIs, error handling, and file I/O into a comprehensive Personal Finance Dashboard, proving you can architect and build a real application.
    - **How can you apply this?** The dashboard patterns you built here scale to real financial tools: budget apps for your family, remittance calculators for OFWs, or expense trackers for small businesses in your barangay.
    - **What's next?** You've reached the midpoint -- ahead are Discord bots, data visualization, NLP, and contributing to open-source. Which path excites you most?

??? checkbox "✅ Chapter Checklist"

    - [ ] I designed a class-based system for managing transactions with categories
    - [ ] I integrated an API to fetch real-time exchange rates for currency conversion
    - [ ] I used string formatting to generate readable financial reports
    - [ ] I implemented error handling so the program doesn't crash on bad input or failed API calls
    - [ ] I saved and loaded financial data to persist between program sessions
