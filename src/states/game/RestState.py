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
        self.time_interval = 3
        self.timer = 0

    def Enter(self,params):
        if self.floor == 0:
            self.player = Player(30)
            self.player.setXY(WIDTH/3 - 50 ,HEIGHT/3)
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