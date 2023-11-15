import pygame
from src.Dependencies import *
from src.constants import *
from src.Deck import Deck
from src.Card import AbilityCard

class Player():
    def __init__(self,max_health, action_points, attack_power, attack_dice):
        self.x = None
        self.y = None

        self.ability_deck = Deck(1,'ability',[AbilityCard(**item) for item in ability_attributes])
        self.player_item_deck = Deck(1,'item',[])
        
        self.action_points = action_points
        self.attack_power = attack_power
        self.attack_dice = attack_dice
        self.damage = attack_power + attack_dice

        self.max_health = max_health
        self.curr_health = self.max_health
        #ablity_deck = Deck("ability")
        self.sprite = pygame.image.load("graphics/char/paladin.png")
        self.sprite = pygame.transform.scale(self.sprite, (165,315))
        

    def attack(self, monster, DN):
        pass

    def heal_self(self, amount):
        self.curr_health += amount
    
    def take_damage(self, damage):
        self.curr_health -= damage

    def got_debuff(self, amount):
        self.damage -= amount

    def increase_atk(self,amount):
        self.damage += amount

    def increase_ap(self, amount):
        self.action_points += amount

    def decrease_ap(self, amount):
        self.action_points -= amount
    
    def reset_atk_power(self):
        self.attack_power = 0

    def setXY(self, x: int = None, y: int = None):
        if x != None:
            self.x = x
        if y != None:
            self.y = y

    def update(self, dt, events):
        if self.curr_health > self.max_health:
            self.curr_health = self.max_health\
    
    def display_HP(self,screen):
        player_hp_text = gFonts['minecraft_small'].render(f"HP: {self.curr_health}", False, (175, 53, 42))
        hp_rect = player_hp_text.get_rect(topleft=(20, 20))
        screen.blit(player_hp_text, hp_rect)
    
    def render(self, screen):
        screen.blit(self.sprite,(self.x,self.y))
        