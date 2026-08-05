import random
from hangman_art import stages , logo
from hangman_words import word_list

lives=6

print(logo)

random_word=random.choice(word_list)
print(random_word)

## placeholder for the blanks
placeholder=""
word_length=len(random_word)
for position in range(word_length):
    placeholder+="_"
print(placeholder)

game_over = False

correct_letter=[]

while not game_over:

    print(f"**********************************{lives}/6 LIVES LEFT ************************************")
    letter=input("Guess a letter :").lower()

    ## putting the guessed letters in the right positions

    if letter in correct_letter:
        print(f"You've already guessed {letter}")

    display=""

    for n in random_word:
        if n==letter:
            display+=n
            correct_letter.append(letter)
        elif n in correct_letter:
            display+=n
        else:
            display+="_"

    print("Word to guess: " +display)

    if letter not in random_word:
        lives-=1
        print(f"You guessed {letter}, that's not in the word. You lose a life.")
        if lives==0:
            game_over = True
            print(f"*************** It was {random_word}! You lose ****************")

    if "_" not in display:
        game_over = True
        print("******************* You Win *****************")

    print(stages[lives])