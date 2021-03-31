from setting_files import settings
from setting_files.utils import direct_coord, map_coord
from random import choice


class Behaviour:
    """ Behaviour of monsters """
    priority = 0

    @staticmethod
    def act(mob, level):
        """ Acting correspondingly """
        pass


class Wander(Behaviour):
    """ Behaviour of random movements """
    @staticmethod
    def act(mob, level):
        positions = [d for d in settings.move_keys.values()
                     if level.is_empty(map_coord(direct_coord(mob.coord, d)))]
        positions += [(0, 0)]
        direction = choice(positions)
        mob.move(level, direction)


class Hunt(Behaviour):
    """ Behaviour of aggression """
    priority = 100

    @staticmethod
    def act(mob, level):
        pass
