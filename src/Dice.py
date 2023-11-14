import pygame
import sys
import random   

pygame.init()

width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Dice Roller")

white = (255, 255, 255)
black = (0, 0, 0)

font = pygame.font.SysFont(None, 40)

def roll_dice(sides):
    return random.randint(1, sides)
    

def draw_text(text, color, x, y):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=(x, y))
    screen.blit(text_surface, text_rect)

d20 = roll_dice()
print(d20)