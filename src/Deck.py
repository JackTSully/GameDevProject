import pygame, random, sys, os
from constants import *
from Dependencies import *
from Card import *

class Deck:
    def __init__(self, deck_id, deck_type, cards):
        self.deck_id = deck_id
        self.type = deck_type
        self.cards = cards
    
    def render(self):
        for card in self.cards:
            print(f"Card ID: {card.card_id}, Name: {card.name}, Description: {card.description}")


main_deck = Deck(list_of_cards)
main_deck.render()

print(main_deck)