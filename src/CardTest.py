import pygame, random, sys, os
from src.constants import *
from src.Dependencies import *

pygame.init()

screen_width, screen_height = 1280, 900
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Card Test")

sprite_manager = SpriteManager()
sprite_collection = sprite_manager.spriteCollection

class Player:
    def __init__(self, name, hp, action_points, turn):
        self.name = name
        self.hp = hp
        self.action_points = action_points
        self.turn = turn
        self.ability_deck = []
        self.item_deck = []
        self.drawn_item = []

    def display_status(self):
        print(f"{self.name}'s Status - HP: {self.hp}, Action Points: {self.action_points}, Turn: {self.turn}")

    def display_ability_deck(self):
        print("\nPlayer's Ability Deck:")
        for ability_card in self.ability_deck:
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

    def render(self, frame_image, item_image, position):
        final_surface = pygame.Surface((frame_image.get_width(), frame_image.get_height())) #Create a surface (rectangle) same size as the frame_image (Just to combine the item and the frame as one)
        final_surface.blit(frame_image, (0, 0))  #put frame on to the surface at pos (0,0)

        item_x = max(0, (frame_image.get_width() - item_image.get_width()) // 2) #pos of item on surface
        item_y = max(0, (frame_image.get_height() - item_image.get_height()) //6)

        final_surface.blit(item_image,(item_x, item_y)) #put item on to the surface

        return final_surface
    
class Card:

    def __init__(self, card_id, name, description):
        self.card_id = card_id
        self.name = name
        self.description = description

list_of_cards = []

class ItemCard(Card):

    def __init__(self, card_id, name, description, effect_id, action_cost, turn_cost):
        super().__init__(card_id, name, description)

        self.effect_id = effect_id
        self.action_cost = action_cost
        self.turn_cost = turn_cost

item_deck = [ItemCard(**item) for item in item_attributes]


class AbilityCard(Card):
    def __init__(self, card_id, name, description, effect_id, action_cost, turn_cost):
        super().__init__(card_id, name, description)

        self.effect_id = effect_id
        self.action_cost = action_cost
        self.turn_cost = turn_cost

ability_deck = [AbilityCard(**item) for item in ability_attributes]

class EventCard(Card):
    def __init__(self, card_id, name, description, effect_id):
        super().__init__(card_id, name, description)
        self.effect_id = effect_id

event_deck = [EventCard(**item) for item in event_attributes]

class EnemyCard(Card):
    def __init__(self, card_id, name, description, max_health, attack_dice, attack_bonus, e_ability_id):
        super().__init__(card_id, name, description)
        self.max_health = max_health
        self.attack_dice = attack_dice
        self.attack_bonus = attack_bonus
        self.e_ability_id = e_ability_id

enemy_deck = [EnemyCard(**item) for item in enemy_attributes]

list_of_cards = item_deck + ability_deck + event_deck + event_deck

for card in list_of_cards:
    if isinstance(card, ItemCard):
        print(f"Card ID: {card.card_id}, Name: {card.name}, Description: {card.description}, Effect ID: {card.effect_id}, Action Cost: {card.action_cost}, Turn Cost: {card.turn_cost}")
    elif isinstance(card, AbilityCard):
        print(f"Card ID: {card.card_id}, Name: {card.name}, Description: {card.description}, Effect ID: {card.effect_id}, Action Cost: {card.action_cost}, Turn Cost: {card.turn_cost}")
    elif isinstance(card, EnemyCard):
        print(f"Card ID: {card.card_id}, Name: {card.name}, Description: {card.description}, HP: {card.max_health}, ATK: {card.attack_dice} + {card.attack_bonus}, Effect ID: {card.e_ability_id}")
    elif isinstance(card, EventCard):
        print(f"Card ID: {card.card_id}, Name: {card.name}, Description: {card.description}, Effect ID: {card.effect_id}")

floor_deck = enemy_deck + event_deck

random.shuffle(floor_deck) 

print("\nFloor Deck list:")
for card in floor_deck:
    if isinstance(card, EnemyCard):
        print(f"Enemy Card - ID: {card.card_id}, Name: {card.name}, Description: {card.description}, HP: {card.max_health}, ATK: {card.attack_dice} + {card.attack_bonus}, Effect ID: {card.e_ability_id}")
    elif isinstance(card, EventCard):
        print(f"Event Card - ID: {card.card_id}, Name: {card.name}, Description: {card.description}, Effect ID: {card.effect_id}")

player = Player("Player1", 10, 3, 1)

player.draw_items(5)

player.display_status()
player.display_ability_deck()
player.display_item_deck()

print("Card IDs in ability_deck:", [ability_card.card_id for ability_card in ability_deck])
print("Card IDs in item_deck:", [item_card.card_id for item_card in player.item_deck])
print("Length of gItems_image_list:", len(gItems_image_list))


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))

    x_offset = 100 #initial position for the fist line of cards
    y_offset = 200

    for enemy_card in enemy_deck:
        enemy_index = enemy_deck.index(enemy_card) #find the index of the ability card
        item_image = gsEnemies_Image_list[enemy_index] 
        frame_image = gFrames_image_list[2]
        position = (x_offset, y_offset)
        final_card = player.render(frame_image, item_image, position) #put in the frame you want, the item you want to merge and the on-screen pos
        screen.blit(final_card, position)
        x_offset += 100 #render the next card to the right

    x_offset = 100 #reset the position for the second line of cards
    y_offset = 450  

    for item_card in player.item_deck:
        item_index = item_card.card_id 
        item_image = gItems_image_list[item_index-1] #-1 since the item index starts from 1 (line above)
        frame_image = gFrames_image_list[3]
        position = (x_offset, y_offset)
        final_card = player.render(frame_image, item_image, position) 
        screen.blit(final_card, position)
        x_offset += 200

    pygame.display.flip() #update the display after rendering


    #all the attributes are in constant.py
    #careful on the subclasses of class card the attributes varies

pygame.quit()