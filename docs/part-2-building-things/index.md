# Part 2: Building Things

> You've mastered the fundamentals. Now it's time to build real things -- tools that connect to the internet, process text, handle errors gracefully, and make your life easier.

---

## What You'll Learn

| Chapter | Topic | Project |
|---------|-------|---------|
| 9 | Classes & OOP | Allowance Manager |
| 10 | Strings & Text | Tagalog Typing Game |
| 11 | APIs & Web Requests | OFW Remittance Tracker |
| 12 | Web Scraping | Shopee Price Tracker |
| 13 | Errors & Debugging | Debugging Challenge |
| 14 | Boss Fight 2 | Midpoint Boss Battle |

## How This Part Works

Part 2 is where things get exciting. You'll:

- Write **classes** to model real-world objects
- Connect to **live APIs** for real-time data
- **Scrape websites** for information
- Handle errors like a professional
- Build a **midpoint Boss Fight** that combines all these skills

## The Allowance Manager Arc

This part introduces **object-oriented programming (OOP)** through the Allowance Manager -- a class-based system that models a student's financial life:

```python
# Chapter 9: Introduction to classes
budget = Budget(500)  # ₱500 weekly allowance
budget.add_expense("pamasahe", 30)
budget.add_expense("kain", 80)
budget.check_remaining()

# Chapter 11: Connect to real data
tracker = OFWTracker()
tracker.fetch_exchange_rate("USD")
tracker.track_remittance(500)
```

## XP Rewards

| Chapter | XP |
|---------|-----|
| Ch 9: Classes | 100 XP + 25 XP per exercise |
| Ch 10: Strings | 100 XP + 25 XP per exercise |
| Ch 11: APIs | 100 XP + 25 XP per exercise |
| Ch 12: Scraping | 100 XP + 25 XP per exercise |
| Ch 13: Errors | 100 XP + 25 XP per exercise |
| Ch 14: Boss Fight | 500 XP (Boss Fight) |

*Let's build.*

---

*Next: [Chapter 9: Classes & OOP](chapter-09-classes.md) -- Modeling the real world with code.*
