import pygame, random
from src.Dependencies import *
from src.constants import *
from src.Room import Room

class Floor():
    def __init__(self, level, event_deck):
        self.floor_lvl = level
        #self.name = to be written in constants.py
        #self.description = to be written in constants.py
        self.event_deck = event_deck # no deck class yet
        
        start_room_id = int(str(self.floor_lvl)+'0')
        self.start_room = Room(start_room_id, self.floor_lvl, None, None)
        
        rooms = {
            'start' : self.start_room,
            'room1' : Room(int(str(self.floor_lvl)+"1"), self.floor_lvl, self.start_room, None),
            'room2' : Room(int(str(self.floor_lvl)+"2"), self.floor_lvl, self.start_room, None),
            'room3' : Room(int(str(self.floor_lvl)+"3"), self.floor_lvl, self.start_room, None),
        }
        
        self.rooms = rooms
        self.curr_room = self.rooms['start']
            
    
    def generate(self):
        pass
                
                
    
    def update(self, dt, events):
        pass
    
    def render(self, screen):
        pass
    