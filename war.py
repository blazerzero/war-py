from dataclasses import dataclass
from rich.console import Console
import numpy as np
import typing

@dataclass
class Card:
    name: str
    value: int

console = Console()

def generate_deck():
    '''Generates the deck of cards'''

    deck: list[Card] = list()
    
    # Define suits and cards
    suits = ['heart', 'diamond', 'spade', 'club']
    cards = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']

    # Add 2 through 10, plus Jack, Queen, King, and Ace, to the deck for each suit
    for suit in suits:
        for i, card in enumerate(cards):
            deck.append(Card(card, i+1))

    # Return the deck
    return np.array(deck)

def war():
    '''Play an interactive game of War'''
    deck = generate_deck()

    # Shuffle the deck
    np.random.shuffle(deck)

if __name__ == '__main__':
    war()
