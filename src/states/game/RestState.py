from src.states.BaseState import BaseState
import pygame, sys
from src.Dependencies import *
from src.constants import *
from src.StateMachine import StateMachine
from src.Player import Player
from src.Floor import Floor

class RestState(BaseState):
    def __init__(self, state_machine):
        super(RestState, self).__init__(state_machine)
        self.bg_image = pygame.image.load("graphics/dungeon_campfire.png")
        self.bg_image = pygame.transform.scale(self.bg_image, (WIDTH + 5, HEIGHT + 5))
        self.time_interval = 3
        self.timer = 0
        
        self.player = Player(30)
        self.player.setXY(WIDTH/3 - 50 ,HEIGHT/3)

        floor1_event_deck = None #placeholder
        
        floors = {
        "mines": Floor(1, floor1_event_deck),
        }
        
        self.floors = floors
        self.curr_floor = self.floors['mines']
        
        

    def Enter(self,params):
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
                if event.key == pygame.K_RETURN:
                    self.state_machine.Change('map',[self.player,self.curr_floor])
        
        self.timer = self.timer + dt


    def render(self, screen):
        screen.blit(self.bg_image, (0, 0)) 

        
        if self.timer < self.time_interval:
            t_press_enter = gFonts['minecraft'].render("Rest Area, Floor 1", False, (255, 255, 255))
            rect = t_press_enter.get_rect(center=(WIDTH / 2, HEIGHT / 2 -192))
            screen.blit(t_press_enter, rect)

        if self.timer > self.time_interval and self.timer < self.time_interval*2:
            t_press_enter = gFonts['minecraft'].render("Discard 2 Cards", False, (255, 255, 255))
            rect = t_press_enter.get_rect(center=(WIDTH / 2, HEIGHT / 2 -192))
            screen.blit(t_press_enter, rect)

        self.player.render(screen)