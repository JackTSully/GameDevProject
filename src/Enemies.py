import pygame, random
from src.constants import *
from src.Dependencies import *
from src.Dice import Dice

class Enemies():
    def __init__(self, card_id, name, description, max_health, attack_dice, attack_bonus, e_ability_id):
        dice_instance = Dice()
        self.card_id = card_id
        self.name = name
        self.description = description
        self.max_health = max_health
        self.cur_health = self.max_health
        self.attack_dice = attack_dice
        self.ori_attack_dice = self.attack_dice
        self.attack_bonus = attack_bonus
        self.e_ability_id = e_ability_id
        self.total_damage = 0
        self.debuff_turns = 0
        self.rolled_damage = 0
        self.x = None
        self.y = None
        self.cur_health = self.max_health
        self.attack_bonus = self.attack_bonus
        self.debuffed = False
        
        self.sprite = gsEnemies_Image_list[card_id-12]
        self.sprite = pygame.transform.scale(self.sprite, (250,250))



    def take_damage(self, amount):
        self.cur_health -= amount
        if self.cur_health < 0:
            self.cur_health = 0

    def restore(self):
        self.debuff_turns = 0 

    def got_debuff(self, amount, duration):
        self.debuff_turns = duration
        if self.debuff_turns > 0:
            self.debuffed = True
            if self.debuffed:
                self.attack_dice -= amount
                self.debuffed = False
        if self.attack_dice < 0:
            self.attack_dice = 0
        else:
            self.debuffed = False

    def reset_debuff(self):
        if not self.debuffed:
            self.attack_dice = self.ori_attack_dice
            self.debuff_turns = 0

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
        self.sprite.set_colorkey((0,0,0))
        screen.blit(self.sprite,(self.x,self.y))