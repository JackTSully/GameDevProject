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
    
    def render(self, screen, frame_image, item_image, position):
        screen.blit(self.sprite,(self.x,self.y))
        
        final_surface = pygame.Surface((frame_image.get_width(), frame_image.get_height())) #Create a surface (rectangle) same size as the frame_image (Just to combine the item and the frame as one)
        final_surface.blit(frame_image, (0, 0))  #put frame on to the surface at pos (0,0)

        item_x = max(0, (frame_image.get_width() - item_image.get_width()) // 2) #pos of item on surface
        item_y = max(0, (frame_image.get_height() - item_image.get_height()) //6)

        final_surface.blit(item_image,(item_x, item_y)) #put item on to the surface

        return final_surface