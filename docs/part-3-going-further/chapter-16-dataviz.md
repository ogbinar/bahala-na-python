# Chapter 16: Data Visualization and the Barangay Dashboard

??? example "📋 Chapter Info"
    | | |
    |---|---|
    | **Difficulty** | ⭐⭐⭐ Advanced |
    | **Time** | 40 min |
    | **XP** | +100 XP |

> **Story Hook:** Your barangay captain wants to know how many families received aid during the last typhoon. The data is in a spreadsheet -- 500 rows, 20 columns. She asks you to "make something visual" so she can present it at the next meeting. You think: "I can do that with Python." So you build a dashboard that turns raw data into beautiful charts.

---

## What You'll Learn

- Creating charts with matplotlib
- Working with pandas for data analysis
- Creating bar charts, line charts, pie charts, and scatter plots
- Building a dashboard with multiple charts
- Saving and sharing visualizations

## Why Visualize Data?

Numbers on a spreadsheet are hard to understand. A chart tells a story at a glance:

- Bar charts: Compare categories
- Line charts: Show trends over time
- Pie charts: Show percentages of a whole
- Scatter plots: Show relationships between variables

## Installing the Tools

```bash
pip install matplotlib pandas numpy
```

??? note "💻 Low-Spec Laptop?"

    Data visualization can be heavy on older machines:

    - **Smaller datasets**: Start with datasets under 1,000 rows. The concepts are the same whether you're charting 10 rows or 1 million — smaller data just runs faster.
    - **Close other browser tabs**: Each tab eats RAM. Close what you don't need before running matplotlib or pandas. Your charts will render much smoother.
    - **Lower resolution for practice**: Use `plt.savefig("chart.png", dpi=100)` instead of the default higher DPI. The chart looks fine on screen and uses less memory to generate.
    - **Pro tip**: If matplotlib windows are slow to pop up, use `%matplotlib inline` in Jupyter or just save directly to files with `plt.savefig()` and skip the interactive window entirely.

## Your First Chart: Bar Chart

```python
import matplotlib.pyplot as plt

# Barangay aid distribution
barangays = ["San Antonio", "Santa Rosa", "Santa Cruz", "Sagrada Familia", "San Jose"]
families_aided = [120, 85, 200, 150, 95]

plt.figure(figsize=(10, 6))
bars = plt.bar(barangays, families_aided, color=["#4CAF50", "#2196F3", "#FF9800", "#9C27B0", "#F44336"])
plt.title("Families Aided by Barangay (Typhoon Response)")
plt.xlabel("Barangay")
plt.ylabel("Number of Families")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig("aid_chart.png", dpi=150)
plt.show()
```

## Pandas: Data Analysis Made Easy

**pandas** is Python's data analysis library. It's like Excel but programmable:

```python
import pandas as pd

# Create a DataFrame (like a spreadsheet in Python)
data = {
    "name": ["Juan", "Maria", "Pedro", "Ana"],
    "age": [25, 30, 22, 28],
    "income": [35000, 50000, 25000, 45000],
    "department": ["IT", "HR", "IT", "Finance"],
}

df = pd.DataFrame(data)
print(df)
print(df.describe())  # Statistical summary
print(df[df["department"] == "IT"])  # Filter rows
```

## Building a Barangay Dashboard

Let's build a complete dashboard:

```python
# Barangay Dashboard
# Chapter 16

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime, timedelta


class BarangayDashboard:
    """Dashboard for barangay data visualization."""

    def __init__(self, barangay_name="Barangay San Antonio"):
        self.barangay_name = barangay_name
        self.aid_records = []
        self.population_data = {}

    def add_aid_record(self, date, families, amount, type="cash"):
        """Add a disaster aid record."""
        self.aid_records.append({
            "date": date,
            "families": families,
            "amount": amount,
            "type": type,
        })

    def add_population(self, age_group, count):
        """Add population data by age group."""
        self.population_data[age_group] = count

    def create_aid_chart(self, filename="aid_chart.png"):
        """Create a bar chart of aid distribution."""
        if not self.aid_records:
            print("No aid records to display.")
            return

        df = pd.DataFrame(self.aid_records)
        df["date"] = pd.to_datetime(df["date"])

        # Group by date
        summary = df.groupby("date").agg(
            total_families=("families", "sum"),
            total_amount=("amount", "sum"),
        ).reset_index()

        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10))

        # Aid by families
        ax1.bar(summary["date"].dt.strftime("%m/%d"), summary["total_families"],
                color="#4CAF50")
        ax1.set_title(f"{self.barangay_name} -- Aid Distribution (Families)")
        ax1.set_ylabel("Families")
        ax1.tick_params(axis="x", rotation=45)

        # Aid by amount
        ax2.bar(summary["date"].dt.strftime("%m/%d"), summary["total_amount"] / 1000,
                color="#2196F3")
        ax2.set_title(f"{self.barangay_name} -- Aid Distribution (₱ in thousands)")
        ax2.set_ylabel("Amount (₱000)")
        ax2.tick_params(axis="x", rotation=45)

        plt.tight_layout()
        plt.savefig(filename, dpi=150)
        plt.show()
        print(f"Chart saved to {filename}")

    def create_population_chart(self, filename="population_chart.png"):
        """Create a population pyramid-style chart."""
        if not self.population_data:
            print("No population data.")
            return

        groups = list(self.population_data.keys())
        counts = list(self.population_data.values())

        colors = plt.cm.viridis(np.linspace(0.2, 0.8, len(groups)))

        plt.figure(figsize=(10, 6))
        plt.barh(groups, counts, color=colors)
        plt.title(f"{self.barangay_name} -- Population by Age Group")
        plt.xlabel("Population")
        plt.tight_layout()
        plt.savefig(filename, dpi=150)
        plt.show()

    def create_summary_report(self, filename="report.png"):
        """Create a complete summary dashboard."""
        fig, axes = plt.subplots(2, 2, figsize=(14, 10))

        # 1. Aid trend (line chart)
        if self.aid_records:
            df = pd.DataFrame(self.aid_records)
            df["date"] = pd.to_datetime(df["date"])
            df = df.sort_values("date")
            df["cumulative"] = df["families"].cumsum()

            axes[0, 0].plot(df["date"].dt.strftime("%m/%d"), df["cumulative"],
                            marker="o", color="#4CAF50")
            axes[0, 0].set_title("Cumulative Families Aided")
            axes[0, 0].tick_params(axis="x", rotation=45)

        # 2. Population (bar chart)
        if self.population_data:
            groups = list(self.population_data.keys())
            counts = list(self.population_data.values())
            axes[0, 1].barh(groups, counts, color="#2196F3")
            axes[0, 1].set_title("Population by Age Group")

        # 3. Aid by type (pie chart)
        if self.aid_records:
            df_pie = pd.DataFrame(self.aid_records)
            type_summary = df_pie.groupby("type")["amount"].sum()
            axes[1, 0].pie(type_summary.values, labels=type_summary.index,
                          autopct="%1.1f%%", colors=["#FF9800", "#9C27B0", "#4CAF50"])
            axes[1, 0].set_title("Aid by Type")

        # 4. Statistics (text)
        if self.aid_records:
            total_families = df["families"].sum()
            total_amount = df["amount"].sum()
            stats_text = (
                f"Total Families Aided: {total_families}\n"
                f"Total Amount: ₱{total_amount:,.2f}\n"
                f"Number of Events: {len(df)}\n"
                f"Avg per Event: {total_families/len(df):.0f} families"
            )
            axes[1, 1].text(0.1, 0.5, stats_text, fontsize=12,
                           fontfamily="monospace",
                           bbox=dict(boxstyle="round", facecolor="wheat", alpha=0.5))
            axes[1, 1].set_title("Summary Statistics")
            axes[1, 1].axis("off")

        plt.suptitle(f"{self.barangay_name} -- Dashboard", fontsize=16, fontweight="bold")
        plt.tight_layout()
        plt.savefig(filename, dpi=150)
        plt.show()
        print(f"Dashboard saved to {filename}")


# Usage
dashboard = BarangayDashboard("Barangay San Antonio")

# Add aid records
dashboard.add_aid_record("2024-01-15", 120, 60000, "cash")
dashboard.add_aid_record("2024-01-15", 85, 42500, "goods")
dashboard.add_aid_record("2024-03-01", 200, 100000, "cash")
dashboard.add_aid_record("2024-03-01", 150, 75000, "goods")
dashboard.add_aid_record("2024-06-10", 95, 47500, "cash")

# Add population data
dashboard.add_population("0-14", 2500)
dashboard.add_population("15-24", 1800)
dashboard.add_population("25-44", 3200)
dashboard.add_population("45-64", 1500)
dashboard.add_population("65+", 800)

# Create charts
dashboard.create_aid_chart()
dashboard.create_population_chart()
dashboard.create_summary_report()
```

??? example "Portfolio Tip: Data Visualization"
    Your barangay data visualization project shows you can turn raw data into visual stories -- a skill in high demand:

    1. **GitHub README** -- Include the generated charts as images in your README. Show before/after: raw data vs. visualized data.
    2. **LinkedIn** -- Add "Data Visualization", "matplotlib", and "pandas" to your skills. Post: "Visualized barangay data to create charts showing aid distribution and population trends. Data tells stories!"
    3. **Interview talking point** -- "I built a data visualization dashboard for barangay data using matplotlib and pandas. I created bar charts for comparisons, pie charts for distributions, and line charts for trends. This is similar to how data analysts create reports for decision-makers."

## Summary

- matplotlib creates charts and graphs
- pandas handles data analysis like Excel
- Bar charts compare categories
- Line charts show trends
- Pie charts show proportions
- Dashboards combine multiple views

## Boss Fight

??? warning "Boss Fight: Complete Barangay Dashboard"

    Extend the dashboard with:

    1. Interactive charts (using plotly)
    2. Export to PDF report
    3. Real-time data updates
    4. Multi-barangay comparison
    5. Historical trend analysis

    **Hint:** Use `plotly` for interactive charts that work in browsers.

??? success "You did it! Level Up!"
    +150 XP. You built data visualizations. Ang galing!

## Side Quests

### Mini-Project: Typhoon Impact Visualizer

??? side-quest "🎯 Mini-Project: Typhoon Impact Visualizer"
    **Type:** Research Quest | **Difficulty:** Hard | **XP:** +50 XP

    Visualize typhoon data to understand weather patterns in the Philippines:

    ```python
    # typhoon_viz.py
    # Your task:
    # 1. Load typhoon data (PAGASA or NOAA)
    # 2. Create a map showing typhoon paths
    # 3. Plot wind speed over time
    # 4. Add affected population estimates
    ```

### Mini-Project: Personal Budget Dashboard

??? side-quest "🎯 Mini-Project: Personal Budget Dashboard"
    **Type:** Creative Quest | **Difficulty:** Medium | **XP:** +25 XP

    Create charts that show your spending habits:

    ```python
    # budget_dashboard.py
    # Your task:
    # 1. Load your expense data (CSV or JSON)
    # 2. Create pie chart of spending by category
    # 3. Create bar chart of monthly totals
    # 4. Create line chart of spending trends
    ```

??? note "Optional: Side Quest"
    - Create a "typhoon tracker" that visualizes storm paths
    - Build a "budget tracker" with interactive charts
    - Add a "health metrics" dashboard for barangay health records

## Further Reading

- [matplotlib documentation](https://matplotlib.org/stable/users/explain/index.html)
- [pandas documentation](https://pandas.pydata.org/docs/)

---

??? example "🧠 Reflection — Data Visualization and the Barangay Dashboard"

    - **What did you learn?** matplotlib and pandas turn raw numbers into visual stories that anyone can understand at a glance.
    - **How can you apply this?** Help your barangay create visual reports for meetings, or track your family's finances with charts instead of spreadsheets.
    - **What's next?** How could you make your charts interactive so barangay officials can click and explore the data themselves?

??? checkbox "✅ Chapter Checklist"

    - [ ] Create a bar chart, line chart, and pie chart with matplotlib
    - [ ] Use pandas to load and analyze data from a DataFrame
    - [ ] Build a multi-chart dashboard combining different visualizations
    - [ ] Save charts as image files for sharing and reporting
    - [ ] Interpret what a chart is telling you about real-world data

---

*Previous: [Chapter 15: Discord Bots](chapter-15-discord-bots.md) -- Building bots for your barkada*
*Next: [Chapter 17: NLP](chapter-17-nlp.md) -- Understanding language.*
