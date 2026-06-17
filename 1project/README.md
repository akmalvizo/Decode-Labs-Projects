# 🤖 Vizo AI — Rule-Based Chatbot

> **Project 1 · DecodeLabs Industrial Training Kit · Batch 2026**  
> Developed by **Muhammad Akmal**

---

## 📌 Overview

**Vizo AI** is a rule-based conversational chatbot built entirely in Python using pure control flow logic — no machine learning, no external AI APIs, no third-party NLP libraries. It simulates human-like conversation by matching user input against a structured knowledge base of keywords and returning context-aware responses.

This project is the **foundation milestone** of the DecodeLabs AI Engineering internship, demonstrating mastery of:

- Program control flow and loop architecture
- Input sanitization and normalization
- Dictionary-based intent matching (O(1) lookup)
- Randomized response generation for natural conversation
- Clean exit handling and defensive programming

---

## 🎯 Project Goals

| Goal | Status |
|------|--------|
| Continuous input loop using `while True` | ✅ Complete |
| Input sanitization (case + whitespace) | ✅ Complete |
| Knowledge base with 5+ intent categories | ✅ Complete (17 categories) |
| Keyword-based intent matching engine | ✅ Complete |
| Fallback response for unknown inputs | ✅ Complete |
| Clean exit strategy with kill command | ✅ Complete |
| Dynamic real-time responses (clock) | ✅ Complete |

---

## 🧠 Architecture

Vizo AI follows the **IPO Model** (Input → Process → Output) — the foundational blueprint for transparent and controlled AI systems.

```
┌─────────────────────────────────────────────────────┐
│                    VIZO AI ENGINE                    │
│                                                      │
│  ┌──────────┐    ┌──────────────┐    ┌───────────┐  │
│  │  INPUT   │───▶│   PROCESS    │───▶│  OUTPUT   │  │
│  │          │    │              │    │           │  │
│  │ raw text │    │ sanitize()   │    │ print     │  │
│  │ from     │    │ match_intent │    │ reply to  │  │
│  │ user     │    │ get_response │    │ console   │  │
│  └──────────┘    └──────────────┘    └───────────┘  │
│                                                      │
│  Sanitization ──▶ Intent Matching ──▶ Response Gen   │
└─────────────────────────────────────────────────────┘
```

### Why Dictionary over If-Elif Ladder?

| Approach | Time Complexity | Scalability | Maintainability |
|----------|----------------|-------------|-----------------|
| If-Elif chain | O(n) — linear | Poor | High technical debt |
| Dictionary `.get()` | O(1) — constant | Excellent | Clean and modular |

Vizo AI uses the **dictionary approach** — the professional standard for rule-based systems.

---

## 💡 Features

- **17 Intent Categories** with 200+ trigger keywords covering everyday conversation
- **Keyword-in-sentence matching** — understands phrases, not just exact words
- **Randomized responses** — multiple replies per intent so the bot never feels repetitive
- **Real-time clock** — dynamically returns the current time and date when asked
- **Graceful exit** — handles `quit`, `exit`, `stop`, `end`, `q`, `Ctrl+C`, and `EOF`
- **Empty input guard** — prompts the user instead of crashing or returning blank output
- **Zero dependencies** — runs on any machine with Python 3 installed, nothing to install

---

## 🗂️ Intent Categories

| # | Category | Example Triggers |
|---|----------|-----------------|
| 1 | Greetings | hello, hi, hey, good morning, howdy |
| 2 | How Are You | how are you, you doing, you alright |
| 3 | Identity | who are you, what is your name, are you a bot |
| 4 | Location | where are you, where are you going, traveling |
| 5 | Current Activity | what are you doing, are you busy, watcha doing |
| 6 | Future Plans | what is your plan, any suggestions, help me plan |
| 7 | Food & Eating | what should i eat, hungry, food recommendation |
| 8 | Weather | weather today, is it raining, will it rain |
| 9 | Time & Date | what time is it, today's date, what day is it |
| 10 | Jokes | tell me a joke, make me laugh, crack a joke |
| 11 | Help | help, what can you do, how do you work |
| 12 | Feelings & Mood | i am sad, feeling bored, i am stressed |
| 13 | Motivation | motivate me, i want to give up, inspire me |
| 14 | Study & Learning | how to learn python, career in ai, coding help |
| 15 | Thanks | thank you, great job, you are helpful |
| 16 | Farewell | bye, goodbye, see you, take care |
| 17 | About AI | what is ai, what is machine learning, explain ai |

---

## 🚀 Getting Started

### Prerequisites

- Python 3.x installed on your machine
- No additional libraries required

### Installation

```bash
# 1. Clone this repository
git clone https://github.com/your-username/vizo-ai-chatbot.git

# 2. Navigate into the project folder
cd vizo-ai-chatbot

# 3. Run the chatbot
python chatbot.py
```

That's it. No `pip install`, no setup files, no configuration needed.

---

## 💬 Usage

Once running, simply type your message and press **Enter**. The bot responds instantly.

```
==================================================
  Vizo AI Chatbot    |  Project 1  |  2026
  Rule-Based Engine  |  Keyword Matching
  Developed by       |  Muhammad Akmal
==================================================
  Type 'help' to see what I can do.
  Type 'quit' or 'exit' to stop.
==================================================

You: hello
Vizo: Hey! Great to have you here. What's on your mind?

You: what should i eat today
Vizo: How about biryani? A classic choice for any time of day!

You: tell me a joke
Vizo: Why do programmers prefer dark mode? Because light attracts bugs!

You: what time is it
Vizo: Right now it's 03:45 PM on Wednesday, June 17, 2026.

You: i am sad
Vizo: I hear you! Feelings are valid. Take a deep breath -- this too shall pass.

You: motivate me
Vizo: Code. Break. Fix. Learn. Repeat. That's the engineer's way.

You: bye
Vizo: Goodbye! Keep coding and stay curious!

You: exit
Vizo: Goodbye! Keep building great things.
```

### Exit Commands

Type any of the following to stop the chatbot:

```
quit    exit    q    stop    end
```

You can also press `Ctrl + C` at any time.

---

## 📁 Project Structure

```
vizo-ai-chatbot/
│
├── chatbot.py          # Main chatbot file — all logic lives here
└── README.md           # Project documentation
```

### Inside `chatbot.py`

| Component | Description |
|-----------|-------------|
| `knowledge_base` | Dictionary of 17 intents, each with keywords and responses |
| `sanitize(text)` | Converts input to lowercase and strips whitespace |
| `match_intent(input)` | Scans all keyword lists and returns the matched intent |
| `get_response(intent)` | Returns a random response; handles dynamic time/date |
| `main()` | The infinite loop — heartbeat of the chatbot |

---

## 🔬 How the Matching Engine Works

```python
# Step 1: User types a message
raw = input("You: ")

# Step 2: Sanitize — normalize case and remove spaces
clean = raw.lower().strip()        # "  HELLO there  " → "hello there"

# Step 3: Match intent — scan every keyword list
for intent, data in knowledge_base.items():
    for keyword in data["keywords"]:
        if keyword in clean:       # substring match, not exact match
            return intent

# Step 4: Get response — pick randomly from matched intent
reply = random.choice(responses)   # never same reply twice in a row

# Step 5: Handle special dynamic intents
if responses == ["__TIME__"]:
    return datetime.datetime.now().strftime(...)
```

The key design decision: `if keyword in clean` checks whether the keyword appears **anywhere inside** the user's sentence. This means phrases like `"what should i eat today"` correctly trigger the `food` intent because `"what should i eat"` is a substring of the input.

---

## 🧩 Core Concepts Demonstrated

```
Control Flow         →  while True loop with break condition
Data Structures      →  Dictionary (Hash Map) for O(1) intent lookup
String Methods       →  .lower(), .strip(), in operator
Functions            →  sanitize(), match_intent(), get_response(), main()
Randomization        →  random.choice() for natural varied responses
Date & Time          →  datetime module for live clock responses
Exception Handling   →  try/except for KeyboardInterrupt and EOFError
Defensive Coding     →  empty input guard, fallback responses
```

---

## 🛡️ Key Design Principles

**White Box System** — Every decision this chatbot makes is fully traceable. Input → Logic → Output. No mystery, no hallucination risk, 100% predictable behavior. This is the core advantage of rule-based AI over probabilistic models.

**Sanitization First** — Before any logic runs, the input is cleaned. This ensures `"Hello"`, `"HELLO"`, `"  hello  "`, and `"HeLLo"` all match the same intent without duplicating keywords.

**Fallback Always Exists** — If no intent matches, the bot gives a helpful fallback rather than crashing or returning nothing. This makes the system robust against unexpected input.

---

## 🔮 Possible Extensions

- Add more intents and expand the keyword lists
- Implement **partial keyword scoring** for better fuzzy matching
- Add a **conversation memory** to remember what was discussed earlier
- Build a **web frontend** using Flask so it runs in a browser
- Connect to a **weather API** for live weather responses
- Export **chat history** to a `.txt` or `.json` log file

---

## 📚 What I Learned

Through building this project I gained hands-on experience with:

- Designing a knowledge base as a structured data model
- The difference between **probabilistic AI** (LLMs) and **deterministic AI** (rule-based)
- Why O(1) dictionary lookup is superior to O(n) if-elif chains at scale
- How real-world AI guardrails and chatbots use rule-based layers on top of LLMs
- Writing defensive Python code that handles edge cases gracefully

---

## 👤 Author

**Muhammad Akmal**  
AI Engineering Intern · DecodeLabs · Batch 2026

---

## 🏢 About DecodeLabs

DecodeLabs is a technology training company based in Greater Lucknow, India, focused on building real-world AI engineering skills through hands-on industrial projects.

🌐 [www.decodelabs.tech](http://www.decodelabs.tech)  
📧 decodelabs.tech@gmail.com

---

## 📄 License

This project was created as part of the DecodeLabs Industrial Training Program.  
© 2026 Muhammad Akmal · DecodeLabs Batch 2026

---

*"An LLM without rules is a hallucination engine. This project builds the skeleton that holds the intelligence." — DecodeLabs*