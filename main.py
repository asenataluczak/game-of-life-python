import pygame
import numpy

cell_size = 10
grid_x = 70
grid_y = 70
control_panel_y = 50

color_alive = (0, 100, 10)
color_dead = (20, 20, 20)
color_grid = (30, 30, 30)

pygame.init()
screen = pygame.display.set_mode((grid_x * cell_size, grid_y * cell_size + control_panel_y))
screen.fill(color_grid)

buttonStart = pygame.draw.rect(screen, (100,255,0),(grid_y*cell_size/2-control_panel_y/2,0,50, 50))
buttonRefresh = pygame.draw.rect(screen, (10,10,255),(200,0,50, 50))
buttonNext = pygame.draw.rect(screen, (150,150,0),(600,0,50, 50))

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
        pygame.draw.rect(surface, color, (x*cell_size, y*cell_size+control_panel_y, cell_size-1, cell_size-1))

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
            if grid_y*cell_size/2-control_panel_y/2 <= mouse[0] <= grid_y*cell_size/2-control_panel_y/2+50 and 0 <= mouse[1] <= 50:
                updating = not updating
            if 200 <= mouse[0] <= 250 and 0 <= mouse[1] <= 50:
                grid = init_grid()
                grid = update(screen, grid, cell_size)
            if 600 <= mouse[0] <= 650 and 0 <= mouse[1] <= 50:
                grid = update(screen, grid, cell_size)

    if updating:
        grid = update(screen, grid, cell_size)
    
    pygame.display.update()

pygame.quit()
