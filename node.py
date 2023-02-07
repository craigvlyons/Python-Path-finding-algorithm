import pygame
from colors import Colors as color


class Node:
    def __init__(self, row, col, width, total_rows):
        self.row = row
        self.col = col
        self.x = row * width
        self.y = col * width
        self.color = color.WHITE
        self.neighbors = []
        self.width = width
        self.total_rows = total_rows

    def get_pos(self):
        return self.row, self.col

    def is_closed(self):
        return self.color == color.RED

    def is_open(self):
        return self.color == color.GREEN

    def is_barrier(self):
        return self.color == color.BLACK

    def is_start(self):
        return self.color == color.ORANGE

    def is_end(self):
        return self.color == color.TURQUOISE

    def reset(self):
        self.color = color.WHITE

    def make_closed(self):
        self.color = color.RED

    def make_open(self):
        self.color = color.GREEN

    def make_barrier(self):
        self.color = color.BLACK

    def make_start(self):
        self.color = color.ORANGE

    def make_end(self):
        self.color = color.TURQUOISE

    def make_path(self):
        self.color = color.PURPLE

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.width))

    # list of all possible neighbors
    def update_neighbors(self, grid):
        self.neighbors = []
        if self.row < self.total_rows - 1 and not grid[self.row + 1][self.col].is_barrier():  # Down
            self.neighbors.append(grid[self.row + 1][self.col])

        if self.row > 0 and not grid[self.row - 1][self.col].is_barrier():  # up
            self.neighbors.append(grid[self.row - 1][self.col])

        if self.col < self.total_rows - 1 and not grid[self.row][self.col + 1].is_barrier():  # RIGHT
            self.neighbors.append(grid[self.row][self.col + 1])

        if self.col > 0 and not grid[self.row][self.col - 1].is_barrier():  # LEFT
            self.neighbors.append(grid[self.row][self.col - 1])

    def __lt__(self, other):
        return False
