#import pygame
#from src.Dependencies import *

class Room():
    def __init__(self, room_id, floor, room_event=None):
        self.room_id = room_id
        self.next_room = []
        self.room_event = room_event
        self.floor = floor
        
    def get_room_id(self):
        return self.room_id
    
    def append_next_room(self, room):
        self.next_room.append(room)
        
    def get_next_rooms(self):
        room_id_list = []
        for room in self.next_room:
            room_id = room.get_room_id()
            room_id_list.append(room_id)
        return room_id_list
    
    def update(self, dt, events):
        pass
    
    def render(self, screen):
        pass
    