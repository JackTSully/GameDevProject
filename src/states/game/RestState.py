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
        
        self.player = Player(30, 3, 0, 20)
        self.player.setXY(WIDTH/3 - 50 ,HEIGHT/3)
        
        event_card_list = [EventCard(**item) for item in event_attributes]
        event_deck = Deck(1,'event',event_card_list*2)
        
        enemy_card_list = [EnemyCard(**item) for item in enemy_attributes]
        floor1_enemy_deck = Deck(1,'enemy',enemy_card_list[0:3]*3)
        #floor1_monster_deck = Deck(1,'monster', floor1_enemy_card_list)
        floor1_enemy_deck.merge_with(event_deck)
        floor1_event_deck = floor1_enemy_deck
        floors = {
        "mines": Floor(1, "The Mines", floor1_event_deck),
        }
        
        self.floors = floors
        self.curr_floor = self.floors['mines']
        
        self.cursor_position = (0, 0)
        self.selected_card = None 
        
        

    def Enter(self,params):
        self.time_interval = 3
        self.timer_text = 0
        
        self.player.reset_atk_power()
        item_card_list = [ItemCard(**item) for item in item_attributes]
        floor_item_deck = Deck(1,'item',item_card_list*3)
        floor_item_deck.shuffle_deck()
        self.curr_floor.set_floor_item_deck(floor_item_deck)
        
        
        drawn_cards = floor_item_deck.draw_card(5)
        #print(drawn_cards)
        self.player.player_item_deck.add_cards(drawn_cards)
        
        #print(self.player.player_item_deck.print_cards())
        
        self.item_description = None
        self.item_description_show_right = True
        
        

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
                    #self.state_machine.Change('map',[self.player,self.curr_floor])
                    pass
                    
                #if event.key == pygame.K_RIGHT:
                    #self.player.player_item_deck.next_card()
                    #index = self.player.player_item_deck.curr_card_index
                    
                #if event.key == pygame.K_LEFT:
                    #self.player.player_item_deck.prev_card()
                
                #if event.key == pygame.K_SPACE:
                    #index = self.player.player_item_deck.curr_card_index
                    #self.player.player_item_deck.remove_card(index)

            if len(self.player.player_item_deck.cards) == 3:
                self.state_machine.Change('map',[self.player,self.curr_floor])

            #if event.type == pygame.MOUSEBUTTONDOWN:  # 1 corresponds to the left mouse button
            
            for i, item_card in enumerate(self.player.player_item_deck.cards):
                x_offset, y_offset = 100 + i * 200, 450
                frame_size = (140,200)
                card_rect = pygame.Rect(x_offset, y_offset, frame_size[0], frame_size[1])
                
                if event.type == pygame.MOUSEBUTTONDOWN:  # 1 corresponds to the left mouse button
                    if card_rect.collidepoint(self.cursor_position) and event.button == 1:
                        self.item_card_index = i
                        
                        self.player.player_item_deck.remove_card(self.item_card_index)
                        break
                    elif card_rect.collidepoint(self.cursor_position) and event.button == 3:
                        self.item_card_index = i

                        self.item_description = self.player.player_item_deck.get_card(self.item_card_index).description
                        if self.item_card_index > 2:
                            self.item_description_show_right = False

                        
                if event.type == pygame.MOUSEMOTION:
                    self.item_description = None
                    self.item_description_show_right = True
            else:
                self.item_card_index = None
                    


        self.cursor_position = pygame.mouse.get_pos()
           
        
        self.timer_text = self.timer_text + dt

    def check_for_pos(self, position):
        pass

    def render(self, screen):
        screen.blit(self.bg_image, (0, 0)) 
        self.player.display_HP(screen)
        
        if self.timer_text < self.time_interval:
            t_press_enter = gFonts['minecraft'].render("Rest Area, Floor 1", False, (175, 53, 42))
            rect = t_press_enter.get_rect(center=(WIDTH / 2, HEIGHT / 2 -192))
            screen.blit(t_press_enter, rect)

        if self.timer_text > self.time_interval:
            t_press_enter = gFonts['minecraft'].render("Discard 2 Cards", False, (175, 53, 42))
            rect = t_press_enter.get_rect(center=(WIDTH / 2, HEIGHT / 2 -192))
            screen.blit(t_press_enter, rect)

        self.player.render(screen)
        x_offset = 100 #reset the position for the second line of cards
        y_offset = HEIGHT-225
        
        for item_card in self.player.player_item_deck.cards:

            item_index = item_card.card_id
            item_image = gItems_image_list[item_index-1] #-1 since the item index starts from 1 (line above)
            frame_image = gFrames_image_list[3]
            position = (x_offset, y_offset)
            final_card = self.player.player_item_deck.render(frame_image, item_image) 
            screen.blit(final_card, position)
            
            item_name = item_card.name.split(" ")
            y = 0
            for string in item_name:
                text = gFonts['minecraft_card'].render(string, False, ('black'))
                rect = text.get_rect(center=(x_offset + 75 , y_offset + 142 + y))
                screen.blit(text, rect)
                y += 17
            
            x_offset += 200
        
        if self.item_description != None:
            description = gFonts['minecraft_tiny'].render(self.item_description, False, "yellow", "black")
            
            if self.item_description_show_right == True:
                rect = description.get_rect(bottomleft=(pygame.mouse.get_pos()))
            else:
                rect = description.get_rect(bottomright=(pygame.mouse.get_pos()))
            screen.blit(description, rect)
            
