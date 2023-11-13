import pygame
from src.Dependencies import *

class Player():
    def __init__(self,max_health):
        self.x = None
        self.y = None

        self.max_health = max_health
        self.cur_health = self.max_health
        #ablity_deck = Deck("ability")
        self.sprite = pygame.image.load("graphics/char/paladin.png")
        self.sprite = pygame.transform.scale(self.sprite, (165,315))

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