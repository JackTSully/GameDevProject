from src.states.BaseState import BaseState
import pygame, sys
from src.Dependencies import *
from src.constants import *
from src.StateMachine import StateMachine
from src.Card import ItemCard, AbilityCard, EventCard, EnemyCard
from src.Player import Player
from src.Floor import *

class MapState(BaseState):
    def __init__(self, state_machine):
        super(MapState, self).__init__(state_machine)

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
        self.floor.Enter()
        
        if  self.floor.curr_room.event_deck == None or len(self.floor.curr_room.event_deck.cards) == 1:
            self.floor.next_room()

        if self.player.check_item_overcap():
            self.state_machine.Change('discard',[self.player,self.floor,'map'])


    def Exit(self):
        pass


    def update(self, dt, events):
        
        self.player.update(dt, events)
        
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if event.key == pygame.K_KP9:
                    #self.state_machine.Change('combat',[self.player])
                    self.floor.next_room()
                
                if event.key == pygame.K_i:
                    self.state_machine.Change('player_info',[self.player,self.floor,'map'])
 
        self.floor.update(dt,events)
        
        if self.floor.curr_room.event_deck != None:
            if len(self.floor.curr_room.event_deck.cards) == 1:
                self.timer = self.timer + dt
            
                if self.timer > self.time_interval and type(self.floor.curr_room.event_deck.cards[0]) == EnemyCard:
                    
                    self.state_machine.Change('combat',[self.player,self.floor,self.floor.curr_room.event_deck.cards[0]])
                elif self.timer > self.time_interval and type(self.floor.curr_room.event_deck.cards[0]) == EventCard:
                    self.state_machine.Change('event',[self.player,self.floor,self.floor.curr_room.event_deck.cards[0]])
        
        if self.player.curr_health <= 0:
            self.state_machine.Change('game_over')

        
        


    def render(self, screen):
        screen.blit(self.bg_image, (0, 0))
        self.player.display_HP(screen)
        

        
        self.floor.render(screen)
        
        text = "Floor "+str(self.floor.get_floor_lvl())+", "+self.floor.get_floor_name()              
        t_press_enter = gFonts['minecraft'].render(text, False, (255, 255, 255))
        rect = t_press_enter.get_rect(center=(WIDTH / 2, HEIGHT / 2 -192))
        screen.blit(t_press_enter, rect)

