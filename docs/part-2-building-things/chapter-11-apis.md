# Chapter 11: APIs and the OFW Remittance Tracker

> **Story Hook:** Your Tita works in Dubai. Every month, she sends money home through a remittance center. But the rate changes -- sometimes ₱54 per dollar, sometimes ₱52, sometimes ₱56. Your Lola always asks: "Ano ang rate ngayon? Magkaiba ba sa last month?" You think: "Kailangan ko ng app na i-track 'to." So you build one, connecting to live exchange rate data.

---

## What You'll Learn

- What APIs are and how they work
- Making HTTP requests with the `requests` library
- Working with JSON responses
- Parsing API data
- Building a real-world tracking tool

## What Is an API?

An **API** (Application Programming Interface) is like a waiter in a restaurant:

1. You (the customer) look at the menu and place an order
2. The waiter (API) takes your order to the kitchen
3. The kitchen (server) prepares your food
4. The waiter brings your food back to you

In programming:
- Your code sends a **request** to a URL
- The server processes it and sends back a **response**
- The response is usually in **JSON** format
- You parse the JSON and use the data

## Installing `requests`

The `requests` library makes working with APIs easy:

```bash
pip install requests
```

## Your First API Request

```python
import requests

# Get exchange rates from a free API
response = requests.get("https://api.exchangerate-api.com/v4/latest/USD")
data = response.json()

print(f"1 USD = {data['rates']['PHP']} PHP")
# 1 USD = 56.23 PHP (example)
```

??? tip "Diskarte"
    `response.json()` converts the API's JSON response into a Python dictionary. Then you access the data just like any other dict: `data["rates"]["PHP"]`.

## Understanding API Responses

Every API response has:

- **Status code**: 200 = success, 404 = not found, 500 = server error
- **Headers**: Metadata about the response
- **Body**: The actual data (usually JSON)

```python
import requests

response = requests.get("https://api.exchangerate-api.com/v4/latest/USD")

print(f"Status code: {response.status_code}")  # 200
print(f"Response time: {response.elapsed}")     # How long it took
print(f"Data keys: {list(response.json().keys())}")  # What data is available
```

## Building the OFW Remittance Tracker

Let's build a tool that tracks exchange rates and calculates remittance impact:

```python
# OFW Remittance Tracker
# Chapter 11

import requests
from datetime import datetime, timedelta


class OFWRemittanceTracker:
    """Track OFW remittances and exchange rates."""

    def __init__(self, ofw_name="Tita Nena", currency_from="USD"):
        self.ofw_name = ofw_name
        self.currency_from = currency_from
        self.history = []
        self.exchange_rates = {}

    def get_exchange_rate(self):
        """Fetch current exchange rate."""
        try:
            url = f"https://api.exchangerate-api.com/v4/latest/{self.currency_from}"
            response = requests.get(url, timeout=10)
            response.raise_for_status()  # Raise error for bad status codes
            data = response.json()
            rate = data["rates"]["PHP"]
            self.exchange_rates[datetime.now().strftime("%Y-%m-%d")] = rate
            print(f"Current rate: 1 {self.currency_from} = ₱{rate:.2f}")
            return rate
        except requests.exceptions.RequestException as e:
            print(f"⚠️  Error fetching rate: {e}")
            print("   Using last known rate.")
            if self.exchange_rates:
                return list(self.exchange_rates.values())[-1]
            return 55.00  # Fallback rate

    def track_remittance(self, amount, rate=None):
        """Record a remittance."""
        if rate is None:
            rate = self.get_exchange_rate()

        php_amount = amount * rate
        entry = {
            "date": datetime.now().strftime("%Y-%m-%d"),
            "amount": amount,
            "currency": self.currency_from,
            "rate": rate,
            "php_amount": php_amount,
        }
        self.history.append(entry)
        print(f"Recorded: {amount} {self.currency_from} → ₱{php_amount:.2f}")

    def yearly_estimate(self, monthly_amount):
        """Estimate yearly remittance."""
        rate = self.get_exchange_rate()
        yearly = monthly_amount * 12 * rate
        print(f"\n=== Yearly Estimate ===")
        print(f"Monthly: {monthly_amount} {self.currency_from} (₱{monthly_amount * rate:.2f})")
        print(f"Yearly: {monthly_amount * 12} {self.currency_from} (₱{yearly:.2f})")
        return yearly

    def rate_change(self):
        """Show exchange rate changes over time."""
        if len(self.exchange_rates) < 2:
            print("Not enough data. Track rates over multiple days.")
            return

        dates = sorted(self.exchange_rates.keys())
        print(f"\n=== Rate History ===")
        for date in dates:
            print(f"  {date}: ₱{self.exchange_rates[date]:.2f}")

        first_rate = self.exchange_rates[dates[0]]
        last_rate = self.exchange_rates[dates[-1]]
        change = last_rate - first_rate
        pct = (change / first_rate) * 100
        print(f"\nChange: {change:+.2f} ({pct:+.1f}%)")

    def summary(self):
        """Show complete remittance summary."""
        if not self.history:
            print("No remittances recorded yet.")
            return

        total_php = sum(e["php_amount"] for e in self.history)
        total_foreign = sum(e["amount"] for e in self.history)
        avg_rate = total_php / total_foreign if total_foreign else 0

        print(f"\n=== Remittance Summary for {self.ofw_name} ===")
        print(f"Total sent: {total_foreign} {self.currency_from}")
        print(f"Total received: ₱{total_php:.2f}")
        print(f"Average rate: ₱{avg_rate:.2f}")
        print(f"Number of remittances: {len(self.history)}")


# Usage
tracker = OFWRemittanceTracker("Tita Nena")

# Fetch current rate
rate = tracker.get_exchange_rate()

# Track some remittances
tracker.track_remittance(500, rate)
tracker.track_remittance(600, rate)

# Yearly estimate
tracker.yearly_estimate(550)

# Rate history and summary
tracker.rate_change()
tracker.summary()
```

## Error Handling with APIs

APIs can fail for many reasons: bad internet, server down, rate limits. Always handle errors:

```python
import requests

try:
    response = requests.get("https://api.example.com/data", timeout=10)
    response.raise_for_status()  # Raises error for 4xx/5xx status codes
    data = response.json()
except requests.exceptions.Timeout:
    print("Request timed out. Subok ulit.")
except requests.exceptions.ConnectionError:
    print("Connection error. Check your internet.")
except requests.exceptions.HTTPError as e:
    print(f"HTTP error: {e}")
except requests.exceptions.RequestException as e:
    print(f"API error: {e}")
```

## API Best Practices

1. **Always set a timeout**: `requests.get(url, timeout=10)` prevents hanging
2. **Use `raise_for_status()`**: Catches HTTP errors automatically
3. **Handle exceptions**: APIs can fail; your code shouldn't crash
4. **Cache responses**: Don't fetch the same data repeatedly
5. **Respect rate limits**: Some APIs limit how many requests you can make

??? example "Portfolio Tip: API Integration"
    Your OFW remittance tracker using live APIs shows you can connect to real-world data -- a highly valued skill:

    1. **GitHub README** -- Document which APIs you used (exchangerate-api, etc.) and why. Include a screenshot of real exchange rate data.
    2. **LinkedIn** -- Add "API Integration" to your skills. Post: "Built a remittance tracker that pulls live exchange rates from APIs. Helps OFW families track how much PHP their USD converts to."
    3. **Interview talking point** -- "I built a remittance tracker that integrates with live exchange rate APIs, handles JSON parsing, and includes error handling for when APIs are down. This mirrors how fintech apps handle real-time currency data."

## Summary

- APIs let your program communicate with other services
- `requests.get()` sends HTTP requests
- `response.json()` parses JSON responses into Python dicts
- Always handle errors: timeouts, connection failures, bad responses
- APIs power real-world tools: exchange rates, weather, maps, social media

## Boss Fight

??? warning "Boss Fight: Complete Remittance Dashboard"

    Extend the tracker with:

    1. Multiple OFW members (family branch tracking)
    2. Exchange rate alerts (notify when rate crosses a threshold)
    3. Historical rate chart (using matplotlib)
    4. Export remittance data to CSV
    5. Family budget impact calculator

    **Hint:** Use a dictionary of trackers, one per OFW member.

??? success "You did it! Level Up!"
    +150 XP. You connected Python to the internet. Ang galing!

## Side Quests

### Mini-Project: GCash Transaction Tracker

??? side-quest "🎯 Mini-Project: GCash Transaction Tracker"
    **Type:** Challenge Quest | **Difficulty:** Medium | **XP:** +25 XP

    Build a mini-project that tracks your daily GCash transactions:

    ```python
    # gcash_tracker.py
    transactions = {
        "2024-01-15": [
            {"type": "sent", "amount": 200, "to": "Tita", "note": "pasaload"},
            {"type": "received", "amount": 500, "from": "Mom", "note": "allowance"},
        ]
    }

    # Your task:
    # 1. Add functions to record transactions
    # 2. Calculate daily/net balance
    # 3. Show transaction summary by category
    ```

### Mini-Project: Palengke Price Comparator

??? side-quest "🎯 Mini-Project: Palengke Price Comparator"
    **Type:** Research Quest | **Difficulty:** Hard | **XP:** +50 XP

    Compare prices across different markets using API data or scraped data:

    ```python
    # price_compare.py
    # Your task:
    # 1. Fetch prices from 2+ sources (APIs or scraping)
    # 2. Compare prices for the same items
    # 3. Show which market has the best prices
    # 4. Alert when price drops below threshold
    ```

??? note "Optional: Side Quest"
    - Add GCash/Maya transaction tracking
    - Build a "best rate" finder that checks multiple sources
    - Create a Telegram bot that sends daily exchange rate updates

## Further Reading

- [Real Python: Working with APIs](https://realpython.com/python-api/)
- [requests library documentation](https://docs.python-requests.org/)

---

*Next: [Chapter 12: Web Scraping](chapter-12-scraping.md) -- Pulling data from websites.*
