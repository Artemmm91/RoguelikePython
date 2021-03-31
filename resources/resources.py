from graphics.interface import InterfacePyGame
from setting_files import settings
from setting_files.file_names import *


def load_atlas(filename, width=16, height=16):
    """ From picture with many images make [[]] of images """
    image = InterfacePyGame().load_image(filename)
    image_width, image_height = image.get_size()
    return [
        [
            (image.subsurface((x * width, y * height, width, height))).scale(
                (settings.cell_size, settings.cell_size)
            )
            for x in range(image_width // width)
        ]
        for y in range(image_height // height)
    ]


def make_list_frames(frames, repeat):
    """ making frame list with repeat """
    new_frames = []
    for frame in frames:
        new_frames.extend([frame] * repeat)

    return new_frames


class Resources(object):
    """ CLass of atlas images """
    def __init__(self):
        self.wall_tiles = load_atlas(wall_file)
        self.floor_tiles = load_atlas(floor_file)
        self.player = [load_atlas(file) for file in player_files]
        self.monsters = [load_atlas(file) for file in monster_files]
        self.doors = [load_atlas(file) for file in door_files]
        self.swipe = load_atlas(swipe_file)

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Resources, cls).__new__(cls)
        return cls.instance


class Design(object):
    """ CLass with certain design of images """
    def __init__(self, wall_set, floor_set, player_set, monster_set, door_set):
        x, y = floor_set
        resources = Resources()
        self.floors = {
            "corner1": resources.floor_tiles[x][y],          # corner |'
            "corner2": resources.floor_tiles[x][y + 2],      # corner '|
            "corner3": resources.floor_tiles[x + 2][y + 2],  # corner _|
            "corner4": resources.floor_tiles[x + 2][y],      # corner |_
            "full": resources.floor_tiles[x + 1][y + 1],     # full cell
            "edge1": resources.floor_tiles[x + 1][y],        # |...
            "edge2": resources.floor_tiles[x][y + 1],        # '''
            "edge3": resources.floor_tiles[x + 1][y + 2],    # ...|
            "edge4": resources.floor_tiles[x + 2][y + 1],    # ___
            "hall1": resources.floor_tiles[x + 1][y + 5],    # up and down walls
            "hall2": resources.floor_tiles[x + 1][y + 3],    # left and right walls
            "end1": resources.floor_tiles[x + 1][y + 4],     # no wall ...|
            "end2": resources.floor_tiles[x][y + 3],         # no wall ___
            "end3": resources.floor_tiles[x + 1][y + 6],     # no wall |...
            "end4": resources.floor_tiles[x + 2][y + 3],     # no wall '''
            "zero": resources.floor_tiles[x][y + 5]          # only walls
        }

        x, y = wall_set
        self.walls = {
            "corner1": resources.wall_tiles[x][y],          # corner |'
            "corner2": resources.wall_tiles[x][y + 2],      # corner '|
            "corner3": resources.wall_tiles[x + 2][y + 2],  # corner _|
            "corner4": resources.wall_tiles[x + 2][y],      # corner |_
            "full": resources.wall_tiles[x + 1][y + 1],     # full cell
            "edge1": resources.wall_tiles[x + 1][y],        # |
            "edge3": resources.wall_tiles[x][y + 1],        # ___
        }

        self.player = {}
        x, y = player_set
        direction_images = {
            0: (x, y),
            2: (x, 7 - y)
        }
        direction_keys = {
            0: settings.left_key,
            2: settings.right_key
        }
        for direction in direction_images:
            x, y = direction_images[direction]
            hero_frames = [resources.player[direction][x][y], resources.player[direction + 1][x][y]]
            hero_still = make_list_frames(hero_frames, settings.frame_tick)
            self.player[direction_keys[direction]] = {
                "still": hero_still,
                "walk": hero_still,
            }

        self.monsters = {}
        for monster_type in monster_set:
            self.monsters[monster_type] = []
            for design in monster_set[monster_type]:
                x, y = design
                monster_frames = [resources.monsters[0][x][y], resources.monsters[1][x][y]]
                monsters_still = make_list_frames(monster_frames, settings.frame_tick)
                self.monsters[monster_type].append({
                    "still": monsters_still,
                    "walk": monsters_still,
                })

        x, y = door_set
        door_open_frames = [resources.doors[0][x][y], resources.doors[1][x][y]]
        door_close_frames = [resources.doors[0][x][y + 1], resources.doors[1][x][y + 1]]
        self.door = {
            "open": make_list_frames(door_open_frames, settings.frame_tick),
            "close": make_list_frames(door_close_frames, settings.frame_tick),
        }

        self.swipe = {
            (1, 0): [frame for frame in resources.swipe[0]],
            (0, 1): [frame for frame in resources.swipe[1]],
            (-1, 0): [frame for frame in resources.swipe[2]],
            (0, -1): [frame for frame in resources.swipe[3]],
        }

    def __new__(cls, wall_set, floor_set, player_set, monster_set, door_set):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Design, cls).__new__(cls)
        return cls.instance


monster_design = {
    "demon": ((3, 2), (1, 3), (1, 2), (1, 0))
}

data = Design(wall_set=(9, 0), floor_set=(9, 0),
              player_set=(3, 3), monster_set=monster_design, door_set=(5, 1))
