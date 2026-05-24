# Part 2: Building Things

> You've mastered the fundamentals. Now it's time to build real things -- tools that connect to the internet, process text, handle errors gracefully, and make your life easier.

---

## What You'll Learn

| Chapter | Topic | Project |
|---------|-------|---------|
| 11 | Classes & OOP | Allowance Manager |
| 12 | Strings & Text | Tagalog Typing Game |
| 13 | APIs & Web Requests | OFW Remittance Tracker |
| 14 | Web Scraping | Shopee Price Tracker |
| 15 | Errors & Debugging | Debugging Challenge |
| 16 | Boss Fight 2 | Midpoint Boss Battle |

## How This Part Works

Part 2 is where things get exciting. You'll:

- Write **classes** to model real-world objects
- Connect to **live APIs** for real-time data
- **Scrape websites** for information
- Handle errors like a professional
- Build a **midpoint Boss Fight** that combines all these skills

## The Allowance Manager Arc

Part 2 starts after the fundamentals boss fight. You already built a working store system with plain data and functions. That approach works well for small tools. Now the book shifts into **object-oriented programming (OOP)** so you can bundle related data and behavior together as your projects get bigger:

```python
# Chapter 11: Introduction to classes
budget = Budget(500)  # ₱500 weekly allowance
budget.add_expense("pamasahe", 30)
budget.add_expense("kain", 80)
budget.check_remaining()

# Chapter 13: Connect to real data
tracker = OFWTracker()
tracker.fetch_exchange_rate("USD")
tracker.track_remittance(500)
```

## XP Rewards

| Chapter | XP |
|---------|-----|
| Ch 11: Classes | 100 XP + 25 XP per exercise |
| Ch 12: Strings | 100 XP + 25 XP per exercise |
| Ch 13: APIs | 100 XP + 25 XP per exercise |
| Ch 14: Scraping | 100 XP + 25 XP per exercise |
| Ch 15: Errors | 100 XP + 25 XP per exercise |
| Ch 16: Boss Fight | 500 XP (Boss Fight) |

*Let's build.*

---

*Previous: [Boss Fight 1](../part-1-fundamentals/chapter-10-boss-fight-1.md) -- First big project*
*Next: [Chapter 11: Classes & OOP](chapter-11-classes.md) -- Modeling the real world with code.*
