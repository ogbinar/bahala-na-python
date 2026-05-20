# Chapter 10: Strings and the Tagalog Typing Game

??? example "📋 Chapter Info"
    | | |
    |---|---|
    | **Difficulty** | ⭐⭐ Intermediate |
    | **Time** | 25 min |
    | **XP** | +100 XP |

> **Story Hook:** You're at a comshop, and the person next to you is furiously typing in Tagalog. You look at their screen: "Ang lalaking nag-iisip nang mabuti ay walang kapantay na lakas." Your eyes glaze over. "How do they type SO fast?" you wonder. You try -- your fingers stumble over the keyboard, especially the words with special characters. "Ano 'yung ñ?" you ask the operator. "Sir, wala pong ñ sa keyboard namin," they reply. You think: "I should build a typing game. In Tagalog."

---

## What You'll Learn

- String methods (upper, lower, strip, split, join, replace)
- String formatting (f-strings, format())
- String slicing and indexing
- Working with Unicode (Tagalog special characters)
- Timing and performance measurement

## Strings: More Than Just Text

Strings are everywhere in programming. They're how you represent text: names, messages, URLs, everything. Python has powerful built-in tools for working with strings.

```python
name = "Juan dela Cruz"

# Common string methods
print(name.upper())     # JUAN DELA CRUZ
print(name.lower())     # juan dela cruz
print(name.title())     # Juan Dela Cruz
print(name.strip())     # Removes leading/trailing whitespace
print(name.replace("Juan", "Maria"))  # Maria dela Cruz
```

## String Slicing: Getting Parts of a String

You can extract portions of a string using slicing:

```python
text = "Kumusta, World!"

text[0]       # 'K' (first character)
text[0:7]     # 'Kumusta' (characters 0-6)
text[-6:]     # 'World!' (last 6 characters)
text[::2]     # 'Kust ood!' (every other character)
text[::-1]    # '!dlroW ,atsumuK' (reversed!)
```

## Splitting and Joining

```python
# Split: break a string into a list
sentence = "pamasahe, kain, photocopy, load"
categories = sentence.split(", ")
print(categories)  # ['pamasahe', 'kain', 'photocopy', 'load']

# Join: combine a list into a string
items = ["laundry soap", "cigarettes", "candy"]
result = ", ".join(items)
print(result)  # laundry soap, cigarettes, candy
```

??? tip "⏸️ Pause and Predict"

    **Predict: what's the difference between `'Hello ' + name` and `f'Hello {name}'`? Which would you prefer and why?**

    Take 30 seconds to think about your answer before reading on. This is how you build real understanding!

## String Formatting

### f-strings (Recommended)

```python
name = "Juan"
age = 17
gwa = 1.75

print(f"Hi, I'm {name}, {age} years old, GWA: {gwa}")
# Hi, I'm Juan, 17 years old, GWA: 1.75

# With formatting
print(f"GWA: {gwa:.2f}")  # GWA: 1.75 (2 decimal places)
print(f"Name: {name:>10}")  # Name:       Juan (right-aligned, width 10)
print(f"Name: {name:<10}")  # Name: Juan      (left-aligned, width 10)
```

## Tagalog Special Characters

Tagalog uses special characters that sometimes cause issues:

- **ñ** (n with tilde) -- as in "bañig," "piñata"
- **ñ** is rare in modern Tagalog (most words use "ny" instead)
- **\'** (apostrophe) -- for contractions like "diko" (di ko), "nila'y"
- **á, é, í, ó, ú** -- accented vowels (rare in modern Tagalog)

```python
# Unicode handling in Python
text = "Kumusta ka?"
print(text.encode("utf-8"))  # Works perfectly with UTF-8
```

## Building a Tagalog Typing Game

Let's build a typing game that practices Tagalog words:

```python
# Tagalog Typing Game
# Chapter 10

import time
import random

# Word lists by difficulty
WORD_BANKS = {
    "easy": [
        "kumusta", "mabuti", "salamat", "oo", "hindi",
        "po", "opo", "opo", "tayo", "kami", "silá",
        "bahay", "kain", "tubig", "gatas", "tinapay",
    ],
    "medium": [
        "magandang", "gabi", "umaga", "hapon", "merienda",
        "pamasahe", "photocopy", "biskwit", "sigarilye",
        "nag-aalok", "nag-aabang", "nag-aayos",
        "barangay", "pamilya", "kaibigan", "barkada",
    ],
    "hard": [
        "pagpapahalaga", "pananampalataya", "pagpapakumbaba",
        "pakikisama", "pagkakaisa", "pagpapahalaga",
        "katarungan", "kalayaan", "karapatan",
        "pinagmulan", "pamamaraan", "pananaw",
    ],
}


class TypingGame:
    def __init__(self, difficulty="medium", word_count=10):
        self.difficulty = difficulty
        self.word_count = word_count
        self.words = []
        self.results = []

    def get_words(self):
        """Select random words from the word bank."""
        self.words = random.sample(WORD_BANKS[self.difficulty], self.word_count)

    def play(self):
        """Run a single typing round."""
        self.get_words()
        print(f"\n=== Tagalog Typing Game ({self.difficulty.upper()}) ===")
        print(f"Type {self.word_count} words. Good luck! Ganap mo 'yan!\n")

        times = []
        for i, word in enumerate(self.words, 1):
            print(f"\n{i}. {word}")
            print("   ", end="")

            start_time = time.time()
            typed = input()
            end_time = time.time()

            elapsed = end_time - start_time
            times.append(elapsed)

            correct = typed.strip().lower() == word.lower()
            self.results.append({
                "word": word,
                "typed": typed.strip(),
                "correct": correct,
                "time": elapsed,
            })

            status = "✅" if correct else "❌"
            print(f"   {status} {elapsed:.1f}s")

        return self._calculate_stats()

    def _calculate_stats(self):
        """Calculate typing statistics."""
        total_words = len(self.results)
        correct = sum(1 for r in self.results if r["correct"])
        accuracy = (correct / total_words) * 100 if total_words else 0
        avg_time = sum(r["time"] for r in self.results) / total_words if total_words else 0
        total_time = sum(r["time"] for r in self.results)

        # Words per minute (based on correct words)
        wpm = (correct / total_time * 60) if total_time > 0 else 0

        stats = {
            "accuracy": accuracy,
            "wpm": wpm,
            "avg_time": avg_time,
            "total_time": total_time,
        }

        print(f"\n=== Results ===")
        print(f"Accuracy: {accuracy:.0f}% ({correct}/{total_words})")
        print(f"Words/min: {wpm:.0f}")
        print(f"Average time: {avg_time:.1f}s per word")
        print(f"Total time: {total_time:.1f}s")

        if accuracy >= 90:
            print("🏅 Galing! Super fast!")
        elif accuracy >= 70:
            print("💪 Good job! Konti pa lang!")
        else:
            print("💪 Subok ulit! Practice makes perfect!")

        return stats


def main():
    print("=== Tagalog Typing Game ===\n")
    print("Difficulty: easy, medium, hard")
    difficulty = input("Choose (default: medium): ").strip() or "medium"
    count = int(input("Number of words (default: 10): ") or "10")

    game = TypingGame(difficulty, count)

    play_again = True
    while play_again:
        game.play()
        play_again = input("\nPlay again? (y/n): ").strip().lower() == "y"

    print("Salamat for playing! Palagi kang pwede mag-improve.")


if __name__ == "__main__":
    main()
```

??? note "Try It Yourself"
    Run the typing game and try all three difficulty levels. Notice how "hard" words like "pagpapahalaga" take much longer to type!

## Summary

- String methods: `upper()`, `lower()`, `strip()`, `split()`, `join()`, `replace()`
- Slicing: `text[0:5]`, `text[-3:]`, `text[::-1]`
- f-strings for clean formatting: `f"Hello, {name}!"`
- Unicode works natively in Python 3
- Timing with `time.time()` measures performance

## Boss Fight

??? warning "Boss Fight: Full Typing Game Suite"

    Extend the typing game with:

    1. Multiple rounds with score tracking
    2. Leaderboard that saves best times to a file
    3. Custom word input (type your own words)
    4. WPM (words per minute) calculation
    5. Difficulty that adapts based on performance

    **Hint:** Use a list of dictionaries to track scores, then sort by WPM.

??? success "You did it! Level Up!"
    +150 XP. You built a typing game. Ang galing!

## Side Quests

??? note "Optional: Side Quest"
    - Add Tagalog proverbs and sayings to the hard word bank
    - Create a "speed run" mode where words appear faster
    - Build a "spelling bee" mode where you hear the word and type it

## Further Reading

- [Python's official string methods](https://docs.python.org/3/library/stdtypes.html#string-methods)
- [Real Python: String formatting](https://realpython.com/python-f-strings/)

---

*Previous: [Chapter 9: Classes](chapter-09-classes.md) -- Object-oriented programming*
*Next: [Chapter 11: APIs](chapter-11-apis.md) -- Connecting to the internet.*

---

??? example "Portfolio Tip"

    **GitHub README**: Your Tagalog typing game is a fun, shareable project. Include instructions for running it, screenshots of the difficulty levels, and a note: "Built to help Filipino learners practice typing in Tagalog -- because most typing games only support English."

    **LinkedIn**: Post: "Created a Tagalog typing game in Python with 3 difficulty levels. Most typing tools only support English, but Filipino students need practice in their own language too. Open source and free. #Python #FilipinoEd". This shows you build for underserved communities.

    **Interview Talking Point**: "I built a typing game that handles Unicode text and Tagalog words, with performance tracking (WPM, accuracy). It uses string methods like `strip()`, `split()`, `lower()`, and f-string formatting extensively. The project showed me how to handle edge cases like special characters and whitespace."

??? example "🧠 Reflection — Strings and Text Processing"

    - **What did you learn?** You mastered string methods like `split`, `join`, `strip`, and `replace`, along with f-strings for formatting and slicing for extracting substrings.
    - **How can you apply this?** String skills are essential for cleaning up messy data from surveys, formatting messages for a text-based game in Tagalog, or processing names and addresses in community databases.
    - **What's next?** How do regular expressions (regex) take pattern matching in strings to the next level?

??? checkbox "✅ Chapter Checklist"

    - [ ] I can use common string methods: `upper()`, `lower()`, `strip()`, `split()`, `join()`, `replace()`
    - [ ] I can format strings cleanly using f-strings with expressions and formatting options
    - [ ] I understand string slicing with start, stop, and step indices
    - [ ] I can work with Unicode characters and handle text from different languages
    - [ ] I built the Tagalog Typing Game project
