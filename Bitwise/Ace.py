import random
from typing import Tuple
from itertools import product

suits = ['S', 'C', 'D', 'H']
ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

class Deck:
    def __init__(self) -> None:
        """Initialize a deck of cards"""
        self.cards = [(rank, suit) for rank, suit in product(ranks, suits)]

    def shuffle(self) -> None:
        """Shuffle a deck of cards"""
        self.cards = random.sample(self.cards, 52)

    def draw(self) -> Tuple[str, str]:
        """Draw a card from the deck"""
        return self.cards.pop()

    def isEmpty(self) -> bool:
        """Check if the deck has cards"""
        return self.cards == []

def simulation() -> int:
    deck = Deck()
    deck.shuffle()

    cards_drawn = 0

    # Keep drawing until we find an ace
    while not deck.isEmpty():
        suit, rank = deck.draw()
        cards_drawn += 1

        if suit == "A":
            return cards_drawn

    return cards_drawn

cards_needed = [simulation() for _ in range(10_000)]

# Get the expected number of cards until we draw our first ace
print(sum(cards_needed) / len(cards_needed))