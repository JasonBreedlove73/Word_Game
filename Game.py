import time
import random

def word_combination_game():
    print("🎮 Welcome to the Word Combination Game!")
    print("Each word must start with the last letter of the previous word.")
    print("You have 10 seconds to respond each round.")
    print("Let’s go!\n")

    # List of starting words
    starting_words = [
        "banana", "apple", "car", "river", "sun", "tiger", "keyboard",
        "house", "elephant", "mountain", "pizza", "laptop", "cloud"
    ]

    current_word = random.choice(starting_words)
    print(f"Your starting word is: **{current_word}**")

    score = 0
    time_limit = 10  # seconds

    while True:
        print(f"\nCurrent word: {current_word}")
        required_letter = current_word[-1]

        print(f"You have {time_limit} seconds to answer...")
        start_time = time.time()
        next_word = input(f"The next word must start with '{required_letter.upper()}': ").strip().lower()
        elapsed_time = time.time() - start_time

        if elapsed_time > time_limit:
            print(f"\n⏱️ Time's up! You took {elapsed_time:.2f} seconds. Game Over!")
            break

        if not next_word:
            print("No word entered. Game Over!")
            break

        if next_word.startswith(required_letter):
            score += 1
            print(f"✅ Great! '{current_word}' → '{next_word}' | Score: {score}")
            current_word = next_word
        else:
            print(f"❌ '{next_word}' does not start with '{required_letter}'. Game Over!")
            break

    print(f"\n🏁 Final Score: {score}")
    print("Thanks for playing!")

# Run the game
word_combination_game()





