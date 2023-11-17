import pygame, random
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
        self.total_damage = 0
        self.debuff_turns = 0

        self.x = None
        self.y = None
        self.cur_health = self.max_health

        self.sprite = gsEnemies_Image_list[card_id-12]
        self.sprite = pygame.transform.scale(self.sprite, (250,250))

    def attack(self, player):
        rolled_damage = self.roll_attack_dice()
        self.total_damage = self.attack_bonus + rolled_damage
        player.take_damage(self.total_damage)
        print(f"Total E Damage: {self.total_damage}")
        return self.total_damage

    def take_damage(self, amount):
        self.cur_health -= amount
        if self.cur_health < 0:
            self.cur_health = 0

    def restore(self):
        self.debuff_turns = 0 

    def got_debuff(self, amount, duration):
        print(f"Before Debuff - Total Damage: {self.total_damage}")
        self.total_damage -= amount
        self.debuff_turns = duration
        if self.total_damage < 0:
            self.total_damage = 0
        print(f"After Debuff - Total Damage: {self.total_damage}")

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

        if self.debuff_turns > 0:
            self.restore()
    
    def render(self, screen):
        screen.blit(self.sprite,(self.x,self.y))