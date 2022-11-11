from typing import Tuple
import pygame


class Button:

    def __init__(self, x, y, colors: Tuple[Tuple[int,int,int]], icon, backup_icon=""):
        self.x = x
        self.y = y
        self.size = 50
        self.main_color = colors[0]
        self.background_color = colors[1]
        self.hover_color = colors[2]
        self.icon = icon
        self.backup_icon = backup_icon

    def draw(self, surface):
        pygame.draw.rect(surface, self.main_color,
                         (self.x, self.y, self.size, self.size), self.size, 5)
        pygame.draw.rect(surface, self.background_color,
                         (self.x+2, self.y+2, self.size-4, self.size-4), self.size-4, 5)
        surface.blit(self.icon, (self.x, self.y))
        if (self.backup_icon):
            print('Switch')
