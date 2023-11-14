from src.states.BaseState import BaseState
import pygame, sys
from src.Dependencies import *
from src.constants import *
from src.StateMachine import StateMachine
from src.Player import Player
from src.Floor import Floor
from src.Card import ItemCard, AbilityCard, EventCard, EnemyCard
from src.Deck import Deck

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
        "mines": Floor(1, "The Mines", floor1_event_deck),
        }
        
        self.floors = floors
        self.curr_floor = self.floors['mines']
        
        
        
        

    def Enter(self,params):
        
        item_card_list = [ItemCard(**item) for item in item_attributes]
        item_deck = Deck(1,'item',item_card_list*2)
        item_deck.shuffle_deck()
        
        #item_deck.print_cards()
        
        drawn_cards = item_deck.draw_card(5)
        #print(drawn_cards)
        self.player.player_item_deck.add_cards(drawn_cards)
        
        #print(self.player.player_item_deck.print_cards())
        
        

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
                    
                if event.key == pygame.K_RIGHT:
                    self.player.player_item_deck.next_card()
                    index = self.player.player_item_deck.curr_card_index
                    print(self.player.player_item_deck.cards[index])
                if event.key == pygame.K_LEFT:
                    self.player.player_item_deck.prev_card()
                
                if event.key == pygame.K_SPACE:
                    index = self.player.player_item_deck.curr_card_index
                    self.player.player_item_deck.remove_card(index)
            if len(self.player.player_item_deck.cards) == 3:
                self.state_machine.Change('map',[self.player,self.curr_floor])
        
        self.timer = self.timer + dt

    def check_for_pos(self, position):
        pass

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
        x_offset = 100 #reset the position for the second line of cards
        y_offset = 450 
        
        i=0
        for item_card in self.player.player_item_deck.cards:
            index = self.player.player_item_deck.curr_card_index
            #print(index)
            
            item_index = item_card.card_id 
            item_image = gItems_image_list[item_index-1] #-1 since the item index starts from 1 (line above)
            frame_image = gFrames_image_list[2]
            position = (x_offset, y_offset)
            final_card = self.player.player_item_deck.render(frame_image, item_image) 
            screen.blit(final_card, position)
            
            if index == i:
                pygame.draw.rect(screen, 'red', pygame.Rect(x_offset, y_offset,50,50))
                print(x_offset,y_offset)
            x_offset += 200   
            i+=1
