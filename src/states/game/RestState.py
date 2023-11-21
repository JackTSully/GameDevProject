from src.states.BaseState import BaseState
import pygame, sys
from src.Dependencies import *
from src.constants import *
from src.StateMachine import StateMachine
from src.Player import Player
from src.Floor import Floor
from src.Card import ItemCard, AbilityCard, EventCard, EnemyCard
from src.Deck import Deck
from src.Dungeon import Dungeon

class RestState(BaseState):
    def __init__(self, state_machine):
        super(RestState, self).__init__(state_machine)
        self.bg_image = pygame.image.load("graphics/dungeon_campfire.png")
        self.bg_image = pygame.transform.scale(self.bg_image, (WIDTH + 5, HEIGHT + 5))
        
        self.player = Player(30, 3, 0, 20)
        self.player.setXY(WIDTH/3 - 50 ,HEIGHT/3)
        self.dungeon = Dungeon()
        self.floor = self.dungeon.get_curr_floor()
        
        
        
        self.cursor_position = (0, 0)
        self.selected_card = None 
        
        

    def Enter(self,params):
        self.time_interval = 3
        self.timer_text = 0
        self.player.reset_atk_power()
        self.item_description = None
        self.item_description_show_right = True
        
        if params == None: 
            self.dungeon.Enter(params)
            
            drawn_cards = self.dungeon.get_drawn_cards()
            
            self.player.player_item_deck.add_cards(drawn_cards)
            
            #print(self.player.player_item_deck.print_cards())
            
            
        else:
            self.dungeon.next_floor()
            self.dungeon.Enter(params)
            
            self.floor = self.dungeon.get_curr_floor()

            drawn_cards = self.dungeon.get_drawn_cards()
            self.player.player_item_deck.add_cards(drawn_cards)
            self.player.heal_self(5)
            
        
        

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
                if event.key == pygame.K_RETURN:
                    if self.floor.get_floor_lvl() == 1:
                        if len(self.player.player_item_deck.cards) == 3:
                            self.state_machine.Change('map',[self.player,self.floor])
                    else:    
                        print(print(self.floor.get_floor_lvl()))
                        self.state_machine.Change('map',[self.player,self.floor])
                
            '''if len(self.player.player_item_deck.cards) == 3 and self.floor.get_floor_lvl() == 1:
                print(print(self.floor.get_floor_lvl()))
                self.state_machine.Change('map',[self.player,self.floor])'''

            
            for i, item_card in enumerate(self.player.player_item_deck.cards):
                x_offset, y_offset = 100 + i * 200, HEIGHT-225
                frame_size = (140,200)
                card_rect = pygame.Rect(x_offset, y_offset, frame_size[0], frame_size[1])
                
                if event.type == pygame.MOUSEBUTTONDOWN:  # 1 corresponds to the left mouse button
                    if card_rect.collidepoint(self.cursor_position) and event.button == 1 and len(self.player.player_item_deck.cards) != 3 and self.floor.get_floor_lvl() == 1:
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
        

        txt = "Rest Area, Floor "+ str(self.floor.get_floor_lvl())
        t_press_enter = gFonts['minecraft'].render(txt, False, (175, 53, 42))
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

        if self.floor.get_floor_lvl() == 1 and len(self.player.player_item_deck.cards) != 3:
            t_press_enter = gFonts['minecraft_tiny'].render("Discard 2 cards, keep 3", False, "white", (175, 53, 42))
            rect = t_press_enter.get_rect(bottomleft=(100 , HEIGHT - 225))
            screen.blit(t_press_enter, rect)
        
        if (self.floor.get_floor_lvl() == 1 and len(self.player.player_item_deck.cards) == 3) or not self.floor.get_floor_lvl() == 1:
            txt = "Press Enter to continue"
            text = gFonts['minecraft_tiny'].render(txt, False, "white", (175, 53, 42))
            rect = text.get_rect(center=(WIDTH/2, HEIGHT/2+120))
            screen.blit(text, rect) 
        
        if self.item_description != None:
            description = gFonts['minecraft_tiny'].render(self.item_description, False, "yellow", "black")
            
            if self.item_description_show_right == True:
                rect = description.get_rect(bottomleft=(pygame.mouse.get_pos()))
            else:
                rect = description.get_rect(bottomright=(pygame.mouse.get_pos()))
            screen.blit(description, rect)
            
        
        


