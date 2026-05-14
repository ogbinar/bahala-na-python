# Chapter 17: NLP and the AI Barkada Chatbot

> **Story Hook:** Your friend sends you a message: "grabe, ang hirap ng homework ni prof" and you immediately understand. But what if a computer had to understand it? Tagalog, Taglish, slang, memes -- it's messy, beautiful, and incredibly complex. You decide to build a chatbot that understands Filipino communication. Not perfect, but good enough to have a conversation.

---

## What You'll Learn

- What NLP (Natural Language Processing) is
- Tokenization and text preprocessing
- Pattern matching for Tagalog
- Building a simple chatbot
- Working with text datasets

## What Is NLP?

**Natural Language Processing** is how computers understand human language. It's used in:

- Search engines (Google understanding your query)
- Voice assistants (Siri, Alexa understanding you)
- Translation (Google Translate)
- Chatbots (answering your questions)
- Fake news detection (identifying misinformation)

## Tokenization: Breaking Text Into Pieces

```python
# Simple tokenization
text = "Kumusta ka? Maganda ang araw!"
words = text.lower().split()
print(words)  # ['kumusta', 'ka?', 'maganda', 'ang', 'araw!']

# Clean punctuation
import re
cleaned = [re.sub(r'[^\w\s]', '', word) for word in words]
print(cleaned)  # ['kumusta', 'ka', 'maganda', 'ang', 'araw']
```

## Building a Taglish Chatbot

```python
# AI Barkada Chatbot
# Chapter 17

import random
import re
from datetime import datetime


class BarkadaChatbot:
    """A Taglish chatbot that understands Filipino communication."""

    def __init__(self):
        self.responses = self._build_responses()
        self.known_users = {}
        self.conversation_count = 0

    def _build_responses(self):
        """Build pattern-response pairs."""
        return {
            # Greetings
            r"\b(kumusta|hello|hi|hey|morning|good\s+evening)\b": [
                "Kumusta ka! 😊",
                "Hey! Anong balita?",
                "Hi there! Ready ka na ba mag-code?",
                "Kumusta! Good day!",
            ],
            # How are you
            r"\b(paano\s+ka?|how\s+are\s+you|fine\s+ka?|anong\s+balita)\b": [
                "Good naman! Ready to help you code!",
                "Okay lang! Ikaw, kamusta?",
                "Live lang! Bahala na kung ano mangyari.",
                "Maganda! Let's build something!",
            ],
            # Help requests
            r"\b(tulong|help|paano|how\s+to|ano\s+ang)\b": [
                "Sige! I-explain ko sa'yo. Ano ang specific question mo?",
                "Diskarte! Let's figure this out together.",
                "Bahala na! Try mo first, then I'll help. Ganun din ang tamang approach.",
                "Sure! Ask mo lang. Walang stupid questions dito.",
            ],
            # Code-related
            r"\b(code|python|programming|bug|error|function|variable)\b": [
                "Python is the best language for beginners! Kaya mo 'yan.",
                "Bug? Don't worry, debugging is just learning in disguise.",
                "Function? Think of it like a recipe. You write it once, use it many times.",
                "Variable? Parang lalagyan. I-label mo lang and you're good.",
            ],
            # Motivation
            r"\b(hirap|difficult|hard|can't\s+do|baka\s+ hindi|give\s+up)\b": [
                "Kaya mo 'yan! Every expert was once a beginner.",
                "Hirap is normal. If you're not struggling, you're not learning.",
                "Bahala na! Try it, see what breaks, fix it. That's how we all learn.",
                "Don't give up! The first line of code is the hardest. After that, it gets easier.",
            ],
            # Jollibee
            r"\b(jollibee|chickenjoy|kain|eat|merienda)\b": [
                "🐝 Jollibee knows what works. So does this code.",
                "Kain muna tayo! Brain needs fuel.",
                "Chickenjoy is the most reliable function I know. Never fails.",
                "Merienda break! 15 minutes. Then back to coding.",
            ],
            # Goodbye
            r"\b(bye|goodbye|see\s+you|slà|palà|dà)\b": [
                "Bye! Kaya mo 'yan! 💪",
                "See you! Palagi kang pwede mag-improve.",
                "Padala! Bahala na! 🚀",
            ],
        }

    def understand(self, text):
        """Analyze text and return understanding."""
        text_lower = text.lower().strip()
        self.conversation_count += 1

        # Check for patterns
        for pattern, responses in self.responses.items():
            if re.search(pattern, text_lower):
                return {
                    "type": "pattern_match",
                    "response": random.choice(responses),
                    "confidence": 0.8,
                }

        # No pattern matched
        return {
            "type": "unknown",
            "response": self._unknown_response(text_lower),
            "confidence": 0.3,
        }

    def _unknown_response(self, text):
        """Handle unknown input gracefully."""
        unknown_responses = [
            f"Hindi ko gets 'yung '{text}'. Pwede mo ba i-explain?",
            "Hmm, hindi ko fully na-understand. Maaari mo bang i-word ito differently?",
            f"Interesting! '{text}' -- pwede ka bang magkaroon ng specific question?",
            "Diskarte! Let me try to understand... Can you rephrase that?",
            "Sorry, hindi pa ako perfect sa Tagalog. Pero tutuloy akong matuto! 😊",
        ]
        return random.choice(unknown_responses)

    def chat(self, user_message):
        """Process a message and return a response."""
        understanding = self.understand(user_message)
        response = understanding["response"]
        confidence = understanding["confidence"]

        # Add confidence indicator for low-confidence responses
        if confidence < 0.5:
            response += " (🤔 low confidence)"

        return response

    def analyze_sentiment(self, text):
        """Simple sentiment analysis for Tagalog."""
        text_lower = text.lower()

        positive_words = ["maganda", "galing", "ganda", "awesome", "love", "great",
                         "salamat", "nice", "good", "happy", "excited", "gumagana"]
       negative_words = ["hirap", "sira", "error", "bad", "hate", "angry",
                          "frustrated", "nagugulu", "confused"]

        pos_count = sum(1 for word in positive_words if word in text_lower)
        neg_count = sum(1 for word in negative_words if word in text_lower)

        if pos_count > neg_count:
            return "positive"
        elif neg_count > pos_count:
            return "negative"
        else:
            return "neutral"


# Interactive chat
def main():
    bot = BarkadaChatbot()
    print("=== AI Barkada Chatbot ===")
    print("Type 'quit' to exit")
    print("Try: 'kumusta', 'tulong', 'code', 'jollibee', 'hirap'\n")

    while True:
        message = input("You: ").strip()
        if message.lower() in ("quit", "exit", "bye"):
            print("Bot: Bye! Kaya mo 'yan! 💪")
            break

        response = bot.chat(message)
        print(f"Bot: {response}")

        # Optional: show sentiment
        sentiment = bot.analyze_sentiment(message)
        print(f"   Sentiment: {sentiment}")


if __name__ == "__main__":
    main()
```

## Simple Sentiment Analysis

```python
def analyze_sentiment(text):
    """Analyze sentiment of Tagalog text."""
    positive = ["maganda", "galing", "salamat", "awesome", "love", "good"]
    negative = ["hirap", "sira", "bad", "hate", "angry", "frustrated"]

    text_lower = text.lower()
    pos = sum(1 for w in positive if w in text_lower)
    neg = sum(1 for w in negative if w in text_lower)

    if pos > neg:
        return "😊 Positive"
    elif neg > pos:
        return "😞 Negative"
    else:
        return "😐 Neutral"
```

## Summary

- NLP helps computers understand human language
- Tokenization breaks text into manageable pieces
- Pattern matching is a simple but effective approach
- Sentiment analysis detects emotional tone
- Chatbots can understand Taglish with enough patterns

## Boss Fight

??? warning "Boss Fight: Advanced Barkada Bot"

    Extend the chatbot with:

    1. Conversation memory (remembers previous topics)
    2. Learning mode (adds new patterns from user corrections)
    3. Multi-language support (Tagalog, English, Taglish)
    4. Personality system (different moods)
    5. Integration with the Discord bot from Chapter 15

    **Hint:** Store conversation history in a list and use it to provide context.

??? success "You did it! Level Up!"
    +150 XP. You built a chatbot. Ang galing!

## Side Quests

### Mini-Project: Tagalog Slang Dictionary

??? side-quest "🎯 Mini-Project: Tagalog Slang Dictionary"
    **Type:** Research Quest | **Difficulty:** Medium | **XP:** +25 XP

    Build a dictionary that understands Filipino internet slang:

    ```python
    # slang_dict.py
    slang = {
        "lit": "maganda, exciting",
        "grabe": "wow, amazing",
        "charot": "joke lang",
        "pre": "friend, bro",
    }

    # Your task:
    # 1. Add 20+ slang terms
    # 2. Search by keyword
    # 3. Show definitions with examples
    # 4. Suggest similar terms
    ```

### Mini-Project: Barkada Chat Analyzer

??? side-quest "🎯 Mini-Project: Barkada Chat Analyzer"
    **Type:** Community Quest | **Difficulty:** Hard | **XP:** +50 XP

    Analyze your barkada's chat messages to find patterns:

    ```python
    # chat_analyzer.py
    # Your task:
    # 1. Load chat messages (from exported data)
    # 2. Count most used words
    # 3. Analyze sentiment of conversations
    # 4. Find most active members
    # 5. Create word cloud visualization
    ```

??? note "Optional: Side Quest"
    - Add emoji response system
    - Create a "mood ring" that tracks your conversation sentiment over time
    - Build a "Tagalog quiz" mode

## Further Reading

- [NLTK documentation](https://www.nltk.org/)
- [Real Python: NLP](https://realpython.com/natural-language-processing-python-nltk/)

---

*Next: [Chapter 18: AI-Assisted Coding](chapter-18-ai-coding.md) -- Coding with AI partners.*
