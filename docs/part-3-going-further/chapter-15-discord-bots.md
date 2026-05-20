# Chapter 15: Discord Bots and Async Python

??? example "📋 Chapter Info"
    | | |
    |---|---|
    | **Difficulty** | ⭐⭐⭐ Advanced |
    | **Time** | 45 min |
    | **XP** | +100 XP |

> **Story Hook:** Your barkada's Discord server has 200 members. Every day, someone asks "Ano yung homework?" at 2 AM. Someone else posts a meme at 3 AM. The group chat is chaos. You think: "I should build a bot. A Filipino Discord bot." So you write one that responds in Taglish, shares daily memes, and reminds everyone about deadlines.

---

## What You'll Learn

- What Discord bots are and how they work
- Async programming with `asyncio` and `discord.py`
- Event-driven programming
- Working with external APIs from a bot
- Deploying a bot to run 24/7

## What Is a Discord Bot?

A Discord bot is a program that lives in a Discord server and responds to messages, plays music, manages roles, or does anything you can program. Discord bots use the **Discord API** to send and receive messages.

## Installing discord.py

```bash
pip install discord.py pytz
```

## Your First Discord Bot

```python
# Simple Discord Bot
# Chapter 15

import discord
import asyncio
import random
from datetime import datetime
import pytz


# Create the bot instance
 intents = discord.Intents.default()
 intents.message_content = True  # Allow bot to read messages

bot = discord.Bot(intents=intents)


# Event: When the bot is ready
@bot.event
async def on_ready():
    print(f"Bot is ready! Logged in as {bot.user}")
    print(f"Bot is in {len(bot.guilds)} servers")


# Event: When a message is received
@bot.event
async def on_message(message):
    # Ignore messages from the bot itself
    if message.author == bot.user:
        return

    # Respond to specific commands
    if message.content.lower() == "kumusta":
        greetings = [
            "Kumusta ka! 😊",
            "Hey! Anong balita?",
            "Hi there! Good day!",
            "Kumusta! Ready ka na ba mag-code?",
        ]
        await message.reply(random.choice(greetings))

    if message.content.lower() == "discarte":
        await message.reply(
            "Diskarte is Filipino resourcefulness. "
            "In programming: find a way that works, even if it's not perfect. "
            "Build first, optimize later. Bahala na!"
        )

    if message.content.lower() == "jollibee":
        await message.reply(
            "🐝 Jollibee knows what works. "
            "So does this code. "
            "Chickenjoy is the most reliable function I know."
        )

    # Call the default bot handler (for slash commands)
    await bot.process_commands(message)


# Slash command: /time
@bot.slash_command(description="Show current time in Philippines")
async def time(ctx):
    ph_time = datetime.now(pytz.timezone("Asia/Manila"))
    await ctx.respond(f"🇵🇭 Philippines time: {ph_time.strftime('%I:%M %p')}")


# Slash command: /quote
@bot.slash_command(description="Get a random Filipino wisdom quote")
async def quote(ctx):
    quotes = [
        "Ang hindi magmahal sa sariling wika ay daang manghina ng sariling buhay.",
        "Kaya mo yan! You can do it!",
        "Bahala na -- not fatalism, but courage in the face of uncertainty.",
        "Diskarte == resourcefulness. The art of making do with what you have.",
        "Bayanihan: lifting each other up, together.",
    ]
    await ctx.respond(random.choice(quotes))


# Run the bot
# Replace "YOUR_TOKEN" with your actual Discord bot token
# Get a token from: https://discord.com/developers/applications
bot.run("YOUR_TOKEN")
```

## Async Programming Basics

Discord bots are **async** -- they can handle multiple things at once:

```python
import asyncio

async def greet(name):
    await asyncio.sleep(1)  # Simulate waiting
    print(f"Hello, {name}!")

# Run multiple tasks concurrently
async def main():
    await asyncio.gather(
        greet("Juan"),
        greet("Maria"),
        greet("Pedro"),
    )

asyncio.run(main())
```

### Key Async Concepts

| Concept | What It Does |
|---------|-------------|
| `async def` | Defines an async function (coroutine) |
| `await` | Waits for an async operation to complete |
| `asyncio.gather()` | Runs multiple coroutines concurrently |
| `asyncio.sleep()` | Non-blocking wait |

??? tip "Diskarte"
    Think of `async` like a waiter in a restaurant. Instead of standing at one table waiting for food (blocking), the waiter takes orders from multiple tables and comes back when each order is ready (non-blocking).

## Building a Filipino Study Bot

Let's build a more complete bot for a study group:

```python
# Filipino Study Group Bot
# Chapter 15

import discord
import asyncio
import random
from datetime import datetime, timedelta
import pytz

intents = discord.Intents.default()
intents.message_content = True

bot = discord.Bot(intents=intents)

# Study reminders
reminders = []


@bot.event
async def on_ready():
    print(f"Study Bot ready! Logged in as {bot.user}")
    bot.loop.create_task(reminder_checker())


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    content = message.content.lower().strip()

    # Set reminder: !remind 30 study
    if content.startswith("!remind "):
        parts = content.split(" ", 2)
        if len(parts) == 3:
            minutes = int(parts[1])
            task = parts[2]
            reminder_id = f"{message.author.id}_{len(reminders)}"
            reminders.append({
                "id": reminder_id,
                "user_id": message.author.id,
                "channel_id": message.channel.id,
                "minutes": minutes,
                "task": task,
            })
            await message.reply(
                f"⏰ Reminder set! I'll remind you to '{task}' in {minutes} minutes."
            )

    # List reminders: !reminders
    elif content == "!reminders":
        if reminders:
            lines = [f"  • {r['task']} (in {r['minutes']} min)" for r in reminders]
            await message.reply(f"📋 Active reminders:\n" + "\n".join(lines))
        else:
            await message.reply("No active reminders. Walang reminder.")

    # Random study tip
    elif content == "!tip" or content == "!studytip":
        tips = [
            "📚 Pomodoro technique: 25 min study, 5 min break. Kain muna sa break!",
            "💡 When stuck, explain the problem out loud. Rubber duck method!",
            "🧠 Study in short bursts. 'Bahala na, 10 minutes lang.' Then repeat.",
            "🎮 Gamify your study: 1 chapter = 100 XP, Boss Fight = 50 XP bonus.",
            "☕ Take merienda breaks. Your brain needs fuel.",
        ]
        await message.reply(random.choice(tips))

    # Random Filipino encouragement
    elif content == "!motivate" or content == "!moti":
        motis = [
            "💪 Kaya mo 'yan! You've got this!",
            "🌟 Every expert was once a beginner. Keep going!",
            "🔥 Ang lakas ng loob mo! Don't give up!",
            "⭐ Progress, not perfection. Babagay sa'yo 'yan!",
            "🎯 Focus on one thing at a time. One step at a time.",
        ]
        await message.reply(random.choice(motis))

    await bot.process_commands(message)


async def reminder_checker():
    """Check for reminders that need to fire."""
    while True:
        now = datetime.now()
        to_remove = []

        for reminder in reminders:
            if not hasattr(reminder, "created_at"):
                reminder["created_at"] = now
                reminder["fire_at"] = now + timedelta(minutes=reminder["minutes"])

            if now >= reminder["fire_at"]:
                # Send the reminder
                try:
                    channel = bot.get_channel(reminder["channel_id"])
                    if channel:
                        await channel.send(
                            f"⏰ Reminder: {reminder['task']}! "
                            f"Time to focus, {bot.get_user(reminder['user_id'])}!"
                        )
                except Exception as e:
                    print(f"Error sending reminder: {e}")
                to_remove.append(reminder)

        for r in to_remove:
            reminders.remove(r)

        await asyncio.sleep(30)  # Check every 30 seconds


@bot.slash_command(description="Start a Pomodoro session")
async def pomodoro(ctx, minutes: int = 25):
    await ctx.respond(f"🍅 Pomodoro started! Focus for {minutes} minutes. Ganap mo 'yan!")
    await asyncio.sleep(minutes * 60)
    await ctx.send(f"🎉 Pomodoro complete! {minutes} minutes of focus. Kaya mo talaga!", ephemeral=True)


# Run the bot
bot.run("YOUR_TOKEN")
```

## Getting a Discord Bot Token

1. Go to [Discord Developer Portal](https://discord.com/developers/applications)
2. Click "New Application" and give it a name
3. Go to "Bot" → "Add Bot"
4. Copy the token (keep it secret!)
5. Invite the bot to your server using the OAuth2 URL generator

## Deploying Your Bot

To run your bot 24/7:

| Platform | Free Tier | Best For |
|----------|-----------|----------|
| **Replit** | ✅ Free always-on | Quick bots, small projects |
| **Railway** | ✅ Free trial | Production bots |
| **Fly.io** | ✅ Free allowance | Always-on services |
| **GitHub Codespaces** | ✅ Free hours | Development |
| **Your own computer** | ✅ Free | Learning, testing |

??? tip "Diskarte"
    For learning, run your bot on your own computer. For a real project, use a free hosting platform like Replit or Railway.

## Summary

- Discord bots interact with the Discord API
- Async programming lets bots handle multiple tasks
- Events (`on_message`, `on_ready`) respond to Discord activity
- Slash commands provide structured bot interactions
- Deploy to keep your bot running 24/7

## Boss Fight

??? warning "Boss Fight: Complete Barkada Bot"

    Build a Discord bot with:

    1. Taglish translation feature
    2. Study group accountability tracker
    3. Meme generator with Filipino templates
    4. Quiz/trivia bot with Filipino culture questions
    5. XP system that tracks member activity

    **Hint:** Use a dictionary to track per-member XP and levels.

??? success "You did it! Level Up!"
    +150 XP. You built a Discord bot. Ang galing!

## Side Quests

??? note "Optional: Side Quest"
    - Add a "tambay mode" that plays lo-fi music reminders
    - Create a "boss fight" channel for coding challenges
    - Build a "show your work" channel with auto-formatting

## Further Reading

- [discord.py documentation](https://discordpy.readthedocs.io/)
- [Real Python: Async programming](https://realpython.com/async-io-python/)

---

??? example "Portfolio Tip"

    **GitHub README**: For your Discord bot repo, include a `demo.gif` showing the bot responding to commands. Add a SETUP.md with step-by-step instructions for creating a Discord application and getting a token. Note: "Never commit your bot token -- use environment variables."

    **LinkedIn**: Post: "Built a Discord bot in Python with async programming that responds in Taglish, manages study reminders, and runs 24/7. Deployed on a free hosting platform. My barkada's Discord server now has its own Filipino study assistant. #Python #DiscordBot". This is a highly visible project.

    **Interview Talking Point**: "I understand async programming -- using `async def`, `await`, and `asyncio.gather()` to handle multiple concurrent tasks. I built and deployed a Discord bot that processes events, manages state, and runs continuously. It's practical experience with event-driven architecture."

??? example "🧠 Reflection — Discord Bots and Async Python"

    - **What did you learn?** Discord bots use async programming to handle multiple events simultaneously, letting you build interactive tools for your community.
    - **How can you apply this?** Build a bot for your barkada's Discord server to automate study reminders, share motis, or manage group activities.
    - **What's next?** How could you connect your Discord bot to a database so it remembers conversations across restarts?

??? checkbox "✅ Chapter Checklist"

    - [ ] Understand how Discord bots interact with the Discord API
    - [ ] Write an async function using `async def` and `await`
    - [ ] Build a bot that responds to messages and slash commands
    - [ ] Deploy a bot to run 24/7 on a free hosting platform
    - [ ] Create at least one Taglish command for your barkada

---

*Previous: [Boss Fight 2: Midpoint Battle](../part-2-building-things/chapter-14-boss-fight-2.md) -- Midpoint boss fight*
*Next: [Chapter 16: Data Visualization](chapter-16-dataviz.md) -- Making charts and graphs.*
