from dataclasses import dataclass
from rich.console import Console
import typing
import random

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
    return deck

def war():
    '''Play an interactive game of War'''
    deck = generate_deck()

    # Shuffle the deck
    random.shuffle(deck)
    
    # Initialize each player's deck
    my_cards = deck[:int(len(deck)/2)]
    opp_cards = deck[int(len(deck)/2):]

    # Initialize each player's stack of cards being used in war
    my_war_stack: list[Card] = list()
    opp_war_stack: list[Card] = list()

    while len(my_cards) > 0 and len(opp_cards) > 0:
        go = input('Press any key to make your next move.')
        my_card: Card = my_cards.pop()
        opp_card: Card = opp_cards.pop()
        
        console.print('Your card is:', my_card.name)
        console.print("Your opponent's card is:", opp_card.name)

        if my_card.value > opp_card.value:
            my_cards = [my_card, opp_card] + my_war_stack + opp_war_stack + my_cards
            my_war_stack = list()
            opp_war_stack = list()

        elif my_card.value < opp_card.value:
            opp_cards = [my_card, opp_card] + my_war_stack + opp_war_stack + opp_cards
            my_war_stack = list()
            opp_war_stack = list()

        elif my_card.value == opp_card.value:
            console.print('War!')
            my_war_stack.append(my_card)
            opp_war_stack.append(opp_card)
            my_war_stack.extend(my_cards[-3:])
            opp_war_stack.extend(opp_cards[-3:])
            my_cards = my_cards[:-3]
            opp_cards = opp_cards[:-3]

    if len(opp_cards) == 0:
        console.print('You win!')
    elif len(my_cards) == 0:
        console.print('Your opponent wins!')
    

if __name__ == '__main__':
    war()
