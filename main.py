import pygame
import numpy
from button import Button

cell_size = 10
button_size = 50
grid_x = 70
grid_y = 70
control_panel_y = 50
screen_width = grid_x * cell_size
screen_height = grid_y * cell_size + control_panel_y

color_alive = (0, 100, 10)
color_dead = (20, 20, 20)
color_grid = (30, 30, 30)
color_button = (255, 255, 255)

pygame.init()
screen = pygame.display.set_mode(
    (screen_width, screen_height))
screen.fill(color_grid)

icon_refresh = pygame.image.load('assets/refresh_icon.svg').convert_alpha()
icon_play = pygame.image.load('assets/play_icon.svg').convert_alpha()
icon_pause = pygame.image.load('assets/pause_icon.svg').convert_alpha()
icon_next = pygame.image.load('assets/next_icon.svg').convert_alpha()
button_center = screen_width / 2 - button_size / 2
buttonRefresh = Button(button_center - button_size - 20, 0, button_size, (color_button, color_grid, color_dead),
                       icon_refresh)
buttonPlayPause = Button(button_center, 0, button_size, (color_button, color_grid, color_dead),
                         icon_play, icon_pause)
buttonNext = Button(button_center + button_size + 20, 0, button_size, (color_button, color_grid, color_dead),
                    icon_next)
Button.draw(buttonRefresh, screen)
Button.draw(buttonPlayPause, screen)
Button.draw(buttonNext, screen)


def init_grid():
    grid = numpy.zeros((grid_y, grid_x))
    start_pattern = numpy.array([[1, 0, 0],
                                 [1, 1, 1],
                                 [0, 1, 0]]).transpose()
    pos = (30, 30)
    grid[pos[0]:pos[0]+start_pattern.shape[0], pos[1]:pos[1]+start_pattern.shape[1]] = start_pattern
    pos = (10, 10)
    grid[pos[0]:pos[0]+start_pattern.shape[0], pos[1]:pos[1]+start_pattern.shape[1]] = start_pattern
    return grid

def draw_cells(surface):
    for x, y in numpy.ndindex(grid.shape):
        color = color_alive if grid[x, y] == 1 else color_dead
        pygame.draw.rect(surface, color, (x*cell_size, y *
                         cell_size+control_panel_y, cell_size-1, cell_size-1))


def update(grid):
    new_grid = numpy.zeros((grid.shape[0], grid.shape[1]))

    for x, y in numpy.ndindex(grid.shape):
        neighborhood = numpy.sum(grid[x-1:x+2, y-1:y+2]) - grid[x, y]

        if (grid[x, y] == 1 and 2 <= neighborhood <= 3) or (grid[x, y] == 0 and neighborhood == 3):
            new_grid[x, y] = 1
    return new_grid


grid = init_grid()
draw_cells(screen)

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
                buttonPlayPause.switch(screen, updating)
                buttonRefresh.disableEnable(screen, updating)
                buttonNext.disableEnable(screen, updating)
            if buttonRefresh.collide(mouse) and not updating:
                grid = init_grid()
                draw_cells(screen)
            if buttonNext.collide(mouse) and not updating:
                grid = update(grid)
                draw_cells(screen)

    if updating:
        grid = update(grid)
        draw_cells(screen)

    pygame.display.update()

pygame.quit()
