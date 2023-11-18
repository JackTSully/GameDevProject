import pygame
import sys
import random

class Dice:

    def roll_dice(self, sides):
        return random.randint(1, sides)

    def draw_text(text, color, x, y):
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect(center=(x, y))
        screen.blit(text_surface, text_rect)

