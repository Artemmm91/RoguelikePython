from objects.thing import Thing
from resources.resources import data


class Weapon(Thing):
    """ CLass of the weapon """
    def __init__(self, frames):
        super(Weapon, self).__init__(frames)
        self.range = {}
        self.damage = 0


class Knife(Weapon):
    """ Basic weapon, player start game with it """
    def __init__(self):
        super(Knife, self).__init__(None)
        self.range = {  # range of attack
            (1, 0): ((1, 0),),
            (-1, 0): ((-1, 0),),
            (0, -1): ((0, -1),),
            (0, 1): ((0, 1),)
        }
        self.damage = 5
