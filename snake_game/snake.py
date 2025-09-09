## Clase Snake

import pygame
from config import BLOCK_SIZE, GREEN

class Snake:
    def __init__(self):
        self.body = [(100, 100), (80, 100), (60, 100)]  # posiciones iniciales
        self.direction = (BLOCK_SIZE, 0)  # movimiento inicial hacia la derecha

    def move(self):
        head_x, head_y = self.body[0]
        dir_x, dir_y = self.direction
        new_head = (head_x + dir_x, head_y + dir_y)
        self.body = [new_head] + self.body[:-1]  # mueve la serpiente

    def grow(self):
        self.body.append(self.body[-1])  # duplica el último segmento de la serpiente

    def change_direction(self, new_direction):
        self.direction = new_direction

    def draw(self, screen):
        for segment in self.body:
            pygame.draw.rect(screen, GREEN, (*segment, BLOCK_SIZE, BLOCK_SIZE))