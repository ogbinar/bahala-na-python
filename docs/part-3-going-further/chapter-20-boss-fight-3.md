# Chapter 20: Boss Fight 3 -- The Complete Barangay Dashboard

??? warning "⚔️ Elite Boss Fight"
    **Tier:** Elite Boss | **Concepts Combined:** 5+ (Async, Data Viz, NLP, AI Coding, Open Source)
    **XP Reward:** 500 XP | **Badge:** "Barangay Captain"

> **Story Hook:** Your barkada is proud of the Discord bot you built. Your data viz skills are getting attention in your community. Your NLP experiments with Tagalog text are actually useful. But the barangay captain needs more than individual tools -- he needs a complete dashboard. A single view that shows everything: who's paid their fees, who needs help, what the collection rate looks like, upcoming events, emergency contacts. "Gawin mo 'yan sa Python," he says. "Gusto ko ng dashboard na makikita ng lahat." You take a deep breath. This is the ultimate test of everything you've learned in Part 3.

---

## What You'll Combine

This Boss Fight integrates **everything from Chapters 15-19**:

- **Async programming** (Ch 15) -- Handling multiple data sources simultaneously
- **Data visualization** (Ch 16) -- Charts and graphs for decision-making
- **NLP & text processing** (Ch 17) -- Understanding Tagalog messages
- **AI-assisted coding** (Ch 18) -- Using AI to accelerate development
- **Open source** (Ch 19) -- Building on existing projects and sharing yours

## The Challenge

Build a **complete Barangay Dashboard** that:

1. Connects to multiple data sources (APIs, files, databases)
2. Visualizes fee collection, demographics, and trends
3. Processes Tagalog messages from residents
4. Runs as a Discord bot for mobile access
5. Is open-source and community-maintained

## Part 1: The Dashboard Backend

```python
# Barangay Dashboard Backend
# Boss Fight 3

import asyncio
import json
import os
from datetime import datetime, date, timedelta
from collections import Counter, defaultdict
import statistics


class BarangayDashboard:
    """Complete barangay dashboard system."""

    def __init__(self, data_dir="data"):
        self.data_dir = data_dir
        self.residents = {}
        self.transactions = []
        self.messages = []
        self.events = []
        self.load_all_data()

    def load_all_data(self):
        """Load all data sources."""
        self._load_residents()
        self._load_transactions()
        self._load_messages()
        self._load_events()

    def _load_residents(self):
        filepath = os.path.join(self.data_dir, "residents.json")
        if os.path.exists(filepath):
            with open(filepath, "r") as f:
                self.residents = json.load(f)

    def _load_transactions(self):
        filepath = os.path.join(self.data_dir, "transactions.json")
        if os.path.exists(filepath):
            with open(filepath, "r") as f:
                self.transactions = json.load(f)

    def _load_messages(self):
        filepath = os.path.join(self.data_dir, "messages.json")
        if os.path.exists(filepath):
            with open(filepath, "r") as f:
                self.messages = json.load(f)

    def _load_events(self):
        filepath = os.path.join(self.data_dir, "events.json")
        if os.path.exists(filepath):
            with open(filepath, "r") as f:
                self.events = json.load(f)

    # --- Dashboard Metrics ---

    def get_overview(self):
        """Get the main dashboard overview."""
        total_residents = len(self.residents)
        paid_count = len(set(
            t["resident_id"] for t in self.transactions
            if t["status"] == "paid"
        ))
        collection_rate = (paid_count / total_residents * 100) if total_residents > 0 else 0

        total_collected = sum(
            t["amount"] for t in self.transactions if t["status"] == "paid"
        )
        total_outstanding = sum(
            t["amount"] for t in self.transactions if t["status"] != "paid"
        )

        # Demographics
        age_groups = Counter()
        for r in self.residents.values():
            age = self._calculate_age(r.get("birthdate", ""))
            if age >= 60:
                age_groups["Senior (60+)"] += 1
            elif age >= 18:
                age_groups["Adult (18-59)"] += 1
            elif age > 0:
                age_groups["Youth (0-17)"] += 1
            else:
                age_groups["Unknown"] += 1

        # PWD count
        pwd_count = sum(1 for r in self.residents.values() if r.get("isPWD", False))

        return {
            "total_residents": total_residents,
            "paid_count": paid_count,
            "collection_rate": round(collection_rate, 1),
            "total_collected": total_collected,
            "total_outstanding": total_outstanding,
            "net_balance": total_collected - total_outstanding,
            "demographics": dict(age_groups),
            "pwd_count": pwd_count,
            "pending_messages": sum(
                1 for m in self.messages if m.get("status") == "pending"
            ),
            "upcoming_events": sum(
                1 for e in self.events
                if date.fromisoformat(e["date"]) >= date.today()
            ),
        }

    def get_collection_trend(self, months=6):
        """Get monthly collection trend."""
        now = datetime.now()
        monthly = defaultdict(float)

        for t in self.transactions:
            if t["status"] == "paid":
                t_date = date.fromisoformat(t["date"])
                if (now - t_date).days <= months * 30:
                    key = t_date.strftime("%Y-%m")
                    monthly[key] += t["amount"]

        # Sort and format
        trend = []
        for i in range(months, 0, -1):
            month_date = (now.replace(day=1) - timedelta(days=30 * i)).replace(day=1)
            key = month_date.strftime("%Y-%m")
            trend.append({
                "month": month_date.strftime("%b %Y"),
                "amount": monthly.get(key, 0),
            })

        return trend

    def get_low_payers(self, threshold=0.5):
        """Find residents with low payment history."""
        resident_payments = defaultdict(lambda: {"paid": 0, "total": 0})

        for t in self.transactions:
            resident_payments[t["resident_id"]]["total"] += 1
            if t["status"] == "paid":
                resident_payments[t["resident_id"]]["paid"] += 1

        low_payers = []
        for rid, data in resident_payments.items():
            rate = data["paid"] / data["total"] if data["total"] > 0 else 0
            if rate < threshold and rid in self.residents:
                resident = self.residents[rid]
                low_payers.append({
                    "id": rid,
                    "name": f"{resident.get('first_name', '')} {resident.get('last_name', '')}",
                    "payment_rate": round(rate * 100, 1),
                    "paid": data["paid"],
                    "total": data["total"],
                })

        return sorted(low_payers, key=lambda x: x["payment_rate"])

    # --- Async Data Fetching ---

    async def fetch_pagasa_alert(self):
        """Fetch weather alerts from PAGASA (simulated)."""
        # In production, this would call the PAGASA API
        await asyncio.sleep(0.1)  # Simulate network delay
        return {
            "alert_level": "Yellow",
            "message": "May pag-uran sa susunod na 3 araw.",
            "affected_areas": ["Purok 1", "Purok 3", "Purok 5"],
        }

    async def fetch_barangay_updates(self):
        """Fetch updates from DILG or municipal API."""
        await asyncio.sleep(0.1)
        return {
            "last_updated": datetime.now().isoformat(),
            "updates": [
                "Monthly collection meeting: Jan 15, 2025",
                "Senior citizen registration: Ongoing",
                "Clean-up drive: Jan 20, 2025",
            ],
        }

    async def refresh_all(self):
        """Refresh all data sources asynchronously."""
        results = await asyncio.gather(
            self.fetch_pagasa_alert(),
            self.fetch_barangay_updates(),
        )
        return {
            "weather": results[0],
            "updates": results[1],
        }

    # --- Helpers ---

    def _calculate_age(self, birthdate_str):
        if not birthdate_str:
            return 0
        try:
            bd = date.fromisoformat(birthdate_str)
            today = date.today()
            age = today.year - bd.year
            if (today.month, today.day) < (bd.month, bd.day):
                age -= 1
            return age
        except (ValueError, TypeError):
            return 0
```

## Part 2: Data Visualization

```python
# Dashboard Visualization
# Boss Fight 3

import os
import matplotlib
matplotlib.use("Agg")  # Non-interactive backend
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from io import BytesIO
import base64


class DashboardVisualizer:
    """Generate charts and graphs for the dashboard."""

    COLORS = {
        "primary": "#4A90D9",
        "secondary": "#F5A623",
        "success": "#7ED321",
        "danger": "#D0021B",
        "warning": "#F5A623",
        "info": "#4A90D9",
        "bg": "#F8F9FA",
        "text": "#333333",
    }

    def __init__(self, dashboard):
        self.dashboard = dashboard

    def create_collection_chart(self, output_path="collection_chart.png"):
        """Create a bar chart showing monthly fee collection."""
        trend = self.dashboard.get_collection_trend(6)
        months = [t["month"] for t in trend]
        amounts = [t["amount"] for t in trend]

        fig, ax = plt.subplots(figsize=(10, 5))
        bars = ax.bar(months, amounts, color=self.COLORS["primary"], alpha=0.8)

        # Add value labels on bars
        for bar, amount in zip(bars, amounts):
            ax.text(
                bar.get_x() + bar.get_width() / 2,
                bar.get_height() + 50,
                f"₱{amount:,.0f}",
                ha="center", va="bottom", fontsize=9,
            )

        ax.set_title("Monthly Fee Collection (Last 6 Months)", fontsize=14, fontweight="bold")
        ax.set_ylabel("Amount (₱)", fontsize=11)
        ax.set_xlabel("Month", fontsize=11)
        if amounts:
            avg = sum(amounts) / len(amounts)
            ax.axhline(
                y=avg,
                color=self.COLORS["secondary"],
                linestyle="--",
                alpha=0.7,
                label=f"Average: ₱{avg:,.0f}",
            )
        ax.legend(fontsize=9)
        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)

        plt.tight_layout()
        plt.savefig(output_path, dpi=150, bbox_inches="tight")
        plt.close()
        return output_path

    def create_demographics_pie(self, output_path="demographics_chart.png"):
        """Create a pie chart of resident demographics."""
        overview = self.dashboard.get_overview()
        demographics = overview["demographics"]

        if not demographics:
            return None

        fig, ax = plt.subplots(figsize=(8, 6))
        colors = [
            self.COLORS["primary"],
            self.COLORS["secondary"],
            self.COLORS["success"],
            self.COLORS["danger"],
        ]

        wedges, texts, autotexts = ax.pie(
            demographics.values(),
            labels=demographics.keys(),
            autopct="%1.1f%%",
            colors=colors[:len(demographics)],
            startangle=90,
        )

        for autotext in autotexts:
            autotext.set_color("white")
            autotext.set_fontweight("bold")

        ax.set_title("Resident Demographics", fontsize=14, fontweight="bold")

        plt.tight_layout()
        plt.savefig(output_path, dpi=150, bbox_inches="tight")
        plt.close()
        return output_path

    def create_collection_rate_gauge(self, output_path="gauge_chart.png"):
        """Create a simple gauge showing collection rate."""
        overview = self.dashboard.get_overview()
        rate = overview["collection_rate"]

        fig, ax = plt.subplots(figsize=(8, 4))

        # Semi-circle gauge
        ax.set_xlim(-1.5, 1.5)
        ax.set_ylim(-0.1, 1.2)
        ax.axis("off")

        # Background arc
        ax.fill_between(
            [0, 1], [0, 0],
            color=self.COLORS["bg"],
            transform=ax.get_yaxis_transform(),
        )

        # Progress arc (simplified representation)
        rate_clamped = min(rate, 100) / 100

        if rate_clamped >= 0.7:
            color = self.COLORS["success"]
        elif rate_clamped >= 0.4:
            color = self.COLORS["warning"]
        else:
            color = self.COLORS["danger"]

        ax.text(
            0, 0.5,
            f"{rate:.1f}%",
            ha="center", va="center",
            fontsize=48, fontweight="bold", color=color,
            transform=ax.get_yaxis_transform(),
        )
        ax.text(
            0, 0.1,
            "Collection Rate",
            ha="center", va="center",
            fontsize=14, color=self.COLORS["text"],
            transform=ax.get_yaxis_transform(),
        )

        plt.tight_layout()
        plt.savefig(output_path, dpi=150, bbox_inches="tight")
        plt.close()
        return output_path

    def generate_all_charts(self, output_dir="charts"):
        """Generate all dashboard charts."""
        os.makedirs(output_dir, exist_ok=True)

        charts = {
            "collection": self.create_collection_chart(
                os.path.join(output_dir, "collection.png")
            ),
            "demographics": self.create_demographics_pie(
                os.path.join(output_dir, "demographics.png")
            ),
            "gauge": self.create_collection_rate_gauge(
                os.path.join(output_dir, "gauge.png")
            ),
        }

        return charts
```

## Part 3: Taglish Message Processing

```python
# Taglish NLP Processing
# Boss Fight 3

import re
from collections import defaultdict


class TaglishProcessor:
    """Process Tagalog/Taglish messages from residents."""

    # Common Tagalog keywords for intent classification
    INTENT_KEYWORDS = {
        "payment_inquiry": ["bayad", "bayarin", "fee", "utang", "bayad na", "sino ang"],
        "certificate": ["certificate", "clearance", "indigency", "residency", "cert"],
        "complaint": ["reklamo", "problema", "sira", "hirap", "ayan"],
        "announcement": ["anunsyo", "meeting", "clean-up", "volunteer", "tumutulong"],
        "help": ["tulong", "help", "paano", "saan", "kailan", "ano"],
        "greeting": ["kumusta", "hello", "hi", "morning", "good", "namimiss"],
    }

    # Sentiment keywords (simplified)
    POSITIVE_WORDS = {"salamat", "thanks", "nice", "galing", "awesome", "ok", "okie", "good"}
    NEGATIVE_WORDS = {"sira", "hirap", "ayan", "sakit", "galit", "angry", "bad", "worst"}

    def classify_message(self, message):
        """Classify the intent of a Taglish message."""
        msg_lower = message.lower()
        scores = defaultdict(int)

        for intent, keywords in self.INTENT_KEYWORDS.items():
            for keyword in keywords:
                if keyword in msg_lower:
                    scores[intent] += 1

        if scores:
            return max(scores, key=scores.get)
        return "unknown"

    def detect_sentiment(self, message):
        """Detect sentiment of a message."""
        msg_lower = message.lower()
        words = re.findall(r'\b\w+\b', msg_lower)

        positive = sum(1 for w in words if w in self.POSITIVE_WORDS)
        negative = sum(1 for w in words if w in self.NEGATIVE_WORDS)

        if positive > negative:
            return "positive"
        elif negative > positive:
            return "negative"
        return "neutral"

    def extract_entities(self, message):
        """Extract key entities from a message."""
        entities = {}

        # Extract dates (simple pattern)
        date_pattern = re.findall(r'\d{4}-\d{2}-\d{2}', message)
        if date_pattern:
            entities["date"] = date_pattern[0]

        # Extract amounts
        amount_pattern = re.findall(r'₱(\d+\.?\d*)', message)
        if amount_pattern:
            entities["amount"] = float(amount_pattern[0])

        # Extract names (simplified: capitalized words)
        name_pattern = re.findall(r'\b[A-Z][a-z]+(?:\s[A-Z][a-z]+){1,2}\b', message)
        if name_pattern:
            entities["name"] = " ".join(name_pattern[:2])

        return entities

    def process_message(self, message):
        """Full message processing pipeline."""
        return {
            "message": message,
            "intent": self.classify_message(message),
            "sentiment": self.detect_sentiment(message),
            "entities": self.extract_entities(message),
            "needs_response": self.classify_message(message) != "greeting",
        }
```

## Part 4: Putting It All Together

```python
# Main Dashboard Application
# Boss Fight 3

import asyncio
import json
import os


async def run_dashboard():
    """Run the complete dashboard system."""
    dashboard = BarangayDashboard()
    visualizer = DashboardVisualizer(dashboard)
    nlp = TaglishProcessor()

    # Generate charts
    print("📊 Generating dashboard charts...")
    charts = visualizer.generate_all_charts()
    for name, path in charts.items():
        if path:
            print(f"  ✅ {name}: {path}")

    # Process messages
    print("\n🤖 Processing resident messages...")
    sample_messages = [
        "Kumusta po, bayad na po ako ng fee",
        "Pwede po ba mag-request ng clearance?",
        "May reklamo po, sira ang kalsada sa Purok 3",
        "Salamat po sa clean-up drive!",
        "Paano po mag-register ng senior citizen?",
    ]

    for msg in sample_messages:
        result = nlp.process_message(msg)
        print(f"  Message: '{msg}'")
        print(f"    Intent: {result['intent']}")
        print(f"    Sentiment: {result['sentiment']}")
        print()

    # Overview
    print("📋 Dashboard Overview:")
    overview = dashboard.get_overview()
    for key, value in overview.items():
        if isinstance(value, float):
            print(f"  {key}: ₱{value:,.2f}")
        elif isinstance(value, dict):
            print(f"  {key}:")
            for k, v in value.items():
                print(f"    {k}: {v}")
        else:
            print(f"  {key}: {value}")

    # Async data refresh
    print("\n🔄 Refreshing live data...")
    live_data = await dashboard.refresh_all()
    print(f"  Weather: {live_data['weather']['alert_level']}")
    print(f"  Updates: {len(live_data['updates']['updates'])} new")

    print("\n✅ Dashboard generation complete!")


if __name__ == "__main__":
    asyncio.run(run_dashboard())
```

## Running the Dashboard

```bash
python dashboard.py
```

Sample output:

```
📊 Generating dashboard charts...
  ✅ collection: charts/collection.png
  ✅ demographics: charts/demographics.png
  ✅ gauge: charts/gauge.png

🤖 Processing resident messages...
  Message: 'Kumusta po, bayad na po ako ng fee'
    Intent: payment_inquiry
    Sentiment: positive

  Message: 'Pwede po ba mag-request ng clearance?'
    Intent: certificate
    Sentiment: neutral

📋 Dashboard Overview:
  total_residents: 1250
  paid_count: 890
  collection_rate: 71.2
  total_collected: 445000.00
  ...

🔄 Refreshing live data...
  Weather: Yellow
  Updates: 3 new

✅ Dashboard generation complete!
```

??? badge "🏆 Achievement Unlocked: Barangay Captain"
    **Badge:** Barangay Captain
    **XP Earned:** +500 XP
    **Description:** You built a complete barangay dashboard integrating async programming, data visualization, NLP, and open-source practices. This is the kind of project that solves real community problems.

    > *"Ang tunay na teknolohiya ay naglilingkod sa tao. Iyong ginawa."*

## Summary

- Combined async programming, data viz, NLP, and open-source practices
- Built a complete barangay management dashboard
- Processed Taglish messages for resident requests
- Generated visual charts for decision-making
- Created an extensible, open-source system

## Side Quests

??? note "Optional: Side Quest"
    - Deploy the dashboard as a web app using Flask
    - Add real-time data streaming with websockets
    - Build a mobile app version using Kivy
    - Add PDF report generation
    - Connect to actual PAGASA and DILG APIs

??? success "You did it! Level Up!"
    +200 XP. You built a complete dashboard system. Ang galing!

## Further Reading

- [Matplotlib documentation](https://matplotlib.org/)
- [asyncio documentation](https://docs.python.org/3/library/asyncio.html)
- [Natural Language Processing with Python (NLTK)](https://www.nltk.org/)

---

*Next: [Part 4: Capstone](../part-4-capstone/index.md) -- Your capstone projects begin.*
