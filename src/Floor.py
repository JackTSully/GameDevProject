import pygame, random
from src.Dependencies import *
from src.constants import *
from src.Room import Room

class Floor():
    def __init__(self, level, name, event_deck):
        self.floor_lvl = level
        self.name = name
        #self.description = to be written in constants.py
        self.event_deck = event_deck # no deck class yet
        
        start_room_id = int(str(self.floor_lvl)+'0')
        self.start_room = Room(start_room_id, self.floor_lvl, None, None)
        
        rooms = {
            'start' : self.start_room,
            'room1' : Room(int(str(self.floor_lvl)+"1"), self.floor_lvl, self.start_room, None),
            'room2' : Room(int(str(self.floor_lvl)+"2"), self.floor_lvl, self.start_room, None),
            'room3' : Room(int(str(self.floor_lvl)+"3"), self.floor_lvl, self.start_room, None),
            'boss'  : Room(int(str(self.floor_lvl)+"4"), self.floor_lvl, self.start_room, None),
        }
        
        self.rooms = rooms
        
        for room in self.rooms:
            if room == 'start':
                prev_room = room
                continue
            rooms[room].set_prev_room(rooms[prev_room])
            prev_room = room
        
        self.curr_room = self.rooms['start']
        
    def get_floor_lvl(self):
        return self.floor_lvl
    
    def get_floor_name(self):
        return self.name
        
    
    def get_rooms(self):
        return self.rooms
    
    def get_curr_room(self):
        return self.curr_room
    
    def next_room(self):
        for room in self.rooms:
            if self.rooms[room].get_prev_room() == self.curr_room:
                self.curr_room = self.rooms[room]
                break
                
    
            
    
    def generate(self):
        pass
                
    
    def update(self, dt, events):
        pass
    
    def render(self, screen):
        
        start_color, room1_color, room2_color, room3_color, boss_color = 'red','red','red','red','red'
        
        if self.curr_room == self.rooms['start']:
            start_color = 'blue'
        elif self.curr_room == self.rooms['room1']:
            room1_color = 'blue'
        elif self.curr_room == self.rooms['room2']:
            room2_color = 'blue'
        elif self.curr_room == self.rooms['room3']:
            room3_color = 'blue'
        elif self.curr_room == self.rooms['boss']:
            boss_color = 'blue'
            
                
        
        
        #start room
        pygame.draw.rect(screen, start_color, pygame.Rect((1/3)*(WIDTH/2) - 30, HEIGHT/2 - 30, 60, 60))

        
        #3 rooms
        pygame.draw.rect(screen, room1_color, pygame.Rect((2/3)*(WIDTH/2) - 30, HEIGHT/2 - 30, 60, 60))
        pygame.draw.rect(screen, room2_color, pygame.Rect(WIDTH/2 - 30, HEIGHT/2 - 30, 60, 60))
        pygame.draw.rect(screen, room3_color, pygame.Rect((4/3)*(WIDTH/2) - 30, HEIGHT/2 - 30, 60, 60))

        
        #boss room
        pygame.draw.rect(screen, boss_color, pygame.Rect((5/3)*(WIDTH/2) - 30, HEIGHT/2 - 30, 60, 60))

        #lines
        pygame.draw.line(screen, 'white', ((1/3)*(WIDTH/2)+30, HEIGHT/2), ((2/3)*(WIDTH/2)-30, HEIGHT/2), width= 5)
        pygame.draw.line(screen, 'white', ((2/3)*(WIDTH/2)+30, HEIGHT/2), ((WIDTH/2)-30, HEIGHT/2), width= 5)
        pygame.draw.line(screen, 'white', ((WIDTH/2)+30, HEIGHT/2), ((4/3)*(WIDTH/2)-30, HEIGHT/2), width= 5)
        pygame.draw.line(screen, 'white', ((4/3)*(WIDTH/2)+30, HEIGHT/2), ((5/3)*(WIDTH/2)-30, HEIGHT/2), width= 5)
    