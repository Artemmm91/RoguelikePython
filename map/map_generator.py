from map.table_map import Map
from setting_files.utils import cartesian_coord
from os.path import join


def read_map(filename):
    """ Read map from file and transform it to Map class """
    field = open(filename, "r")
    table_map = []
    max_length = 0
    hero_pos = None
    monsters_pos = []
    exit_pos = None
    for i, line in enumerate(field):
        new_line = [9]
        max_length = max(max_length, len(line))
        for j, symbol in enumerate(line):
            if symbol == "#":
                new_line.append(1)
            elif symbol == "h":
                new_line.append(2)
                hero_pos = list(cartesian_coord((j + 1, i + 1)))
            elif symbol == "m":
                new_line.append(3)
                monsters_pos.append(cartesian_coord((j + 1, i + 1)))
            elif symbol == " ":
                new_line.append(9)
            elif symbol == "_":
                new_line.append(0)
            elif symbol == "e":
                new_line.append(4)
                exit_pos = list(cartesian_coord((j + 1, i + 1)))
            j += 1
        i += 1
        table_map.append(new_line)

    max_length += 1

    line1 = [9] * (max_length + 1)

    for line in table_map:
        while len(line) < max_length:
            line.append(9)
        line.append(9)

    table_map.insert(0, line1)
    table_map.append(line1)

    return Map(table_map, hero_pos, monsters_pos, exit_pos)


def generate_map(level):
    """ Generate map of dungeon """
    return read_map(join("map", "map_examples", str(level) + ".txt"))
