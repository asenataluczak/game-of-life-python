import pygame
import numpy

cell_size = 10
grid_x = 70
grid_y = 70

pygame.init()
screen = pygame.display.set_mode((grid_x * cell_size, grid_y * cell_size))

grid = numpy.zeros((grid_y, grid_x))
start_pattern = numpy.array([[1, 0, 0],
                             [1, 1, 1],
                             [0, 1, 0]])
pos = (30, 30)
grid[pos[0]:pos[0]+start_pattern.shape[0], pos[1]:pos[1]+start_pattern.shape[1]] = start_pattern
pos = (10, 10)
grid[pos[0]:pos[0]+start_pattern.shape[0], pos[1]:pos[1]+start_pattern.shape[1]] = start_pattern

screen.fill((30, 30, 30))

def update(surface, grid, cell_size):
    new_grid = numpy.zeros((grid.shape[0], grid.shape[1]))

    for x, y in numpy.ndindex(grid.shape):
        neighborhood = numpy.sum(grid[x-1:x+2, y-1:y+2]) - grid[x, y]

        if (grid[x, y] == 1 and 2 <= neighborhood <= 3) or (grid[x, y] == 0 and neighborhood == 3):
            new_grid[x, y] = 1
            color = (0, 100, 10)

        color = color if grid[x, y] == 1 else (20, 20, 20)
        pygame.draw.rect(surface, color, (y*cell_size, x*cell_size, cell_size-1, cell_size-1))

    return new_grid


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    grid = update(screen, grid, cell_size)
    pygame.display.update()


pygame.quit()
