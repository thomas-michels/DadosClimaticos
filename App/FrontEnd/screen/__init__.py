
import pygame


class Screen:

    _size = width, height = 640, 480
    _pygame = pygame
    _clock = _pygame.time.Clock()

    def __init__(self):
        self._pygame.init()

    def create_screen(self):
        self._screen = self._pygame.display.set_mode(self._size)

    def update_screen(self):
        self._pygame.display.update()

    def handle_events(self):
        for event in self._pygame.event.get():
            if event.type == self._pygame.QUIT:
                quit()

    def add_graphic_elements(self):
        pass

    def graphic_elements(self):
        pass

    def init_screen(self):
        self.create_screen()

        while True:
            self._clock.tick(60)
            self.graphic_elements()
            self.handle_events()
            self.update_screen()
