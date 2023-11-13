import pygame, random
from src.Dependencies import *
from src.constants import *
from src.Room import Room

class Floor():
    def __init__(self, level, monster_deck):
        self.floor_lvl = level
        #self.name = to be written in constants.py
        #self.description = to be written in constants.py
        self.monster_deck = monster_deck # no deck class yet
        
        root_room_id = int(str(self.floor_lvl)+'0'+'0')
        self.root_room = Room(root_room_id, self.floor_lvl, None, None)
        
    
    def generate(self):
        room_set_list = [] # e.g. [1,3,2]
        for set in range(3):
            room_amount = random.randint(1,3)
            room_set_list.append(room_amount)
            
        floor = []
        depth = 0
        for i in range(len(room_set_list)):
            room_list = []
            for j in range(room_set_list[i]):
                room_id = int(str(self.floor_lvl)+str(i+1)+str(j+1))
                if depth == 0:
                    Room(room_id,self.floor_lvl,None,self.root_room)
                else:
                    pass
                room_list.append
                
                
                
    
    def update(self, dt, events):
        pass
    
    def render(self, screen):
        pass
    