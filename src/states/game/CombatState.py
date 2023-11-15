from src.states.BaseState import BaseState
import pygame, sys
from src.Dependencies import *
from src.constants import *
from src.StateMachine import StateMachine
from src.Player import Player
from src.Card import *
from src.Deck import *
from src.Effect import *
from src.Dice import *
from src.Enemies import *

class CombatState(BaseState):
    def __init__(self, state_machine):
        super(CombatState, self).__init__(state_machine)

        self.bg_image = pygame.image.load("graphics/stages/mines.png")
        self.bg_image = pygame.transform.scale(self.bg_image, (WIDTH + 5, HEIGHT + 5))

        self.turn = 1
        self.enemy_rounds = 0
        self.player_rounds = 0
        self.attack_delay = 1500
        self.attack_timer = None
        self.damage_text = None

        self.time_interval = 3
        self.timer = 0
        
        self.player = None
        self.floor = None

        self.cursor_position = (0, 0)
        self.selected_card = None

        self.show_ability_cards = False
        self.show_item_cards = False

    def Enter(self,params):
        self.player = params[0]
        self.player.setXY(WIDTH/11,None)
        self.enemies = Enemies(params[2].card_id,params[2].name,params[2].description,params[2].max_health,params[2].attack_dice,
                               params[2].attack_bonus, params[2].e_ability_id)
        self.enemies.setXY(WIDTH-300 ,HEIGHT/3)

        #self.floor = params[1]


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
                    self.state_machine.Change('combat',[self.player])

                if event.key == pygame.K_UP:
                    self.show_ability_cards = False
                    self.show_item_cards =True

                if event.key == pygame.K_DOWN:
                    self.show_ability_cards = True
                    self.show_item_cards = False
                
                
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and self.turn % 2 != 0:
                if self.selected_card:
                    print(f"Clicked on the selected card: {self.selected_card.card_id}")
                    if self.selected_card.effect_id == 1001: #Heal
                        pygame.time.delay(self.attack_delay)
                        self.player.heal_self(5)
                        self.player.action_points -= 1
                    elif self.selected_card.effect_id == 1002: # dec_atk
                        pygame.time.delay(self.attack_delay)
                        self.enemies.got_debuff(5)
                        self.player.action_points -= 1
                    elif self.selected_card.effect_id == 1003: #dis_skill
                        pygame.time.delay(self.attack_delay)
                        self.enemies.disabled_skill()
                        self.player.action_points -= 1
                    elif self.selected_card.effect_id == 1004: #inv
                        pass
                        self.player.action_points -= 1
                    elif self.selected_card.effect_id == 1005: #inc_ap
                        self.player.increase_ap(1)
                    elif self.selected_card.effect_id == 1006: #inc_atk
                        pygame.time.delay(self.attack_delay)
                        self.player.increase_atk(5)
                        self.player.action_points -= 1
                    elif self.selected_card.effect_id == 1007: #dup_card
                        pygame.time.delay(self.attack_delay)
                        pass
                        self.player.action_points -= 1
                    elif self.selected_card.effect_id == 1008: #add_roll
                        pygame.time.delay(self.attack_delay)
                        pass
                        self.player.action_points -= 1
                    elif self.selected_card.effect_id == 2001: #attack
                        pygame.time.delay(self.attack_delay) 
                        self.enemies.take_damage(d20)
                        self.player.action_points -= 1
                    elif self.selected_card.effect_id == 2002: #charged
                        pygame.time.delay(self.attack_delay) 
                        self.enemies.take_damage(d20*2)
                        self.player.action_points -= 2
                    elif self.selected_card.effect_id == 2003: #counter
                        pygame.time.delay(self.attack_delay)
                        pass
                        self.player.action_points -= 1
                    elif self.selected_card.effect_id == 2004: #block
                        pygame.time.delay(self.attack_delay)
                        self.enemies.got_debuff(5)
                        self.player.action_points -= 1

        if self.turn % 2 != 0:
            self.player_rounds += 1
            if self.player.action_points <= 0:
                self.turn += 1         
                self.player.action_points = 3
        else:
                if self.enemy_rounds == 3:
                    pygame.time.delay(self.attack_delay)
                    self.turn += 1
                    self.player.got_debuff(5) 
                else:
                    self.turn += 1
                    pygame.time.delay(self.attack_delay)
                    damage = d(8)
                    self.player.take_damage(damage)
                    self.enemy_rounds += 1

        frame_size = (140, 200)
        self.selected_card = None

        if self.show_ability_cards:

            for i, ability_card in enumerate(self.player.ability_deck.cards):
                x_offset, y_offset = 100 + i * 150, 450
                card_rect = pygame.Rect(x_offset, y_offset, frame_size[0], frame_size[1])

                if card_rect.collidepoint(self.cursor_position):
                    if self.show_ability_cards:
                        self.selected_card = ability_card  
                    else: 
                        None
                    break

        if self.show_item_cards:

            for i, item_card in enumerate(self.player.player_item_deck.cards):
                x_offset, y_offset = 100 + i * 150, 450
                card_rect = pygame.Rect(x_offset, y_offset, frame_size[0], frame_size[1])

                if card_rect.collidepoint(self.cursor_position):
                    if self.show_item_cards:
                        self.selected_card = item_card
                    else:
                        None
                    break
            else:
                self.selected_card = None

        self.cursor_position = pygame.mouse.get_pos()
                    
        
        self.timer = self.timer + dt


    def render(self, screen):
        
        screen.blit(self.bg_image, (0, 0)) 

        player_hp_text = gFonts['minecraft_small'].render(f"HP: {self.player.cur_health}", False, (175, 53, 42))
        hp_rect = player_hp_text.get_rect(topleft=(20, 20))
        screen.blit(player_hp_text, hp_rect)
        player_ap_text = gFonts['minecraft_small'].render(f"AP: {self.player.action_points}", False, (255, 255, 255))
        hp_rect = player_ap_text.get_rect(topleft=(20, 80))
        screen.blit(player_ap_text, hp_rect)

        turn_text = "Your turn" if self.turn % 2 != 0 else "Enemy's turn"
        turn_enter = gFonts['minecraft_small'].render(f"Turn: {turn_text}", False, (175, 53, 42))
        rect = turn_enter.get_rect(center=(WIDTH / 2, 30))
        screen.blit(turn_enter, rect)

        enemies_hp_text = gFonts['minecraft_small'].render(f"HP: {self.enemies.cur_health}", False, (175, 53, 42))
        hp_rect = enemies_hp_text.get_rect(topright=(WIDTH - 20, 20))
        screen.blit(enemies_hp_text, hp_rect)

        if self.timer < self.time_interval:
            t_press_enter = gFonts['minecraft'].render("Combat Event", False, (175, 53, 42))
            rect = t_press_enter.get_rect(center=(WIDTH / 2, HEIGHT / 2 -192))
            screen.blit(t_press_enter, rect)

        self.player.render(screen)
        x_offset = 100 #reset the position for the second line of cards
        y_offset = 450 
        
        self.enemies.render(screen)

        if self.show_ability_cards:
            for ability_card in self.player.ability_deck.cards:
                ability_index = ability_card.card_id
                ability_image = gAbilities_image_list[ability_index - 8]  # -1 since the item index starts from 1
                frame_image = gFrames_image_list[0]
                position = (x_offset, y_offset)
                final_card = self.player.player_item_deck.render(frame_image, ability_image)
                screen.blit(final_card, position)
                x_offset += 150

        if self.show_item_cards:
            x_offset, y_offset = 100, 450
            for item_card in self.player.player_item_deck.cards:
                item_index = item_card.card_id
                item_image = gItems_image_list[item_index - 1]  # -1 since the item index starts from 1
                frame_image = gFrames_image_list[3]
                position = (x_offset, y_offset)
                final_card = self.player.player_item_deck.render(frame_image, item_image)
                screen.blit(final_card, position)
                x_offset += 150

        elif not self.show_item_cards and not self.show_ability_cards:
                x_offset, y_offset = 100, 450
                back_of_item = gFrames_image_list[4]
                screen.blit(back_of_item, (x_offset, y_offset))

                 


            