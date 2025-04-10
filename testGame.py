def word_combination_game():
    print("Welcome to the Word Combination Game!")
    print("Rules: You will start with a word. The next word you enter must form a meaningful phrase or compound word with the previous one.")

    # Prompt the user for the first word
    current_word = input("Enter the starting word: ").strip().lower()

    while True:
        print(f"\nCurrent word: {current_word}")
        next_word = input("Enter the next word that forms a phrase with the current word: ").strip().lower()

        # You could add logic here to check if the combination is valid
        # For now, this is a freeform game where the user decides the combinations
        if next_word.startswith(current_word[-1]):
            print(f"Good job! '{current_word}' and '{next_word}' make a meaningful pair!")
            current_word = next_word  # Update the current word for the next round
        else:
            print(f"Oops! '{next_word}' does not start with '{current_word[-1]}'. Game Over!")
            break

    print("Thanks for playing!")