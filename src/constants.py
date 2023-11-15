import math

WIDTH = 1280
HEIGHT = 720

TILE_SIZE = 48

PLAYER_WALK_SPEED = 180

NUMBER_OF_MONSTER=10

MAP_WIDTH = WIDTH // TILE_SIZE - 2
MAP_HEIGHT = int(math.floor(HEIGHT/TILE_SIZE)) - 2


MAP_RENDER_OFFSET_X = (WIDTH - (MAP_WIDTH * TILE_SIZE)) / 2
MAP_RENDER_OFFSET_Y = (HEIGHT - (MAP_HEIGHT *TILE_SIZE)) / 2

TILE_TOP_LEFT_CORNER = 4
TILE_TOP_RIGHT_CORNER = 5
TILE_BOTTOM_LEFT_CORNER = 23
TILE_BOTTOM_RIGHT_CORNER = 24

TILE_FLOORS = [
    7, 8, 9, 10, 11, 12, 13,
    26, 27, 28, 29, 30, 31, 32,
    45, 46, 47, 48, 49, 50, 51,
    64, 65, 66, 67, 68, 69, 70,
    88, 89, 107, 108
]

TILE_EMPTY = 19

TILE_TOP_WALLS = [58, 59, 60]
TILE_BOTTOM_WALLS = [79, 80, 81]
TILE_LEFT_WALLS = [77, 96, 115]
TILE_RIGHT_WALLS = [78, 97, 116]

item_attributes = [
    {"card_id": 1, "name": "Healing Flask", "description": "+5 HP", "effect_id": 1001, "action_cost": 1, "turn_cost": 0},
    {"card_id": 2, "name": "Potion of Stupidity", "description": "-5 ATK (Selected Enemy)", "effect_id": 1002, "action_cost": 1, "turn_cost": 1},
    {"card_id": 3, "name": "Potion of Relaxation", "description": "Disables enemy's skill (Selected Enemy)", "effect_id": 1003, "action_cost": 1, "turn_cost": 1},
    {"card_id": 5, "name": "Shield", "description": "Invulnerable to the next attack", "effect_id": 1004, "action_cost": 1, "turn_cost": 1},
    {"card_id": 4, "name": "Potion of Swiftness", "description": "+1 AP", "effect_id": 1005, "action_cost": 0, "turn_cost": 1},
    {"card_id": 6, "name": "Potion of Prowess", "description": "+ 5 ATK for the duration of the fight", "effect_id": 1006, "action_cost": 1, "turn_cost": 1},
    {"card_id": 7, "name": "Replicator", "description": "Duplicates selected cards on-hand", "effect_id": 1007, "action_cost": 1, "turn_cost": 1},
    {"card_id": 8, "name": "Double Roll", "description": "Gain an additional roll", "effect_id": 1008, "action_cost": 1, "turn_cost": 0},
]

ability_attributes = [
    {"card_id": 8, "name": "Attack", "description": "Deal DMG (D20) to the selected enemy", "effect_id": 2001, "action_cost": 1, "turn_cost": 1},
    {"card_id": 9, "name": "Charged Attack", "description": "Charge your attack to deal an instance of increased DMG (2D20) next turn", "effect_id": 2002, "action_cost": 2, "turn_cost": 2},
    {"card_id": 10, "name": "Counter Attack", "description": "Blocks 2 DMG recieved and deal DMG (D20) to the attacking enemy for their whole turn.", "effect_id": 2003, "action_cost": 2, "turn_cost": 1},
    {"card_id": 11, "name": "Block", "description": "Blocks 5 DMG from the enemy's attack in their next turn.", "effect_id": 2004, "action_cost": 1, "turn_cost": 1},
]

event_attributes = [
    {"card_id": 12, "name": "Secret Room", "description": "Draw 3 Item Cards", "effect_id": 3001},
    {"card_id": 13, "name": "Fountain of Healing", "description": "Heal to full HP", "effect_id": 3002},
    {"card_id": 14, "name": "Hero's monument", "description": "ATK +3 for the whole floor", "effect_id": 3003},
    {"card_id": 15, "name": "Wounded Adventurer", "description": "Choice: Exchange a Healing Flask for another random item. (Y/N)", "effect_id": 3004},
    {"card_id": 16, "name": "Pitfall Trap", "description": "Athletic Check (10) Fail: Take D4 Damage Pass: Get Item Card", "effect_id": 3005},
    {"card_id": 17, "name": "Dart Trap", "description": "Athletic Check (13) Fail: Take D6 Damage Pass: Get Item Card", "effect_id": 3006},
    {"card_id": 18, "name": "Boulder Trap", "description": "Athletic Check (10/10) Fail: Take D8 Damage Pass: Get 2x Item Card", "effect_id": 3007},
]

enemy_attributes = [
                    {"card_id": 19, "name": "Slime", "description": "A small green creature", "max_health": 40, "attack_dice": 6, "attack_bonus": 0, "e_ability_id": 0},
                    {"card_id": 20, "name": "Stone Golem", "description": "Harden(A): -2 incoming DMG for 1 turn, CD for 2 turns", "max_health": 50, "attack_dice": 6, "attack_bonus": 1, "e_ability_id": 1},
                    {"card_id": 21, "name": "Diamond Golem", "description": "Blinding Shimmer(P): -1 Player AP", "max_health": 60, "attack_dice": 6, "attack_bonus": 0, "e_ability_id": 2},
                    {"card_id": 22, "name": "Skeleton", "description": "Woke from the grave", "max_health": 50, "attack_dice": 6, "attack_bonus": 0, "e_ability_id": 3},
                    {"card_id": 23, "name": "Skeleton Mage", "description": "Fireball(A): D4 DoT for 3 turns, CD for 4 turns", "max_health": 30, "attack_dice": 6, "attack_bonus": 1, "e_ability_id": 4},
                    {"card_id": 24, "name": "Skeleton Juggernuat", "description": "Detonate(P): Explodes for 8 DMG in D4+2 turns", "max_health": 60, "attack_dice": 8, "attack_bonus": 0, "e_ability_id": 5},
                    {"card_id": 25, "name": "Temple Guardian", "description": "Charge(A): Skip 1 turn then attack with 2D6s, CD for 1 turn", "max_health": 50, "attack_dice": 6, "attack_bonus": -1, "e_ability_id": 6},
                    {"card_id": 26, "name": "Fanatic Cultist", "description": "Prayer(P): +1 ATK every turn", "max_health": 45, "attack_dice": 6-1, "attack_bonus": -1, "e_ability_id": 7},
                    {"card_id": 27, "name": "Vampire Bat", "description": "Lifesteal(P): steals 1 HP everytime it attacks", "max_health": 40, "attack_dice": 6, "attack_bonus": 0, "e_ability_id": 8},
                    {"card_id": 28, "name": "Feral Monkey", "description": "Manic Burst(A): +2 ATK for 2 turns, CD for 3 turns", "max_health": 50, "attack_dice": 6, "attack_bonus": 2, "e_ability_id": 9},
                    {"card_id": 29, "name": "King Ape", "description": "Eat Banana(A): +10 HP, CD for 2 turns", "max_health": 70, "attack_dice": 6, "attack_bonus": 4, "e_ability_id": 10},
                    {"card_id": 30, "name": "Underminer", "description": "Shifting Grounds(P): -2 AP every odd numbered turn for the Player","max_health": 65, "attack_dice": 6, "attack_bonus": 1, "e_ability_id": 11},
                    {"card_id": 31, "name": "Necromancer", "description": "Raise the Dead(A): Summon 10HP skeleton with D4 ATK, CD 3 turns", "max_health": 60, "attack_dice": 6, "attack_bonus": 0, "e_ability_id": 12},
                    {"card_id": 32, "name": "Cult Leader", "description": "Sacrifice(P): every attacking turn, roll another D6 “Blood die”, add the value to the ATK and deduct it from their HP", "max_health": 100, "attack_dice": 6, "attack_bonus": 1, "e_ability_id": 13},
                    {"card_id": 33, "name": "Emperor Gorilla", "description": "Royal Smash(A): -2 AP for 2 turns for the Player, CD 4 turns", "max_health": 65, "attack_dice": 12, "attack_bonus": 0, "e_ability_id": 14},
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

