# Chapter 7: Files and the Filipino Recipe Organizer

> **Story Hook:** Your Lola has been cooking adobo for 40 years. No measurements, no recipes -- just "sapat na asin" (enough salt) and "hanggang luto na" (cook until done). You ask her for her secret adobo recipe, and she points to a small notebook on the kitchen shelf. The pages are stained with soy sauce and cooking oil. You take a photo, but then you think: "Why not digitize Lola's recipes? Let's make a searchable recipe database."

---

## What You'll Learn

- Reading from and writing to files
- CSV format for structured data
- JSON format for flexible data storage
- File handling with `with` statements
- Basic data persistence

## Why Save Data?

So far, all our data disappears when the program ends. Variables live only in memory. But what if you want your sari-sari store inventory to still be there when you restart the program? Or your budget tracker to remember last week's numbers?

**Files** let you save data permanently. When your program writes to a file, the data survives even after the program closes.

## The `with` Statement: Safe File Handling

The `with` statement automatically closes files when you're done:

```python
# Writing to a file
with open("inventory.txt", "w") as file:
    file.write("laundry soap: 10\n")
    file.write("cigarettes: 50\n")
    file.write("candy: 25\n")

# Reading from a file
with open("inventory.txt", "r") as file:
    content = file.read()
    print(content)
```

??? tip "Diskarte"
    Always use `with` when working with files. It's Python's way of saying "I'll close this file for you when you're done." No need to remember `file.close()`.

## File Modes

| Mode | Meaning | Creates file? |
|------|---------|---------------|
| `"r"` | Read (default) | No |
| `"w"` | Write (overwrites) | Yes |
| `"a"` | Append (adds to end) | Yes |
| `"r+"` | Read and write | No |

## CSV: Tables in Text Files

**CSV** (Comma-Separated Values) stores tabular data in plain text. Each line is a row, and commas separate columns:

```csv
item,quantity,price
laundry soap,10,15.00
cigarettes,50,5.00
candy,25,3.00
instant noodles,30,8.00
```

### Reading CSV Files

```python
import csv

# Read inventory from CSV
inventory = {}
with open("inventory.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        inventory[row["item"]] = {
            "qty": int(row["quantity"]),
            "price": float(row["price"]),
        }

for item, data in inventory.items():
    print(f"{item}: {data['qty']} @ ₱{data['price']}")
```

### Writing CSV Files

```python
import csv

data = [
    {"item": "adobo", "servings": 4, "prep_min": 30},
    {"item": "sinigang", "servings": 6, "prep_min": 45},
    {"item": "kare-kare", "servings": 4, "prep_min": 60},
]

with open("recipes.csv", "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["item", "servings", "prep_min"])
    writer.writeheader()
    writer.writerows(data)
```

## JSON: Flexible Data Storage

**JSON** (JavaScript Object Notation) is great for nested, hierarchical data. It's the same format used by APIs:

```json
{
    "store_name": "Lola's Sari-Sari Store",
    "location": "Barangay San Antonio",
    "inventory": {
        "laundry soap": {"qty": 10, "price": 15.00},
        "cigarettes": {"qty": 50, "price": 5.00}
    }
}
```

### Working with JSON

```python
import json

# Write data to JSON
data = {
    "store_name": "Lola's Sari-Sari Store",
    "inventory": {
        "laundry soap": {"qty": 10, "price": 15.00},
        "cigarettes": {"qty": 50, "price": 5.00},
    }
}

with open("store.json", "w") as file:
    json.dump(data, file, indent=4)

# Read data from JSON
with open("store.json", "r") as file:
    loaded = json.load(file)

print(loaded["store_name"])
print(loaded["inventory"]["laundry soap"]["qty"])
```

??? tip "Diskarte"
    JSON is like Python dictionaries but saved to a file. If you know how to work with dicts, you already know how to work with JSON. The only new thing is `json.dump()` and `json.load()`.

## Building a Filipino Recipe Organizer

Let's build a searchable recipe database:

```python
# Filipino Recipe Organizer
# Chapter 7

import json
import os

RECIPES_FILE = "filipino_recipes.json"

# Default recipes if none exist
DEFAULT_RECIPES = [
    {
        "name": "Chicken Adobo",
        "type": "main dish",
        "prep_time": 45,
        "servings": 4,
        "ingredients": ["chicken", "soy sauce", "vinegar", "garlic", "bay leaves", "peppercorns"],
        "difficulty": "easy",
    },
    {
        "name": "Sinigang na Baboy",
        "type": "soup",
        "prep_time": 60,
        "servings": 6,
        "ingredients": ["pork", "tamarind", "radish", "string beans", "spinach", "tomato", "onion"],
        "difficulty": "medium",
    },
    {
        "name": "Kare-Kare",
        "type": "main dish",
        "prep_time": 90,
        "servings": 4,
        "ingredients": ["oxtail", "peanuts", "banana blossom", "eggplant", "string beans", "bagoong"],
        "difficulty": "hard",
    },
    {
        "name": "Halo-Halo",
        "type": "dessert",
        "prep_time": 20,
        "servings": 2,
        "ingredients": ["ice", "evaporated milk", "leche flan", "hamon", " ube halaya", "sweet beans", "corn"],
        "difficulty": "easy",
    },
]


def load_recipes():
    """Load recipes from file, or use defaults."""
    if os.path.exists(RECIPES_FILE):
        with open(RECIPES_FILE, "r") as f:
            return json.load(f)
    else:
        save_recipes(DEFAULT_RECIPES)
        return DEFAULT_RECIPES


def save_recipes(recipes):
    """Save recipes to file."""
    with open(RECIPES_FILE, "w") as f:
        json.dump(recipes, f, indent=4)
    print(f"Saved {len(recipes)} recipes.")


def add_recipe(recipes):
    """Add a new recipe."""
    name = input("Recipe name: ")
    for recipe in recipes:
        if recipe["name"].lower() == name.lower():
            print(f"Recipe '{name}' already exists!")
            return

    recipe = {
        "name": name,
        "type": input("Type (main dish/soup/dessert/snack): "),
        "prep_time": int(input("Prep time (minutes): ")),
        "servings": int(input("Servings: ")),
        "ingredients": [i.strip() for i in input("Ingredients (comma-separated): ").split(",")],
        "difficulty": input("Difficulty (easy/medium/hard): "),
    }
    recipes.append(recipe)
    save_recipes(recipes)
    print(f"Added {name}!")


def search_recipes(recipes, query):
    """Search recipes by name, type, or ingredient."""
    query = query.lower()
    results = []

    for recipe in recipes:
        if (query in recipe["name"].lower() or
            query in recipe["type"].lower() or
            any(query in ing.lower() for ing in recipe["ingredients"])):
            results.append(recipe)

    return results


def display_recipe(recipe):
    """Display a recipe in a nice format."""
    print(f"\n🍽️  {recipe['name']}")
    print(f"   Type: {recipe['type']}")
    print(f"   Prep time: {recipe['prep_time']} minutes")
    print(f"   Servings: {recipe['servings']}")
    print(f"   Difficulty: {recipe['difficulty']}")
    print(f"   Ingredients: {', '.join(recipe['ingredients'])}")


# Main menu
def main():
    recipes = load_recipes()

    while True:
        print("\n=== Filipino Recipe Organizer ===")
        print("1. Add recipe")
        print("2. Search recipes")
        print("3. List all recipes")
        print("4. Exit")

        choice = input("\nChoose (1-4): ")

        if choice == "1":
            add_recipe(recipes)
        elif choice == "2":
            query = input("Search (name, type, or ingredient): ")
            results = search_recipes(recipes, query)
            if results:
                print(f"\nFound {len(results)} recipe(s):")
                for r in results:
                    display_recipe(r)
            else:
                print("No recipes found. Subok ulit.")
        elif choice == "3":
            print(f"\n{len(recipes)} recipes:")
            for r in recipes:
                print(f"  • {r['name']} ({r['type']})")
        elif choice == "4":
            print("Saving and exiting...")
            save_recipes(recipes)
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
```

??? note "Try It Yourself"
    Run the recipe organizer and try:
    1. Adding your Lola's adobo recipe
    2. Searching for recipes with "chicken" or "pork"
    3. Listing all recipes

??? example "Portfolio Tip: Data Persistence"
    Your recipe organizer shows you understand file I/O and data persistence -- skills used in every real application:

    1. **GitHub README** -- Include a sample `recipes.json` file to show the data structure. Add a screenshot of the search feature working.
    2. **LinkedIn** -- Post: "Built a searchable recipe database with Python. It saves to JSON and supports keyword search. Inspired by my Lola's handwritten cookbook."
    3. **Interview talking point** -- "I built a recipe organizer that persists data between sessions using JSON. This taught me about file handling, data serialization, and building search functionality from scratch."

## Summary

- Files let you save data permanently
- `with open()` safely handles file opening and closing
- CSV is great for tabular data (rows and columns)
- JSON is great for nested, structured data
- Always save your data to a file before the program ends

## Boss Fight

??? warning "Boss Fight: Full Recipe Manager"

    Extend the recipe organizer to include:

    1. Edit existing recipes
    2. Delete recipes
    3. Filter by difficulty level
    4. Export recipes to CSV format
    5. Import recipes from a CSV file

    **Hint:** Use the existing `load_recipes()` and `save_recipes()` functions as your foundation.

??? success "You did it! Level Up!"
    +150 XP. You mastered file handling. Ang galing!

## Side Quests

??? note "Optional: Side Quest"
    - Add a "cooking timer" that counts down prep time
    - Create a "shopping list" feature that extracts ingredients from selected recipes
    - Add nutritional information to each recipe

## Further Reading

- [Python's official tutorial on file I/O](https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files)
- [Real Python: JSON](https://realpython.com/python-json/)

---

*Next: [Chapter 8: Boss Fight 1](chapter-08-boss-fight-1.md) -- Combining everything you've learned.*
