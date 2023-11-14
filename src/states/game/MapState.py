from src.states.BaseState import BaseState
import pygame, sys
from src.Dependencies import *
from src.constants import *
from src.StateMachine import StateMachine
from src.Player import Player
from src.Floor import *

class MapState(BaseState):
    def __init__(self, state_machine):
        super(MapState, self).__init__(state_machine)

        self.bg_image = pygame.image.load("graphics/dungeon_wall_bg.png")
        self.bg_image = pygame.transform.scale(self.bg_image, (WIDTH + 5, HEIGHT + 5))
        
        self.time_interval = 3
        self.timer = 0

        self.player = None
        self.floor = None

        self.cursor_position = (0, 0)
        self.selected_card = None 

    def Enter(self,params):
        self.player = params[0]
        self.floor = params[1]


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
                    #self.state_machine.Change('combat',[self.player])
                    self.floor.next_room()

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # 1 corresponds to the left mouse button

                for i, card in enumerate(self.map.curr_room.event_deck.cards):
                    x_offset, y_offset = 100 + i * 200, 450
                    frame_size = (200, 200)
                    card_rect = pygame.Rect(x_offset, y_offset, frame_size[0], frame_size[1])

                    if card_rect.collidepoint(self.cursor_position):
                        self.event_card_index = i
                        self.selected_card = card
                        self.player.player_item_deck.remove_card(self.event_card_index)
                        break
                else:
                    self.item_card_index = None


        self.cursor_position = pygame.mouse.get_pos()
        
        
        self.floor.update(dt,events)
        
        self.timer = self.timer + dt
        
        


    def render(self, screen):
        screen.blit(self.bg_image, (0, 0))
        

        
        self.floor.render(screen)
        
        text = "Floor "+str(self.floor.get_floor_lvl())+", "+self.floor.get_floor_name()              
        t_press_enter = gFonts['minecraft'].render(text, False, (255, 255, 255))
        rect = t_press_enter.get_rect(center=(WIDTH / 2, HEIGHT / 2 -192))
        screen.blit(t_press_enter, rect)

