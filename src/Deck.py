import pygame, random, sys, os
from src.constants import *
from src.Dependencies import *
from src.Card import Card, ItemCard, AbilityCard, EventCard, EnemyCard

class Deck():
    def __init__(self, deck_id, deck_type, cards : list):
        self.deck_id = deck_id
        self.type = deck_type
        self.cards = cards
        self.curr_card_index = 0
        
    
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
    
    def next_card(self):
        if self.curr_card_index+1 != len(self.cards):
            self.curr_card_index += 1
    
    def prev_card(self):
        if self.curr_card_index != 0:
            self.curr_card_index -= 1
    
    def shuffle_deck(self):
        random.shuffle(self.cards)
    
    def add_cards(self, cards: list):
        if isinstance(cards, list):
            self.cards.extend(cards)
        else:
            self.cards.append(cards)
    
    def remove_card(self, card_index):
        del self.cards[card_index]
        
    def get_card(self, card_index) -> Card:
        return self.cards[card_index]
    
    def merge_with(self, deck):
        #self.type = [self.type, deck.get_deck_type())
        self.type = 'mixed'
        self.cards.extend(deck.get_cards())
    
    def draw_card(self, amount):
        card_list = []
        for i in range(amount):
            drawn_card = random.choice(self.cards)
            card_list.append(drawn_card)
            self.cards.remove(drawn_card)
        return card_list   
    
    
    def render(self,frame_image, card_image):
        frame_surface = pygame.Surface((frame_image.get_width(), frame_image.get_height())) #Create a surface (rectangle) same size as the frame_image (Just to combine the item and the frame as one)
        frame_surface.blit(frame_image, (0, 0))  #put frame on to the surface at pos (0,0)
        
        item_x = max(0, (frame_image.get_width() - card_image.get_width()) // 2) #pos of item on surface
        item_y = max(0, (frame_image.get_height() - card_image.get_height()) //6)
        
        item_surface = pygame.Surface((frame_image.get_width(), frame_image.get_height()))
        item_surface.blit(card_image,(item_x, item_y)) #put item on to the surface
        item_surface.set_colorkey((0,0,0))
        item_surface.set_colorkey((0,0,0))
        
        frame_surface.blit(item_surface,(0,0))

        return frame_surface
