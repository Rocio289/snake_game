## Clase Game (para la lógica general del juego)

import pygame
from snake import Snake
from fruit import Fruit
from config import SCREEN_WIDTH, SCREEN_HEIGHT, BLACK

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.logo = pygame.image.load("assets/logo.png").convert_alpha()
        self.logo = pygame.transform.scale(self.logo, (140, 140))
        pygame.display.set_caption("Snake Game")
        self.clock = pygame.time.Clock()
        self.FPS = 10
        self.snake = Snake()
        self.fruit = Fruit()
        self.running = True

    def check_collision(self):
        if self.snake.body[0] == self.fruit.position:
            self.snake.grow()
            self.fruit = Fruit()

    def check_game_over(self):
        head = self.snake.body[0]

        x, y = head
        if (
            x < 0 or x >= SCREEN_WIDTH or
            y < 0 or y >= SCREEN_HEIGHT
        ):
            self.running = False

        if head in self.snake.body[1:]:
            self.running = False

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.snake.change_direction((0, -20))
                elif event.key == pygame.K_DOWN:
                    self.snake.change_direction((0, 20))
                elif event.key == pygame.K_LEFT:
                    self.snake.change_direction((-20, 0))
                elif event.key == pygame.K_RIGHT:
                    self.snake.change_direction((20, 0))

    def update(self):
        self.snake.move()
        self.check_collision()
        self.check_game_over()

    def draw(self):
        self.screen.fill(BLACK)
        self.snake.draw(self.screen)
        self.fruit.draw(self.screen)
        pygame.display.update()

    def run(self):
        self.show_start_menu()

        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(self.FPS)

        self.show_game_over()
        pygame.quit()

    def show_game_over(self):
        font = pygame.font.Font("fonts/PressStart2P-Regular.ttf", 30)
        text = font.render("Game Over", True, (222, 137, 224))
        text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))

        self.screen.blit(text, text_rect)
        pygame.display.update()

        pygame.time.delay(2000)

    def show_start_menu(self):
        font = pygame.font.Font("fonts/RussoOne-Regular.ttf", 40)
        small_font = pygame.font.Font("fonts/RussoOne-Regular.ttf", 26)

        title_text = font.render("Snake Game", True, (209, 130, 194))
        instr_text = small_font.render("Presiona ENTER para jugar o ESC para salir", True, (111, 232, 230))

        logo_rect = self.logo.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 120))
        title_rect = title_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 20))
        instr_rect = instr_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 70))

        waiting = True
        clock = pygame.time.Clock()
        while waiting:
            self.screen.fill((0, 0, 0))  

            self.screen.blit(self.logo, logo_rect)
            self.screen.blit(title_text, title_rect)
            self.screen.blit(instr_text, instr_rect)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:  # ENTER
                        waiting = False
                    elif event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        exit()

            clock.tick(60)