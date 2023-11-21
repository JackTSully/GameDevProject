from src.states.BaseState import BaseState
import pygame, sys, copy, time, threading
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

        self.dice_instance = Dice()

        self.bg_image = None
        

        self.turn = 0
        self.enemy_rounds = 0
        self.player_rounds = 0
        self.attack_delay = 500
        self.enemy_delay = 1000
        self.rolling_delay = 3000
        self.rolled_damage = 0
        self.e_rolled_damage = 0

        self.time_interval = 3
        self.timer = 0
        
        self.time_interval_next = 3
        self.timer_next = 0
        
        self.player = None
        self.floor = None

        self.cursor_position = (0, 0)

        self.selected_card = None
        self.show_ability_cards = False
        self.show_item_cards = False
        
        self.duplication_effect_active = False
        self.double_roll_active = False
        self.charged_attack_active = False
        self.charged_cooldown = 0
        self.counter_attack_active = False
        self.counter_cooldown = 0
        self.enemies_attack = False
        self.invincible_active = False
        self.rolling = False
        self.e_rolling = False

        self.color_player = (0, 0, 0) 
        self.color_enemy = (0, 0, 0)
        self.P_roll = 0
        self.E_roll = 0
        
        self.item_description = None
        self.item_description_show_right = True
         

    def Enter(self,params):
        self.player = params[0]
        self.floor = params[1]
        self.player.setXY(WIDTH/11,None)
        self.enemies = Enemies(params[2].card_id,params[2].name,params[2].description,params[2].max_health,params[2].attack_dice,
                               params[2].attack_bonus, params[2].e_ability_id)
        self.enemies.setXY(WIDTH-300 ,HEIGHT/3)
        
        self.charged_cooldown = 0
        self.counter_cooldown = 0
        
        bg_image_path = floor_background[self.floor.get_floor_lvl()-1]
        self.bg_image = pygame.image.load(bg_image_path)
        self.bg_image = pygame.transform.scale(self.bg_image, (WIDTH + 5, HEIGHT + 5))

        #self.floor = params[1]
        
        
        self.time_interval = 3
        self.timer = 0
        self.time_interval_next = 3
        self.timer_next = 0


    def Exit(self):
        pass


    def update(self, dt, events):

        self.rolled_damage = self.dice_instance.roll_dice(20)
        self.e_rolled_damage = self.dice_instance.roll_dice(abs(self.enemies.attack_dice)) + self.enemies.attack_bonus

        
        if self.enemies.cur_health <= 0:
            self.timer_next += dt
            if self.timer_next > self.time_interval_next:
                
                if self.floor.curr_room == self.floor.rooms["boss"]:
                    if self.floor.get_floor_lvl() == 4:
                        self.state_machine.Change('win',[self.player,self.floor])
                    else:    
                        self.state_machine.Change('rest',[self.player,self.floor])
                else:    
                    self.state_machine.Change('map',[self.player, self.floor])
                


        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if event.key == pygame.K_RETURN:
                          
                    if self.floor.curr_room == self.floor.rooms["boss"]:
                        if self.floor.get_floor_lvl() == 4:
                            self.state_machine.Change('win',[self.player,self.floor])
                        else:    
                            self.state_machine.Change('rest',[self.player,self.floor])
                    else:    
                        self.state_machine.Change('map',[self.player, self.floor])
                    

                if event.key == pygame.K_UP:
                    self.show_ability_cards = False
                    self.show_item_cards =True

                if event.key == pygame.K_DOWN:
                    self.show_ability_cards = True
                    self.show_item_cards = False
                    
            frame_size = (140, 200)
            self.selected_card = None

            if self.show_ability_cards:

                for i, ability_card in enumerate(self.player.ability_deck.cards):
                    x_offset, y_offset = 100 + i * 150, HEIGHT-225 
                    card_rect = pygame.Rect(x_offset, y_offset, frame_size[0], frame_size[1])

                    if event.type == pygame.MOUSEBUTTONDOWN: 
                        if card_rect.collidepoint(self.cursor_position) and event.button == 1:
                            self.selected_card = ability_card 
                            break
                        elif card_rect.collidepoint(self.cursor_position) and event.button == 3:
                            self.item_card_index = i

                            self.item_description = self.player.ability_deck.get_card(self.item_card_index).description
                            if self.item_card_index > 2:
                                self.item_description_show_right = False

                            
                    if event.type == pygame.MOUSEMOTION:
                        self.item_description = None
                        self.item_description_show_right = True
                else:
                    self.item_card_index = None
                    self.selected_card = None

            if self.show_item_cards:

                for i, item_card in enumerate(self.player.player_item_deck.cards):
                    x_offset, y_offset = 100 + i * 150, HEIGHT-225 
                    card_rect = pygame.Rect(x_offset, y_offset, frame_size[0], frame_size[1])

                    if event.type == pygame.MOUSEBUTTONDOWN:  # 1 corresponds to the left mouse button
                        if card_rect.collidepoint(self.cursor_position) and event.button == 1:
                            self.selected_card = item_card
                            
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
                    self.selected_card = None
        
        
            
                
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and self.turn == 1:
                #print(event.type, self.turn, self.selected_card) 
                if self.selected_card:
                    print(f"Clicked on the selected card: {self.selected_card.card_id}")
                    
                    if self.selected_card:
                        if self.duplication_effect_active:
                            duplicated_card = copy.deepcopy(self.selected_card)
                            self.player.player_item_deck.add_cards(duplicated_card)
                    
                    if self.selected_card.effect_id == 1001: #Heal

                        if self.duplication_effect_active:
                            self.duplication_effect_active = False
                        else:
                            self.player.heal_self(5)
                            self.player.action_points_offset -= 1
                            self.player.player_item_deck.cards.remove(self.selected_card)


                    elif self.selected_card.effect_id == 1002: # dec_atk

                        if self.duplication_effect_active:
                            self.duplication_effect_active = False

                        else:
                            print(f"Before Enemy Debuff - Attack Dice: {self.enemies.attack_dice}")
                            self.enemies.got_debuff(5,1)
                            self.player.action_points_offset -= 1
                            self.player.player_item_deck.cards.remove(self.selected_card)
                            print(f"After Enemy Debuff - Attack Dice: {self.enemies.attack_dice}")

                    elif self.selected_card.effect_id == 1003: #dis_skill

                        if self.duplication_effect_active:
                            self.duplication_effect_active = False
                        else:
                            self.enemies.disabled_skill()
                            self.player.action_points_offset -= 1
                            self.player.player_item_deck.cards.remove(self.selected_card)                        

                    elif self.selected_card.effect_id == 1004: #inv

                        if self.duplication_effect_active:
                            self.duplication_effect_active = False
                        else:
                            self.player.action_points_offset -= 1
                            self.invincible_active = True
                            self.player.player_item_deck.cards.remove(self.selected_card)                            

                    elif self.selected_card.effect_id == 1005: #inc_ap
    
                        if self.duplication_effect_active:
                            self.duplication_effect_active = False
                        else:
                            self.player.increase_ap(1)
                            self.player.player_item_deck.cards.remove(self.selected_card)

                    elif self.selected_card.effect_id == 1006: #inc_atk
                        
                        if self.duplication_effect_active:
                            self.duplication_effect_active = False

                        else:
                            self.player.increase_atk(5)
                            self.player.action_points_offset -= 1
                            self.player.player_item_deck.cards.remove(self.selected_card)

                    elif self.selected_card.effect_id == 1007: #dup_card
                        self.player.action_points_offset -= 1
                        self.duplication_effect_active = True
                        self.player.player_item_deck.cards.remove(self.selected_card)

                    elif self.selected_card.effect_id == 1008: #add_roll
                        if self.duplication_effect_active:
                            self.duplication_effect_active = False
                            self.selected_card = None
                        else:
                            self.player.action_points_offset -= 1
                            self.player.player_item_deck.cards.remove(self.selected_card)
                            self.double_roll_active = True


                    elif self.selected_card.effect_id == 2001: #attack
                        self.charged_cooldown -= 1
                        self.counter_cooldown -= 1
                        if not self.double_roll_active: 
                            self.rolling = True
                            self.enemies.take_damage(self.rolled_damage + self.player.attack_power)
                            self.player.action_points -= 1
                            self.selected_card = None
                            self.turn = 2
                            
                            print(self.turn)
                        if self.double_roll_active:
                            self.rolling = True
                            self.enemies.take_damage(self.rolled_damage*2 + self.player.attack_power)
                            self.player.action_points -= 1
                            self.selected_card = None
                            self.turn = 2
                            print(self.turn)


                    elif self.selected_card.effect_id == 2002: #charge

                        if not self.charged_attack_active and self.charged_cooldown == 0:
                            
                            if not self.double_roll_active:
                                self.roll1 = self.rolled_damage + self.player.attack_power
                                print(f"Roll 1: {self.roll1}")
                                self.rolling = True
                                self.player.action_points -= 2
                                self.selected_card = None
                                self.turn = 2
                                self.charged_attack_active = True
                                self.charged_cooldown = 2
                                self.P_roll += self.roll1

                            elif self.double_roll_active:
                                self.roll1 = self.rolled_damage*2 + self.player.attack_power
                                print(f"Roll 1: {self.roll1}")
                                self.rolling = True
                                self.player.action_points -= 2
                                self.selected_card = None
                                self.turn = 2
                                self.charged_attack_active = True
                                self.charged_cooldown = 2


                    elif self.selected_card.effect_id == 2003: #counter
                        
                        if not self.counter_attack_active and self.counter_cooldown == 0:

                            if not self.enemies_attack:
                                pygame.time.delay(self.attack_delay)
                                print(f"Before Enemy Debuff - Damage: {self.enemies.attack_dice}")
                                self.player.action_points -= 2
                                self.enemies.got_debuff(2, 1)
                                print(f"After Enemy Debuff - Damage: {self.enemies.attack_dice}")
                                self.turn = 2
                                self.selected_card = None
                                self.counter_attack_active = True
                                self.counter_cooldown = 2  
                        
                    elif self.selected_card.effect_id == 2004: #block
                        self.charged_cooldown -= 1
                        self.counter_cooldown -= 1
                        pygame.time.delay(self.attack_delay)
                        print(f"Before Enemy Debuff - Damage: {self.enemies.attack_dice}")
                        self.player.action_points -= 1
                        self.enemies.got_debuff(5,1)
                        print(f"After Enemy Debuff - Damage: {self.enemies.attack_dice}")
                        self.selected_card = None
                        self.turn = 2

                    self.P_roll = self.rolled_damage + self.player.attack_power
                    self.E_roll = self.e_rolled_damage + self.enemies.attack_bonus

                    if self.double_roll_active:
                        self.P_roll *= 2
                        self.E_roll *= 2

                    return
            
             


        if self.charged_cooldown < 0:
            self.charged_cooldown = 0
        if self.counter_cooldown < 0:
            self.counter_cooldown = 0                

        if self.turn == 0:
            self.turn = 1

        if self.turn == 1:
            self.enemies.reset_debuff()
            self.player.action_points = 3 + self.player.action_points_offset
            self.enemies_attack = False
            self.rolling = False

            if self.charged_attack_active: 
                    if not self.double_roll_active:
                        self.roll2 = self.rolled_damage + self.player.attack_power
                        self.total_roll = self.roll1 + self.roll2
                        print(f"fRoll 2: {self.roll2}")
                        print(f"Total Roll: {self.total_roll}")
                        self.rolling = True
                        pygame.time.delay(self.attack_delay) 
                        self.enemies.take_damage(self.total_roll)
                        self.selected_card = None
                        self.P_roll += self.roll2
                        self.turn = 2  
                        self.charged_attack_active = False
                        self.rolling = False

                    elif self.double_roll_active:
                        self.roll2 = self.rolled_damage*2 + self.player.attack_power
                        self.total_roll = self.roll1 + self.roll2
                        print(f"fRoll 2: {self.roll2}")
                        print(f"Total Roll: {self.total_roll}")
                        self.rolling = True
                        pygame.time.delay(self.attack_delay) 
                        self.enemies.take_damage(self.total_roll)
                        self.rolling = False
                        self.selected_card = None
                        self.turn = 2                                                          
                        self.charged_attack_active = False



        if self.turn == 1 and self.player.action_points <= 0:
            self.charged_cooldown -= 1
            self.counter_cooldown -= 1
            self.turn = 2
            self.player.action_points_offset = 0
            self.double_roll_active = False
            self.enemies.reset_debuff()

        if self.enemies.attack_dice < 0:
            self.enemies.attack_dice = 0

        elif self.turn == 2:
            if 1 == 2: # was "self.enemy_rounds == 3"
                pygame.time.delay(self.enemy_delay)
                self.player.got_debuff(2, 1) 
                self.turn = 1
                self.enemy_rounds += 1
                self.player.action_points_offset = 0
                self.duplication_effect_active = False
                self.enemies.debuff_turns = 0
                self.e_rolling = True
                
            else:
                if not self.invincible_active:
                    print(self.turn)
                    self.enemies_attack = True

                    if self.enemies_attack and self.counter_attack_active:
                        if not self.double_roll_active:
                            counter_attack_damage = self.rolled_damage + self.player.attack_power 
                            self.enemies.take_damage(counter_attack_damage)
                            print(f"Counter Attack: {counter_attack_damage}")
                            self.enemies_attack = False
                            self.counter_attack_active = False

                        if self.double_roll_active:
                            counter_attack_damage = self.dice_instance.roll_dice(20)*2 + self.player.attack_power 
                            self.enemies.take_damage(counter_attack_damage)
                            print(f"Counter Attack: {counter_attack_damage}")
                            self.enemies_attack = False
                            self.counter_attack_active = False


                    pygame.time.delay(self.enemy_delay)
                    self.player.take_damage(self.e_rolled_damage + self.enemies.attack_bonus)
                    print(f"Enemies Attack Damage {self.e_rolled_damage + self.enemies.attack_bonus}")
                    self.enemy_rounds += 1
                    self.turn = 1
                    print(self.enemy_rounds)
                    self.player.action_points_offset = 0
                    self.duplication_effect_active = False
                    self.enemies.debuff_turns = 0
                    self.invincible_active = False
                    self.e_rolling = False

                elif self.invincible_active:
                    self.enemies_attack = True

                    if self.enemies_attack:
                        if not self.double_roll_active:
                            counter_attack_damage = self.rolled_damage + self.player.attack_power 
                            self.enemies.take_damage(counter_attack_damage)
                            print(f"Counter Attack: {counter_attack_damage}")
                            self.enemies_attack = False
                        if self.double_roll_active:
                            counter_attack_damage = self.rolled_damage*2 + self.player.attack_power 
                            self.enemies.take_damage(counter_attack_damage)
                            print(f"Counter Attack: {counter_attack_damage}")
                            self.enemies_attack = False

                    self.e_rolled_damage = 0
                    pygame.time.delay(self.enemy_delay)
                    self.player.take_damage(self.e_rolled_damage + self.enemies.attack_bonus)
                    print(f"Enemies Attack Damage {self.e_rolled_damage + self.enemies.attack_bonus}")
                    self.enemy_rounds += 1
                    self.turn = 1
                    print(self.enemy_rounds)
                    self.player.action_points_offset = 0
                    self.duplication_effect_active = False
                    self.invincible_active = False

        if self.player.curr_health <= 0:
            #self.player.curr_health = self.player.max_health
            self.state_machine.Change('game_over')


        

        self.cursor_position = pygame.mouse.get_pos()
                    
        
        self.timer = self.timer + dt


    def render(self, screen):
        
        screen.blit(self.bg_image, (0, 0)) 
        
        if self.enemies.cur_health <= 0:
            victory_text = gFonts['minecraft_small'].render("VICTORY", False, "white", "green")
            victory_rect = victory_text.get_rect(center=(WIDTH/2, HEIGHT/2))
            screen.blit(victory_text, victory_rect)

        player_hp_text = gFonts['minecraft_small'].render(f"HP: {self.player.curr_health}", False, (175, 53, 42))
        hp_rect = player_hp_text.get_rect(topleft=(20, 20))
        screen.blit(player_hp_text, hp_rect)
        player_ap_text = gFonts['minecraft_small'].render(f"AP: {self.player.action_points}", False, (255, 255, 255))
        hp_rect = player_ap_text.get_rect(topleft=(20, 80))
        screen.blit(player_ap_text, hp_rect)
        player_ap_text = gFonts['minecraft_small'].render(f"ATK: {self.player.attack_power}", False, (255, 255, 255))
        hp_rect = player_ap_text.get_rect(topleft=(20, 140))
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
        y_offset = HEIGHT-225 
        
        self.enemies.render(screen)

        if self.show_ability_cards:

            for ability_card in self.player.ability_deck.cards:
                ability_index = ability_card.card_id
                ability_image = gAbilities_image_list[ability_index - 8] 
                frame_image = gFrames_image_list[0]
                position = (x_offset, y_offset)


                charged_has_cooldown = ability_card == self.selected_card and self.charged_cooldown > 0
                counter_has_cooldown = ability_card == self.selected_card and self.counter_cooldown > 0

                final_card = self.player.player_item_deck.render(frame_image, ability_image)
                screen.blit(final_card, position)
                
                ability_name = ability_card.name.split(" ")
                y = 0
                
                # Renders card names
                for string in ability_name:
                    text = gFonts['minecraft_card'].render(string, False, ('black'))
                    rect = text.get_rect(center=(x_offset + 75 , y_offset + 142 + y))
                    screen.blit(text, rect)
                    y += 17

                if charged_has_cooldown:
           
                    darkened_position = (250, y_offset)
                    darkened_card = pygame.Surface((140, 200), pygame.SRCALPHA)
                    darkened_card.fill((0, 0, 0, 128))
                    screen.blit(darkened_card, darkened_position)

                    cooldown_text = gFonts['minecraft_small'].render(f"{self.charged_cooldown}", False, (255, 255, 255))
                    cooldown_rect = cooldown_text.get_rect(center=(250 + 140 // 2, y_offset + 200 // 2))
                    screen.blit(cooldown_text, cooldown_rect)

                if counter_has_cooldown:
           
                    darkened_position = (400, y_offset)
                    darkened_card = pygame.Surface((140, 200), pygame.SRCALPHA)
                    darkened_card.fill((0, 0, 0, 128))
                    screen.blit(darkened_card, darkened_position)

                    cooldown_text = gFonts['minecraft_small'].render(f"{self.counter_cooldown}", False, (255, 255, 255))
                    cooldown_rect = cooldown_text.get_rect(center=(400 + 140 // 2, y_offset + 200 // 2))
                    screen.blit(cooldown_text, cooldown_rect)

                x_offset += 150


        if self.show_item_cards:
            x_offset, y_offset = 100, HEIGHT-225 
            for item_card in self.player.player_item_deck.cards:
                item_index = item_card.card_id
                item_image = gItems_image_list[item_index-1]  # -1 since the item index starts from 1
                frame_image = gFrames_image_list[3]
                position = (x_offset, y_offset)
                final_card = self.player.player_item_deck.render(frame_image, item_image)
                screen.blit(final_card, position)
                
                # Renders card names
                item_name = item_card.name.split(" ")
                y = 0
                for string in item_name:
                    text = gFonts['minecraft_card'].render(string, False, ('black'))
                    rect = text.get_rect(center=(x_offset + 75 , y_offset + 142 + y))
                    screen.blit(text, rect)
                    y += 17
                
                x_offset += 150
            
        if self.item_description != None:
            description = gFonts['minecraft_tiny'].render(self.item_description, False, "yellow", "black")
            
            if self.item_description_show_right == True:
                rect = description.get_rect(bottomleft=(100, HEIGHT/2+120))
            else:
                rect = description.get_rect(bottomleft=(100, HEIGHT/2+120))
            screen.blit(description, rect)

        elif not self.show_item_cards and not self.show_ability_cards:
                x_offset, y_offset = 100, HEIGHT-225
                back_of_item = gFrames_image_list[4]
                screen.blit(back_of_item, (x_offset, y_offset))


        def render_dice_number(dice_image, number, color=(0, 0, 0)):
            font = pygame.font.Font(None, 52)
            text = font.render(str(number), True, color)
            dice_image.blit(text, (dice_image.get_width() / 2 - text.get_width() / 2, dice_image.get_height() / 2 - text.get_height() / 2))

        E_Dice_type = self.enemies.attack_dice
        P_Dice_type = self.player.attack_dice
        E_Dice_image = gDice_image_list[E_Dice_type].copy()
        P_Dice_image = gDice_image_list[P_Dice_type].copy()

        if self.rolling:
                P_Number_surface = pygame.Surface((P_Dice_image.get_width()+30, P_Dice_image.get_height()), pygame.SRCALPHA)

                P_roll = self.rolled_damage

                render_dice_number(P_Number_surface, P_roll, color=(0, 0 , 0))

                P_Dice_image.blit(P_Number_surface, (0, 0))

                screen.blit(P_Dice_image, (WIDTH/2 - 80, HEIGHT/2 - 60))

                pygame.display.flip()

        if self.rolling and self.charged_attack_active:
                P_Number_surface = pygame.Surface((P_Dice_image.get_width()+30, P_Dice_image.get_height()), pygame.SRCALPHA)

                P_roll = self.rolled_damage
                E_roll = self.e_rolled_damage

                render_dice_number(P_Number_surface, P_roll, color=(0, 0 , 0))

                P_Dice_image.blit(P_Number_surface, (0, 0))

                screen.blit(P_Dice_image, (WIDTH/2 - 80, HEIGHT/2 - 60))

                pygame.display.flip()
            
        if self.e_rolling:
                E_Number_surface = pygame.Surface((E_Dice_image.get_width()+30, E_Dice_image.get_height()), pygame.SRCALPHA)

                E_roll = self.e_rolled_damage

                render_dice_number(E_Number_surface, E_roll, color=(0, 0 , 0))

                E_Dice_image.blit(E_Number_surface, (0, 0))

                screen.blit(E_Dice_image, (WIDTH/2 - 80, HEIGHT/2 - 60))

                pygame.display.flip()




        
        



            