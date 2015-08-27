'''
shuffle_enhanced.py

Shuffle a deck of 52 cards
'''
import random

class Card:
    def __init__(self, suite, rank):
        self.suite = suite
        self.rank = rank
        
def initialize_deck():
    suites = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    ranks = ['Ace', '2', '3','4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
    cards = []
    for suite in suites:
        for rank in ranks:
            card = Card(suite, rank)
            cards.append(card)
    return cards

def shuffle_and_print(cards):
    random.shuffle(cards)
    for card in cards:
        print('{0} of {1}'.format(card.rank, card.suite))
    
if __name__ == '__main__':
    cards = initialize_deck()
    shuffle_and_print(cards)
