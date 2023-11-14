import pygame, random, sys, os
from src.constants import *
from src.Dependencies import *
from src.Card import Card, ItemCard, AbilityCard, EventCard, EnemyCard

class Deck():
    def __init__(self, deck_id, deck_type, cards : list):
        self.deck_id = deck_id
        self.type = deck_type
        self.cards = cards
        
    
    def print_cards(self):
        for card in self.cards:
            card_name = card.get_name()
            print(card_name)
    
    def get_deck_id(self):
        return self.deck_id
    
    def get_deck_type(self):
        return self.type
    
    def get_cards(self):
        return self.cards
    
    def shuffle_deck(self):
        random.shuffle(self.cards)
    
    def add_cards(self, cards: list):
        self.cards.extend(cards)
    
    def merge_with(self, deck):
        #self.type = [self.type, deck.get_deck_type())
        self.type = 'mixed'
        self.cards.extend(deck.get_cards())
    
    def draw_card(self, amount):
        card_list = []
        for i in range(amount):
            drawn_card = random.choice(self.cards)
            card_list.append(drawn_card)
        return card_list
    
            
    
    
    def render(self):
        for card in self.cards:
            print(f"Card ID: {card.card_id}, Name: {card.name}, Description: {card.description}")
