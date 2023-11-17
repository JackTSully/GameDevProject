import pygame
import sys
import random   

pygame.init()

width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Dice")

white = (255, 255, 255)
black = (0, 0, 0)

font = pygame.font.SysFont(None, 40)

def roll_dice(sides):
    return random.randint(1, sides)

def multi_roll(sides):
    roll1 = random.randint(1, sides)
    roll2 = random.randint(1,sides)
    total_roll = roll1 + roll2
    return total_roll, roll1, roll2
    

def draw_text(text, color, x, y):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=(x, y))
    screen.blit(text_surface, text_rect)

def enemy_roll_attack_dice(self):
    if self.attack_dice.lower().startswith("d"):
        sides = int(self.attack_dice[1:])
        return random.randint(1, sides)

d20 = roll_dice(20)
d8 = roll_dice(8)
d6 = roll_dice(6)
d4 = roll_dice(4)
total_roll, roll1, roll2 = multi_roll(20)
print(d20)