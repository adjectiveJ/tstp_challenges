"""
The Self-Taught Programmer - Chapter 10 Hangman
Author: Dante Valentine
Date: 7 June, 2021
"""

import random
def hangman(word):
    wrong = 0
    guessed = []
    stages = ["",
    " _____       ",
    "|     |      ",
    "|     |      ",
    "|     O      ",
    "|    /|\     ",
    "|    / \     ",
    "|            ",]
    rletters = list(word)
    board = ["__"] * len(word)
    win = False
    print("Welcome to Hangman\n")
    print((" ".join(board))+"\n")
    while wrong < len(stages)-1:
        print("\n")
        msg = "Guess a letter:\n > "
        char = input(msg)
        print("\n")
        if char in guessed:
            print("You've already tried that letter.\n")
        elif char in rletters:
            for idx, c in enumerate(rletters):
                if c == char:
                    board[idx] = char
        else:
            wrong += 1
        guessed.append(char)
        print((" ".join(board)))
        e = wrong + 1
        print("\n".join(stages[0:e]))
        if "__" not in board:
            print("You win! It was \"{}\".".format(word))
            win = True
            break
    if not win:
        print("\n".join(stages[0:wrong]))
        print("You lose! It was \"{}\".\n".format(word))

def main():
    words = []
    with open("hangmanwords.txt") as f:
        words = f.read().split("\n")
    again = "y"
    while again == "y":
        wind = random.randint(0,len(words)-1)
        chosen = words[wind]
        hangman(chosen)
        again = input("\nPlay again? (y or n):\n > ")
        again = again.lower()
        print()

if __name__ == "__main__":
    main()