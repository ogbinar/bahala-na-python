# Chapter 12: Web Scraping and the Shopee Price Tracker

??? example "📋 Chapter Info"
    | | |
    |---|---|
    | **Difficulty** | ⭐⭐ Intermediate |
    | **Time** | 35 min |
    | **XP** | +100 XP |

> **Story Hook:** It's 11.11 sale season. You're on Shopee, comparing prices for the same item across 50 sellers. Some claim "50% off!" but their "original price" is inflated. You wonder: "How much has the price changed over the past month? Is this really a deal?" So you write a script that tracks prices automatically. No more guessing.

Sa totoo lang, ganito rin tayo mamili minsan: titingin muna sa presyo, rereview pa ang deal, tapos tsaka magdedesisyon.

> **Output:** A scraper that collects product prices and saves comparison data you can review later.

---

## What You'll Learn

- What web scraping is and when to use it
- Parsing HTML with BeautifulSoup
- Extracting specific data from web pages
- Handling scraping ethics and limitations
- Building a price tracker

## What Is Web Scraping?

**Web scraping** is the process of extracting data from websites programmatically. Instead of manually copying prices, you write a script that:

1. Visits a webpage
2. Reads the HTML
3. Finds the data you want
4. Extracts and saves it

??? warning "Boss Fight Warning"
    Always check a website's terms of service before scraping. Some sites prohibit it. Never scrape personal data. Be respectful: add delays between requests, don't overload servers.

??? note "🐌 Slow Internet?"

    Web scraping normally needs live internet, but here's how to practice offline:

    - **Save HTML pages locally**: When you have internet, use your browser to visit a page, then "Save Page As" (Ctrl+S / Cmd+S) to save the full HTML to your computer. Then practice scraping on the saved file instead of hitting the live site.
    - **Practice with saved files**: Point your BeautifulSoup code at the saved HTML file:

    ```python
    from bs4 import BeautifulSoup

    # Load a saved HTML file instead of fetching from the web
    with open("shopee_product.html", "r") as f:
        soup = BeautifulSoup(f.read(), "html.parser")

    title = soup.find("title")
    print(title.text)  # Works completely offline!
    ```

    - **Pro tip**: This is actually better for learning! You can reload the same page over and over without worrying about rate limits or the website changing. Many professional scrapers test on saved HTML snapshots before running against live sites.

## Installing BeautifulSoup

```bash
pip install beautifulsoup4 requests
```

## How BeautifulSoup Works

BeautifulSoup turns HTML into a Python-friendly format:

```python
from bs4 import BeautifulSoup
import requests

# Get a webpage
html = requests.get("https://example.com").text

# Parse it
soup = BeautifulSoup(html, "html.parser")

# Find elements
title = soup.find("title")  # First <title> tag
links = soup.find_all("a")   # All <a> tags
```

## Common BeautifulSoup Methods

| Method | What It Does |
|--------|-------------|
| `soup.find("tag")` | Find the first element with that tag |
| `soup.find_all("tag")` | Find all elements with that tag |
| `soup.find(id="name")` | Find element by ID |
| `soup.find(class_="name")` | Find element by class |
| `element.text` | Get the text inside an element |
| `element["href"]` | Get an attribute value |

## Building a Price Tracker

Let's build a Shopee price tracker (using a mock example since real scraping requires handling anti-bot measures):

```python
# Shopee Price Tracker
# Chapter 12

import requests
from bs4 import BeautifulSoup
import json
import time
from datetime import datetime


class PriceTracker:
    """Track prices of products across time."""

    def __init__(self, product_name, save_file="price_history.json"):
        self.product_name = product_name
        self.save_file = save_file
        self.history = self.load_history()

    def load_history(self):
        """Load existing price history."""
        try:
            with open(self.save_file, "r") as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def save_history(self):
        """Save price history to file."""
        with open(self.save_file, "w") as f:
            json.dump(self.history, f, indent=4)

    def search_price(self, url):
        """Search for a product price (conceptual example)."""
        print(f"Searching: {self.product_name}")
        print(f"URL: {url}")

        # NOTE: Real scraping requires handling:
        # - Anti-bot measures (CAPTCHAs, JavaScript rendering)
        # - Dynamic content (loaded via JavaScript)
        # - Rate limiting
        # This is a simplified educational example

        try:
            headers = {
                "User-Agent": "Mozilla/5.0 (Educational Price Tracker)"
            }
            response = requests.get(url, headers=headers, timeout=10)
            response.raise_for_status()

            soup = BeautifulSoup(response.text, "html.parser")

            # Find price elements (selectors vary by website)
            # This is illustrative -- real selectors depend on the site
            price_elements = soup.find_all("span", class_=["price", "price__amount"])

            if price_elements:
                price_text = price_elements[0].text.strip()
                # Extract number from price text
                normalized_price = price_text.replace("₱", "").replace(",", "").strip()
                price = float(normalized_price)
                self.record_price(price)
                return price
            else:
                print("Price element not found. Check the page structure.")
                return None

        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")
            return None

    def record_price(self, price):
        """Record a price with timestamp."""
        entry = {
            "date": datetime.now().isoformat(),
            "product": self.product_name,
            "price": price,
        }
        self.history.append(entry)
        print(f"Recorded: ₱{price:.2f} at {entry['date']}")
        self.save_history()

    def show_stats(self):
        """Show price statistics."""
        if not self.history:
            print("No price data yet.")
            return

        prices = [e["price"] for e in self.history]
        current = prices[-1]
        lowest = min(prices)
        highest = max(prices)
        average = sum(prices) / len(prices)
        change = current - prices[0]
        pct_change = (change / prices[0]) * 100

        print(f"\n=== Price Stats: {self.product_name} ===")
        print(f"Current: ₱{current:.2f}")
        print(f"Lowest: ₱{lowest:.2f}")
        print(f"Highest: ₱{highest:.2f}")
        print(f"Average: ₱{average:.2f}")
        print(f"Change: {change:+.2f} ({pct_change:+.1f}%)")

        if change < 0:
            print("📉 Price went down! Good time to buy!")
        elif change > 0:
            print("📈 Price went up. Wait for a sale!")
        else:
            print("➡️ Price unchanged.")

    def show_history(self):
        """Show full price history."""
        if not self.history:
            print("No history yet.")
            return

        print(f"\n=== Price History: {self.product_name} ===")
        for entry in self.history:
            date = datetime.fromisoformat(entry["date"]).strftime("%Y-%m-%d %H:%M")
            print(f"  {date}: ₱{entry['price']:.2f}")


# Usage
tracker = PriceTracker("iPhone 15 Case")

# Record some prices (in real use, you'd call search_price() with actual URLs)
tracker.record_price(299.00)
tracker.record_price(350.00)
tracker.record_price(280.00)
tracker.record_price(310.00)

# Check stats
tracker.show_stats()
tracker.show_history()
```

## Handling Dynamic Content

Many modern websites load content via JavaScript, which means the HTML you get from `requests` doesn't include the data you want. Solutions:

| Tool | Best For |
|------|----------|
| **requests + BeautifulSoup** | Static HTML pages |
| **Selenium** | JavaScript-rendered pages |
| **playwright** | Modern JavaScript pages |
| **API inspection** | Finding the actual API behind the page (best approach) |

??? tip "Diskarte"
    Before scraping, check if the website has an API. Open your browser's Developer Tools (F12), go to the "Network" tab, and look for API calls. Often you can call the API directly instead of scraping HTML.

## Ethical Scraping Checklist

- [ ] Check the website's `robots.txt` file (e.g., `https://shopee.ph/robots.txt`)
- [ ] Read the terms of service
- [ ] Don't scrape personal data
- [ ] Add delays between requests (at least 1 second)
- [ ] Identify your bot with a proper User-Agent
- [ ] Respect rate limits
- [ ] Have a fallback plan if scraping fails

??? example "Portfolio Tip: Data Collection"
    Your Shopee price tracker demonstrates web scraping and data collection -- skills used in e-commerce, research, and analytics:

    1. **GitHub README** -- Include sample scraped data (anonymized) and explain your ethical approach to scraping
    2. **LinkedIn** -- Add "Web Scraping" and "BeautifulSoup" to your skills. Post: "Built a price tracker that monitors e-commerce prices automatically. Learned BeautifulSoup and ethical scraping practices."
    3. **Interview talking point** -- "You can say: I built a price comparison tool that scrapes product data from e-commerce sites. I respected rate limits and terms of service, and built in delays between requests to be a good citizen of the web."

## Summary

- Web scraping extracts data from websites
- BeautifulSoup parses HTML into searchable objects
- `find()` and `find_all()` locate elements by tag, ID, or class
- Always scrape ethically and legally
- Inspect network requests to find APIs before scraping HTML

## Boss Fight

??? warning "Boss Fight: Multi-Platform Price Comparator"

    Build a tool that:

    1. Tracks prices across multiple platforms (Shopee, Lazada, TikTok Shop)
    2. Detects fake discounts (price inflated before "sale")
    3. Sends alerts when prices drop below a threshold
    4. Generates a price comparison report

    **Hint:** Use a list of trackers, one per platform.

??? success "You did it! Level Up!"
    +150 XP. You built a price tracking system. Ang galing!

## Side Quests

### Mini-Project: Facebook Marketplace Alert Bot

??? side-quest "🎯 Mini-Project: Facebook Marketplace Alert Bot"
    **Type:** Creative Quest | **Difficulty:** Medium | **XP:** +25 XP

    Build a bot that monitors Facebook Marketplace for specific items and sends you alerts when new listings appear:

    ```python
    # marketplace_alert.py
    # Your task:
    # 1. Scrape listings for a specific item (e.g., "iPhone 12")
    # 2. Track new listings vs. seen listings
    # 3. Alert when price is below your threshold
    # 4. Save results to a file for later review
    ```

### Mini-Project: Load Sharing Tracker

??? side-quest "🎯 Mini-Project: Load Sharing Tracker"
    **Type:** Community Quest | **Difficulty:** Easy | **XP:** +15 XP

    Track who paid, who used how much load, and who owes whom in your barkada:

    ```python
    # load_tracker.py
    # Your task:
    # 1. Track who paid for shared load/data
    # 2. Track who used how much
    # 3. Calculate who owes whom
    # 4. Show summary report
    ```

??? note "Optional: Side Quest"
    - Add a "deal score" that rates how good a price is
    - Create a browser extension for easy price tracking
    - Build a "price prediction" using simple linear regression

## Further Reading

- [BeautifulSoup documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- [Real Python: Web Scraping](https://realpython.com/beautiful-soup-web-scraper-python/)

---

*Previous: [Chapter 11: APIs](chapter-11-apis.md) -- Connecting to live data*
*Next: [Chapter 13: Errors & Debugging](chapter-13-errors.md) -- Handling problems gracefully.*

---

??? example "🧠 Reflection — Web Scraping"

    - **What did you learn?** You learned how to programmatically extract data from websites using BeautifulSoup to parse HTML and pull out specific information like prices, product names, and descriptions.
    - **How can you apply this?** You can track Shopee or Lazada prices for your family's online shopping, monitor palengke prices posted online, or collect data for school research projects without manual copy-pasting.
    - **What's next?** What happens when a website changes its layout, and how do you build scrapers that can adapt to those changes?

??? checkbox "✅ Chapter Checklist"

    - [ ] I understand what web scraping is and when it's appropriate to use
    - [ ] I can install and use BeautifulSoup to parse HTML content
    - [ ] I can locate and extract specific data elements from a webpage using CSS selectors or tags
    - [ ] I know the ethical considerations of web scraping: checking terms of service, adding delays, and avoiding personal data
    - [ ] I built the Shopee Price Tracker project
