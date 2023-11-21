from src.states.BaseState import BaseState
import pygame, sys
from src.Dependencies import *
from src.constants import *
from src.StateMachine import StateMachine
from src.Player import Player

class GameOverState(BaseState):
    def __init__(self, state_machine):
        super(GameOverState, self).__init__(state_machine)
        
    def Enter(self, params):
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
                    pygame.quit()
                    sys.exit()


    def render(self, screen):
        t_title = gFonts['minecraft'].render("GAME OVER", False, (175, 53, 42))
        rect = t_title.get_rect(center=(WIDTH / 2, HEIGHT / 2 - 144))
        screen.blit(t_title, rect)

        t_press_enter = gFonts['minecraft'].render("Press Enter", False, (175, 53, 42))
        rect = t_press_enter.get_rect(center=(WIDTH / 2, HEIGHT / 2 + 48))
        screen.blit(t_press_enter, rect)
        
    def Exit(self):
        pass