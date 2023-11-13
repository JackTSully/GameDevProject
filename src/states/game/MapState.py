from src.states.BaseState import BaseState
import pygame, sys
from src.Dependencies import *
from src.constants import *
from src.StateMachine import StateMachine
from src.Player import Player

class MapState(BaseState):
    def __init__(self, state_machine):
        super(MapState, self).__init__(state_machine)

        self.bg_image = pygame.image.load("graphics/dungeon_campfire2.jpg")
        self.bg_image = pygame.transform.scale(self.bg_image, (WIDTH + 5, HEIGHT + 5))
        
        self.time_interval = 3
        self.timer = 0

        self.player = None
        self.floor = None

    def Enter(self,params):
        self.player = params[0]
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
        
        self.timer = self.timer + dt


    def render(self, screen):
        #screen.blit(self.bg_image, (0, 0)) 

        
        
        t_press_enter = gFonts['minecraft'].render("Placeholder State", False, (255, 255, 255))
        rect = t_press_enter.get_rect(center=(WIDTH / 2, HEIGHT / 2 -192))
        screen.blit(t_press_enter, rect)