import pygame, random
from src.Dependencies import *
from src.constants import *
from src.Room import Room
from src.Deck import Deck

class Floor():
    def __init__(self, level, name, event_deck: Deck):
        self.floor_lvl = level
        self.name = name
        #self.description = to be written in constants.py
        self.event_deck = event_deck
        
        self.cursor_position = (0, 0)
        self.pause = False
        
        start_room_id = int(str(self.floor_lvl)+'0')
        self.start_room = Room(start_room_id, self.floor_lvl, None, None)
        
        #self.event_deck.shuffle_deck()
        
        room1_cards = self.event_deck.draw_card(5)
        
        room2_cards = self.event_deck.draw_card(5)
        
        room3_cards = self.event_deck.draw_card(5)
        
        room1_deck = Deck('1', 'mixed', room1_cards)
        room2_deck = Deck('2', 'mixed', room2_cards)
        room3_deck = Deck('3', 'mixed', room3_cards)
        
        rooms = {
            'start' : self.start_room,
            'room1' : Room(int(str(self.floor_lvl)+"1"), self.floor_lvl, self.start_room, room1_deck),
            'room2' : Room(int(str(self.floor_lvl)+"2"), self.floor_lvl, self.start_room, room2_deck),
            'room3' : Room(int(str(self.floor_lvl)+"3"), self.floor_lvl, self.start_room, room3_deck),
            'boss'  : Room(int(str(self.floor_lvl)+"4"), self.floor_lvl, self.start_room, None),
        }
        
        self.rooms = rooms
        
        #print(rooms['room1'].event_deck)
        
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
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # 1 corresponds to the left mouse button

                for i, card in enumerate(self.curr_room.event_deck.cards):
                    x_offset, y_offset = 100 + i * 200, 450
                    frame_size = (140,200)
                    card_rect = pygame.Rect(x_offset, y_offset, frame_size[0], frame_size[1])

                    if card_rect.collidepoint(self.cursor_position):
                        self.card_index = i
                        self.selected_card = card
                        self.curr_room.event_deck.remove_card(self.card_index)
                        break
                else:
                    self.item_card_index = None
            
        self.cursor_position = pygame.mouse.get_pos()
    
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
        
        if self.curr_room != self.rooms['start'] and self.curr_room != self.rooms['boss']:
            x_offset = 100 #reset the position for the second line of cards
            y_offset = HEIGHT - 225
        
            i=0
            for card in self.curr_room.event_deck.cards:
        
                item_index = card.card_id 
                

                item_image = gsEnemies_Image_list[item_index-12] #-1 since the item index starts from 1 (line above)
                
                frame_image = gFrames_image_list[3]
                position = (x_offset, y_offset)
                final_card = self.curr_room.event_deck.render(frame_image, item_image) 
                screen.blit(final_card, position)
        
                x_offset += 200   
                i+=1
                
            if len(self.curr_room.event_deck.cards) == 3:
                for i in range(len(self.curr_room.event_deck.cards)-1):
                    card = random.choice(self.curr_room.event_deck.cards)
                    self.curr_room.event_deck.cards.remove(card)
                    
            if  len(self.curr_room.event_deck.cards) == 1:
                txt = self.curr_room.event_deck.cards[0].name
                text = gFonts['minecraft_small'].render(txt, False, (255, 255, 255))
                rect = text.get_rect(center=(WIDTH/2, HEIGHT -225))
                screen.blit(text, rect)
        
    