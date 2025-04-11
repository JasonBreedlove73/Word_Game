# 🔤 Word Combination Game (Python)

A fun, fast-paced terminal word game where each word must start with the last letter of the previous word! Challenge yourself and test your vocabulary under pressure.

---

## 🎮 How to Play

- You’ll be given a **starting word**.
- Your goal is to enter a word that **starts with the last letter** of the current word.
- You have **10 seconds** to respond each round.
- The game ends if:
  - You run out of time
  - You enter an invalid word
  - You submit a word that doesn't follow the rule

---

## 🧠 Example

Starting word: apple
Your word: elephant ✅
Your word: tiger ✅
Your word: rabbit ❌ (if "tiger" ends with 'r', this is valid)


---

## 🛠️ Requirements

- Python 3.x

No external libraries needed.

---

## 🚀 How to Run

1. Clone or download the script:

```bash
git clone https://github.com/your-username/word-combination-game.git
cd word-combination-game
Run the game:

bash
Copy
Edit
python word_game.py
💡 Features
⏱️ 10-second timer for each response

🧩 Word chain logic

🧠 Great for vocabulary practice

✅ Easy to modify or extend (e.g., with a word list validator)

🧰 File Structure
bash
Copy
Edit
word_game.py         # Main script containing the game logic
🚧 Possible Enhancements
Add a dictionary check for real words

Multiplayer mode

Save high scores

Add hints or a skip option
