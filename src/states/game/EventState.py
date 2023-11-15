from src.states.BaseState import BaseState
import pygame, sys
from src.Dependencies import *
from src.constants import *
from src.StateMachine import StateMachine
from src.Card import ItemCard, AbilityCard, EventCard, EnemyCard
from src.Player import Player
from src.Floor import *

class EventState(BaseState):
    def __init__(self, state_machine):
        super(EventState, self).__init__(state_machine)
        self.bg_image = pygame.image.load("graphics/dungeon_wall_bg.png")
        self.bg_image = pygame.transform.scale(self.bg_image, (WIDTH + 5, HEIGHT + 5))
        
        self.time_interval = 1.5
        self.timer = 0
        
        self.player = None
        self.floor = None
        
        self.cursor_position = (0, 0)
        self.selected_card = None 
        
        self.card15 = False

    def Enter(self,params):
        self.player : Player= params[0]
        self.floor : Floor = params[1]
        self.event_card = params[2]
        
        card_id = self.event_card.card_id
        if card_id == 12: #Secret Room
            #draw 3 cards
            drawn_cards = self.floor.floor_item_deck.draw_card(3)
            self.player.player_item_deck.add_cards(drawn_cards)
        
        elif card_id == 13: #Fountain of Healing
            #heal to full HP
            self.player.curr_health = self.player.max_health
            
        elif card_id == 14: #Hero's monument
            #ATK +3 for the whole floor
            self.player.attack_power += 3
        
        elif card_id == 15: #Wounded Adventurer
            #Choice: Exchange a Healing Flask for another random item
            
            for card in self.player.player_item_deck.cards:
                if card.name == "Healing Flask":
                    self.card15 = True
        
        elif card_id == 16: #Pitfall Trap
            #Athletic Check (10) Fail: Take D4 Damage Pass: Get Item Card
            pass
        
        elif card_id == 17: #Dart Trap
            #Athletic Check (13) Fail: Take D6 Damage Pass: Get Item Card
            pass
        
        elif card_id == 18: #Boulder Trap
            #Athletic Check (10/10) Fail: Take D8 Damage Pass: Get 2x Item Card
            pass


    def Exit(self):
        pass


    def update(self, dt, events):
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if event.key == pygame.K_y:
                    drawn_cards = self.floor.floor_item_deck.draw_card(1)
                    self.player.player_item_deck.add_cards(drawn_cards)
                    self.state_machine.Change('map',[self.player,self.curr_floor])
                if event.key == pygame.K_n:
                    self.state_machine.Change('map',[self.player,self.curr_floor])
        
        
        


    def render(self, screen):
        screen.blit(self.bg_image, (0, 0))
        self.player.display_HP(screen)
        
        x_offset = WIDTH/2 - 70 #reset the position for the second line of cards
        y_offset = HEIGHT/4 - 100
        
        event_index = self.event_card.card_id 
        event_image = gsEnemies_Image_list[event_index-12] #-1 since the item index starts from 1 (line above)
        frame_image = gFrames_image_list[3]
        position = (x_offset, y_offset)
        final_card = self.player.player_item_deck.render(frame_image, event_image) 
        screen.blit(final_card, position)
        x_offset += 200
        
        text = "Room event"          
        t_press_enter = gFonts['minecraft_small'].render(text, False, (255, 255, 255))
        rect = t_press_enter.get_rect(center=(WIDTH / 2, 50))
        screen.blit(t_press_enter, rect)
        
        txt = self.event_card.description
        text = gFonts['minecraft_tiny'].render(txt, False, (255, 255, 255))
        rect = text.get_rect(center=(WIDTH/2, HEIGHT/2))
        screen.blit(text, rect)

