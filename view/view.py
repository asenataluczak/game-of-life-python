import pygame
from view import Button

cell_size = 10
button_size = 50
control_panel_y = 50

color_alive = (0, 100, 10)
color_dead = (20, 20, 20)
color_grid = (30, 30, 30)
color_button = (255, 255, 255)


class View:

    def __init__(self, cells_amount_x, cells_amount_y):
        self.cells_amount_x = cells_amount_x
        self.cells_amount_y = cells_amount_y
        self.screen_width = cells_amount_x * cell_size
        self.screen_height = cells_amount_y * cell_size + control_panel_y
        self.button_center = self.screen_width / 2 - button_size / 2
        pygame.init()
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        self.screen.fill(color_grid)
        self.__load_icons()
        self.__draw_buttons()

    def get_surface(self):
        return self.screen

    def draw_cells(self, grid, grid_iterable):
        for x, y in grid_iterable:
            color = color_alive if grid[x, y] == 1 else color_dead
            pygame.draw.rect(self.screen, color, (x * cell_size, y *
                                                  cell_size + control_panel_y, cell_size - 1, cell_size - 1))

    @staticmethod
    def get_event():
        return pygame.event.get()

    @staticmethod
    def get_event_type(event_type):
        return getattr(pygame, event_type)

    @staticmethod
    def update_screen():
        pygame.display.update()

    @staticmethod
    def get_mouse_position():
        return pygame.mouse.get_pos()

    @staticmethod
    def quit():
        pygame.quit()

    def __load_icons(self):
        self.icon_refresh = pygame.image.load('assets/refresh_icon.svg').convert_alpha()
        self.icon_play = pygame.image.load('assets/play_icon.svg').convert_alpha()
        self.icon_pause = pygame.image.load('assets/pause_icon.svg').convert_alpha()
        self.icon_next = pygame.image.load('assets/next_icon.svg').convert_alpha()

    def __draw_buttons(self):
        self.buttonRefresh = Button(self.button_center - button_size - 20, 0, button_size,
                                    (color_button, color_grid, color_dead),
                                    self.icon_refresh)
        self.buttonPlayPause = Button(self.button_center, 0, button_size, (color_button, color_grid, color_dead),
                                      self.icon_play, self.icon_pause)
        self.buttonNext = Button(self.button_center + button_size + 20, 0, button_size,
                                 (color_button, color_grid, color_dead),
                                 self.icon_next)
        self.buttonRefresh.draw(self.screen)
        self.buttonPlayPause.draw(self.screen)
        self.buttonNext.draw(self.screen)
