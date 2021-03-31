from graphics.interface import InterfacePyGame
from resources.resources import data
from setting_files.utils import distance


class Thing(InterfacePyGame.Sprite):
    """ Class of the objects """
    def __init__(self, frames):
        super(Thing, self).__init__(frames)
        self.coord = None

    def set_coord(self, coord):
        """ Set coordinates of thing """
        self.coord = [coord[0], coord[1]]


class Exit(Thing):
    """ Exit portal to next level """
    def __init__(self):
        super(Exit, self).__init__(data.door["close"])
        self.all_frames = data.door
        self.priority = 200

    def change_frames(self, animation_type):
        """ Change frame set """
        self.frames = self.all_frames[animation_type]

    def react(self, level):
        """ It is changing when player is nearby """
        state = "close"
        if distance(level.hero.coord, self.coord, 1) < 2.1:
            state = "open"
        self.change_frames(state)
