import pygame
from src.Util import SpriteManager, Animation
import src.Util as Util
from src.StateMachine import StateMachine

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

gEnemies_Image_list = [sprite_collection["Slime"].image, 
                       sprite_collection["Stone_Golem"].image, 
                       sprite_collection["Diamond_Golem"].image,
                       sprite_collection["Skeleton"].image,
                       sprite_collection["Skeleton_Mage"].image,
                       sprite_collection["Skeleton_Juggernaut"].image,
                       sprite_collection["Temple_Guardian"].image, 
                       sprite_collection["Fanatic_Cultist"].image,
                       sprite_collection["Vampire_Bat"].image,
                       sprite_collection["Feral_Monkey"].image,
                       sprite_collection["King_Ape"].image,
                       sprite_collection["Underminer"].image,
                       sprite_collection["Necromancer"].image,
                       sprite_collection["Cult_Leader"].image,
                       sprite_collection["Emperor_Gorilla"].image]

gsEnemies_Image_list = [sprite_collection["sSlime"].image, 
                        sprite_collection["sStone_Golem"].image, 
                        sprite_collection["sDiamond_Golem"].image,
                        sprite_collection["sSkeleton"].image,
                        sprite_collection["sSkeleton_Mage"].image,
                        sprite_collection["sSkeleton_Juggernaut"].image,
                        sprite_collection["sTemple_Guardian"].image, 
                        sprite_collection["sFanatic_Cultist"].image,
                        sprite_collection["sVampire_Bat"].image,
                        sprite_collection["sFeral_Monkey"].image,
                        sprite_collection["sKing_Ape"].image,
                        sprite_collection["sUnderminer"].image,
                        sprite_collection["sNecromancer"].image,
                        sprite_collection["sCult_Leader"].image,
                        sprite_collection["sEmperor_Gorilla"].image,
                        sprite_collection["Boulder_Trap"].image, 
                        sprite_collection["Dart_Trap"].image,
                        sprite_collection["Fountain_of_Healing"].image,
                          sprite_collection["Pitfall_Trap"].image,
                        sprite_collection["Secret_Room"].image,
                          sprite_collection["Wounded_Adventurer"].image,
                        sprite_collection["Heroes_Monument"].image]



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
from src.states.game.GameOverState import GameOverState
from src.StateMachine import StateMachine

