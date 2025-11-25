import pygame
import sys
import random

# Инициализация Pygame
pygame.init()

# Константы
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
ORANGE = (255, 165, 0)
COLORS = [RED, GREEN, BLUE, YELLOW, ORANGE]


class Paddle:
    def __init__(self):
        self.width = 100
        self.height = 20
        self.x = SCREEN_WIDTH // 2 - self.width // 2
        self.y = SCREEN_HEIGHT - 50
        self.speed = 8
        self.color = WHITE

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))

    def move(self, direction):
        if direction == "left" and self.x > 0:
            self.x -= self.speed
        if direction == "right" and self.x < SCREEN_WIDTH - self.width:
            self.x += self.speed

    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)


class Ball:
    def __init__(self):
        self.radius = 10
        self.x = SCREEN_WIDTH // 2
        self.y = SCREEN_HEIGHT // 2
        self.dx = 5 * random.choice([-1, 1])
        self.dy = -5
        self.color = WHITE
        self.active = True

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)

    def move(self):
        if not self.active:
            return

        self.x += self.dx
        self.y += self.dy

        # Отскок от стен
        if self.x <= self.radius or self.x >= SCREEN_WIDTH - self.radius:
            self.dx *= -1
        if self.y <= self.radius:
            self.dy *= -1

        # Проверка выхода за нижнюю границу
        if self.y >= SCREEN_HEIGHT:
            self.active = False

    def get_rect(self):
        return pygame.Rect(self.x - self.radius, self.y - self.radius,
                           self.radius * 2, self.radius * 2)

    def reset(self):
        self.x = SCREEN_WIDTH // 2
        self.y = SCREEN_HEIGHT // 2
        self.dx = 5 * random.choice([-1, 1])
        self.dy = -5
        self.active = True


class Brick:
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.visible = True

    def draw(self, screen):
        if self.visible:
            pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))

    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)


class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Arkanoid")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 36)

        self.paddle = Paddle()
        self.ball = Ball()
        self.bricks = []
        self.score = 0
        self.lives = 3
        self.level = 1

        self.create_bricks()

    def create_bricks(self):
        self.bricks = []
        brick_width = 70
        brick_height = 30
        margin = 5
        start_x = 50
        start_y = 50

        for row in range(5):
            for col in range(10):
                x = start_x + col * (brick_width + margin)
                y = start_y + row * (brick_height + margin)
                color = COLORS[row % len(COLORS)]
                brick = Brick(x, y, brick_width, brick_height, color)
                self.bricks.append(brick)

    def handle_collisions(self):
        # Столкновение мяча с платформой
        if self.ball.get_rect().colliderect(self.paddle.get_rect()) and self.ball.dy > 0:
            self.ball.dy *= -1
            # Изменение направления в зависимости от места удара
            hit_pos = (self.ball.x - self.paddle.x) / self.paddle.width
            self.ball.dx = 8 * (hit_pos - 0.5)

        # Столкновение мяча с кирпичами
        for brick in self.bricks:
            if brick.visible and self.ball.get_rect().colliderect(brick.get_rect()):
                brick.visible = False
                self.ball.dy *= -1
                self.score += 10

                # Проверка завершения уровня
                if all(not brick.visible for brick in self.bricks):
                    self.level += 1
                    self.create_bricks()
                    self.ball.reset()

    def draw_ui(self):
        score_text = self.font.render(f"Счет: {self.score}", True, WHITE)
        lives_text = self.font.render(f"Жизни: {self.lives}", True, WHITE)
        level_text = self.font.render(f"Уровень: {self.level}", True, WHITE)

        self.screen.blit(score_text, (10, SCREEN_HEIGHT - 30))
        self.screen.blit(lives_text, (200, SCREEN_HEIGHT - 30))
        self.screen.blit(level_text, (400, SCREEN_HEIGHT - 30))

    def run(self):
        running = True

        while running:
            # Обработка событий
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            # Управление
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                self.paddle.move("left")
            if keys[pygame.K_RIGHT]:
                self.paddle.move("right")
            if keys[pygame.K_SPACE] and not self.ball.active:
                self.ball.reset()

            # Обновление
            self.ball.move()
            self.handle_collisions()

            # Проверка потери жизни
            if not self.ball.active:
                self.lives -= 1
                if self.lives <= 0:
                    self.show_game_over()
                    running = False
                else:
                    self.ball.reset()

            # Отрисовка
            self.screen.fill(BLACK)

            # Рисование игровых объектов
            self.paddle.draw(self.screen)
            self.ball.draw(self.screen)
            for brick in self.bricks:
                brick.draw(self.screen)

            # Рисование UI
            self.draw_ui()

            pygame.display.flip()
            self.clock.tick(FPS)

        pygame.quit()
        sys.exit()

    def show_game_over(self):
        self.screen.fill(BLACK)
        game_over_text = self.font.render("ИГРА ОКОНЧЕНА", True, RED)
        score_text = self.font.render(f"Финальный счет: {self.score}", True, WHITE)

        self.screen.blit(game_over_text, (SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 - 50))
        self.screen.blit(score_text, (SCREEN_WIDTH // 2 - 120, SCREEN_HEIGHT // 2))

        pygame.display.flip()
        pygame.time.wait(3000)


# Запуск игры
if __name__ == "__main__":
    game = Game()
    game.run()