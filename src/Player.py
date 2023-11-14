import pygame
from src.Dependencies import *
from src.constants import *
from src.Deck import Deck
from src.Card import AbilityCard

class Player():
    def __init__(self,max_health, action_points, attack_power):
        self.x = None
        self.y = None

        self.ability_deck = Deck(1,'ability',[AbilityCard(**item) for item in ability_attributes])
        self.player_item_deck = Deck(1,'item',[])
        
        self.action_points = action_points
        self.attack_power = attack_power
        
        self.max_health = max_health
        self.cur_health = self.max_health
        #ablity_deck = Deck("ability")
        self.sprite = pygame.image.load("graphics/char/paladin.png")
        self.sprite = pygame.transform.scale(self.sprite, (165,315))
        

    def attack(self, monster, DN):
        pass

    def heal_self(self, amount):
        self.cur_health += amount
    
    def take_damage(self, damage):
        self.cur_health -= damage  

    def setXY(self, x: int = None, y: int = None):
        if x != None:
            self.x = x
        if y != None:
            self.y = y

    def update(self, dt, events):
        if self.cur_health > self.max_health:
            self.cur_health = self.max_health
    
    def render(self, screen):
        screen.blit(self.sprite,(self.x,self.y))
        
        