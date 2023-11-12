from src.states.BaseState import BaseState
import pygame, sys
from src.Dependencies import *
from src.constants import *
from src.StateMachine import StateMachine
from src.Player import Player

class RestState(BaseState):
    def __init__(self, state_machine):
        super(RestState, self).__init__(state_machine)
        self.bg_image = pygame.image.load("graphics/dungeon_campfire.png")
        self.bg_image = pygame.transform.scale(
            self.bg_image, (WIDTH + 5, HEIGHT + 5))
        self.floor = 0

    def Enter(self,params):
        if self.floor == 0:
            self.player = Player(30)
            self.player.setXY(50,50)
            #floors = {
            #   "The Mines": Floor(1, floor1_monster_deck)
            # }
        #self.floor = floors[0]

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

    def render(self, screen):
        screen.blit(self.bg_image, (0, 0))
        
        self.player.render(screen)