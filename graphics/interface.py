import pygame
from graphics.abstract_interface import AbstractInterface
from setting_files import settings


class InterfacePyGame(AbstractInterface):
    def __init__(self):
        pygame.init()
        pygame.font.init()
        self.flags = {
            pygame.KEYDOWN: settings.keydown_flag,
            pygame.QUIT: settings.quit_flag,
        }

        self.keys = {
            pygame.K_ESCAPE: settings.escape_key,
            pygame.K_DOWN: settings.down_key,
            pygame.K_UP: settings.up_key,
            pygame.K_LEFT: settings.left_key,
            pygame.K_RIGHT: settings.right_key,
        }

    def get_event(self):
        return pygame.event.get()

    def wait(self, milliseconds):
        pygame.time.wait(milliseconds)

    def get_event_type(self, event):
        if event.type in self.flags:
            return self.flags[event.type]
        return None

    def update(self):
        pygame.display.update()

    def set_screen(self, size, is_full_screen):
        if is_full_screen:
            return pygame.display.set_mode(size, pygame.FULLSCREEN)
        return pygame.display.set_mode(size)

    def get_key(self, event):
        if event.key in self.keys:
            return self.keys[event.key]
        return None

    def get_pressed_keys(self):
        return pygame.key.get_pressed()

    class Sprite(pygame.sprite.Sprite):
        def __init__(self):
            super().__init__()

    class Image:
        def __init__(self, image=None, size=(50, 50)):
            if not image:
                self.image = pygame.Surface(size)
                self.image.fill(settings.BLACK)
            else:
                self.image = image
            self.rect = self.image.get_rect()

        def set_image(self, img):
            self.image = img.image

        def move_rect(self, shift):
            self.rect.move_ip(shift[0], shift[1])

        def set_rect(self, left):
            im_size = self.image.get_size()
            right = (left[0] + im_size[0], left[1] + im_size[1])
            self.rect.update(left, right)

        def subsurface(self, rect):
            return InterfacePyGame.Image(self.image.subsurface(rect))

        def get_size(self):
            return self.image.get_size()

        def scale(self, new_size):
            return InterfacePyGame.Image(pygame.transform.scale(self.image, new_size))

        def merge(self, image):
            self.image.blit(image.image, image.rect)

    def load_image(self, filename):
        return self.Image(pygame.image.load("resources/images/" + filename))


interface = InterfacePyGame()