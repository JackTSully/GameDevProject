from src.states.BaseState import BaseState
import pygame, sys
from src.Dependencies import *
from src.constants import *
from src.StateMachine import StateMachine
from src.Player import Player
from src.Card import *
from src.Deck import *

class CombatState(BaseState):
    def __init__(self, state_machine):
        super(CombatState, self).__init__(state_machine)

        self.bg_image = pygame.image.load("graphics/stages/mines.png")
        self.bg_image = pygame.transform.scale(self.bg_image, (WIDTH + 5, HEIGHT + 5))
        
        self.time_interval = 3
        self.timer = 0
        
        self.player = None
        self.floor = None

        self.cursor_position = (0, 0)
        self.selected_card = None 

    def Enter(self,params):
        self.player = params[0]
        self.player.setXY(WIDTH/11,None )


        #self.floor = params[1]


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
                if event.key == pygame.K_RETURN:
                    self.state_machine.Change('combat',[self.player])


            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1: 
                if self.selected_card:
                    print(f"Clicked on the selected card: {self.selected_card.card_id}")

        frame_size = (200, 200)

        for i, ability_card in enumerate(self.player.ability_deck.cards):
            x_offset, y_offset = 100 + i * 150, 450
            card_rect = pygame.Rect(x_offset, y_offset, frame_size[0], frame_size[1])

            if card_rect.collidepoint(self.cursor_position):
                self.selected_card = ability_card
                break
        else:
            for i, item_card in enumerate(self.player.player_item_deck.cards):
                x_offset, y_offset = 700 + i * 150, 450
                card_rect = pygame.Rect(x_offset, y_offset, frame_size[0], frame_size[1])

                if card_rect.collidepoint(self.cursor_position):
                    self.selected_card = item_card
                    break
            else:
                self.selected_card = None


        self.cursor_position = pygame.mouse.get_pos()                
                    
        
        self.timer = self.timer + dt


    def render(self, screen):
        screen.blit(self.bg_image, (0, 0)) 

        
        if self.timer < self.time_interval:
            t_press_enter = gFonts['minecraft'].render("Combat Event", False, (255, 255, 255))
            rect = t_press_enter.get_rect(center=(WIDTH / 2, HEIGHT / 2 -192))
            screen.blit(t_press_enter, rect)

        self.player.render(screen)
        x_offset = 100 #reset the position for the second line of cards
        y_offset = 450 
        
        for ability_card in self.player.ability_deck.cards:
            ability_index = ability_card.card_id
            ability_image = gAbilities_image_list[ability_index-8] #-1 since the item index starts from 1 (line above)
            frame_image = gFrames_image_list[0]
            position = (x_offset, y_offset)
            final_card = self.player.player_item_deck.render(frame_image, ability_image) 
            screen.blit(final_card, position)
            x_offset += 150
            
        for item_card in self.player.player_item_deck.cards:
            item_index = item_card.card_id 
            item_image = gItems_image_list[item_index-1] #-1 since the item index starts from 1 (line above)
            frame_image = gFrames_image_list[3]
            position = (x_offset, y_offset)
            final_card = self.player.player_item_deck.render(frame_image, item_image) 
            screen.blit(final_card, position)
            x_offset += 150
            