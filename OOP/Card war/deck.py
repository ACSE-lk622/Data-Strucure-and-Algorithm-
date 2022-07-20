import random
from card import Card
from suit import Suit

#import class 

class Deck :
    
    SUITS =("clubs","diamonds","hearts","spades")
    
    def __init__(self,is_empty= False):
        self._cards = [] #Bottom [] #Top

        if not is_empty :
            self.build()
    
    @property
    def size(self):
        return len(self._cards)

    def build(self):
        for suit in Deck.SUITS:
            for value in range(2,15):
                self._cards.append(Card(Suit(suit),value)) # create Card object with suit and value 
    def show(self):
        for card in self._cards:
            card.show() #show method from card class 
    def shuffle(self):
        random.shuffle(self.cards) #shuffle function 
    def draw(self):
        if self._cards: #True when not empty 
            return self._cards.pop() # take the last of element in list 
        else :
            return None     
    def add(self,card):
        self._cards.insert(0,card)