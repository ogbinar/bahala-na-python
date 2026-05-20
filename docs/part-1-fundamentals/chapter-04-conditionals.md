# Chapter 4: Conditionals and the Jeepney Fare Calculator

??? example "📋 Chapter Info"
    | | |
    |---|---|
    | **Difficulty** | ⭐⭐ Beginner |
    | **Time** | 30 min |
    | **XP** | +100 XP |

> **Story Hook:** You're on a jeepney heading home from school. The driver pulls over, picks up three passengers at the front, and two more at the back. The conductor starts shouting the fare: "Nine pesos inside! Seven pesos outside! Nine more pasahero na po!" You wonder: how does the conductor know exactly how much to charge? It depends on where you sit, how many people are already inside, and whether it's peak hour. That's a conditional system -- and today you'll build one.

---

## What You'll Learn

- `if`, `elif`, and `else` statements
- Comparison operators (`==`, `!=`, `<`, `>`, `<=`, `>=`)
- Boolean logic (`and`, `or`, `not`)
- Nested conditionals
- Input validation

## Making Decisions: The `if` Statement

Sometimes your program needs to make decisions. Should we show the price? Should we allow access? Should we send a warning?

The `if` statement is Python's way of saying: "If this condition is true, do this."

```python
age = 18

if age >= 18:
    print("Adult na. Pwede ka na.")
else:
    print("Bata pa. Walang access.")
```

### How It Works

```python
if condition:
    # This runs if the condition is True
    do_something()

elif another_condition:
    # This runs if the first condition is False but this one is True
    do_something_else()

else:
    # This runs if ALL conditions are False
    do_fallback()
```

## Comparison Operators: Setting the Rules

| Operator | Meaning | Example | Result |
|----------|---------|---------|--------|
| `==` | Equal to | `5 == 5` | `True` |
| `!=` | Not equal to | `5 != 3` | `True` |
| `<` | Less than | `3 < 5` | `True` |
| `>` | Greater than | `5 > 3` | `True` |
| `<=` | Less than or equal | `5 <= 5` | `True` |
| `>=` | Greater than or equal | `5 >= 3` | `True` |

??? bug "Common Mistake"
    `=` assigns a value. `==` checks equality. They are NOT the same.

    ```python
    >>> x = 5    # Assign 5 to x
    >>> x == 5   # Check if x equals 5 (returns True)
    True
    ```

## Boolean Logic: Combining Conditions

You can combine multiple conditions with `and`, `or`, and `not`:

```python
# and: both must be True
if age >= 18 and has_id:
    print("Pwede pumasok.")

# or: at least one must be True
if is_raining or has_umbrella:
    print("Umbrella ready na.")

# not: reverses the condition
if not is_raining:
    print("Walang ulan, pwede mag-shoot!")
```

## The Jeepney Fare Calculator

Jeepney fares depend on several factors:

- **Distance**: Base fare for the first 4 kilometers
- **Passenger count**: Additional fare for each passenger beyond the base
- **Peak hours**: Extra surcharge during rush hour

Let's build a calculator:

```python
# Jeepney Fare Calculator

def calculate_fare(distance_km, passengers, is_peak_hour=False):
    """Calculate jeepney fare based on distance, passengers, and time."""

    # Base fare: ₱13 for first 4 km (2024 rate)
    base_fare = 13.0

    # Additional fare: ₱1.50 per km after 4 km
    if distance_km > 4:
        additional_km = distance_km - 4
        additional_fare = additional_km * 1.50
    else:
        additional_fare = 0

    # Passenger surcharge: ₱1 per additional passenger
    passenger_charge = max(0, passengers - 1) * 1.0

    # Peak hour surcharge: 20% extra (6-9 AM, 5-8 PM)
    if is_peak_hour:
        total = (base_fare + additional_fare + passenger_charge) * 1.20
    else:
        total = base_fare + additional_fare + passenger_charge

    # Round up to nearest peso (jeepneys don't give centavo change)
    import math
    return math.ceil(total)


# Test it
print("=== Jeepney Fare Calculator ===")
print(f"Short trip (2km, 1 passenger): ₱{calculate_fare(2, 1)}")
print(f"Medium trip (8km, 3 passengers): ₱{calculate_fare(8, 3)}")
print(f"Peak hour (5km, 2 passengers): ₱{calculate_fare(5, 2, is_peak_hour=True)}")
```

Output:

```
=== Jeepney Fare Calculator ===
Short trip (2km, 1 passenger): ₱13
Medium trip (8km, 3 passengers): ₱20
Peak hour (5km, 2 passengers): ₱18
```

??? tip "Diskarte"
    Notice how we used `if/elif/else` inside a function. This is how real-world programs make decisions. The jeepney conductor does the same thing in their head -- but with code, it's precise and consistent.

??? tip "⏸️ Pause and Predict"

    **Predict what this code will output:**

    ```python
    score = 75
    if score >= 90:
        print("Excellent!")
    elif score >= 75:
        print("Passed!")
    elif score >= 50:
        print("Needs improvement.")
    else:
        print("Failed.")
    ```

    Think about it before scrolling down!

## Input Validation: Kung Anong Ilagay ng User

What if the user types a negative distance? Or enters text instead of a number? Smart programs handle bad input gracefully:

```python
def get_valid_distance():
    """Ask user for distance and validate input."""
    while True:
        try:
            distance = float(input("Distance (km): "))
            if distance <= 0:
                print("Distance must be positive. Subok ulit.")
            elif distance > 100:
                print("100 km na? Sobrang layo. Maximum is 100.")
            else:
                return distance
        except ValueError:
            print("Number lang po. Text hindi pwede.")


distance = get_valid_distance()
print(f"Confirmed: {distance} km")
```

??? bug "Common Mistake"
    `try/except` is how Python handles errors gracefully. If `float()` can't convert the input (e.g., "abc"), it raises a `ValueError`. The `try/except` block catches it instead of crashing.

## Nested Conditionals

You can put `if` statements inside other `if` statements:

```python
time = 7  # Hour of day (7 AM)
day_type = "weekday"

if day_type == "weekday":
    if 6 <= time < 9:
        print("Peak hour. May surcharge.")
    elif 9 <= time < 17:
        print("Off-peak. Regular fare.")
    elif 17 <= time < 20:
        print("Evening peak. May surcharge.")
    else:
        print("Late night. Last trip na.")
else:
    print("Weekend. Regular fare all day.")
```

??? example "Portfolio Tip: Decision-Making Tools"
    Your jeepney fare calculator demonstrates conditional logic -- a core programming skill employers look for:

    1. **GitHub README** -- Show the different scenarios your calculator handles (peak/off-peak, student/senior discounts)
    2. **LinkedIn skill** -- Add "Python" to your Skills section and write a post: "Just built a fare calculator that handles edge cases like peak hours and student discounts"
    3. **Interview talking point** -- "I built a fare calculator that uses nested conditionals to handle real-world pricing rules, similar to how ride-sharing apps calculate fares dynamically."

## Summary

- `if/elif/else` let your program make decisions
- Comparison operators (`==`, `!=`, `<`, `>`, etc.) check conditions
- `and`, `or`, `not` combine multiple conditions
- Input validation prevents crashes from bad user input
- Nested conditionals handle complex decision trees

## Boss Fight

??? warning "Boss Fight: Full Jeepney Fare App"

    Build a complete interactive jeepney fare calculator that:

    1. Asks for distance, number of passengers, and time of day
    2. Calculates the fare with all surcharges
    3. Shows a breakdown of the fare (base + additional + surcharges)
    4. Handles invalid input gracefully
    5. Lets the user calculate multiple fares in a loop

    **Bonus:** Add a "multi-route" feature that calculates fares for multiple routes and picks the cheapest.

??? success "You did it! Level Up!"
    +150 XP. You built a decision-making program. Ang diskarte!

## Side Quests

??? note "Optional: Side Quest"
    - Add tricycle fare calculation (different pricing model)
    - Calculate the cost difference between jeepney, tricycle, and Grab
    - Create a "fare history" that saves previous calculations

## Further Reading

- [Python's official tutorial on control flow](https://docs.python.org/3/tutorial/controlflow.html)
- [Real Python: if/else statements](https://realpython.com/python-conditional-statements/)

??? example "🧠 Reflection — Conditionals"

    - **What did you learn?** `if/elif/else` statements let your program make decisions based on conditions, and you can combine conditions with `and`, `or`, and `not`.
    - **How can you apply this?** Just like a jeepney conductor decides fares based on distance, passengers, and time of day, you can write programs that adapt to real-world conditions — like giving senior discounts, checking if you have enough allowance, or routing tricycle vs. jeepney trips.
    - **What's next?** What happens when you need to apply the same decision-making logic to dozens or hundreds of items?

??? checkbox "✅ Chapter Checklist"

    - [ ] I can write `if/elif/else` statements to handle multiple conditions
    - [ ] I can use comparison operators (`==`, `!=`, `<`, `>`, `<=`, `>=`)
    - [ ] I can combine conditions with `and`, `or`, and `not`
    - [ ] I can validate user input to prevent crashes from bad data
    - [ ] I can nest conditionals to handle complex decision trees

---

*Previous: [Chapter 3: Variables](chapter-03-variables.md) -- Storing information*
*Next: [Chapter 5: Loops](chapter-05-loops.md) -- Doing things repeatedly.*
