from graphics.interface import InterfacePyGame
from setting_files.utils import shift_coord, make_splitting
from setting_files import settings


class Mob(InterfacePyGame.Sprite):
    """ Class Mob - all live creatures"""
    def __init__(self, frames):
        super().__init__(None)
        self.coord = None
        self.animation = None
        self.all_frames = frames
        self.hp = None

    def set_coord(self, coord):
        """ Set coordinates of the Mob """
        self.coord = [coord[0], coord[1]]

    def change_frames(self, animation_type="still"):
        """ Change frame set """
        self.frames = self.all_frames[animation_type]

    def set_animation(self, animation):
        """ Set new animation """
        self.animation = animation

    def walk_animation(self, direction):
        """ Basic walk animation """
        shift_list = make_splitting(settings.cell_size, settings.animation_frames, direction)
        for shift in shift_list:
            yield
            self.move_image(shift_coord(self.image_coord, shift))
            self.change_frames("walk")

    def update(self, display):
        """ Update image to screen """
        if self.animation:
            try:
                next(self.animation)
            except StopIteration:
                self.set_animation(None)
        else:
            self.change_frames()
        super().update(None)

    def take_damage(self, damage):
        """ Take damage """
        self.hp -= damage

    def is_alive(self):
        """ Checks if mob is alive """
        return self.hp > 0
