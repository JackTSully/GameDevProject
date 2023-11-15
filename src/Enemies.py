import pygame
from src.Dependencies import *

class Enemies():
    def __init__(self, card_id, name, description, max_health, attack_dice, attack_bonus, e_ability_id):
        self.card_id = card_id
        self.name = name
        self.description = description
        self.max_health = max_health
        self.cur_health = self.max_health
        self.attack_dice = attack_dice
        self.attack_bonus = attack_bonus
        self.e_ability_id = e_ability_id
        self.damage = attack_bonus + attack_dice

        self.x = None
        self.y = None
        self.cur_health = self.max_health

        self.sprite = gsEnemies_Image_list[card_id-12]
        self.sprite = pygame.transform.scale(self.sprite, (250,250))

    def attack(self, monster, DN):
        pass

    def attack(self, player):
        player.take_damage(self.damage)

    def take_damage(self, amount):
        self.cur_health -= amount
        if self.cur_health < 0:
            self.cur_health = 0 

    def got_debuff(self, amount):
        self.damage -= amount

    def increase_atk(self, amount):
        self.damage += amount
    
    def debuff_player(self, player, amount):
        player.damage -= amount

    def disabled_skill(self):
        self.e_ability_id = 0

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