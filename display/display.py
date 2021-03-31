from setting_files import settings
from resources.resources import data
from setting_files.utils import shift_coord
from random import choice


class Display:
    """ Class representing screen of game """
    def __init__(self, interface):
        self.interface = interface
        self.screen = self.interface.set_display(settings.SCREEN_SIZE, settings.FULLSCREEN_DEFAULT)
        self.camera = [0, 0]
        self.animation = None

    def fullscreen(self):
        """ Become fullscreen """
        pass

    def update(self):
        """ Updating screen """
        self.interface.update()

    def screen_fill(self, color):
        """ Filling screen with color """
        self.screen.fill(color)

    def draw(self, sprite):
        """ Draw sprite to screen """
        self.interface.blit(self.screen, sprite)

    def draw_image(self, image):
        """ Draw image to screen """
        self.interface.blit(self.screen, image)

    def shift_camera(self, shift):
        """ Change coords of camera """
        self.camera[0] += shift[0]
        self.camera[1] += shift[1]

    def fade(self, is_reverse):
        """ Make fade-in or fade-out """
        screen_copy = self.interface.copy(self.screen)
        alpha_range = range(0, 255, 255 // settings.fade_frames)
        if is_reverse:
            alpha_range = reversed(alpha_range)
        fade = self.interface.Image(None, self.screen.get_size())
        for alpha in alpha_range:
            fade.set_alpha(alpha)
            self.draw(screen_copy)
            self.draw(fade)
            self.update()
            self.interface.wait(settings.frame_wait)


def swipe_animation(display, attack_cells):
    """ Animation with weapon swipe """
    swipe_frames = data.swipe
    number_frames = len(swipe_frames[(1, 0)])
    for frame_id in range(number_frames):
        for direction, cell in attack_cells:
            frame = swipe_frames[direction][frame_id]
            frame.set_rect(shift_coord(cell, display.camera, -1))
            display.draw(frame)
        yield


def shake_screen_animation(display):
    """ Animation of shaking screen """
    init_camera = display.camera
    c = settings.shake_range
    for i in range(settings.shake_screen_frames):
        shift = (choice(range(-c, c + 1)), choice(range(-c,  c + 1)))
        display.camera = list(shift_coord(shift, init_camera))
        yield
    display.camera = list(init_camera)


