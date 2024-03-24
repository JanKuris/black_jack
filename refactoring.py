import random
from replit import clear
from art import logo 

def card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    number = random.choice(cards)
    return number

def gameStart():
    player_hand = []
    player_hand.append(card())
    player_hand.append(card())
    dealer_hand = []
    dealer_hand.append(card())
    dealer_hand.append(card())
    dealer_value = sum(dealer_hand)
    print(f"Your card is {player_hand} current score is {sum(player_hand)}")
    print(f"Dealers first card: {dealer_hand[0]}")

def dealingCards(player_hand, dealer_hand, cards):
    another_card = input("Do you want to get another card? Type 'y' or 'n': ").lower()
    if another_card == "y":
        player_hand.append(card())
        print(f"Your card is {player_hand} current score is {sum(player_hand)}")
    elif another_card == "n":
        dealer_value = sum(dealer_hand)
        player_value = sum(player_hand)

    if dealer_value < 17:
        dealer_hand.append(card())
        dealer_value = sum(dealer_hand)

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
        return sum(cards)
    
    return dealer_value, player_value


def compare(dealer_value, player_value):
#this fnc return boolens 
    if player_value == dealer_value:
        print("Draw")
    elif player_value == 21:
        print("You win")
    elif dealer_value > 21 and player_value <= 22:
        print("You win")
    elif player_value > 21 and dealer_value > 21:
        print("You went over. You lose")
    elif player_value > 21 and dealer_value < 22:
        print("Dealer wins1")
    elif player_value < 22 and dealer_value > 21:
        print("You win2")
    elif player_value < dealer_value:
        print("Dealer wins")
    else:
        print("You win1")

print(logo)
black_jack = True
while black_jack:
    gameStart()
    
    



