class Card :
    SPECIAL_CARDS = {11:"Jack",12:"Queen",13:"King",14:"Ace"}
    def __init__(self,suit,value):
        self._suit = suit 
        self._value = value 

    @property 
    def suit(self):
        return self._suit
    @property
    def value(self):
        return self._value
    def is_special(self):
        return self._value >= 11  
    def show(self):
        card_value = self._value
        card_suit = self._suit.description.capitalize() # method of suit class ,
        card_symbol = self._suit.symbol

        if self.is_special():
            card_description = Card.SPECIAL_CARDS[card_value]
            print(f"{card_value} of {card_suit} {card_symbol}")
        else :
            print(f"{card_value} of {card_suit} {card_symbol}")


