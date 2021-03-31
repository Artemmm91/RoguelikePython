from abc import ABCMeta, abstractmethod
from time import sleep


class AbstractInterface(metaclass=ABCMeta):
    """ Abstract interface, that says whivch methods needs to be implemented """
    def __new__(cls):
        """ Singleton class, because there is only one interface at one time"""
        if not hasattr(cls, 'instance'):
            cls.instance = super(AbstractInterface, cls).__new__(cls)
        return cls.instance

    @abstractmethod
    def update(self):
        """ Update display """
        pass

    @abstractmethod
    def set_display(self, size, is_full_screen):
        """ Set new display """
        pass

    @abstractmethod
    def load_image(self, filename):
        """ Load image with filename name """
        pass

    @staticmethod
    @abstractmethod
    def blit(screen, image):
        """ Put image onto the screen """
        pass

    def wait(self, milliseconds):
        """ Waiting milliseconds """
        sleep(milliseconds)

    @abstractmethod
    def copy(self, another_image):
        """ Return copy of image """
        pass

    @abstractmethod
    class Event:
        """ Class of Player's events - all his actions """
        @staticmethod
        @abstractmethod
        def get_event():
            """ Get last events """
            pass

        @staticmethod
        @abstractmethod
        def get_event_type(event):
            """ Get type of event """
            pass

        @staticmethod
        @abstractmethod
        def get_pressed_keys():
            """ Gets all keys pressed at the time """
            pass

        @staticmethod
        @abstractmethod
        def get_key(event):
            """ Return key pressed in event """
            pass

    class AbstractSprite(metaclass=ABCMeta):
        """ Class of sprite to render images """
        @abstractmethod
        def __init__(self):
            pass

        @abstractmethod
        def update(self, display):
            """ Updating images """
            pass

        @abstractmethod
        def draw(self, display):
            """ Draw images to display """
            pass

    class GroupSprite:
        """ Bunch of sprites """
        def __init__(self):
            self.list = []

        def add(self, sprite):
            """ Add sprite to group """
            if not isinstance(sprite, AbstractInterface.AbstractSprite):
                raise Exception("Is Not Sprite")
            self.list.append(sprite)
            self.list.sort(key=lambda one_sprite: -one_sprite.priority)

        def draw(self, display):
            """ Draw all the sprites """
            for sprite in self.list:
                sprite.draw(display)

        def update(self, display):
            """ Update all the sprites """
            for sprite in self.list:
                sprite.update(display)

        def clear(self):
            """ Clear group of sprites """
            self.list = []

        def erase(self, sprite):
            """ Delete sprite from group """
            if sprite in self.list:
                self.list.remove(sprite)

    @abstractmethod
    class Image:
        """ Class to work with images """
        @abstractmethod
        def set_image(self, img):
            """ Set new image """
            pass

        @abstractmethod
        def move_rect(self, shift):
            """ Move frame - rectangle - of image """
            pass

        @abstractmethod
        def set_rect(self, left):
            """ Set rectangle with left upper corner """
            pass

        @abstractmethod
        def subsurface(self, rect):
            """ Return subsurface with size of rect """
            pass

        @abstractmethod
        def get_size(self):
            """ Return size of image """
            pass

        @abstractmethod
        def scale(self, new_size):
            """ Return scaled image """
            pass

        @abstractmethod
        def merge(self, image):
            """ Merge image to this image """
            pass
