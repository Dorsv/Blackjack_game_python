from random import randint
from time import sleep


class Card():
    '''
    creates card object
    takes in: face name (number and suit) and value/s
    '''
    def __init__(self, face, value1, value2=0):
        self.name = face
        self.value1 = value1
        self.value2 = value2 

    def __str__(self):
        '''
        Returns face and it's value
        '''
        if self.value2 == 0:
            return f"{self.name} value: {self.value1}"
        else:
            return f"{self.name} value: {self.value1} or {self.value2}"


class Player():
    '''
    creates player object
    takes in name and optional cash amount
    '''
    def __init__(self, name, cash=500):
        self.cash = cash
        self.name = name
    
    def __str__(self):
        '''
        returns player's name and balance
        '''
        return f"Player: {self.name}\nBalance: {self.cash}$"

    def double_cash(self):
        self.cash = self.cash*2

    def create_hand(self, card1, card2):
        '''
        creates hand attribute
        takes in 2 card object from Card class
        '''
        self.hand = list((card1, card2))

    def hit(self, card):
        self.hand.append(card)

    def show_hand(self):
        '''
        prints out hand and it's value
        '''
        self.han_val = 0
        self.han_val2 = 0

        for card in self.hand:
            if card.value2 == 0:
                self.han_val += card.value1
                self.han_val2 += card.value1
            else:
                self.han_val += card.value1
                self.han_val2 += card.value2

        for card in self.hand:
            print("\n")
            print(card)
            sleep(0.5)
        if self.han_val == self.han_val2:
            print("\n")
            print("--------------------------")
            print(f"Total value: {self.han_val}")
        else:
            print("\n")
            print("--------------------------")
            print(f"Total value: {self.han_val}/{self.han_val2}")                



class Dealer():
    '''
    creates dealer object
    '''
    def __init__(self):
        pass

    def create_hand(self, card1, card2):
        '''
        creates hand attribute
        takes in 2 card object from Card class
        '''
        self.hand = list((card1, card2))

    def hit(self, card):
        self.hand.append(card)

    def show_hand(self):
        '''
        prints out hand and it's value
        '''

        self.han_val = 0
        self.han_val2 = 0

        for card in self.hand:
            if card.value2 == 0:
                self.han_val += card.value1
                self.han_val2 += card.value1
            else:
                self.han_val += card.value1
                self.han_val2 += card.value2

        for card in self.hand:
            print("\n")
            print(card)
            sleep(0.5)
        if self.han_val == self.han_val2:
            print("\n")
            print("--------------------------")
            print(f"Total value: {self.han_val}")
        else:
            print("\n")
            print("--------------------------")
            print(f"Total value: {self.han_val}/{self.han_val2}")      



def card_pick(deck):
    '''
    takes in a deck and removes random card returning it
    '''
    card_num = randint(0, len(deck)-1)
    return deck.pop(card_num)






# DEFINING STANDARD DECK OF 52 CARDS
suits = ["clubs", "diamonds", "hearts", "spades"]
faces = ["2","3","4","5","6","7","8","9","10","Jack","Queen","King","Ace"]
values = [1,2,3,4,5,6,7,8,9,10,11]


card_names = []
for suit in suits:
    for face in faces:
        name = face + ' of ' + suit
        card_names.append(name)

cards = []
for name in card_names:
    try:
        if int(name[0]) in values and int(name[:2]) != 10:
            card = (name, int(name[0]))
            cards.append(card) 
        elif "10" in name:
            card = (name, 10)
            cards.append(card)        
    except:
        if "King" in name:
            card = (name, 10)
            cards.append(card)
        elif "Queen" in name:
            card = (name, 10)
            cards.append(card)        
        elif "Jack" in name:
            card = (name, 10)
            cards.append(card)    
        elif "Ace" in name:
            card = (name, 11, 1)
            cards.append(card)    
    else:
        continue

deck = []

for card in cards:
    if len(card) == 2:
        deck.append(Card(card[0], card[1]))
    else:
        deck.append(Card(card[0], card[1], card[2]))


