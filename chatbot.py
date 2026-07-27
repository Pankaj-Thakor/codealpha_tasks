# ============================================================
# Project : Smart Rule-Based Chatbot
# Author  : Thakor Pankajji Devendraji
# Language: Python
# ============================================================

import random
import datetime
import time
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

try:
    import pyttsx3
    engine = pyttsx3.init()
    engine.setProperty("rate", 170)
    engine.setProperty("volume", 1.0)
    TTS_AVAILABLE = True
except Exception:
    TTS_AVAILABLE = False
    print("Voice engine not available. Continuing in text-only mode.")

# ============================================================
# COLORS
# ============================================================

RESET = "\033[0m"
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
CYAN = "\033[96m"
MAGENTA = "\033[95m"

# ============================================================
# TYPING EFFECT
# ============================================================

def bot_print(text):
    """Print bot message with typing animation and voice."""

    print(f"{GREEN}Bot : ", end="")

    for letter in text:
        print(letter, end="", flush=True)
        time.sleep(0.02)

    print(RESET)

    if TTS_AVAILABLE:
        try:
            engine.say(text)
            engine.runAndWait()
        except Exception:
            pass


# ============================================================
# SAVE CHAT HISTORY
# ============================================================

def save_chat(user, message):
    with open("chat_history.txt", "a", encoding="utf-8") as file:
        file.write(f"{user} : {message}\n")


# ============================================================
# DATE
# ============================================================

def current_date():

    today = datetime.datetime.now()

    return today.strftime("%d-%m-%Y")


# ============================================================
# TIME
# ============================================================

def current_time():

    now = datetime.datetime.now()

    return now.strftime("%I:%M:%S %p")


# ============================================================
# RANDOM JOKES
# ============================================================

jokes = [

    "Why do programmers prefer dark mode? Because light attracts bugs!",

    "Why did the Python programmer wear glasses? Because he couldn't C.",

    "Debugging is like being the detective in a crime movie where you are also the criminal.",

    "Why don't robots get scared? Because they have nerves of steel."

]


# ============================================================
# MOTIVATION
# ============================================================

motivations = [

    "Success comes from consistency.",

    "Believe in yourself. Every expert was once a beginner.",

    "Practice today, achieve tomorrow.",

    "Small progress every day leads to big success.",

    "Never stop learning."

]


# ============================================================
# RANDOM QUOTES
# ============================================================

quotes = [

    "Dream big and dare to fail.",

    "Knowledge is power.",

    "Hard work beats talent when talent doesn't work hard.",

    "Stay hungry, stay foolish.",

    "The future depends on what you do today."

]


# ============================================================
# PROGRAMMING INFORMATION
# ============================================================

languages = {

    "python": "Python is a high-level programming language used in AI, Data Science, Automation and Web Development.",

    "java": "Java is an Object-Oriented Programming language used for Android and Enterprise Applications.",

    "c": "C is a procedural programming language widely used for System Programming.",

    "c++": "C++ supports Object-Oriented Programming and is widely used in Game Development.",

    "html": "HTML is used to create the structure of web pages.",

    "css": "CSS is used to design beautiful web pages.",

    "javascript": "JavaScript makes websites interactive.",

    "sql": "SQL is used to manage relational databases."

}


# ============================================================
# STUDY TIPS
# ============================================================

study_tips = [

    "Revise daily instead of studying everything at the last moment.",

    "Love your self !",

    "Practice previous year papers.",

    "Take short breaks after every 45-60 minutes.",

    "Focus on understanding concepts rather than memorizing.",

    "Avoid mobile distractions while studying."

]


# ============================================================
# HELP MENU
# ============================================================

def help_menu():

    print(f"""{CYAN}

================= HELP MENU =================

hello / hi

how are you

your name

date

time

joke

quote

motivate me

study tips

python

java

c

c++

html

css

javascript

sql

calculate

bye

=============================================

{RESET}""")


# ============================================================
# CALCULATOR
# ============================================================

def calculator():

    bot_print("Enter expression like 25+10 or 50/2 for do Task")

    expression = input(f"{YELLOW}Calculator : {RESET}")

    # Fix: restrict eval so only numbers/operators can run, not arbitrary code
    allowed_chars = set("0123456789+-*/(). ")
    if not set(expression) <= allowed_chars:
        bot_print("Invalid Expression. Only numbers and + - * / ( ) are allowed.")
        return

    try:
        answer = eval(expression, {"__builtins__": {}}, {})
        bot_print(f"Result = {answer}")
    except ZeroDivisionError:
        bot_print("Error: Division by zero is not allowed.")
    except Exception:
        bot_print("Invalid Expression.")


# ============================================================
# WELCOME SCREEN
# ============================================================

print(f"""{BLUE}

==================================================================
        SMART RULE-BASED PYTHON CHATBOT FOR CODE ALPHA INTERNSHIP
==================================================================

Hello!

I'm SmartBot Created by Pankaj.

Type 'help' to see all commands.

Type 'bye' to exit.

====================================================

{RESET}""")

username = input("Enter your name : ")

bot_print(f"Welcome {username}! Nice to meet you!  How can i help you? ")
save_chat("Bot", f"Welcome {username}")


# ============================================================
# MAIN CHATBOT LOOP
# ============================================================

while True:

    user = input(f"{YELLOW}{username} : {RESET}").strip().lower()

    save_chat(username, user)

    # --------------------------------------------------------
    # EXIT
    # --------------------------------------------------------

    if user in ["bye", "exit", "quit"]:

        bot_print(f"Goodbye {username}! Have a wonderful day.")
        save_chat("Bot", "Session Ended")
        break

    # --------------------------------------------------------
    # HELP
    # --------------------------------------------------------

    elif user == "help":

        help_menu()

    # --------------------------------------------------------
    # GREETING
    # --------------------------------------------------------

    elif user in ["hello", "hi", "hey", "good morning", "good evening"]:

        greetings = [

            f"Hello {username}! ",

            f"Hi {username}! Nice to see you.",

            f"Welcome back {username}.",

            f"Hey {username}! How can I help you today?"

        ]

        bot_print(random.choice(greetings))

    # --------------------------------------------------------
    # HOW ARE YOU
    # --------------------------------------------------------

    elif user == "how are you":

        bot_print("I'm doing great! Thanks for asking.")

    # --------------------------------------------------------
    # BOT NAME
    # --------------------------------------------------------

    elif user in ["your name", "what is your name", "who are you"]:

        bot_print("I am SmartBot, a Python Rule-Based Chatbot.")

    # --------------------------------------------------------
    # CREATOR
    # --------------------------------------------------------

    elif user in ["who made you", "creator"]:

        bot_print("I was created using Python for an internship project by Pankaj.")

    # --------------------------------------------------------
    # DATE
    # --------------------------------------------------------

    elif user == "date":

        bot_print(f"Today's Date : {current_date()}")

    # --------------------------------------------------------
    # TIME
    # --------------------------------------------------------

    elif user == "time":

        bot_print(f"Current Time : {current_time()}")

    # --------------------------------------------------------
    # JOKE
    # --------------------------------------------------------

    elif user == "joke":

        bot_print(random.choice(jokes))

    # --------------------------------------------------------
    # QUOTE
    # --------------------------------------------------------

    elif user == "quote":

        bot_print(random.choice(quotes))

    # --------------------------------------------------------
    # MOTIVATION
    # --------------------------------------------------------

    elif user in ["motivate me", "motivation"]:

        bot_print(random.choice(motivations))

    # --------------------------------------------------------
    # STUDY TIPS
    # --------------------------------------------------------

    elif user == "study tips":

        bot_print(random.choice(study_tips))

    # --------------------------------------------------------
    # WEATHER
    # --------------------------------------------------------

    elif user == "weather":

        bot_print("Sorry, I cannot access live weather without internet.")

    # --------------------------------------------------------
    # CALCULATOR
    # --------------------------------------------------------

    elif user == "calculate":

        calculator()

    # --------------------------------------------------------
    # PROGRAMMING LANGUAGES
    # --------------------------------------------------------

    elif user in languages:

        bot_print(languages[user])

    # --------------------------------------------------------
    # THANK YOU
    # --------------------------------------------------------

    elif user in ["thanks", "thank you"]:

        bot_print("You're welcome! ")

    # --------------------------------------------------------
    # GOOD
    # --------------------------------------------------------

    elif user == "good":

        bot_print("Glad to hear that!")

    # --------------------------------------------------------
    # BAD
    # --------------------------------------------------------

    elif user == "bad":

        bot_print("Don't worry. Tomorrow will be better.")

    # --------------------------------------------------------
    # AGE
    # --------------------------------------------------------

    elif user == "your age":

        bot_print("Bots don't have age ")

    # --------------------------------------------------------
    # FAVOURITE LANGUAGE
    # --------------------------------------------------------

    elif user in ["favorite language", "favourite language"]:

        bot_print("Python is one of my favorite programming languages.")

    # --------------------------------------------------------
    # AI
    # --------------------------------------------------------

    elif user == "ai":

        bot_print("Artificial Intelligence enables machines to simulate human intelligence.")

    # --------------------------------------------------------
    # MACHINE LEARNING
    # --------------------------------------------------------

    elif user == "machine learning":

        bot_print("Machine Learning allows computers to learn from data.")

    # --------------------------------------------------------
    # DATA SCIENCE
    # --------------------------------------------------------

    elif user == "data science":

        bot_print("Data Science combines statistics, programming and machine learning.")

    # --------------------------------------------------------
    # WEB DEVELOPMENT
    # --------------------------------------------------------

    elif user == "web development":

        bot_print("Web Development involves HTML, CSS, JavaScript and backend technologies.")

    # --------------------------------------------------------
    # UNKNOWN COMMAND
    # --------------------------------------------------------

    else:

        responses = [

            "Sorry, I don't understand that.",

            "Please type 'help' to see available commands.",

            "I'm still learning. Try another command.",

            "I couldn't recognize your request."

        ]

        bot_print(random.choice(responses))