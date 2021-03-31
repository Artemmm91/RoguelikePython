SCREEN_SIZE = (WIDTH, HEIGHT) = (1280, 720)
FULLSCREEN_DEFAULT = False

hero_hp = 100
monster_hp = 10

cell_size = 56

frame_tick = 16
frame_wait = 16
animation_frames = 8
# for good animation needs to divide cell_size

fade_frames = 32
shake_screen_frames = 3
shake_range = 8

colors = {
    "BLACK": (0, 0, 0),
    "GREEN": (0, 255, 0)
}

quit_flag = "QUIT"
keydown_flag = "KEYDOWN"

escape_key = "ESCAPE"
down_key = "DOWN"
up_key = "UP"
left_key = "LEFT"
right_key = "RIGHT"
a_key = "A",
s_key = "S",
d_key = "D",
w_key = "W",

move_keys = {
    down_key: (0, 1),
    up_key: (0, -1),
    left_key: (-1, 0),
    right_key: (1, 0)
}

attack_keys = {
    s_key: (0, 1),
    w_key: (0, -1),
    a_key: (-1, 0),
    d_key: (1, 0),
}

map_symbols = {
    9: "empty",
    0: "floor",
    1: "wall",
    2: "hero",
    3: "monster",
    4: "exit",
}

empty = ["floor", "monster", "hero", "exit"]
