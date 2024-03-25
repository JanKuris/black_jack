import random
from art import logo 
import os 

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def adjust_ace(hand):
        if 11 in hand and sum(hand) > 21:
            hand.remove(11)
            hand.append(1)

def print_score(player_hand, dealer_hand): 
    print(f"Your cards: {player_hand}, current score: {sum(player_hand)}")
    print(f"Dealer's first card: {dealer_hand[0]}")

def determine_winner(player_hand, dealer_hand):
    player_value = sum(player_hand)
    dealer_value = sum(dealer_hand)
    
    if player_value > 21:
        return "Player busts, Dealer wins!"
    elif dealer_value == 21 and len(dealer_hand) == 2:
         return "Dealer has a BLACK JACK!"
    elif player_value == 21 and len(player_hand) == 2:
         return "Player have a BLACK JACK!"
    elif dealer_value > 21 or player_value > dealer_value:
        return "Player wins!"
    elif dealer_value > player_value:
        return "Dealer wins!"
    else:
        return "It's a draw!"
def game():
    player_hand = [deal_card(), deal_card()]
    dealer_hand = [deal_card(), deal_card()]
    
    print_score(player_hand, dealer_hand)

    while sum(player_hand) < 22:
        another_card = input("Do you want to get another card? Type 'y' or 'n': ").lower()
        
        if another_card == "y":
            player_hand.append(deal_card())
            adjust_ace(player_hand)
            print_score(player_hand, dealer_hand)
        elif another_card == "n":
            while sum(dealer_hand) < 17:
                dealer_hand.append(deal_card())
                adjust_ace(dealer_hand) 
            print(f"Your final score is {sum(player_hand)}")
            print(f"Dealer's final score is: {sum(dealer_hand)}")
            print(determine_winner(player_hand, dealer_hand))
            return
        else:
            print("Invalid input. Please type 'y' or 'n'.")
play_again = True
while play_again:
    repeat = input("Do you want to play a new game? (y/n)").lower()
    clear_screen()
    print(logo)
    if repeat == 'y':
       game()
    elif repeat == "n":
        play_again = False
    else:
        play_again = True

#there is an issue with player black jack rule 
        


        


