from src.states.BaseState import BaseState
import pygame, sys
from src.Dependencies import *
from src.constants import *
from src.StateMachine import StateMachine
from src.Card import ItemCard, AbilityCard, EventCard, EnemyCard
from src.Player import Player
from src.Floor import *
from src.Dice import *

class EventState(BaseState):
    def __init__(self, state_machine):
        self.dice_instance = Dice()
        super(EventState, self).__init__(state_machine)
        self.bg_image = pygame.image.load("graphics/dungeon_wall_bg.png")
        self.bg_image = pygame.transform.scale(self.bg_image, (WIDTH + 5, HEIGHT + 5))
    
        
        self.player = None
        self.floor = None
        
        self.cursor_position = (0, 0)
        self.selected_card = None 
        

    def Enter(self,params):
        self.time_interval = 1
        self.timer = 0
        self.first = True
        
        self.player : Player= params[0]
        self.floor : Floor = params[1]
        if len(params) > 2:
            self.event_card = params[2]
        
        self.drawn_cards = None
        self.card15 = False
        
        self.item_description = None
        self.item_description_show_right = True
        
        self.card_id = self.event_card.card_id
        if self.card_id == 12: #Secret Room
            #draw 3 cards
            self.drawn_cards = self.floor.floor_item_deck.draw_card(3)
            self.player.player_item_deck.add_cards(self.drawn_cards)
        
        elif self.card_id == 13: #Fountain of Healing
            #heal to full HP
            self.player.curr_health = self.player.max_health
            
        elif self.card_id == 14: #Hero's monument
            #ATK +3 for the whole floor
            self.player.attack_power += 3
        
        elif self.card_id == 15: #Wounded Adventurer
            #Choice: Exchange a Healing Flask for another random item
            
            for card in self.player.player_item_deck.cards:
                if card.name == "Healing Flask":
                    self.card15 = True
        
        


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
                    
                if event.key == pygame.K_y and self.card15:
                    self.drawn_cards = self.floor.floor_item_deck.draw_card(1)
                    self.player.player_item_deck.add_cards(self.drawn_cards)
                    for i, card in enumerate(self.player.player_item_deck.cards):
                
                        if card.name == "Healing Flask":
                            self.player.player_item_deck.remove_card(i)
                
                    self.state_machine.Change('map',[self.player,self.floor])
                    
                if event.key == pygame.K_n and self.card15:
                    self.state_machine.Change('map',[self.player,self.floor])
                
                if event.key == pygame.K_i:
                    self.state_machine.Change('player_info',[self.player,self.floor,'event'])
                    
                if event.key == pygame.K_RETURN:
                    self.state_machine.Change('map',[self.player,self.floor])
            
            if self.drawn_cards != None:
                for i, item_card in enumerate(self.drawn_cards):
                    x_offset, y_offset = 100 + i * 200, HEIGHT-225
                    frame_size = (140,200)
                    card_rect = pygame.Rect(x_offset, y_offset, frame_size[0], frame_size[1])
                
                    if event.type == pygame.MOUSEBUTTONDOWN:
                    
                        if card_rect.collidepoint(self.cursor_position) and event.button == 3:
                            self.item_card_index = i

                            self.item_description = self.drawn_cards[self.item_card_index].description
                            if self.item_card_index > 2:
                                self.item_description_show_right = False

                        
                    if event.type == pygame.MOUSEMOTION:
                        self.item_description = None
                        self.item_description_show_right = True
                else:
                    self.item_card_index = None
            
        if self.player.curr_health <= 0:
            self.state_machine.Change('game_over',[self.player,self.floor])
                    
        self.timer = self.timer + dt
        
        self.cursor_position = pygame.mouse.get_pos()
        
        
        


    def render(self, screen):
        screen.blit(self.bg_image, (0, 0))
        self.player.display_HP(screen)
        
        x_offset = WIDTH/2 - 70 #reset the position for the second line of cards
        y_offset = HEIGHT/4 - 100
        
        event_index = self.event_card.card_id 
        event_image = gsEnemies_Image_list[event_index-12] #-1 since the item index starts from 1 (line above)
        frame_image = gFrames_image_list[3]
        position = (x_offset, y_offset)
        final_card = self.player.player_item_deck.render(frame_image, event_image) 
        screen.blit(final_card, position)
        event_name = self.event_card.name.split(" ")
        y = 0
        for string in event_name:
            text = gFonts['minecraft_card'].render(string, False, ('black'))
            rect = text.get_rect(center=(x_offset + 75 , y_offset + 142 + y))
            screen.blit(text, rect)
            y += 17

        
        txt = "Room event"          
        text = gFonts['minecraft_small'].render(txt, False, (255, 255, 255))
        rect = text.get_rect(center=(WIDTH / 2, 50))
        screen.blit(text, rect)
        
        txt = self.event_card.description
        text = gFonts['minecraft_tiny'].render(txt, False, (255, 255, 255))
        rect = text.get_rect(center=(WIDTH/2, HEIGHT/2))
        screen.blit(text, rect)
        
        if self.timer > self.time_interval:
            txt = "Press Enter to continue"
            text = gFonts['minecraft_tiny'].render(txt, False, (255, 255, 255))
            rect = text.get_rect(center=(WIDTH/2, HEIGHT/2+120))
            screen.blit(text, rect)           
        
        if self.card_id == 15:
            x_offset = 100 
            y_offset = HEIGHT-225
            for card in self.player.player_item_deck.cards:
                
                if card.name == "Healing Flask":
                    item_index = card.card_id 
                    item_image = gItems_image_list[item_index-1] #-1 since the item index starts from 1 (line above)
                    frame_image = gFrames_image_list[3]
                    position = (x_offset, y_offset)
                    final_card = self.player.player_item_deck.render(frame_image, item_image) 
                    screen.blit(final_card, position)
                    item_name = card.name.split(" ")
                    y = 0
                    for string in item_name:
                        text = gFonts['minecraft_card'].render(string, False, ('black'))
                        rect = text.get_rect(center=(x_offset + 75 , y_offset + 142 + y))
                        screen.blit(text, rect)
                        y += 17
                    x_offset += 200
                    
        if self.card_id == 16: #Pitfall Trap
            #Athletic Check (10) Fail: Take D4 Damage Pass: Get Item Card
            if self.first:
                self.roll = self.dice_instance.roll_dice(20)
                if self.roll < 10:
                    dmg = self.dice_instance.roll_dice(4)
                    self.player.take_damage(dmg)
                else:
                    self.drawn_cards = self.floor.floor_item_deck.draw_card(1)
                    self.player.player_item_deck.add_cards(self.drawn_cards)
                self.first = False
            if self.roll < 10:
                txt = "you rolled a "+str(self.roll)+" you failed"
            else:
                txt = "you rolled a "+str(self.roll)+" you won!"
            text = gFonts['minecraft_tiny'].render(txt, False, (255, 255, 255))
            rect = text.get_rect(center=(WIDTH/2, HEIGHT/2 + 30))
            screen.blit(text, rect)
        
        elif self.card_id == 17: #Dart Trap
            #Athletic Check (13) Fail: Take D6 Damage Pass: Get Item Card
            if self.first:
                self.roll = self.dice_instance.roll_dice(20)
                if self.roll < 13:
                    dmg = self.dice_instance.roll_dice(6)
                    self.player.take_damage(dmg)
                else:
                    self.drawn_cards = self.floor.floor_item_deck.draw_card(1)
                    self.player.player_item_deck.add_cards(self.drawn_cards)
                self.first = False
            if self.roll < 13:
                txt = "you rolled a "+str(self.roll)+" you failed"
            else:
                txt = "you rolled a "+str(self.roll)+" you won!"
            text = gFonts['minecraft_tiny'].render(txt, False, (255, 255, 255))
            rect = text.get_rect(center=(WIDTH/2, HEIGHT/2 + 30))
            screen.blit(text, rect)
            
        elif self.card_id == 18: #Boulder Trap
            #Athletic Check (10/10) Fail: Take D8 Damage Pass: Get 2x Item Card
            if self.first:
                self.roll1 = self.dice_instance.roll_dice(20)
                self.roll2 = self.dice_instance.roll_dice(20)
                if self.roll1 < 10 and self.roll2 < 10:
                    dmg = self.dice_instance.roll_dice(8)
                    self.player.take_damage(dmg)
                elif self.roll1 >= 10 and self.roll2 < 10:
                    pass
                elif self.roll1 >= 10 and self.roll2 >= 10:
                    self.drawn_cards = self.floor.floor_item_deck.draw_card(2)
                    self.player.player_item_deck.add_cards(self.drawn_cards)
                self.first = False
                 
            if self.roll1 < 10 and self.roll2 < 10:
                txt = "you rolled a "+str(self.roll1)+" and a "+str(self.roll2)+" you failed big!"
            elif self.roll1 >= 10 and self.roll2 < 10:
                txt = "you rolled a "+str(self.roll1)+" and a "+str(self.roll2)+" you were spared!"
            elif self.roll1 < 10 and self.roll2 >= 10:
                txt = "you rolled a "+str(self.roll1)+" and a "+str(self.roll2)+" you were spared!"
            elif self.roll1 >= 10 and self.roll2 >= 10:
                txt = "you rolled a "+str(self.roll1)+" and a "+str(self.roll2)+" you won!"
            else:
                txt = "you rolled a "+str(self.roll1)+" and a "+str(self.roll2)+" error"
            text = gFonts['minecraft_tiny'].render(txt, False, (255, 255, 255))
            rect = text.get_rect(center=(WIDTH/2, HEIGHT/2 + 30))
            screen.blit(text, rect)
        
        
        
        # Shows item cards drawn from event
        if self.drawn_cards != None:       
            x_offset = 100 #reset the position for the second line of cards
            y_offset = HEIGHT-225
                 
            for item_card in self.drawn_cards:

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
