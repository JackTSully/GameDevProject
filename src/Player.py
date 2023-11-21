import pygame
from src.Dependencies import *
from src.constants import *
from src.Deck import Deck
from src.Card import AbilityCard
from src.Animation import *

class Player():
    def __init__(self,max_health, action_points, attack_power, attack_dice):
        self.x = None
        self.y = None

        self.ability_deck = Deck(1,'ability',[AbilityCard(**item) for item in ability_attributes])
        self.player_item_deck = Deck(1,'item',[])
        
        self.attack_power = attack_power
        self.attack_dice = attack_dice
        self.damage = attack_power + attack_dice
        self.action_points_offset = 0
        self.action_points = action_points + self.action_points_offset
        self.debuff_turns = 0

        self.max_health = max_health
        self.curr_health = self.max_health
        #ablity_deck = Deck("ability")

        #self.sprite = pygame.transform.scale(self.sprites, (165,315))

        self.sprite = pygame.image.load("graphics/char/paladin.png")
        self.sprite = pygame.transform.scale(self.sprite, (165,315))
        self.animation_state = "idle"
        self.animation_list = gPlayer_animation_list
        self.state_machine = None
        self.curr_animation = None


    def ChangeAnimation(self, name):
        self.curr_animation = self.animation_list[name]

    def ChangeState(self, name):
        self.state_machine.Change(name)
        
    def check_item_overcap(self):
        
        if len(self.player_item_deck.get_cards()) > 6:
            return True
        else:
            return False

    def heal_self(self, amount):
        self.curr_health += amount
    
    def take_damage(self, damage):
        self.curr_health -= damage

    def got_debuff(self, amount, duration):
        self.damage -= amount
        self.debuff_turns = duration
        if self.damage <= 0:
            self.damage = 0

    def increase_atk(self,amount):
        self.attack_power += amount

    def increase_ap(self, amount):
        self.action_points_offset += amount
        self.action_points += self.action_points_offset
        self.action_points = 3


    def decrease_ap(self, amount):
        self.action_points -= amount
    
    def reset_atk_power(self):
        self.attack_power = 0

    def restore(self):
        self.debuff_turns = 0 

    def setXY(self, x: int = None, y: int = None):
        if x != None:
            self.x = x
        if y != None:
            self.y = y

    def update(self, dt, events):

        self.action_points_offset = 0

        if self.curr_health > self.max_health:
            self.curr_health = self.max_health
            #self.state_machine.update(dt, events)

        if self.debuff_turns > 0:
            self.restore()
        
        #self.current_animation.update(dt)

        
    def display_HP(self,screen):
        player_hp_text = gFonts['minecraft_small'].render(f"HP: {self.curr_health}", False, (175, 53, 42))
        hp_rect = player_hp_text.get_rect(topleft=(20, 20))
        screen.blit(player_hp_text, hp_rect)

        if self.debuff_turns > 0:
            self.restore()

    def render(self, screen):
        screen.blit(self.sprite, (self.x, self.y))
        #print(cur_frame)
    
    def CreateAnimations(self):
        self.animation_list = gPlayer_animation_list
        