import math

WIDTH = 1280
HEIGHT = 720

item_attributes = [
    {"card_id": 1, "name": "Healing Flask", "description": "+5 HP", "effect_id": 1001, "action_cost": 1, "turn_cost": 0},
    {"card_id": 2, "name": "Potion of Resistance", "description": "-5 incoming DMG for this turn", "effect_id": 1002, "action_cost": 1, "turn_cost": 1},
    {"card_id": 3, "name": "Potion of Revival", "description": "After death, revives you back to 10 HP", "effect_id": 1003, "action_cost": 1, "turn_cost": 1},
    {"card_id": 4, "name": "Shield", "description": "Invulnerable to the next attack", "effect_id": 1004, "action_cost": 1, "turn_cost": 1},
    {"card_id": 5, "name": "Potion of Swiftness", "description": "+1 AP", "effect_id": 1005, "action_cost": 0, "turn_cost": 1},
    {"card_id": 6, "name": "Potion of Prowess", "description": "+ 5 ATK for the duration of the fight", "effect_id": 1006, "action_cost": 1, "turn_cost": 1},
    {"card_id": 7, "name": "Replicator", "description": "Duplicates selected cards on-hand", "effect_id": 1007, "action_cost": 1, "turn_cost": 1},
    {"card_id": 8, "name": "Double Roll", "description": "Gain an additional roll", "effect_id": 1008, "action_cost": 1, "turn_cost": 0},
]

ability_attributes = [
    {"card_id": 8, "name": "Attack 1AP", "description": "Deal DMG (D20) to the selected enemy", "effect_id": 2001, "action_cost": 1, "turn_cost": 1},
    {"card_id": 9, "name": "Charged Attack 2AP", "description": "Charge your attack to deal an instance of increased DMG (2D20) next turn", "effect_id": 2002, "action_cost": 2, "turn_cost": 2},
    {"card_id": 11, "name": "Counter Attack 2AP", "description": "Blocks 2 DMG recieved and deal DMG (D20) to the attacking enemy for their whole turn.", "effect_id": 2003, "action_cost": 2, "turn_cost": 1},
    {"card_id": 10, "name": "Block 1AP", "description": "Blocks 5 DMG from the enemy's attack in their next turn.", "effect_id": 2004, "action_cost": 1, "turn_cost": 1},
]

event_attributes = [
    {"card_id": 12, "name": "Secret Room", "description": "Draw 3 Item Cards", "effect_id": 3001},
    {"card_id": 13, "name": "Fountain of Healing", "description": "Heal to full HP", "effect_id": 3002},
    {"card_id": 14, "name": "Hero's monument", "description": "ATK +3 for the whole floor", "effect_id": 3003},
    {"card_id": 15, "name": "Wounded Adventurer", "description": "Exchange a Healing Flask for another random item.(Y/N)", "effect_id": 3004},
    {"card_id": 16, "name": "Pitfall Trap", "description": "Athletic Check (10) Fail: Take D4 Damage,  Pass: Get Item Card", "effect_id": 3005},
    {"card_id": 17, "name": "Dart Trap", "description": "Athletic Check (13) Fail: Take D6 Damage,  Pass: Get Item Card", "effect_id": 3006},
    {"card_id": 18, "name": "Boulder Trap", "description": "Athletic Check (10/10) Fail: Take D8 Damage,  Pass: Get 2x Item Card", "effect_id": 3007},
]

enemy_attributes = [
                    {"card_id": 19, "name": "Slime", "description": "HP: 40, ATK: D6", "max_health": 40, "attack_dice": 6, "attack_bonus": 0, "e_ability_id": 0},
                    {"card_id": 20, "name": "Stone Golem", "description": "HP: 50, ATK: D6+1", "max_health": 50, "attack_dice": 6, "attack_bonus": 1, "e_ability_id": 1},
                    {"card_id": 21, "name": "Diamond Golem", "description": "HP: 60, ATK: D6", "max_health": 60, "attack_dice": 6, "attack_bonus": 0, "e_ability_id": 2},
                    {"card_id": 22, "name": "Skeleton", "description": "HP: 50, ATK: D6", "max_health": 50, "attack_dice": 6, "attack_bonus": 0, "e_ability_id": 3},
                    {"card_id": 23, "name": "Skeleton Mage", "description": "HP: 30, ATK: D6+1", "max_health": 30, "attack_dice": 6, "attack_bonus": 1, "e_ability_id": 4},
                    {"card_id": 24, "name": "Skeleton Juggernuat", "description": "HP: 60, ATK: D3+2", "max_health": 60, "attack_dice": 3, "attack_bonus": 2, "e_ability_id": 5},
                    {"card_id": 25, "name": "Temple Guardian", "description": "HP: 50, ATK: D6+1", "max_health": 50, "attack_dice": 6, "attack_bonus": 1, "e_ability_id": 6},
                    {"card_id": 26, "name": "Fanatic Cultist", "description": "HP: 45, ATK: D4+1", "max_health": 45, "attack_dice": 4, "attack_bonus": 1, "e_ability_id": 7},
                    {"card_id": 27, "name": "Vampire Bat", "description": "HP: 40, ATK: D6", "max_health": 40, "attack_dice": 6, "attack_bonus": 0, "e_ability_id": 8},
                    {"card_id": 28, "name": "Feral Monkey", "description": "HP: 50, ATK: D6", "max_health": 50, "attack_dice": 6, "attack_bonus": 2, "e_ability_id": 9},
                    {"card_id": 29, "name": "King Ape", "description": "HP: 70, ATK: D6+1", "max_health": 70, "attack_dice": 6, "attack_bonus": 1, "e_ability_id": 10},
                    {"card_id": 30, "name": "Underminer", "description": "HP: 65, ATK: D6+1","max_health": 65, "attack_dice": 6, "attack_bonus": 1, "e_ability_id": 11},
                    {"card_id": 31, "name": "Necromancer", "description": "HP: 60, ATK: D6", "max_health": 60, "attack_dice": 6, "attack_bonus": 0, "e_ability_id": 12},
                    {"card_id": 32, "name": "Cult Leader", "description": "HP: 65, ATK: D6+1", "max_health": 65, "attack_dice": 6, "attack_bonus": 1, "e_ability_id": 13},
                    {"card_id": 33, "name": "Emperor Gorilla", "description": "HP: 65, ATK: D10", "max_health": 65, "attack_dice": 10, "attack_bonus": 0, "e_ability_id": 14},
]

floor_background = [
    "graphics/stages/mines.png",
    "graphics/stages/catacombs.png",
    "graphics/stages/temple.png",
    "graphics/stages/forest.png"
]

EFFECT_TYPE_HEAL = 1001
EFFECT_TYPE_DECREASE_ATK = 1002
EFFECT_TYPE_DISABLE_SKILL = 1003
EFFECT_TYPE_INVULNERABLE = 1004
EFFECT_TYPE_INCREASE_AP = 1005
EFFECT_TYPE_INCREASE_ATK = 1006
EFFECT_TYPE_DUPLICATE_CARDS = 1007
EFFECT_TYPE_ADDITIONAL_ROLL = 1008

EFFECT_TYPE_ATTACK = 2001
EFFECT_TYPE_CHARGED = 2002
EFFECT_TYPE_COUNTER = 2003
EFFECT_TYPE_BLOCK = 2004

EFFECT_TYPE_DRAW = 3001
EFFECT_TYPE_EXCHANGE = 3004
EFFECT_TYPE_CHECK_10 = 3005
EFFECT_TYPE_CHECK_13 = 3006
EFFECT_TYPE_CHECK_10_10 = 3007

E_ABILITY_NONE = 0
E_ABILITY_HARDEN = 1
E_ABILITY_BLINDING_SHIMMER = 2
E_ABILITY_FIREBALL = 4
E_ABILITY_DETONATE = 5
E_ABILITY_CHARGE = 6
E_ABILITY_PRAYER = 7
E_ABILITY_LIFESTEAL = 8
E_ABILITY_MANIC_BURST = 9
E_ABILITY_EAT_BANANA = 10
E_ABILITY_SHIFTING_GROUND = 11
E_ABILITY_RAISE_THE_DEAD = 12
E_ABILITY_SACRIFICE = 13
E_ABILITY_ROYAL_SMASH = 14




