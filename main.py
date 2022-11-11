import pygame
import numpy
from button import Button

cell_size = 10
grid_x = 70
grid_y = 70
control_panel_y = 50

color_alive = (0, 100, 10)
color_dead = (20, 20, 20)
color_grid = (30, 30, 30)
color_button = (255, 255, 255)

pygame.init()
screen = pygame.display.set_mode(
    (grid_x * cell_size, grid_y * cell_size + control_panel_y))
screen.fill(color_grid)

icon_refresh = pygame.image.load('assets/refresh_icon.svg').convert_alpha()
icon_play = pygame.image.load('assets/play_icon.svg').convert_alpha()
icon_pause = pygame.image.load('assets/pause_icon.svg').convert_alpha()
icon_next = pygame.image.load('assets/next_icon.svg').convert_alpha()
buttonRefresh = Button(200, 0, (color_button, color_grid, color_dead),
                       icon_refresh)
buttonPlayPause = Button(400, 0, (color_button, color_grid, color_dead),
                         icon_play, icon_pause)
buttonNext = Button(600, 0, (color_button, color_grid, color_dead),
                    icon_next)
Button.draw(buttonRefresh, screen)
Button.draw(buttonPlayPause, screen)
Button.draw(buttonNext, screen)


def init_grid():
    grid = numpy.zeros((grid_y, grid_x))
    start_pattern = numpy.array([[1, 0, 0],
                                 [1, 1, 1],
                                 [0, 1, 0]])
    pos = (30, 30)
    grid[pos[0]:pos[0]+start_pattern.shape[0], pos[1]:pos[1]+start_pattern.shape[1]] = start_pattern
    pos = (10, 10)
    grid[pos[0]:pos[0]+start_pattern.shape[0], pos[1]:pos[1]+start_pattern.shape[1]] = start_pattern
    return grid


def update(surface, grid, cell_size):
    new_grid = numpy.zeros((grid.shape[0], grid.shape[1]))

    for x, y in numpy.ndindex(grid.shape):
        neighborhood = numpy.sum(grid[x-1:x+2, y-1:y+2]) - grid[x, y]

        if (grid[x, y] == 1 and 2 <= neighborhood <= 3) or (grid[x, y] == 0 and neighborhood == 3):
            new_grid[x, y] = 1
            color = color_alive

        color = color if grid[x, y] == 1 else color_dead
        pygame.draw.rect(surface, color, (x*cell_size, y *
                         cell_size+control_panel_y, cell_size-1, cell_size-1))

    return new_grid


grid = init_grid()
grid = update(screen, grid, cell_size)

updating = False
running = True
while running:
    mouse = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if buttonPlayPause.collide(mouse):
                updating = not updating
            if buttonRefresh.collide(mouse):
                grid = init_grid()
                grid = update(screen, grid, cell_size)
            if buttonNext.collide(mouse):
                grid = update(screen, grid, cell_size)

    if updating:
        grid = update(screen, grid, cell_size)

    pygame.display.update()

pygame.quit()
