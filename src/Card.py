import pygame, random
from src.Dependencies import *
from src.constants import *

class Card():
    def __init__(self, card_id, name, description):
        self.card_id = card_id
        self.name = name
        self.description = description
    
    def get_name(self):
        return self.name
        


class ItemCard(Card):

    def __init__(self, card_id, name, description, effect_id, action_cost, turn_cost):
        super().__init__(card_id, name, description)

        self.effect_id = effect_id
        self.action_cost = action_cost
        self.turn_cost = turn_cost



class AbilityCard(Card):
    def __init__(self, card_id, name, description, effect_id, action_cost, turn_cost):
        super().__init__(card_id, name, description)

        self.effect_id = effect_id
        self.action_cost = action_cost
        self.turn_cost = turn_cost



class EventCard(Card):
    def __init__(self, card_id, name, description, effect_id):
        super().__init__(card_id, name, description)
        self.effect_id = effect_id



class EnemyCard(Card):
    def __init__(self, card_id, name, description, max_health, attack_dice, attack_bonus, e_ability_id):
        super().__init__(card_id, name, description)
        self.max_health = max_health
        self.attack_dice = attack_dice
        self.attack_bonus = attack_bonus
        self.e_ability_id = e_ability_id