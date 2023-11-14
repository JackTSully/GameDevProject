import pygame, random, sys, os
from constants import *
from Dependencies import *
from Enemies import *
from Player import *


def apply_effect(self, effect):
        if effect["effect_id"] == EFFECT_TYPE_HEAL:
             player.heal_self(5)
        elif effect["effect_id"] == EFFECT_TYPE_DECREASE_ATK:
             pass
        elif effect["effect_id"] == EFFECT_TYPE_DISABLE_SKILL:
             pass
        elif effect["effect_id"] == EFFECT_TYPE_INVULNERABLE:
             pass
        elif effect["effect_id"] == EFFECT_TYPE_INCREASE_AP:
             pass
        elif effect["effect_id"] == EFFECT_TYPE_INCREASE_ATK:
             pass
        elif effect["effect_id"] == EFFECT_TYPE_DUPLICATE_CARDS:
             pass
        elif effect["effect_id"] == EFFECT_TYPE_ADDITIONAL_ROLL:
             pass