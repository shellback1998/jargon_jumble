import random

word_bank = [
    ("standup", "Every morning, our fifteen-minute ____ meeting lasts until lunch."),
    ("syntax", "One missing bracket, and Python hits me with a ____ error."),
    ("debug", "I spent four hours trying to ____ my code."),
    ("deploy", "It's Friday at 5pm, definitely the best time to ____ new code."),
    ("bandwidth", "Sorry boss, I can't take on more work. I just don't have the ____."),
    ("meeting", "That ninety-minute ____ could have been an email."),
    ("deadline", "Of course we'll hit the ____, no problem!"),
    ("backup", "We finally made a ____ of everything, the day after the laptop died."),
    ("server", "I'm getting a 500 error, which means the ____ is down again."),
    ("prototype", "It's just an early ____, so please ignore that clicking anywhere crashes it."),
    ("algorithm", "A set of rules to be followed in calculations or problem-solving."),
    ("database", "I need to query the ____ to find out why the records are missing."),
    ("compiler", "A program that translates source code into machine code."),
    ("framework", "A supporting structure used to build applications more efficiently."),
    ("firewall", "A network security system that monitors and controls incoming traffic."),
    ("latency", "The delay before a transfer of data begins following an instruction."),
    ("terminal", "I prefer typing commands directly into the ____ rather than using a GUI."),
    ("interface", "The point where two systems, subjects, or programs meet and interact."),
    ("repository", "We keep all our version-controlled code in a central ____."),
    ("hardware", "The physical components that make up a computer system."),
    ("boolean", "A data type that has one of two possible values: true or false."),
    ("variable", "A named storage location in memory for data."),
    ("function", "A block of organized, reusable code used to perform a single action."),
    ("compiler", "The tool that turns human-readable code into machine-executable binaries."),
    ("encryption", "The process of converting information into a code to prevent unauthorized access."),
    ("binary", "A numbering system that represents data using only zeros and ones."),
    ("browser", "Software used to access information on the World Wide Web."),
    ("cache", "A small, fast memory component used to speed up data access."),
    ("cloud", "Storing and accessing data over the internet instead of on a hard drive."),
    ("cookies", "Small files stored on your computer by websites to track your activity."),
    ("domain", "The human-readable address of a website, like google.com."),
    ("frontend", "The part of a website that the user interacts with directly."),
    ("backend", "The part of a website that handles data and server-side logic."),
    ("git", "The industry-standard tool for version control."),
    ("kernel", "The core part of an operating system that manages system resources."),
    ("library", "A collection of pre-written code that developers can use."),
    ("malware", "Software designed to cause damage to a computer or network."),
    ("network", "A group of computers connected together to share resources."),
    ("open", "A type of source code that is made freely available for possible modification."),
    ("packet", "A small unit of data sent over a network."),
    ("pixel", "The smallest unit of a digital image or display."),
    ("query", "A request for information from a database."),
    ("ram", "The computer's short-term memory."),
    ("script", "A series of commands that a program follows to automate tasks."),
    ("software", "Programs and other operating information used by a computer."),
    ("syntax", "The set of rules that defines the combinations of symbols in a language."),
    ("thread", "A sequence of programmed instructions that can be managed independently."),
    ("upload", "Transferring data from your computer to another system."),
    ("virtual", "Something simulated by a computer, often referring to machines or reality."),
    ("website", "A collection of related web pages under a single domain name.")
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