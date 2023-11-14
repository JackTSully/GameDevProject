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

                if event.key == pygame.K_RIGHT:
                    self.player.next_card()
                    index = self.player.curr_card_index

                if event.key == pygame.K_LEFT:
                    self.player.prev_card()
                
                if event.key == pygame.K_SPACE:
                    index = self.player.curr_card_index
                    #self.player.player_item_deck.remove_card(index)
                    
        
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
        
        i=0
        for ability_card in self.player.ability_deck.cards:
            index = self.player.ability_deck.curr_card_index
            #print(index)
            ability_index = ability_card.card_id
            ability_image = gAbilities_image_list[ability_index-8] #-1 since the item index starts from 1 (line above)
            frame_image = gFrames_image_list[0]
            position = (x_offset, y_offset)
            final_card = self.player.player_item_deck.render(frame_image, ability_image) 
            screen.blit(final_card, position)
            
        for item_card in self.player.player_item_deck.cards:
            index = self.player.player_item_deck.curr_card_index
            #print(index)
            item_index = item_card.card_id 
            item_image = gItems_image_list[item_index-1] #-1 since the item index starts from 1 (line above)
            frame_image = gFrames_image_list[3]
            position = (x_offset, y_offset)
            final_card = self.player.player_item_deck.render(frame_image, item_image) 
            screen.blit(final_card, position)

            if index == i:
                pygame.draw.rect(screen, 'red', pygame.Rect(x_offset, y_offset,50,50))
                print(x_offset,y_offset)
            x_offset += 150   
            i+=1
            
