from src.states.BaseState import BaseState
import pygame, sys
from src.Dependencies import *
from src.constants import *
from src.StateMachine import StateMachine
from src.Player import Player

class MapState(BaseState):
    def __init__(self, state_machine):
        super(MapState, self).__init__(state_machine)

        self.bg_image = pygame.image.load("graphics/dungeon_wall_bg.png")
        self.bg_image = pygame.transform.scale(self.bg_image, (WIDTH + 5, HEIGHT + 5))
        
        self.time_interval = 3
        self.timer = 0

        self.player = None
        self.floor = None

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
                    print(self.floor.get_curr_room().get_room_id())
        
        self.timer = self.timer + dt
        
        


    def render(self, screen):
        screen.blit(self.bg_image, (0, 0))
        
        #for room in self.floor.get_rooms():
        '''
        #start room
        pygame.draw.rect(screen, 'red', pygame.Rect((1/3)*(WIDTH/2) - 30, HEIGHT/2 - 30, 60, 60))

        
        #3 rooms
        pygame.draw.rect(screen, 'red', pygame.Rect((2/3)*(WIDTH/2) - 30, HEIGHT/2 - 30, 60, 60))
        pygame.draw.rect(screen, 'red', pygame.Rect(WIDTH/2 - 30, HEIGHT/2 - 30, 60, 60))
        pygame.draw.rect(screen, 'red', pygame.Rect((4/3)*(WIDTH/2) - 30, HEIGHT/2 - 30, 60, 60))

        
        #boss room
        pygame.draw.rect(screen, 'red', pygame.Rect((5/3)*(WIDTH/2) - 30, HEIGHT/2 - 30, 60, 60))

        #lines
        pygame.draw.line(screen, 'white', ((1/3)*(WIDTH/2)+30, HEIGHT/2), ((2/3)*(WIDTH/2)-30, HEIGHT/2), width= 5)
        pygame.draw.line(screen, 'white', ((2/3)*(WIDTH/2)+30, HEIGHT/2), ((WIDTH/2)-30, HEIGHT/2), width= 5)
        pygame.draw.line(screen, 'white', ((WIDTH/2)+30, HEIGHT/2), ((4/3)*(WIDTH/2)-30, HEIGHT/2), width= 5)
        pygame.draw.line(screen, 'white', ((4/3)*(WIDTH/2)+30, HEIGHT/2), ((5/3)*(WIDTH/2)-30, HEIGHT/2), width= 5)
        '''
        
        self.floor.render(screen)
        
        
        t_press_enter = gFonts['minecraft'].render("Placeholder State", False, (255, 255, 255))
        rect = t_press_enter.get_rect(center=(WIDTH / 2, HEIGHT / 2 -192))
        screen.blit(t_press_enter, rect)