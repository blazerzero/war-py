from dataclasses import dataclass
from rich.console import Console
import random
import sys

# Modules for testing
import io
import time
from unittest import TestCase, mock, main

@dataclass
class Card:
    '''An individual card in the deck'''
    name: str # The name of the card
    value: int # The value of the card

console = Console() # Console logging with formatting

# Define suits and cards
suits = ['heart', 'diamond', 'spade', 'club']
cards = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']

def generate_deck():
    '''Generates the deck of cards'''

    deck: list[Card] = list()

    # Add 2 through 10, plus Jack, Queen, King, and Ace, to the deck for each suit
    for suit in suits:
        for i, card in enumerate(cards):
            deck.append(Card(card, i+1))

    # Return the deck
    return deck

class WarGameTests(TestCase):

    def testDeckLength(self):
        '''Tests that the deck has 52 cards'''
        deck = generate_deck()
        self.assertEqual(len(deck), 52) # Deck should have 52 cards
    
    def testCardsInDeck(self):
        '''Tests that the deck has 4 of each card'''
        deck = generate_deck()
        cards_in_deck = [c.name for c in deck]
        self.assertEqual([cards_in_deck.count(c) for c in cards], [4,4,4,4,4,4,4,4,4,4,4,4,4])

    @mock.patch('builtins.input', return_value='')
    def testPlay(self, _):
        '''Tests that the game of War runs successfully'''
        sys.stdout = io.StringIO()
        
        start = time.time()
        play()
        end = time.time()

        sys.stdout = sys.__stdout__
        console.print(f'The game took {end - start} seconds to run.')
        return


def play():
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

    # Indicate whether or not we're currently "at war"
    war = False

    console.print()
    while len(my_cards) > 0 and len(opp_cards) > 0:
        # The user presses a key to flip the next card and begin the battle
        # NOTE: I've separated the input statement from the actual input function
        # so that I can apply styling to the input statement.
        console.print('Press any key to flip your next card.', end="", style="bold blue")
        input()


        # Flip a card
        my_card: Card = my_cards.pop()
        opp_card: Card = opp_cards.pop()
        
        # Show what each player's card is
        console.print(f'Your card is: [bold]{my_card.name}[/bold]')
        console.print(f"Your opponent's card is: [bold]{opp_card.name}[/bold]")

        if my_card.value > opp_card.value:
            # The player wins the battle
            console.print(f'You win this {"war" if war else "battle"}!', style="green")
            my_cards = [my_card, opp_card] + my_war_stack + opp_war_stack + my_cards
            my_war_stack = list()
            opp_war_stack = list()
            war = False

            console.print(f'You have {len(my_cards)} cards')
            console.print(f'Your opponent has {len(opp_cards)} cards\n\n')

        elif my_card.value < opp_card.value:
            # The opponent wins the battle
            console.print(f'Your opponent wins this {"war" if war else "battle"}!', style="red")
            opp_cards = [my_card, opp_card] + my_war_stack + opp_war_stack + opp_cards
            my_war_stack = list()
            opp_war_stack = list()
            war = False

            console.print(f'You have {len(my_cards)} cards')
            console.print(f'Your opponent has {len(opp_cards)} cards\n\n')

        elif my_card.value == opp_card.value:
            # Cards tied; begin war
            war = True
            console.print('War! Place three cards face down!\n\n', style="bold red")
            my_war_stack.append(my_card)
            opp_war_stack.append(opp_card)
            my_war_stack.extend(my_cards[-3:])
            opp_war_stack.extend(opp_cards[-3:])
            my_cards = my_cards[:-3]
            opp_cards = opp_cards[:-3]

    # Check who won
    if len(opp_cards) == 0:
        console.print('You win!\n', style="bold green")
    elif len(my_cards) == 0:
        console.print('Your opponent wins!\n', style="bold red")
    

if __name__ == '__main__':
    if len(sys.argv) == 1:
        # Play the game
        play()
    elif sys.argv[1] == 'test':
        # Run the tests
        main(argv=['first-arg-is-ignored'], exit=False)
    else:
        # Invalid command-line arguments
        console.print('\n[ERROR: INVALID COMMAND LINE ARGUMENTS]', style="bold red")
        console.print('Valid command-line formats:\n', style="red")
        console.print('[bold blue]To play:[/bold blue] python war.py')
        console.print('[bold blue]To test:[/bold blue] python war.py test\n')
