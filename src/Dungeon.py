import pygame, random
from src.Dependencies import *
from src.constants import *
from src.Floor import Floor
from src.Deck import Deck
from src.Card import ItemCard, AbilityCard, EventCard, EnemyCard

class Dungeon():
    def __init__(self):
        event_card_list = [EventCard(**item) for item in event_attributes]
        event_deck = Deck(1,'event',event_card_list*2)
        enemy_card_list = [EnemyCard(**item) for item in enemy_attributes]
        
        floor1_enemy_deck = Deck(1,'enemy',enemy_card_list[0:3]*3)
        floor1_enemy_deck.merge_with(event_deck) 
        floor1_event_deck = floor1_enemy_deck
        floor1_boss_deck = Deck(1,'enemy',[enemy_card_list[11]])
        
        
        floor2_enemy_deck = Deck(2,'enemy',enemy_card_list[3:6]*3)
        floor2_enemy_deck.merge_with(event_deck) 
        floor2_event_deck = floor2_enemy_deck
        floor2_boss_deck = Deck(2,'enemy',[enemy_card_list[12]])
        
        
        floor3_enemy_deck = Deck(3,'enemy',enemy_card_list[6:8]*4)
        floor3_enemy_deck.merge_with(event_deck) 
        floor3_event_deck = floor3_enemy_deck
        floor3_boss_deck = Deck(3,'enemy',[enemy_card_list[13]])
        
        
        floor4_enemy_deck = Deck(4,'enemy',enemy_card_list[8:11]*3)
        floor4_enemy_deck.merge_with(event_deck)
        floor4_event_deck = floor4_enemy_deck
        floor4_boss_deck = Deck(4,'enemy',[enemy_card_list[14]])
        
        
        floors = [
        Floor(1, "The Mines", floor1_event_deck,floor1_boss_deck),
        Floor(2, "The Catacombs", floor2_event_deck,floor2_boss_deck),
        Floor(3, "The Temple", floor3_event_deck,floor3_boss_deck),
        Floor(4, "The Jungle", floor4_event_deck,floor4_boss_deck),
        
        ]
        
        self.floors = floors
        self.curr_floor = self.floors[0]
        
        self.drawn_cards = None
    
    
    def Enter(self, params):
        item_card_list = [ItemCard(**item) for item in item_attributes]
        floor_item_deck = Deck(1,'item',item_card_list*3)
        floor_item_deck.shuffle_deck()
        self.curr_floor.set_floor_item_deck(floor_item_deck)
        if params == None:
            self.drawn_cards = floor_item_deck.draw_card(5)
        else:
            self.drawn_cards = floor_item_deck.draw_card(2)
    
    def get_drawn_cards(self):
        return self.drawn_cards
    
    def get_curr_floor(self):
        return self.curr_floor
    
    def next_floor(self):
        next_floor_index = self.curr_floor.get_floor_lvl()
        self.curr_floor = self.floors[next_floor_index]

    def update(self, dt, events):
        pass
        