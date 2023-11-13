import pygame
from src.Util import SpriteManager, Animation
import src.Util as Util
from src.StateMachine import StateMachine

sprite_collection = SpriteManager().spriteCollection

gFonts = {
    'small': pygame.font.Font('fonts/font.ttf', 24),
    'medium': pygame.font.Font('fonts/font.ttf', 48),
    'large': pygame.font.Font('fonts/font.ttf', 96),
    'zelda_small': pygame.font.Font('fonts/zelda.otf', 96),
    'zelda': pygame.font.Font('fonts/zelda.otf', 128),
    'gothic_medium': pygame.font.Font('fonts/GothicPixels.ttf', 48),
    'gothic_large': pygame.font.Font('fonts/GothicPixels.ttf', 96),
    'minecraft': pygame.font.Font('fonts/Minecraft.ttf', 96),
    'dungeon': pygame.font.Font('fonts/DUNGRG__.TTF', 200),

}

from src.states.game.StartState import StartState
from src.states.game.RestState import RestState
from src.states.game.MapState import MapState
from src.states.game.CombatState import CombatState
from src.StateMachine import StateMachine