from mobs.mob import Mob
from resources.resources import data
from mobs.behaviour import *


class Monster(Mob):
    """ Monsters - aggressive to Hero Mobs"""
    def __init__(self, frames):
        super().__init__(frames)
        self.hp = settings.monster_hp
        self.behaviours = []
        self.priority = 100

    def move(self, level, direction):
        """ Moving mob in direction """
        level.place_mob(self, direct_coord(self.coord, direction))
        self.set_animation(self.walk_animation(direction))

    def act(self, level):
        """ Act according to behaviours """
        for behaviour in self.behaviours:
            behaviour.act(self, level)

    def add_behaviour(self, behaviour):
        """ Adding new behaviour """
        self.behaviours.append(behaviour)
        self.behaviours.sort(key=lambda b: -b.priority)


class Demon(Monster):
    """ Demon - monster from hell """
    def __init__(self):
        super(Demon, self).__init__(choice(data.monsters["demon"]))
        self.add_behaviour(Wander)
