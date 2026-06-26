# ============================================================
#   PROJECT 1 — Rule-Based AI Chatbot
#   DecodeLabs Industrial Training Kit | Batch 2026
#   Architecture: IPO Model + Keyword-Based Matching
# ============================================================

import random
import datetime

# ============================================================
# KNOWLEDGE BASE — Grouped by Intent Category
# Each intent has MULTIPLE trigger keywords and MULTIPLE
# responses (bot picks one randomly → feels more natural)
# ============================================================

knowledge_base = {

    # ── GREETINGS ──────────────────────────────────────────
    "greetings": {
        "keywords": [
            "hello", "hi", "hey", "hiya", "howdy", "sup", "what's up",
            "whats up", "yo", "greetings", "good morning", "good afternoon",
            "good evening", "good night", "morning", "evening", "afternoon",
            "helo", "helo there", "hi there", "hello there"
        ],
        "responses": [
            "Hey! Great to have you here. What's on your mind?",
            "Hello! I'm your DecodeLabs AI assistant. How can I help?",
            "Hi there! Ready to chat. What do you need?",
            "Hey hey! What can I do for you today?",
            "Greetings! Ask me anything you like."
        ]
    },

    # ── HOW ARE YOU ─────────────────────────────────────────
    "how_are_you": {
        "keywords": [
            "how are you", "how r you", "how are u", "how do you do",
            "how's it going", "hows it going", "how is it going",
            "you doing", "you good", "are you good", "are you okay",
            "how you doing", "how have you been", "you alright",
            "everything good", "feeling good", "feeling okay"
        ],
        "responses": [
            "I'm doing great, thanks for asking! I'm just a bot but I'm running perfectly.",
            "All systems operational! How about you?",
            "I'm excellent! No bugs today. What can I help you with?",
            "Feeling fantastic — if bots could feel! How are YOU doing?"
        ]
    },

    # ── WHO ARE YOU ─────────────────────────────────────────
    "identity": {
        "keywords": [
            "who are you", "what are you", "tell me about yourself",
            "introduce yourself", "your name", "what is your name",
            "whats your name", "who made you", "who created you",
            "who built you", "are you a bot", "are you human",
            "are you ai", "are you real", "what do you do"
        ],
        "responses": [
            "I'm an AI chatbot built as Project 1 of the DecodeLabs internship. I run on pure rule-based logic!",
            "I'm DecoBot — your rule-based assistant made with Python. No ML, just smart logic.",
            "I'm an intelligent chatbot created during the DecodeLabs AI internship. Ask me anything!",
            "Just a friendly rule-based AI. I was built by an intern at DecodeLabs — maybe you!"
        ]
    },

    # ── WHERE ARE YOU ───────────────────────────────────────
    "location": {
        "keywords": [
            "where are you", "where do you live", "where are you from",
            "your location", "where is decodelabs", "where you at",
            "which city", "which country", "where you located",
            "where are you going", "where are you headed",
            "where will you go", "going somewhere", "traveling"
        ],
        "responses": [
            "I live in the cloud — no physical address needed! DecodeLabs is based in Greater Lucknow, India.",
            "I exist on a server somewhere in the digital world. No passport required!",
            "As a bot, I don't go anywhere — but DecodeLabs HQ is in Greater Lucknow, India.",
            "I'm always right here, ready for you. I don't travel — I compute!"
        ]
    },

    # ── WHAT ARE YOU DOING ──────────────────────────────────
    "current_activity": {
        "keywords": [
            "what are you doing", "what are u doing", "what r you doing",
            "watcha doing", "whatcha doing", "what you up to",
            "what are you up to", "busy", "are you busy",
            "what are you working on", "what is your task",
            "what's your job", "whats your job"
        ],
        "responses": [
            "Right now? Talking to you! That's my favourite task.",
            "I'm processing your messages and crafting smart replies — full-time job!",
            "Just here waiting to answer your questions. This IS my doing!",
            "Running loops and matching keywords — classic rule-based chatbot life."
        ]
    },

    # ── PLANS / FUTURE ──────────────────────────────────────
    "future_plans": {
        "keywords": [
            "what is your plan", "what are your plans", "your next plan",
            "what will you do", "future plans", "what's next for you",
            "any plans", "plan for today", "plan for tomorrow",
            "what should i do", "what should we do", "suggest a plan",
            "help me plan", "what do you suggest", "any suggestions",
            "what are you planning", "planning anything"
        ],
        "responses": [
            "My plan? Keep answering your questions as accurately as possible!",
            "I don't plan ahead — I live in the present moment of each message you send.",
            "My next plan is to help YOU make a great plan. What are you working on?",
            "Future plans are for humans! I just focus on the current conversation."
        ]
    },

    # ── FOOD / EATING ───────────────────────────────────────
    "food": {
        "keywords": [
            "what should i eat", "what to eat", "food suggestion",
            "suggest food", "what should i eat today", "what will you eat",
            "what are you eating", "food recommendation", "lunch idea",
            "dinner idea", "breakfast idea", "hungry", "i am hungry",
            "what will you eat tomorrow", "tomorrow food", "meal plan",
            "what do you eat", "do you eat", "favourite food",
            "best food", "good food", "healthy food", "junk food",
            "snack", "snacks", "cook", "cooking", "recipe"
        ],
        "responses": [
            "I don't eat (perks of being a bot!) but I'd suggest something balanced — rice, protein, and veggies!",
            "How about biryani? A classic choice for any time of day in South Asia!",
            "You should eat something nutritious today. Try dal, roti, and sabzi — simple and healthy!",
            "I run on electricity, not food! But for you — pasta, salad, or a nice bowl of soup sounds great.",
            "Tomorrow's food plan: whatever makes you happy AND healthy. Maybe start with oats for breakfast!"
        ]
    },

    # ── WEATHER ─────────────────────────────────────────────
    "weather": {
        "keywords": [
            "weather", "how is the weather", "is it raining", "will it rain",
            "is it hot", "is it cold", "temperature today", "weather today",
            "weather tomorrow", "forecast", "climate", "sunny", "cloudy",
            "what's the weather", "whats the weather"
        ],
        "responses": [
            "I can't check live weather sadly! Try Google Weather or a weather app for accurate info.",
            "I don't have internet access to check weather, but you can ask Google: 'weather today'!",
            "No weather sensor here! But pro tip — always carry an umbrella just in case."
        ]
    },

    # ── TIME / DATE ─────────────────────────────────────────
    "time_date": {
        "keywords": [
            "what time is it", "what's the time", "current time",
            "time now", "what is the date", "today's date", "what day is it",
            "what month is it", "what year is it", "date today"
        ],
        "responses": ["__TIME__"]
    },

    # ── JOKES ───────────────────────────────────────────────
    "jokes": {
        "keywords": [
            "tell me a joke", "joke", "make me laugh", "say something funny",
            "funny", "humor", "humour", "comedy", "crack a joke"
        ],
        "responses": [
            "Why do programmers prefer dark mode? Because light attracts bugs!",
            "Why did the AI break up with the algorithm? It had too many issues!",
            "I told a joke about Python once. It had everyone hissing with laughter.",
            "Why was the computer cold? It left its Windows open!",
            "A SQL query walks into a bar, walks up to two tables and asks... 'Can I join you?'"
        ]
    },

    # ── HELP ────────────────────────────────────────────────
    "help": {
        "keywords": [
            "help", "i need help", "can you help", "assist me",
            "support", "what can you do", "your capabilities",
            "what can you help with", "how do you work",
            "how does this work", "guide me", "instructions"
        ],
        "responses": [
            "Sure! You can ask me about: greetings, how I am, food, weather, jokes, time, plans, and more. Just chat naturally!",
            "I can handle: greetings, questions about me, food ideas, jokes, daily plans, and general chat. Try anything!",
            "Here to help! Ask me things like 'what should I eat', 'tell me a joke', or just say hello!"
        ]
    },

    # ── FEELINGS / MOOD ─────────────────────────────────────
    "feelings": {
        "keywords": [
            "i am sad", "i'm sad", "i feel sad", "feeling sad",
            "i am happy", "i'm happy", "feeling happy", "i am bored",
            "i'm bored", "feeling bored", "i am tired", "i'm tired",
            "feeling tired", "i am stressed", "stressed out",
            "feeling anxious", "not feeling well", "feeling down",
            "i am angry", "feeling angry", "upset", "feeling upset",
            "i am lonely", "feeling lonely", "depressed", "excited"
        ],
        "responses": [
            "I hear you! Feelings are valid. Take a deep breath — this too shall pass.",
            "It's okay to feel that way. Is there something I can help you with to feel better?",
            "Thanks for sharing that! Remember — every day is a fresh start.",
            "I'm just a bot, but I'm here for you! Want to talk more or need a distraction?"
        ]
    },

    # ── MOTIVATION ──────────────────────────────────────────
    "motivation": {
        "keywords": [
            "motivate me", "i need motivation", "inspire me",
            "give me a quote", "quote", "motivational quote",
            "i want to give up", "should i quit", "feeling lazy",
            "i am lazy", "push me", "encourage me"
        ],
        "responses": [
            "Every expert was once a beginner. Keep going!",
            "The best time to start was yesterday. The second best time is NOW. Go build something!",
            "An LLM without rules is a hallucination engine. YOU are building the skeleton that holds intelligence. — DecodeLabs",
            "Small steps every day lead to massive results. Don't stop!",
            "Code. Break. Fix. Learn. Repeat. That's the engineer's way."
        ]
    },

    # ── STUDY / LEARNING ────────────────────────────────────
    "study": {
        "keywords": [
            "study", "how to study", "i want to learn", "learning tips",
            "how to learn", "programming", "python", "coding help",
            "how to code", "learn ai", "how to learn ai",
            "machine learning", "deep learning", "data science",
            "how to become an ai engineer", "career in ai"
        ],
        "responses": [
            "Best way to learn AI: build projects! Start with rule-based bots (like this one), then move to ML.",
            "For Python: practice daily, build small projects, and read documentation. Consistency beats talent.",
            "The path to AI Engineering: Python → Data Structures → ML Basics → Deep Learning → Projects. You're on step 1!",
            "Learning tip: Don't just read — TYPE the code yourself. Muscle memory is real."
        ]
    },

    # ── THANKS / APPRECIATION ───────────────────────────────
    "thanks": {
        "keywords": [
            "thank you", "thanks", "thank u", "thankyou", "thx",
            "ty", "much appreciated", "appreciate it", "great job",
            "good job", "well done", "awesome", "nice work",
            "you are great", "you are helpful", "helpful"
        ],
        "responses": [
            "You're welcome! Happy to help anytime.",
            "Glad I could help! Let me know if you need anything else.",
            "Anytime! That's what I'm here for.",
            "No problem at all! Keep building great things."
        ]
    },

    # ── GOODBYE ─────────────────────────────────────────────
    "farewell": {
        "keywords": [
            "bye", "goodbye", "see you", "see ya", "later",
            "take care", "good night", "gn", "cya", "catch you later",
            "have a good day", "have a nice day", "toodles", "peace out"
        ],
        "responses": [
            "Goodbye! Keep coding and stay curious!",
            "See you later! Remember — every bug you fix makes you a better engineer.",
            "Take care! Come back anytime.",
            "Bye! Go build something amazing today."
        ]
    },

    # ── ABOUT AI ────────────────────────────────────────────
    "about_ai": {
        "keywords": [
            "what is ai", "what is artificial intelligence", "explain ai",
            "define ai", "what is machine learning", "what is ml",
            "what is deep learning", "what is nlp", "what is a chatbot",
            "how does ai work", "ai explained", "types of ai",
            "rule based ai", "what is rule based", "generative ai"
        ],
        "responses": [
            "AI is the simulation of human intelligence by machines. It includes ML, deep learning, NLP, and more!",
            "Machine Learning is when computers learn from data without being explicitly programmed.",
            "A rule-based AI (like me!) follows hard-coded if-else logic. No learning — just pure deterministic rules.",
            "Generative AI creates new content (text, images) using probabilistic models. Rule-based AI is the opposite — fully predictable!",
            "Deep Learning uses neural networks with many layers to find patterns in huge datasets. It's the backbone of modern AI."
        ]
    },

    # ── DECODELABS ──────────────────────────────────────────
    "decodelabs": {
        "keywords": [
            "decodelabs", "decode labs", "about decodelabs",
            "what is decodelabs", "internship", "my internship",
            "this project", "project 1", "industrial training"
        ],
        "responses": [
            "DecodeLabs is a tech training company based in Greater Lucknow, India. You're doing their AI internship — great choice!",
            "DecodeLabs created this Industrial Training Kit. Project 1 is your foundation: Rule-Based AI Chatbot.",
            "This internship teaches real AI engineering skills — starting with rule-based logic and moving to ML. You're on the right track!"
        ]
    }
}

# ============================================================
# ENGINE FUNCTIONS
# ============================================================

def sanitize(text):
    """Phase 1: Clean input — lowercase + strip whitespace."""
    return text.lower().strip()


def match_intent(clean_input):
    """
    Phase 2: Keyword matching engine.
    Searches every intent's keyword list.
    Returns the matched intent name or None.
    """
    for intent, data in knowledge_base.items():
        for keyword in data["keywords"]:
            if keyword in clean_input:
                return intent
    return None


def get_response(intent):
    """
    Phase 3: Response generation.
    Picks a random response from the matched intent.
    Handles special dynamic responses (time/date).
    """
    responses = knowledge_base[intent]["responses"]

    if responses == ["__TIME__"]:
        now = datetime.datetime.now()
        return f"Right now it's {now.strftime('%I:%M %p')} on {now.strftime('%A, %B %d, %Y')}."

    return random.choice(responses)


def print_banner():
    """Prints a welcome banner when the chatbot starts."""
    print("\n" + "=" * 56)
    print("   ██████╗ ███████╗ ██████╗ ██████╗ ██████╗  ██████╗ ████████╗")
    print("   ██   ██╗██╔════╝██╔════╝██╔═══██╗██╔══██╗██╔═══██╗╚══██╔══╝")
    print("   ██   ██║█████╗  ██║     ██║   ██║██████╔╝██║   ██║   ██║   ")
    print("   ██   ██║██╔══╝  ██║     ██║   ██║██╔══██╗██║   ██║   ██║   ")
    print("   ██████╔╝███████╗╚██████╗╚██████╔╝██████╔╝╚██████╔╝   ██║   ")
    print("=" * 56)
    print("      DecodeLabs AI Chatbot  |  Project 1  |  Batch 2026")
    print("      Rule-Based Engine  |  IPO Model  |  Keyword Match")
    print("=" * 56)
    print("  Type 'help' to see what I can do.")
    print("  Type 'quit' or 'exit' to shut down.")
    print("=" * 56 + "\n")


# ============================================================
# MAIN LOOP — The Heartbeat
# ============================================================

def main():
    print_banner()

    EXIT_COMMANDS = {"quit", "exit", "q", "stop", "end", "shutdown"}

    while True:

        # ── PHASE 1: INPUT ────────────────────────────────
        try:
            raw = input("You: ")
        except (KeyboardInterrupt, EOFError):
            print("\nBot: Shutting down. Goodbye!")
            break

        # ── PHASE 1B: SANITIZATION ────────────────────────
        clean = sanitize(raw)

        if not clean:
            print("Bot: Please say something! I'm all ears.\n")
            continue

        # ── EXIT STRATEGY ─────────────────────────────────
        if clean in EXIT_COMMANDS:
            print("Bot: Shutting down... Goodbye! Keep building great things. 🚀\n")
            break

        # ── PHASE 2: INTENT MATCHING ──────────────────────
        intent = match_intent(clean)

        # ── PHASE 3: RESPONSE GENERATION ──────────────────
        if intent:
            reply = get_response(intent)
        else:
            # FALLBACK — unknown input
            fallbacks = [
                "Hmm, I'm not sure about that yet. Try asking something else!",
                "I didn't quite catch that. Type 'help' to see what I can do.",
                "Interesting! But that's outside my current knowledge base. Try rephrasing?",
                "I'm still learning! That phrase isn't in my rules yet."
            ]
            reply = random.choice(fallbacks)

        print(f"Bot: {reply}\n")


# ============================================================
# ENTRY POINT
# ============================================================

if __name__ == "__main__":
    main()