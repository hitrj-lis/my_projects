#

import pygame
from random import randint

pygame.init()

#==================== variable ======================#

screen_x = 800
screen_y = 800
background_color = (0, 0, 0)

window = pygame.display.set_mode((screen_x, screen_y))

#===================== arrays =======================#

grid = []
sector_types = [
                    {'name': 'water', 'color': (0, 0, 255)},
                    {'name': 'soil', 'color': (0, 255, 0)},
                    {'name': 'wilderness', 'color': (255, 250, 0)},
                    {'name': 'mountain', 'color': (150, 127, 150)},
                    {'name': 'hill', 'color': (127, 200, 0)},
                ]

natural_resources = [
                        {'name': 'oil', 'color': (0, 0, 0)},
                        {'name': ''}
                    ]


coordinates_sector = {'x': 50,
                      'y': 50}
coordinates_quarter = {'x': 100,
                       'y': 100}

#===================== Classes ======================#

class Cursor():
    """ Create cursor class """

    def __init__(self, coordinates):
        """ Initiation cursor class """
        self.color = (255, 0, 0,)
        self.widht_and_height = 50
        self.coordinates = coordinates
        self.x = self.coordinates['x']
        self.y = self.coordinates['y']

    def draw(self):
        """ Draw cursor """
        pygame.draw.rect(window, self.color, (self.x, self.y, self.widht_and_height, self.widht_and_height))

    def move_right(self):
        """"""
        if self.x == screen_x - 50:
            self.x = screen_x - 50
        else:
            pygame.draw.rect(window, self.color, (self.x + 50, self.y, self.widht_and_height, self.widht_and_height))

    def move_left(self):
        """"""
        if self.x == 0:
            self.x = 0
        else:
            pygame.draw.rect(window, self.color, (self.x - 50, self.y, self.widht_and_height, self.widht_and_height))

    def move_up(self):
        """"""
        if self.y == screen_y - 50:
            self.y = screen_y - 50
        else:
            pygame.draw.rect(window, self.color, (self.x, self.y, self.widht_and_height, self.widht_and_height))


class Sector():
    """ Create Sector class """

    def __init__(self, sector_type, coordinates):
        """ Initiation Sector class """
        self.sector_type = sector_type
        self.coordinates = coordinates
        self.color = sector_type['color']
        self.name_type = sector_type['name']
        self.widht_and_height = 50
        self.x = self.coordinates['x']
        self.y = self.coordinates['y']

    def draw(self):
        """ Draw sector """
        pygame.draw.rect(window, self.color, (self.x, self.y, self.widht_and_height, self.widht_and_height))

    def type(self):
        """  Show type """
        return self.name_type

    def show(self):
        """ Show all parameters """
        print('name =', self.name_type, ',', 'color =', self.color, ',', 'coordinates =', self.coordinates)

class Quarter():
    """ Create Quarter class """

    def __init__(self, coordinates):
        """ Initiation Quarter class """
        self.coordinates = coordinates
        self.quarter = []

    def draw(self):
        """ Draw quarter """

#==================== functions ======================#


def random_grid():
    """ Create random playing territory """
    for y in range(int(screen_y / 50) + 1):
        line = []
        for x in range(int(screen_x / 50) + 1):
            sector = Sector(sector_type=sector_types[randint(0, 4)], coordinates={'x': x * 50, 'y': y * 50})
            line.append(sector)
        grid.append(line)

def draw_grid():
    """ Draw grid """
    for line in grid:
        for cell in line:
            cell.draw()
