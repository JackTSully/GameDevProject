import random

class Player:
    def __init__(self, name, hp, action_points, turn):
        self.name = name
        self.hp = hp
        self.action_points = action_points
        self.turn = turn
        self.ability_deck = []
        self.item_deck = []

    def display_status(self):
        print(f"{self.name}'s Status - HP: {self.hp}, Action Points: {self.action_points}, Turn: {self.turn}")

    def display_ability_deck(self):
        print("\nPlayer's Ability Deck:")
        for ability_card in ability_deck:
            print(f"Card ID: {ability_card.card_id}, Name: {ability_card.name}, Description: {ability_card.description}")

    def draw_items(self, num_items):
        item_deck_extended = item_deck * 3

        random.shuffle(item_deck_extended)

        drawn_items = item_deck_extended[:num_items]

        self.item_deck.extend(drawn_items)

    def display_item_deck(self):
        print("\nPlayer's Item Deck:")
        for card in self.item_deck:
            print(f"Card ID: {card.card_id}, Name: {card.name}, Description: {card.description}")

class Card:

    def __init__(self, card_id, name, description):
        self.card_id = card_id
        self.name = name
        self.description = description

list_of_cards = []

card1 = Card(1, "test", "test")
card2 = Card(2, "test2", "test2")

list_of_cards.append(card1)
list_of_cards.append(card2)

print(list_of_cards[1].name)

class ItemCard(Card):

    def __init__(self, card_id, name, description, effect_id, action_cost, turn_cost):
        super().__init__(card_id, name, description)

        self.effect_id = effect_id
        self.action_cost = action_cost
        self.turn_cost = turn_cost

item_attributes = [
    {"card_id": 1, "name": "Healing Flask", "description": "+5 HP", "effect_id": 1001, "action_cost": 1, "turn_cost": 0},
    {"card_id": 2, "name": "Potion of Stupidity", "description": "-5 ATK (Selected Enemy)", "effect_id": 1002, "action_cost": 1, "turn_cost": 1},
    {"card_id": 3, "name": "Potion of Relaxation", "description": "Disables enemy's skill (Selected Enemy)", "effect_id": 1003, "action_cost": 1, "turn_cost": 1},
    {"card_id": 4, "name": "Shield", "description": "Invulnerable to the next attack", "effect_id": 1004, "action_cost": 1, "turn_cost": 1},
    {"card_id": 5, "name": "Potion of Swiftness", "description": "+1 AP", "effect_id": 1005, "action_cost": 0, "turn_cost": 1},
    {"card_id": 6, "name": "Potion of Prowess", "description": "+ 5 ATK for the duration of the fight", "effect_id": 1006, "action_cost": 1, "turn_cost": 1},
    {"card_id": 7, "name": "Replicator", "description": "Duplicates selected cards on-hand", "effect_id": 1007, "action_cost": 1, "turn_cost": 1},
    {"card_id": 8, "name": "Double Roll", "description": "Gain an additional roll", "effect_id": 1007, "action_cost": 1, "turn_cost": 0},
]
item_deck = [ItemCard(**item) for item in item_attributes]

for item_card in item_deck:
    print(f"Card ID: {item_card.card_id}, Name: {item_card.name}, Description: {item_card.description}, Effect ID: {item_card.effect_id}, Action Cost: {item_card.action_cost}, Turn Cost: {item_card.turn_cost}")


class AbilityCard(Card):
    def __init__(self, card_id, name, description, effect_id, action_cost, turn_cost):
        super().__init__(card_id, name, description)

        self.effect_id = effect_id
        self.action_cost = action_cost
        self.turn_cost = turn_cost

ability_attributes = [
    {"card_id": 8, "name": "Attack", "description": "Deal DMG (D20) to the selected enemy", "effect_id": 2001, "action_cost": 1, "turn_cost": 1},
    {"card_id": 9, "name": "Charged Attack", "description": "Charge your attack to deal an instance of increased DMG (2D20) next turn", "effect_id": 2002, "action_cost": 2, "turn_cost": 2},
    {"card_id": 10, "name": "Counter Attack", "description": "Blocks 2 DMG recieved and deal DMG (D20) to the attacking enemy for their whole turn.", "effect_id": 2003, "action_cost": 2, "turn_cost": 1},
    {"card_id": 11, "name": "Block", "description": "Blocks 5 DMG from the enemy's attack in their next turn.", "effect_id": 2004, "action_cost": 1, "turn_cost": 1},
]
ability_deck = [AbilityCard(**item) for item in ability_attributes]

for ability_card in ability_deck:
    print(f"Card ID: {ability_card.card_id}, Name: {ability_card.name}, Description: {ability_card.description}, Effect ID: {ability_card.effect_id}, Action Cost: {ability_card.action_cost}, Turn Cost: {ability_card.turn_cost}")

class EventCard(Card):
    def __init__(self, card_id, name, description, effect_id):
        super().__init__(card_id, name, description)
        self.effect_id = effect_id

event_attributes = [
    {"card_id": 12, "name": "Secret Room", "description": "Draw 3 Item Cards", "effect_id": 3001},
    {"card_id": 13, "name": "Fountain of Healing", "description": "Heal to full HP", "effect_id": 3002},
    {"card_id": 14, "name": "Hero's monument", "description": "ATK +3 for the whole floor", "effect_id": 3003},
    {"card_id": 15, "name": "Wounded Adventurer", "description": "Choice: Exchange a Healing Flask for another random item", "effect_id": 3004},
    {"card_id": 16, "name": "Pitfull Trap", "description": "Athletic Check (10) Fail: Take D4 Damage Pass: Get Item Card", "effect_id": 3005},
    {"card_id": 17, "name": "Dart Trap", "description": "Athletic Check (13) Fail: Take D6 Damage Pass: Get Item Card", "effect_id": 3006},
    {"card_id": 18, "name": "Boulder Trap", "description": "Athletic Check (10/10) Fail: Take D8 Damage Pass: Get 2x Item Card", "effect_id": 3007},
]

event_deck = [EventCard(**item) for item in event_attributes]

for event_card in event_deck:
    print(f"Card ID: {event_card.card_id}, Name: {event_card.name}, Description: {event_card.description}, Effect ID: {event_card.effect_id}")


class EnemyCard(Card):
    def __init__(self, card_id, name, description, max_health, attack_dice, attack_bonus, e_ability_id):
        super().__init__(card_id, name, description)
        self.max_health = max_health
        self.attack_dice = attack_dice
        self.attack_bonus = attack_bonus
        self.e_ability_id = e_ability_id


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

enemy_deck = [EnemyCard(**item) for item in enemy_attributes]

for enemies_card in enemy_deck:
    print(f"Card ID: {enemies_card.card_id}, Name: {enemies_card.name}, Description: {enemies_card.description}, HP: {enemies_card.max_health}, ATK: {enemies_card.attack_dice} + {enemies_card.attack_bonus}, Effect ID: {enemies_card.e_ability_id}")


player = Player("Player1", 10, 3, 1)

player.draw_items(3)

player.display_status()
player.display_ability_deck()
player.display_item_deck()

