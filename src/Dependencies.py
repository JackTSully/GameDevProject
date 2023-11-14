import pygame
from Util import SpriteManager, Animation
import Util as Util
from StateMachine import StateMachine

pygame.init()

sprite_collection = SpriteManager().spriteCollection


gItems_image_list = [sprite_collection["Flask_of_Healing"].image,
                     sprite_collection["Potion_of_Stupidity"].image,
                     sprite_collection["Potion_of_Relaxation"].image,
                     sprite_collection["Potion_of_Swiftness"].image,
                     sprite_collection["Potion_of_Prowess"].image,
                     sprite_collection["Replicator"].image,
                     sprite_collection["Double Roll"].image,
                     sprite_collection["Shield"].image]

gFrames_image_list = [sprite_collection["Abilities_Frames"].image,
                      sprite_collection["Boss_Frames"].image,
                    sprite_collection["Enemies_Frames"].image,
                    sprite_collection["Item_Frames"].image]

gAbilities_image_list = [sprite_collection["Attack"].image,
                         sprite_collection["Block"].image,
                    sprite_collection["Charged_Attack"].image,
                    sprite_collection["Counter_Attack"].image]

gFonts = {
    'small': pygame.font.Font('fonts/font.ttf', 24),
    'medium': pygame.font.Font('fonts/font.ttf', 48),
    'large': pygame.font.Font('fonts/font.ttf', 96),
    'zelda_small': pygame.font.Font('fonts/zelda.otf', 96),
    'zelda': pygame.font.Font('fonts/zelda.otf', 128),
    'gothic_medium': pygame.font.Font('fonts/GothicPixels.ttf', 48),
    'gothic_large': pygame.font.Font('fonts/GothicPixels.ttf', 96),

}

