import random

word_bank = [
    ("standup", "Every morning, our fifteen-minute ____ meeting lasts until lunch."),
    ("syntax", "One missing bracket, and Python hits me with a ____ error."),
    ("debug", "I spent four hours trying to ____ my code. Turns out I was missing comma."),
    ("deploy", "It's Friday at 5pm, definitely the best time to ____ new code."),
    ("bandwidth", "Sorry boss, I can't take on more work. I just don't have the ____."),
    ("meeting", "That ninety-minute ____ could have been an email."),
    ("deadline", "Of course we'll hit the ____, no problem! Well, within a couple of days. Maybe a week."),
    ("backup", "We finally made a ____ of everything, the day after the laptop died."),
    ("server", "I'm getting a 500 error, which means the ____ is down again."),
    ("prototype", "It's just an early ____, so please ignore that clicking anywhere crashes it."),
]

ROUNDS = 5
round_num = 1
used = []  # 1. Track used pairs

while round_num <= ROUNDS:

    # 2. Keep picking until we find an unused pair
    pair = random.choice(word_bank)
    while pair in used:
        pair = random.choice(word_bank)

    # 3. Mark as used
    used.append(pair)
    word, hint = pair

    letters = list(word)
    random.shuffle(letters)
    scrambled_word = "".join(letters).upper()

    print(f"\n--- Round {round_num} ---")
    print(f"Scrambled: {scrambled_word}")

    guess = input("Guess the word (or type 'hint' / 'skip' / 'quit'): ").strip().lower()

    if guess == "quit":
        print("Thanks for playing!")
        break
    elif guess == "hint":
        print(f"\n💡 Hint: {hint}")
        guess = input("Your guess (or 'skip' / 'quit'): ").strip().lower()
        if guess == "quit":
            print("Thanks for playing!")
            break

    if guess == "skip":
        print(f"Skipped! The word was '{word}'.")
    elif guess == word:
        print("✅ Correct!")
    else:
        print(f"❌ Sorry, the word was '{word}'.")

    round_num += 1