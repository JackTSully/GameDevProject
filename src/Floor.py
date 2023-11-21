import pygame, random
from src.Dependencies import *
from src.constants import *
from src.Room import Room
from src.Deck import Deck
from src.Card import EnemyCard
pygame.mixer.pre_init(44100, -16, 2, 4096)
music_channel = pygame.mixer.Channel(0)
music_channel.set_volume(0.2)


class Floor():
    def __init__(self, level, name, event_deck: Deck, boss: Deck):
        self.floor_lvl = level
        self.name = name
        #self.description = to be written in constants.py
        self.event_deck = event_deck
        self.floor_item_deck = None
        
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
        boss_deck = boss
        
        rooms = {
            'start' : self.start_room,
            'room1' : Room(int(str(self.floor_lvl)+"1"), self.floor_lvl, self.start_room, room1_deck),
            'room2' : Room(int(str(self.floor_lvl)+"2"), self.floor_lvl, self.start_room, room2_deck),
            'room3' : Room(int(str(self.floor_lvl)+"3"), self.floor_lvl, self.start_room, room3_deck),
            'boss'  : Room(int(str(self.floor_lvl)+"4"), self.floor_lvl, self.start_room, boss_deck),
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
    
    def Enter(self):
        self.item_description = None
        self.item_description_show_right = True
        
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
    
    def set_floor_item_deck(self, item_deck : Deck):
        self.floor_item_deck = item_deck
    
            
    
    def generate(self):
        pass
                
    
    def update(self, dt, events):
        for event in events:
            for i, item_card in enumerate(self.curr_room.event_deck.cards):
                x_offset, y_offset = 100 + i * 200, HEIGHT-225
                frame_size = (140,200)
                card_rect = pygame.Rect(x_offset, y_offset, frame_size[0], frame_size[1])
                
                if event.type == pygame.MOUSEBUTTONDOWN:  # 1 corresponds to the left mouse button
                    if card_rect.collidepoint(self.cursor_position) and event.button == 1 and len(self.curr_room.event_deck.cards) > 3:
                        self.item_card_index = i
                        gSounds['item'].play(0) 
                        
                        self.curr_room.event_deck.remove_card(self.item_card_index)
                        break
                    elif card_rect.collidepoint(self.cursor_position) and event.button == 3:
                        self.item_card_index = i

                        self.item_description = self.curr_room.event_deck.get_card(self.item_card_index).description
                        if self.item_card_index > 2:
                            self.item_description_show_right = False

                        
                if event.type == pygame.MOUSEMOTION:
                    self.item_description = None
                    self.item_description_show_right = True
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
        text = gFonts['minecraft_card'].render("REST", False, "white")
        rect = text.get_rect(center=((1/3)*(WIDTH/2), HEIGHT/2))
        screen.blit(text, rect) 

        
        #3 rooms
        pygame.draw.rect(screen, room1_color, pygame.Rect((2/3)*(WIDTH/2) - 30, HEIGHT/2 - 30, 60, 60))
        text = gFonts['minecraft_tiny'].render("1", False, "white")
        rect = text.get_rect(center=((2/3)*(WIDTH/2), HEIGHT/2))
        screen.blit(text, rect)
        
        pygame.draw.rect(screen, room2_color, pygame.Rect(WIDTH/2 - 30, HEIGHT/2 - 30, 60, 60))
        text = gFonts['minecraft_tiny'].render("2", False, "white")
        rect = text.get_rect(center=((WIDTH/2), HEIGHT/2))
        screen.blit(text, rect)
        
        pygame.draw.rect(screen, room3_color, pygame.Rect((4/3)*(WIDTH/2) - 30, HEIGHT/2 - 30, 60, 60))
        text = gFonts['minecraft_tiny'].render("3", False, "white")
        rect = text.get_rect(center=((4/3)*(WIDTH/2), HEIGHT/2))
        screen.blit(text, rect)

        
        #boss room
        pygame.draw.rect(screen, boss_color, pygame.Rect((5/3)*(WIDTH/2) - 30, HEIGHT/2 - 30, 60, 60))
        text = gFonts['minecraft_card'].render("BOSS", False, "white")
        rect = text.get_rect(center=((5/3)*(WIDTH/2), HEIGHT/2))
        screen.blit(text, rect)

        #lines
        pygame.draw.line(screen, 'white', ((1/3)*(WIDTH/2)+30, HEIGHT/2), ((2/3)*(WIDTH/2)-30, HEIGHT/2), width= 5)
        pygame.draw.line(screen, 'white', ((2/3)*(WIDTH/2)+30, HEIGHT/2), ((WIDTH/2)-30, HEIGHT/2), width= 5)
        pygame.draw.line(screen, 'white', ((WIDTH/2)+30, HEIGHT/2), ((4/3)*(WIDTH/2)-30, HEIGHT/2), width= 5)
        pygame.draw.line(screen, 'white', ((4/3)*(WIDTH/2)+30, HEIGHT/2), ((5/3)*(WIDTH/2)-30, HEIGHT/2), width= 5)
        
        if self.curr_room != self.rooms['start']:
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
                
                card_name = card.name.split(" ")
                y = 0
                for string in card_name:
                    text = gFonts['minecraft_card'].render(string, False, ('black'))
                    rect = text.get_rect(center=(x_offset + 75 , y_offset + 142 + y))
                    screen.blit(text, rect)
                    y += 17
        
                x_offset += 200   
                i+=1
            
            if len(self.curr_room.event_deck.cards) > 3:
                text = gFonts['minecraft_small'].render("Discard 2 from the Event Pool", False, ('white'))
                rect = text.get_rect(bottomleft=(100 , HEIGHT - 225))
                screen.blit(text, rect)
                
            if len(self.curr_room.event_deck.cards) == 3:
                for i in range(len(self.curr_room.event_deck.cards)-1):
                    card = random.choice(self.curr_room.event_deck.cards)
                    self.curr_room.event_deck.cards.remove(card)
                    
            if  len(self.curr_room.event_deck.cards) == 1:
                txt = self.curr_room.event_deck.cards[0].name
                text = gFonts['minecraft_small'].render(txt, False, (255, 255, 255))
                rect = text.get_rect(center=(WIDTH/2, HEIGHT -225))
                screen.blit(text, rect)
            
            if self.item_description != None:

                item_description = self.item_description.split("  ")
                y = 0
                for string in item_description:
                
                    description = gFonts['minecraft_tiny'].render(string, False, "yellow", "black")
                    mouse_pos = pygame.mouse.get_pos()
                    pos = [mouse_pos[0],mouse_pos[1]+y]
                
                    if self.item_description_show_right == True:
                        rect = description.get_rect(bottomleft=(pos))
                    else:
                        rect = description.get_rect(bottomright=(pos))
                    screen.blit(description, rect)
                    y += 25
        
    