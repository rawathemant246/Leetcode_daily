import collections
from random import choice
Card = collections.namedtuple('Cards',['rank','suit'])

class FrenchDeck():
    ranks = [str(n) for n in range(2,11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()
    
    def __init__(self):
        self._cards = [Card(rank,suit) for suit in self.suits
                       for rank in self.ranks]
        
    def __len__(self):
        return len(self._cards)
    
    def __getitem__(self, position):
        return self._cards[position]
    


# beer_card = Card('7','diamond')
# print(beer_card)

deck = FrenchDeck()
# print(len(deck))

# print(deck[0])
# print(deck[-1])

# print(choice(deck))

#Top 3 cards from new deck

# print(deck[:3])

#just picking up the Ace

# print(deck[12::13])

#__getitem__ iterbale

# for card in deck:
#     print(card)


#sorting the cards by ranks spades highest clubs lowest

suits_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)

def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suits_values) + suits_values[card.suit]

for card in sorted(deck,key=spades_high):
    print(card)
    

