from src.states.BaseState import BaseState
import pygame, sys
from src.Dependencies import *
from src.constants import *
from src.StateMachine import StateMachine
from src.Player import Player
from src.Floor import Floor
from src.Card import ItemCard, AbilityCard, EventCard, EnemyCard
from src.Deck import Deck

class RewardState(BaseState):
    def __init__(self, state_machine):
        super(RewardState, self).__init__(state_machine)
        self.bg_image = pygame.image.load("graphics/stages/mines.png")
        self.bg_image = pygame.transform.scale(self.bg_image, (WIDTH + 5, HEIGHT +5))
        self.time_interval = 3
        self.timer = 0
        
        self.player = Player(30)
        self.player.setXY(WIDTH/3 - 50, HEIGHT/3)
        
    def Enter(self, params):
        item_card_list = [ItemCard(**item) for item in item_attributes]
        item_deck = Deck(1,'item', item_card_list*2)
        item_deck.shuffle_deck()
        
        drawn_cards = item_deck.draw_card(2)
           
    def events(self):
        self.mouse_pressed = 0
        self.mouse_pos = pygame.mouse.get_pos()        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.mouse_pressed = event.button
                
    def mouse_over(self):
        return self.rect.collidepoint(self.game.mouse_pos)
    
    def mouse_clicked(self):
        return self.mouse_over() and self.game.mouse_pressed == 1
           
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
                    self.state_machine.Change('map')

                                   
    def render(self, screen):
        screen.blit(self.bg_image, (0, 0)) 

        
        if self.timer < self.time_interval:
            t_press_enter = gFonts['minecraft'].render("Rewards", False, (255, 255, 255))
            rect = t_press_enter.get_rect(center=(WIDTH / 2, HEIGHT / 2 -192))
            screen.blit(t_press_enter, rect)

        if self.timer > self.time_interval and self.timer < self.time_interval*2:
            t_press_enter = gFonts['minecraft'].render("Pick 1 Card", False, (255, 255, 255))
            rect = t_press_enter.get_rect(center=(WIDTH / 2, HEIGHT / 2 -192))
            screen.blit(t_press_enter, rect)

        #self.player.render(screen)
        x_offset = 100 #reset the position for the second line of cards
        y_offset = 450 
        
        for item_card in self.player.player_item_deck.cards:
            item_index = item_card.card_id 
            item_image = gItems_image_list[item_index-1] #-1 since the item index starts from 1 (line above)
            frame_image = gFrames_image_list[2]
            position = (x_offset, y_offset)
            final_card = self.player.render(screen, frame_image, item_image, position) 
            screen.blit(final_card, position)
            x_offset += 200
    
    def Exit(self):
        pass
