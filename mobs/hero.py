from setting_files.utils import *
from mobs.mob import Mob
from resources.resources import data
from objects.weapons import Knife
from mobs.behaviour import Hunt


def jump_function(dist):
    """ Calculate height of jump """
    c = settings.cell_size
    return round(dist * (c - dist) * 2 / c)


def get_jump_shift(direction, dist):
    """ Return shift of jump """
    return dist * direction[0], dist * direction[1] - jump_function(dist)


class Hero(Mob):
    """ Class of the Hero """
    def __init__(self):
        super().__init__(data.player[settings.left_key])
        self.hp = settings.hero_hp
        self.direction_image = settings.left_key
        self.camera_shift = (0, 0)
        self.weapon = Knife()

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Hero, cls).__new__(cls)
        return cls.instance

    def act(self, key, level):
        """ Make action according to key """
        if key in settings.move_keys:
            direction = settings.move_keys[key]
            new_coord = direct_coord(self.coord, direction)
            if level.is_empty(map_coord(new_coord)):
                self.move(key, level, new_coord, direction)
                return True
        if key in settings.attack_keys:
            attack_direction = settings.attack_keys[key]
            return self.attack(level, attack_direction)
        return False

    def attack(self, level, attack_direction):
        """ Attack sells in direction """
        attack_cells = self.weapon.range[attack_direction]
        attack_cells = [shift_coord(self.coord, direction, settings.cell_size)
                        for direction in attack_cells]
        result = [(attack_direction, cell) for cell in attack_cells]
        for cell in attack_cells:
            if cell in level.mobs:
                attacked_mob = level.mobs[cell]
                attacked_mob.add_behaviour(Hunt)
                attacked_mob.take_damage(self.weapon.damage)
        return result

    def move(self, key, level, new_coord, direction):
        """ Moving in direction """
        level.place_mob(self, new_coord)
        if key in [settings.left_key, settings.right_key]:
            self.direction_image = key
        self.set_animation(self.walk_animation(direction))

    def walk_animation(self, direction):
        """ Animation of walking (jumping) """
        shift_list = make_splitting(settings.cell_size, settings.animation_frames, direction)
        init_image_coord = self.image_coord
        current_distance = 0
        for shift in shift_list:
            self.camera_shift = shift
            yield
            current_distance += abs(shift[0] + shift[1])
            hero_shift = get_jump_shift(direction, current_distance)
            self.move_image(shift_coord(init_image_coord, hero_shift))
            self.change_frames("walk")

    def update(self, display):
        """ Updating image of hero """
        self.all_frames = data.player[self.direction_image]
        super().update(display)
        display.shift_camera(self.camera_shift)
        self.camera_shift = (0, 0)

    def center_camera(self, display):
        """ Centering camera to the hero """
        display_coord = center(display.screen.get_size())
        display.camera = list(shift_coord(self.image_coord, display_coord, -1))
