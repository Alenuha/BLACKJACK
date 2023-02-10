import random
from art import logo


def deal():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calc_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards. append(1)
    return sum(cards)


def compare(score1, score2):
    if score1 > 21 & score2 > 21:
        return "You went over! You lose \U0001F62C"
    if score1 == 0:
        return "You've got BlackJack!!! \U0001F973"
    elif score2 == 0:
        return "Computer has BlackJack! Sorry! \U0001F622"
    elif score1 == score2 :
        return "It's a draw. \U0001F643"
    elif score2 > 21:
        return "You win! Computer went over. \U0001F603"
    elif score1 > 21:
        return "You went over! Computer wins \U0001F641"
    elif score1 > score2:
        return "You won! \U0001F603"
    else:
        return "Computer wins \U0001F641"


def play_game():
    print(logo)

    player_hand = []
    computer_hand = []
    game_on = True
    for c in range(2):
        new_card = deal()
        player_hand.append(deal())
        computer_hand.append(deal())


    while game_on:

        player_score = calc_score(player_hand)
        computer_score = calc_score(computer_hand)
        print(f"Your cards: {player_hand}, current score: {player_score}")
        print(f"Computer's first card is: {computer_hand[0]}")

        if player_score == 0 or computer_score == 0 or player_score >21:
            game_on = False
        else:
            game_continue = input("Type 'y' to get another card, or 'n' to pass: ")
            if game_continue == 'y':
                player_hand.append(deal())
            else:
                game_on = False


    while computer_score != 0 and computer_score < 17:
        computer_hand.append(deal())
        computer_score = calc_score(computer_hand)

    print(f"Your final hand is: {player_hand}. Final score: {player_score}")
    print(f"Computer's final hand: {computer_hand}. Score: {computer_score}")
    print(compare(player_score, computer_score))


while input("Would you like to play a game of BlackJack? 'y' or 'n': ") == 'y':
    play_game()
