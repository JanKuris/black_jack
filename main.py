import random
from replit import clear
from art import logo 
def game():
    def card():
        cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
        number = random.choice(cards)
        return number
    
    def adjust_ace(hand):
        if 11 in hand and sum(hand) > 21:
            hand.remove(11)
            hand.append(1)
            
    player_hand = []
    player_hand.append(card())
    player_hand.append(card())
    dealer_hand = []
    dealer_hand.append(card())
    dealer_hand.append(card())
    dealer_value = sum(dealer_hand)
    print(f"Your card is {player_hand} current score is {sum(player_hand)}")
    print(f"Dealers first card: {dealer_hand[0]}")

    black_jack = True
    while black_jack == True:
        another_card = input("Do you want to get another card? Type 'y' or 'n': ").lower()
        if another_card == "y":
            player_hand.append(card())
            adjust_ace(player_hand)
            print(f"Your card is {player_hand} current score is {sum(player_hand)}")
            print(f"Dealers first card: {dealer_hand[0]}")
        elif another_card == "n":
            dealer_value = sum(dealer_hand)
            player_value = sum(player_hand)
    
            while dealer_value < 17:
                dealer_hand.append(card())
                adjust_ace(dealer_hand)  
                dealer_value = sum(dealer_hand)
        
            print(f"Player = {player_value}")
            print(f"Dealer = {dealer_value} and {dealer_hand}")
            
            if player_value == dealer_value:
                print("Draw")
                black_jack = False
            elif player_value == 21:
                print("You win")
                black_jack = False
            elif dealer_value > 21 and player_value <= 22:
                print("You win")
                black_jack = False
            elif player_value >= 22 and dealer_value >= 22:
                if dealer_value > player_value:
                    print("Dealer wins")
                    black_jack = False
                elif dealer_value == player_value:
                    print("Draw")
                    black_jack = False
            elif player_value > 21 and dealer_value < 22:
                print("Dealer wins")
                black_jack = False
            elif player_value < 22 and dealer_value > 21:
                print("You win")
                black_jack = False
            elif player_value < dealer_value:
                print("Dealer wins")
                black_jack = False
            else:
                print("You win")
                black_jack = False
new_game = True
while new_game:
    new_game = input("Do you want to play new game? (y/n)").lower()
    clear()
    print(logo)
    if new_game == 'y':
        game()
        
    else: 
        new_game = False





        


