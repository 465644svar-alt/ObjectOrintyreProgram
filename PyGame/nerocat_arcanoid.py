# Нейрокот, [25.11.2025 23:55]
# Конечно! Ниже представлен пример простого варианта игры Арканоид на языке Python с использованием библиотеки Pygame и классов.
# Эта версия включает основные элементы: ракетку, мяч и блоки. Вы можете расширять и модифицировать её по желанию.

import pygame
import sys
import random

# Инициализация Pygame
pygame.init()

# Размеры окна
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Арканоид")

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
COLORS = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 165, 0)]

# Скорость мячика
BALL_SPEED = 5

# Класс ракетки
class Paddle:
    def __init__(self):
        self.width = 100
        self.height = 20
        self.x = (WIDTH - self.width) // 2
        self.y = HEIGHT - self.height - 10
        self.speed = 10
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def move(self, direction):
        if direction == 'left':
            self.x -= self.speed
        elif direction == 'right':
            self.x += self.speed
        # Ограничение по границам
        self.x = max(0, min(self.x, WIDTH - self.width))
        self.rect.x = self.x

    def draw(self, surface):
        pygame.draw.rect(surface, WHITE, self.rect)

# Класс мячика
class Ball:
    def __init__(self):
        self.radius = 10
        self.x = WIDTH // 2
        self.y = HEIGHT // 2
        # Начальные скорости
        self.dx = random.choice([-BALL_SPEED, BALL_SPEED])
        self.dy = -BALL_SPEED
        self.rect = pygame.Rect(self.x - self.radius, self.y - self.radius,
                                self.radius*2, self.radius*2)

    def move(self):
        self.x += self.dx
        self.y += self.dy
        self.rect.x = self.x - self.radius
        self.rect.y = self.y - self.radius

        # Столкновение со стенами
        if self.x - self.radius <= 0 or self.x + self.radius >= WIDTH:
            self.dx *= -1
        if self.y - self.radius <= 0:
            self.dy *= -1

    def draw(self, surface):
        pygame.draw.circle(surface, WHITE, (self.x, self.y), self.radius)

    def reset(self):
        self.x = WIDTH // 2
        self.y = HEIGHT // 2
        self.dx = random.choice([-BALL_SPEED, BALL_SPEED])
        self.dy = -BALL_SPEED

# Класс блока (кирпича)
class Brick:
    def __init__(self, x, y, width, height, color):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.destroyed = False

    def draw(self, surface):
        if not self.destroyed:
            pygame.draw.rect(surface, self.color, self.rect)

# Создаем игровую сцену

ef create_bricks():
    bricks = []
    rows = 5
    cols = 8
    brick_width = WIDTH // cols
    brick_height = 30
    for row in range(rows):
        for col in range(cols):
            x = col * brick_width
            y = row * brick_height + 50
            color = COLORS[row % len(COLORS)]
            brick = Brick(x, y, brick_width - 2, brick_height - 2, color)
            bricks.append(brick)
    return bricks

def main():
    clock = pygame.time.Clock()
    paddle = Paddle()
    ball = Ball()
    bricks = create_bricks()

    running = True
    while running:
        clock.tick(60)  # 60 FPS
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Обработка нажатий клавиш
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            paddle.move('left')
        if keys[pygame.K_RIGHT]:
            paddle.move('right')

        # Перемещение мячика
        ball.move()

        # Проверка столкновения мяча с ракеткой
        if ball.rect.colliderect(paddle.rect):
            ball.dy *= -1
            ball.y = paddle.rect.y - ball.radius

        # Проверка столкновения с кирпичами
        for brick in bricks:
            if not brick.destroyed and ball.rect.colliderect(brick.rect):
                brick.destroyed = True
                ball.dy *= -1
                break

        # Проверка, если мяч упал ниже
        if ball.y - ball.radius > HEIGHT:
            ball.reset()

        # Отрисовка
        screen.fill(BLACK)
        paddle.draw(screen)
        ball.draw(screen)
        for brick in bricks:
            brick.draw(screen)

        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
# ```
#
# **Что делает эта программа:**
#
# - Создает окно 800x600.
# - Имеется ракетка, которая управляется стрелками влево и вправо.
# - Мяч движется и отбивается от ракетки и стен.
# - Есть несколько рядов кирпичей, которые исчезают при попадании по ним мяча.
# - Игра продолжается до закрытия окна.
#
# Вы можете расширять этот код, добавляя уровни, счет, звуки и другие улучшения!