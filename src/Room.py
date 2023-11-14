#import pygame
#from src.Dependencies import *
from src.Deck import Deck

class Room():
    def __init__(self, room_id, floor, prev_room=None, event_deck : Deck = None):
        self.room_id = room_id
        self.prev_room = prev_room
        self.event_deck = event_deck
        self.floor = floor
        
    def get_room_id(self):
        return self.room_id
       
    def get_prev_room(self):
        return self.prev_room
    
    def set_prev_room(self, prev_room):
        self.prev_room = prev_room
    
    def choose_event(self):
        #shows 5 cards and player discards 2
        #choose event randomly from the 3 cards left
        pass
    
        
    
    def update(self, dt, events):
        pass
    
    def render(self, screen):
        pass
    