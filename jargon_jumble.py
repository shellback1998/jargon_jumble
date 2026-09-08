import random

word_bank = [
    ("standup", "Every morning, our fifteen-minute ____ meeting lasts until lunch."),
    ("syntax", "One missing bracket, and Python hits me with a ____ error."),
    ("debug", "I spent four hours trying to ____ my code."),
    ("deploy", "It's Friday at 5pm, definitely the best time to ____ new code."),
    ("bandwidth", "Sorry boss, I can't take on more work. I just don't have the ____."),
    ("meeting", "That ninety-minute ____ could have been an email."),
    ("deadline", "Of course we'll hit the ____, no problem!"),
    ("backup", "We finally made a ____ of everything."),
    ("server", "I'm getting a 500 error, which means the ____ is down again."),
    ("prototype", "It's just an early ____, so please ignore that clicking anywhere crashes it."),
]

ROUNDS = 5
best_score = 0  # In a real app, this would be loaded from a file!
used = []

while True:
    round_num = 1
    score = 0
    used = []

    print(f"\n--- Current Best Score: {best_score}/{ROUNDS} ---")

    while round_num <= ROUNDS:
        pair = random.choice(word_bank)
        while pair in used:
            pair = random.choice(word_bank)

        used.append(pair)
        word, hint = pair

        letters = list(word)
        random.shuffle(letters)
        scrambled_word = "".join(letters).upper()

        print(f"\nRound {round_num}")
        print(f"Scrambled: {scrambled_word}")

        guess = input("Guess (or 'hint' / 'skip' / 'quit'): ").strip().lower()

        if guess == "quit":
            break
        elif guess == "hint":
            print(f"\n💡 Hint: {hint}")
            guess = input("Your guess (or 'skip' / 'quit'): ").strip().lower()
            if guess == "quit":
                break

        if guess == "skip":
            print(f"Skipped! The word was '{word}'.")
        elif guess == word:
            print("✅ Correct!")
            score += 1
        else:
            print(f"❌ Sorry, the word was '{word}'.")

        round_num += 1

    # Update Best Score
    if score > best_score:
        best_score = score
        print("\n🏆 New High Score!")

    print(f"\nGame Over! Final Score: {score}/{ROUNDS}.")

    play_again = input("\nPlay again? (y/n): ").strip().lower()
    if play_again != 'y':
        print("Thanks for playing!")
        break