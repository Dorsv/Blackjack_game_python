from scripts import *
from time import sleep



def game_of_blackjack():
# READY TO PLAY?    
    while True:
        try:
            print("\n"*2)
            response = input("Ready to play some Blackjack? (Y/N): ")
            if response != "Y" and response != "y":
                raise Exception("meh")
        except:
            continue
        else:
            break


# ASKING FOR PLAYERNAME AND DEFINING PLAYER AND DEALER OBJECTS
    print("\n"*2)
    player1_name = input("What is your name? : ")

    player1 = Player(name = player1_name)
    dealer = Dealer()
# INITIATING GAME 
    playing = True

    print("\n"*2)
    print("Let us begin!\nDealing Cards...")

    sleep(1.5)
# CREATING HANDS FOR PLAYER AND DEALER
    player1.create_hand(card_pick(deck), card_pick(deck))
    dealer.create_hand(card_pick(deck), card_pick(deck))
    player1_playing = True


    while playing:
# PLAYER'S TURN
        if player1_playing:
            print("\n"*2)
            print("Your hand:")
            sleep(1)
            player1.show_hand()

            # WIN FROM HAND = 21
            if player1.han_val == 21 or player1.han_val2 == 21:
                player1.double_cash()
                print("\n"*2)
                print(f"Seems like you have won!\n Your balance just doubled to {player1.cash}")
                playing = False
                player1_playing = False
                break

            # LOSE FROM HAND >21    
            if player1.han_val > 21 and player1.han_val2 > 21:
                player1.cash = 0
                print("\n"*2)
                print(f"Seems like you have lost!\n Your balance just went to 0$")
                playing = False
                player1_playing = False
                break

# DECISION STAND/HIT
            print("\n")
            reply = input("What would you like to do?\n(stand/hit): ")
            if reply == "hit":
                player1.hit(card_pick(deck))
                sleep(0.5)
            else:
# DEFINE PLAYER'S VALUE CLOSEST TO 21 AND ENDING PLAYERS TURN                
                player1_winning_val = 0
                if abs(21 - player1.han_val) >= abs(21 - player1.han_val2):
                    player1_winning_val = player1.han_val
                else:
                    player1_winning_val = player1.han_val2
                player1_playing = False
                continue
# DEALER'S TURN                
        elif player1_playing == False:
            sleep(2)
            print("\n"*2)
            print("Dealer's turn!")
            print("\n"*2)
            sleep(1)
            print("Dealer's hand:")
            sleep(1)
            print("\n")
            dealer.show_hand()

# DEALER WINNING FROM HAND = 21
            if dealer.han_val == 21 or dealer.han_val2 == 21:
                player1.cash = 0
                print("\n")
                print(f"Dealer has beaten {player1.name}!\nYour balance is now 0$")
                playing = False
                break

# DEALER LOSING FROM HAND > 21
            if dealer.han_val > 21 and dealer.han_val2 > 21:
                player1.double_cash()
                print("\n"*2)
                print(f"Seems like you have won!\n Your balance just doubled to {player1.cash}")
                playing = False
                break   
# DEFINING DEALER'S VALUE CLOSEST TO 21
            dealer_winning_val = 0
            if abs(21 - dealer.han_val) >= abs(21 - dealer.han_val2):
                dealer_winning_val = dealer.han_val
            else:
                dealer_winning_val = dealer.han_val2
# IF DEALER HAND IS WINNING - DEALER WIN
            if dealer_winning_val > player1_winning_val:
                player1.cash = 0
                print("\n")
                print(f"Dealer has beaten {player1.name}!\nYour balance is now 0$")
                playing = False
                break
# IF DEALER'S HAND IS WORSE THAN PLAYER'S  - HIT
            if dealer_winning_val <= player1_winning_val:
                print("\n")
                print("Dealer hits!")
                dealer.hit(card_pick(deck))
                sleep(2)
                               
                




game_of_blackjack()