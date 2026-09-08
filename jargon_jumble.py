import random

word_bank = [
    ("standup", "Every morning, our fifteen-minute ____ meeting lasts until lunch."),
    ("syntax", "One missing bracket, and Python hits me with a ____ error."),
    ("debug", "I spent four hours trying to ____ my code. Turns out I was missing comma."),
    ("deploy", "It's Friday at 5pm, definitely the best time to ____ new code."),
    ("bandwidth", "Sorry boss, I can't take on more work. I just don't have the ____."),
    ("meeting", "That ninety-minute ____ could have been an email."),
    # Added some custom pairs:
    ("algorithm", "A step-by-step procedure to solve a problem."),
    ("compiler", "It translates high-level code into machine language.")
]

# 1. Unpack the pair
word, hint = random.choice(word_bank)

# Scramble the word (using the first element of the tuple)
letters = list(word)
random.shuffle(letters)
scrambled_word = "".join(letters).upper()

print(f"Scrambled: {scrambled_word}")

# 2. Use a loop to keep the game going if a hint is requested
playing = True
while playing:
    guess = input("Guess the word (or type 'hint' or 'skip'): ").strip().lower()

    # 3. Handle 'hint' separately so the turn continues
    if guess == "hint":
        print(f"💡 Hint: {hint}")
    elif guess == "skip":
        print(f"Skipped! The word was '{word}'.")
        playing = False
    elif guess == word:
        print("✅ Correct!")
        playing = False
    else:
        print(f"❌ Sorry, that's not it. Try again!")
