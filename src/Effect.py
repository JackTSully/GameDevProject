import pygame, random, sys, os
from src.constants import *
from src.Dependencies import *
from src.Enemies import *
from src.Player import *


def apply_effect(self, effect):
        if effect["effect_id"] == EFFECT_TYPE_HEAL:
             self.player.heal_self(5)
        elif effect["effect_id"] == EFFECT_TYPE_DECREASE_ATK:
             self.enemies.got_debuff(5)
        elif effect["effect_id"] == EFFECT_TYPE_DISABLE_SKILL:
             self.enemies.disabled_skill()
        elif effect["effect_id"] == EFFECT_TYPE_INVULNERABLE:
             pass
        elif effect["effect_id"] == EFFECT_TYPE_INCREASE_AP:
             self.player.increase_ap(1)
        elif effect["effect_id"] == EFFECT_TYPE_INCREASE_ATK:
             self.player.increase_atk(5)
        elif effect["effect_id"] == EFFECT_TYPE_DUPLICATE_CARDS:
             pass
        elif effect["effect_id"] == EFFECT_TYPE_ADDITIONAL_ROLL:
             pass
        
        elif effect["effect_id"] == EFFECT_TYPE_ATTACK:
             self.enemies.got_debuff(5)
        elif effect["effect_id"] == EFFECT_TYPE_CHARGED:
             self.enemies.disabled_skill()
        elif effect["effect_id"] == EFFECT_TYPE_COUNTER:
             pass
        elif effect["effect_id"] == EFFECT_TYPE_BLOCK:
             self.enemies.got_debuff(5)
        elif effect["effect_id"] == EFFECT_TYPE_DRAW:
             self.player.increase_atk(5)
        elif effect["effect_id"] == EFFECT_TYPE_EXCHANGE:
             pass
        elif effect["effect_id"] == EFFECT_TYPE_CHECK_10:
             pass
        elif effect["effect_id"] == EFFECT_TYPE_CHECK_13:
             pass
        elif effect["effect_id"] == EFFECT_TYPE_CHECK_10_10:
             pass


        