#!/usr/bin/python3

import random

# List of programming jokes
jokes = [
    "Why do Python programmers wear glasses? Because they can't C!",
    "I told my computer I needed a break, and it said: 'Why? I’m not even tired.'",
    "Why did the programmer quit his job? Because he didn’t get arrays.",
    "How many programmers does it take to change a light bulb? None. It's a hardware problem.",
    "I would tell you a joke about recursion... but you'd have to understand recursion first.",
    "Why do Java developers wear glasses? Because they can't C#.",
    "In Python, we don't do 'while(true)', we do 'for _ in iter(int, 1)'. Elegance matters.",
    "There are only 10 types of people in the world: those who understand binary, and those who don’t.",
    "I named my dog ‘Python’. Now I can say I have a snake as a pet and still sound techy.",
    "What's a programmer's favorite hangout place? The Foo Bar."
]

# Pick a random joke
random_joke = random.choice(jokes)

# Display the joke
print(random_joke)
print("\nRun me again for another laugh!\n")
