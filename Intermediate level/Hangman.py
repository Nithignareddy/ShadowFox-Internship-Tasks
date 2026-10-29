import random

words = ["apple", "python", "computer", "school"]
word = random.choice(words)

guessed = ""
chances = 6

while chances > 0:
    display = ""

    for letter in word:
        if letter in guessed:
            display += letter
        else:
            display += "_"

    print("Word:", display)

    if "_" not in display:
        print("You won!")
        break

    guess = input("Guess a letter: ")
    guessed += guess

    if guess not in word:
        chances -= 1
        print("Wrong! Chances left:", chances)

if chances == 0:
    print("Game Over!")
    print("The word was:", word)