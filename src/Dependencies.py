import pygame
from src.Util import SpriteManager, Animation
import src.Util as Util
from src.StateMachine import StateMachine

pygame.init()

sprite_collection = SpriteManager().spriteCollection

gPlayer_animation_list = { "idle": sprite_collection["character_idle"].animation,
                           "attack": sprite_collection["character_attack"].animation,
                           "charged_attack": sprite_collection["character_charged_Attack"].animation

}

gDice_image_list = [sprite_collection["Fake0"].image,
                    sprite_collection["Fake1"].image,
                    sprite_collection["Fake2"].image,
                    sprite_collection["Fake3"].image,
                    sprite_collection["Fake4"].image,
                    sprite_collection["Fake5"].image,
                    sprite_collection["D6"].image,
                    sprite_collection["Fake6"].image,
                    sprite_collection["D8"].image,
                    sprite_collection["Fake7"].image,
                    sprite_collection["D10"].image,
                    sprite_collection["Fake9"].image,
                    sprite_collection["D12"].image,
                    sprite_collection["Fake10"].image,
                    sprite_collection["Fake11"].image,
                    sprite_collection["Fake12"].image,
                    sprite_collection["Fake13"].image,
                    sprite_collection["Fake14"].image,
                    sprite_collection["Fake15"].image,
                    sprite_collection["Fake16"].image,
                    sprite_collection["D20"].image      
                    
]

gItems_image_list = [sprite_collection["Flask_of_Healing"].image,
                     sprite_collection["Potion_of_Stupidity"].image,
                     sprite_collection["Potion_of_Relaxation"].image,
                     sprite_collection["Shield"].image,
                     sprite_collection["Potion_of_Swiftness"].image,
                     sprite_collection["Potion_of_Prowess"].image,
                     sprite_collection["Replicator"].image,
                     sprite_collection["Double Roll"].image
                     ]

gFrames_image_list = [sprite_collection["Abilities_Frames"].image,
                      sprite_collection["Boss_Frames"].image,
                    sprite_collection["Enemies_Frames"].image,
                    sprite_collection["Item_Frames"].image,
                    sprite_collection["Back_Abilities_Frames"].image,
                    sprite_collection["Back_Item_Frames"].image]

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

gsEnemies_Image_list = [
                        sprite_collection["Secret_Room"].image,
                        sprite_collection["Fountain_of_Healing"].image,
                        sprite_collection["Heroes_Monument"].image,
                        sprite_collection["Wounded_Adventurer"].image,
                        sprite_collection["Pitfall_Trap"].image,
                        sprite_collection["Dart_Trap"].image,
                        sprite_collection["Boulder_Trap"].image, 
                        sprite_collection["Slime"].image, 
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
                        sprite_collection["Emperor_Gorilla"].image
                      ]

gSounds = {
    'bg_music':pygame.mixer.Sound('sounds/main_menu_theme.mp3')
}

gFonts = {
    'small': pygame.font.Font('fonts/font.ttf', 24),
    'medium': pygame.font.Font('fonts/font.ttf', 48),
    'large': pygame.font.Font('fonts/font.ttf', 96),
    'zelda_small': pygame.font.Font('fonts/zelda.otf', 96),
    'zelda': pygame.font.Font('fonts/zelda.otf', 128),
    'gothic_medium': pygame.font.Font('fonts/GothicPixels.ttf', 48),
    'gothic_large': pygame.font.Font('fonts/GothicPixels.ttf', 96),
    'minecraft': pygame.font.Font('fonts/Minecraft.ttf', 96),
    'minecraft_small': pygame.font.Font('fonts/Minecraft.ttf', 50),
    'minecraft_tiny': pygame.font.Font('fonts/Minecraft.ttf', 27),
    'minecraft_card': pygame.font.Font('fonts/Minecraft.ttf', 18),
    'dungeon': pygame.font.Font('fonts/DUNGRG__.TTF', 200),

}

from src.states.game.StartState import StartState
from src.states.game.RestState import RestState
from src.states.game.MapState import MapState
from src.states.game.EventState import EventState
from src.states.game.CombatState import CombatState
from src.states.game.GameOverState import GameOverState
from src.states.game.WinState import WinState
from src.states.game.PlayerInfoState import PlayerInfoState
from src.states.game.DiscardState import DiscardState

from src.StateMachine import StateMachine

