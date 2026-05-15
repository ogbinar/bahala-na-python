# Chapter 9: Classes and the Allowance Manager

??? example "📋 Chapter Info"
    | | |
    |---|---|
    | **Difficulty** | ⭐⭐ Intermediate |
    | **Time** | 35 min |
    | **XP** | +100 XP |

> **Story Hook:** You receive ₱500 every Monday as allowance. By Wednesday, you've already spent ₱380 on "small things" -- ₱15 for pamasahe three times, ₱50 for merienda, ₱80 for photocopy, ₱30 for load. You check your wallet: ₱120 left for four more days. You think: "I need a system. Not just a notebook -- something that tracks everything automatically and tells me when I'm overspending." So you create a class.

---

## What You'll Learn

- What classes and objects are
- Defining classes with `class`
- The `__init__` method (constructor)
- Instance methods and attributes
- `self`: the bridge between objects and their data
- Encapsulation: keeping data safe

## What Is a Class?

A **class** is a blueprint for creating objects. Think of it like a cookie cutter:

- The **class** is the cutter (the blueprint)
- The **objects** are the cookies (the actual things)

??? tip "⏸️ Pause and Predict"

    **Before looking at the code: if a class is like a blueprint, what do you think `self` represents in the actual building?**

    Take 30 seconds to think about your answer before reading on. This is how you build real understanding!

```python
# Class definition
class Student:
    def __init__(self, name, gwa):
        self.name = name
        self.gwa = gwa

    def is_deans_list(self):
        return self.gwa <= 1.75

# Creating objects from the class
juan = Student("Juan", 1.5)
maria = Student("Maria", 2.0)

print(juan.name)  # Juan
print(juan.is_deans_list())  # True
print(maria.is_deans_list())  # False
```

## The `__init__` Method

`__init__` is called when you create a new object. It sets up the object's initial state:

```python
class Budget:
    def __init__(self, allowance):
        self.allowance = allowance
        self.expenses = []
        self.total_spent = 0

    def add_expense(self, category, amount):
        self.expenses.append({"category": category, "amount": amount})
        self.total_spent += amount

    def remaining(self):
        return self.allowance - self.total_spent
```

## `self`: The Key to Classes

`self` refers to the current object. It's how Python knows which object's data to use:

```python
class Budget:
    def __init__(self, allowance):
        self.allowance = allowance  # This object's allowance

    def add_expense(self, amount):
        self.total_spent += amount  # Update this object's spending

# Two different Budget objects
budget1 = Budget(500)
budget2 = Budget(300)

budget1.add_expense(50)  # Updates budget1's total_spent
budget2.add_expense(100)  # Updates budget2's total_spent
```

??? tip "Diskarte"
    Think of `self` like your name. When someone says "Juan, pass the salt," Juan knows they're being addressed. Similarly, `self` tells Python which object the method belongs to.

## Building the Allowance Manager

Let's build a complete allowance management system using classes:

```python
# Allowance Manager
# Chapter 9

from datetime import datetime, date


class Expense:
    """Represents a single expense."""

    def __init__(self, category, amount, description=""):
        self.category = category
        self.amount = amount
        self.description = description
        self.date = datetime.now()

    def __str__(self):
        return f"₱{self.amount:.2f} - {self.category}"


class Budget:
    """Manages a weekly allowance budget."""

    def __init__(self, allowance, week_start=None):
        self.allowance = allowance
        self.week_start = week_start or date.today()
        self.expenses = []

    def add_expense(self, category, amount, description=""):
        """Add an expense and return the remaining budget."""
        expense = Expense(category, amount, description)
        self.expenses.append(expense)
        return self.remaining()

    def remaining(self):
        """Calculate remaining budget."""
        total_spent = sum(e.amount for e in self.expenses)
        return self.allowance - total_spent

    def spent(self):
        """Calculate total spent."""
        return sum(e.amount for e in self.expenses)

    def category_totals(self):
        """Group expenses by category."""
        totals = {}
        for e in self.expenses:
            if e.category not in totals:
                totals[e.category] = 0
            totals[e.category] += e.amount
        return totals

    def is_over_budget(self):
        """Check if spending exceeds allowance."""
        return self.remaining() < 0

    def daily_budget(self):
        """Calculate how much you can spend per day."""
        today = date.today()
        days_left = (self.week_start.replace(day=self.week_start.day + 7) - today).days
        if days_left <= 0:
            days_left = 1
        return self.remaining() / days_left

    def summary(self):
        """Print a budget summary."""
        print(f"\n=== Budget Summary ===")
        print(f"Allowance: ₱{self.allowance:.2f}")
        print(f"Spent: ₱{self.spent():.2f}")
        print(f"Remaining: ₱{self.remaining():.2f}")

        if self.is_over_budget():
            print("⚠️  OVER BUDGET! Diskarte na!")

        print(f"\nDaily budget: ₱{self.daily_budget():.2f}/day")

        print(f"\nBy category:")
        for cat, total in sorted(self.category_totals().items()):
            pct = (total / self.allowance) * 100
            print(f"  {cat}: ₱{total:.2f} ({pct:.0f}%)")

        print(f"\nAll expenses:")
        for e in self.expenses:
            print(f"  {e.date.strftime('%m/%d')} - {e}")
            if e.description:
                print(f"    {e.description}")


# Usage
budget = Budget(500)

budget.add_expense("pamasahe", 15, "UD to school")
budget.add_expense("kain", 50, "Jollibee meal")
budget.add_expense("pamasahe", 15, "School to home")
budget.add_expense("photocopy", 30, "20 pages")
budget.add_expense("load", 50, "Smart load")
budget.add_expense("kain", 80, "Merienda with barkada")

budget.summary()
```

Output:

```
=== Budget Summary ===
Allowance: ₱500.00
Spent: ₱240.00
Remaining: ₱260.00

Daily budget: ₱52.00/day

By category:
  kain: ₱130.00 (26%)
  load: ₱50.00 (10%)
  pamasahe: ₱30.00 (6%)
  photocopy: ₱30.00 (6%)

All expenses:
  05/13 - ₱15.00 - pamasahe
    UD to school
  05/13 - ₱50.00 - kain
    Jollibee meal
  05/13 - ₱15.00 - pamasahe
    School to home
  05/13 - ₱30.00 - photocopy
    20 pages
  05/13 - ₱50.00 - load
    Smart load
  05/13 - ₱80.00 - kain
    Merienda with barkada
```

## Inheritance: Classes That Build on Classes

Sometimes you want a class that's similar to another but with extra features. That's **inheritance**:

```python
class Student:
    def __init__(self, name, id_number):
        self.name = name
        self.id_number = id_number

    def introduce(self):
        return f"Hi, I'm {self.name} (ID: {self.id_number})"


class GraduateStudent(Student):
    def __init__(self, name, id_number, thesis_topic):
        super().__init__(name, id_number)  # Call parent's __init__
        self.thesis_topic = thesis_topic

    def introduce(self):
        base = super().introduce()
        return f"{base}. Thesis: {self.thesis_topic}"
```

??? tip "Diskarte"
    `super()` calls the parent class. It's like saying "do everything the parent does, then add my stuff on top."

??? example "Portfolio Tip: OOP Skills"
    Your allowance manager using classes demonstrates Object-Oriented Programming -- one of the most requested skills in job postings:

    1. **GitHub README** -- Include a class diagram (even a simple ASCII one) to show your understanding of object relationships
    2. **LinkedIn** -- Add "Object-Oriented Programming" to your skills. Post: "Just learned OOP in Python by building an allowance manager with inheritance!"
    3. **Interview talking point** -- "I built an allowance management system using classes and inheritance. The Student class inherits from Person, which I think shows I understand code reuse and hierarchical data modeling."

## Summary

- Classes are blueprints for creating objects
- `__init__` sets up the object when it's created
- `self` refers to the current object's data
- Methods are functions that belong to a class
- Inheritance lets classes build on other classes

## Boss Fight

??? warning "Boss Fight: Complete Budget Manager"

    Extend the Budget class with:

    1. A `Savings` subclass that tracks savings goals
    2. A `WeeklyBudget` class that manages a full week of budgets
    3. Expense categories with spending limits
    4. Alerts when any category reaches 80% of its limit
    5. A "recommendation" method that suggests where to cut spending

    **Hint:** Use the `category_totals()` method to identify overspending.

??? success "You did it! Level Up!"
    +150 XP. You built classes that model real-world objects. Ang galing!

## Side Quests

??? note "Optional: Side Quest"
    - Add a GUI using tkinter for the budget manager
    - Create a "spending streak" feature that tracks consecutive days under budget
    - Build a "budget comparison" tool that shows this week vs. last week

## Further Reading

- [Python's official tutorial on classes](https://docs.python.org/3/tutorial/classes.html)
- [Real Python: OOP in Python](https://realpython.com/python3-object-oriented-programming/)

---

*Next: [Chapter 10: Strings](chapter-10-strings.md) -- Working with text.*

---

??? example "🧠 Reflection — Classes and Objects"

    - **What did you learn?** You learned how classes serve as blueprints for creating objects, using `__init__` to set up data and `self` to connect methods with their object's attributes.
    - **How can you apply this?** You can model real-world things as classes: a `Student` for tracking grades, an `OFW` for managing remittance records, or a `TricycleDriver` for computing daily earnings.
    - **What's next?** How do classes communicate with each other, and when should you use inheritance to share behavior between related classes?

??? checkbox "✅ Chapter Checklist"

    - [ ] I understand the difference between a class (blueprint) and an object (instance)
    - [ ] I can define a class with an `__init__` method and instance attributes
    - [ ] I know how `self` connects methods to an object's data
    - [ ] I can write instance methods that operate on an object's attributes
    - [ ] I built the Allowance Manager project using classes
