import random
from replit import clear
from art import logo

def game():
    def card():
        cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
        number = random.choice(cards)
        return number

    def adjust_ace(hand):
        # Check if there's an Ace in the hand
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
    print(f"Your cards are {player_hand}. Current score: {sum(player_hand)}")
    print(f"Dealer's first card: {dealer_hand[0]}")

    black_jack = True
    while black_jack:
        another_card = input("Do you want to get another card? Type 'y' or 'n': ").lower()
        if another_card == "y":
            player_hand.append(card())
            adjust_ace(player_hand)  # Adjust Ace value if needed
            print(f"Your cards are {player_hand}. Current score: {sum(player_hand)}")
        elif another_card == "n":
            dealer_value = sum(dealer_hand)
            player_value = sum(player_hand)

            while dealer_value < 17:
                dealer_hand.append(card())
                adjust_ace(dealer_hand)  # Adjust Ace value for dealer
                dealer_value = sum(dealer_hand)

            print(f"Player = {player_value}")
            print(f"Dealer = {dealer_value} and {dealer_hand}")

            if player_value == dealer_value:
                print("It's a draw!")
            elif player_value == 21:
                print("You win!")
            elif dealer_value > 21 or (player_value <= 21 and player_value > dealer_value):
                print("You win!")
            else:
                print("Dealer wins!")

            black_jack = False

game()
