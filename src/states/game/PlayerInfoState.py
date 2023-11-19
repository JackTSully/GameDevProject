from src.states.BaseState import BaseState
import pygame, sys
from src.Dependencies import *
from src.constants import *
from src.StateMachine import StateMachine
from src.Card import ItemCard, AbilityCard, EventCard, EnemyCard
from src.Player import Player
from src.Floor import *

class PlayerInfoState(BaseState):
    def __init__(self, state_machine):
        super(PlayerInfoState, self).__init__(state_machine)

        self.bg_image = pygame.image.load("graphics/dungeon_wall_bg.png")
        self.bg_image = pygame.transform.scale(self.bg_image, (WIDTH + 5, HEIGHT + 5))
        

        self.player = None
        self.floor = None

        self.cursor_position = (0, 0)

    def Enter(self,params):
        self.time_interval = 1.5
        self.timer = 0
        
        self.player : Player = params[0]
        self.floor : Floor = params[1]
        self.prev_state : str = params[2]

        self.item_description = None
        self.item_description_show_right = True
        


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
                
                if event.key == pygame.K_i:
                    self.state_machine.Change(self.prev_state,[self.player,self.floor])
        
            for i, item_card in enumerate(self.player.player_item_deck.cards):
                x_offset, y_offset = 100 + i * 200, HEIGHT-225
                frame_size = (140,200)
                card_rect = pygame.Rect(x_offset, y_offset, frame_size[0], frame_size[1])
                
                if event.type == pygame.MOUSEBUTTONDOWN:  # 1 corresponds to the left mouse button
                    '''
                    if card_rect.collidepoint(self.cursor_position) and event.button == 1:
                        self.item_card_index = i
                        
                        self.player.player_item_deck.remove_card(self.item_card_index)
                        break
                    '''
                    if card_rect.collidepoint(self.cursor_position) and event.button == 3:
                        self.item_card_index = i

                        self.item_description = self.player.player_item_deck.get_card(self.item_card_index).description
                        if self.item_card_index > 2:
                            self.item_description_show_right = False

                        
                if event.type == pygame.MOUSEMOTION:
                    self.item_description = None
                    self.item_description_show_right = True
            else:
                self.item_card_index = None
                    
        self.cursor_position = pygame.mouse.get_pos()
                    
        



    def render(self, screen):
        screen.blit(self.bg_image, (0, 0))
        self.player.display_HP(screen)
        
        
        text = "Card Inventory"          
        t_press_enter = gFonts['minecraft'].render(text, False, (255, 255, 255))
        rect = t_press_enter.get_rect(center=(WIDTH / 2, HEIGHT / 2 -192))
        screen.blit(t_press_enter, rect)
        
        x_offset = 100 #reset the position for the second line of cards
        y_offset = HEIGHT-225
        
        for item_card in self.player.player_item_deck.cards:

            item_index = item_card.card_id
            item_image = gItems_image_list[item_index-1] #-1 since the item index starts from 1 (line above)
            frame_image = gFrames_image_list[3]
            position = (x_offset, y_offset)
            final_card = self.player.player_item_deck.render(frame_image, item_image) 
            screen.blit(final_card, position)
            
            item_name = item_card.name.split(" ")
            y = 0
            for string in item_name:
                text = gFonts['minecraft_card'].render(string, False, ('black'))
                rect = text.get_rect(center=(x_offset + 75 , y_offset + 142 + y))
                screen.blit(text, rect)
                y += 17
            
            x_offset += 200
        
        if self.item_description != None:
            description = gFonts['minecraft_tiny'].render(self.item_description, False, "yellow", "black")
            
            if self.item_description_show_right == True:
                rect = description.get_rect(bottomleft=(pygame.mouse.get_pos()))
            else:
                rect = description.get_rect(bottomright=(pygame.mouse.get_pos()))
            screen.blit(description, rect)

