from setting_files import settings


def shift_coord(coord, shift, coefficient=1):
    return coord[0] + coefficient * shift[0], coord[1] + coefficient * shift[1]


def direct_coord(coord, direction):
    return shift_coord(coord, direction, settings.cell_size)


def map_coord(coord):
    return coord[0] // settings.cell_size, coord[1] // settings.cell_size


def cartesian_coord(map_coordinates, is_reverse=False):
    if is_reverse:
        return map_coordinates[1] * settings.cell_size, map_coordinates[0] * settings.cell_size
    return map_coordinates[0] * settings.cell_size, map_coordinates[1] * settings.cell_size


def center(window_size):
    center_screen = (window_size[0] // 2, window_size[1] // 2)
    half_side = settings.cell_size // 2
    return center_screen[0] - half_side, center_screen[1] - half_side


def make_splitting(length, number, k):
    required_list = [length // number] * (number - 1) + [length // number + length % number]
    return [(k[0] * element, k[1] * element) for element in required_list]


def distance(coord1, coord2, p=2):
    return ((abs(coord1[0] - coord2[0])**p + abs(coord1[1] - coord2[1]) ** p) ** (1 / p)) / settings.cell_size
