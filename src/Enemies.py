import pygame
from src.Dependencies import *

class Enemies():
    def __init__(self, card_id, name, description, max_health, attack_dice, attack_bonus, e_ability_id):
        self.card_id = card_id
        self.name = name
        self.description = description
        self.max_health = max_health
        self.attack_dice = attack_dice
        self.attack_bonus = attack_bonus
        self.e_ability_id = e_ability_id

        self.x = None
        self.y = None
        self.cur_health = self.max_health
        #ablity_deck = Deck("ability")

    def attack(self, monster, DN):
        pass

    def heal_self(self, amount):
        self.cur_health += amount
    
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