from blackjack_art import logo
import random
import os


def deal_card():
    """
    return a random card
    """
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(cards):
    """
    take a list of card as input and returen the socer from the cards. check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game. check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1.
    """
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def compare(user_score, computer_score):
    """
    compare scores between user and computer and show the result of the game.
    """
    if user_score > 21 and computer_score > 21:
        return "You went over. You lose 😤"
    elif user_score == computer_score:
        return "Draw 🙃"
    elif computer_score == 0:
        return "Lose, opponent has Blackjack 😱"
    elif user_score == 0:
        return "Win with a Blackjack 😎"
    elif user_score > 21:
        return "You went over. You lose 😭"
    elif computer_score > 21:
        return "Opponent went over. You win 😁"
    elif user_score > computer_score:
        return "You win 😃"
    else:
        return "You lose 😤"


def play_game():
    """
    main play game function.
    """
    print(logo)

    # deal the user and computer 2 cards each
    user_cards = []
    computer_cards = []
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    # score rechecked with every new card drawn
    while not is_game_over:
        # if the computer has blackjack or if user's score is over 21 the the games end.
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f" Your cards: {user_cards}, Current Score: {user_score} ")
        print(
            f" Computer cards: {computer_cards}, Current Score: {computer_score} ")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input(
                "Type 'y' to get another card or type 'n' to pass:  ")
            if user_should_deal == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    # User is done. Now it's computer time until computer score less than 17
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f" Your final hand: {user_cards}, Final Score: {user_score} ")
    print(
        f" Computer final hand: {computer_cards}, Final Score: {computer_score} ")
    print(compare(user_score, computer_score))

# ask the user to restart the game. if answer is yes the clear the screan and star new game.


while input("Do you want to play a game of Blackjack? Type 'y' or 'n' \n=> ") == "y":
    os.system('cls' if os.name == 'nt' else 'clear')
    play_game()