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
            # Рамка вокруг кирпича
            pygame.draw.rect(screen, WHITE, (self.x, self.y, self.width, self.height), 2)

    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)


class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Arkanoid")
        self.clock = pygame.time.Clock()

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
                    # Увеличиваем скорость мяча с каждым уровнем
                    self.ball.dx *= 1.1
                    self.ball.dy *= 1.1

    def draw_text(self, text, x, y, color=WHITE):
        # Простая функция для рисования текста без использования шрифтов
        # Вместо текста рисуем простые фигуры или используем системный шрифт
        font = pygame.font.SysFont(None, 36)
        text_surface = font.render(text, True, color)
        self.screen.blit(text_surface, (x, y))

    def draw_ui(self):
        # Рисуем информацию об игре
        self.draw_text(f"Счет: {self.score}", 10, SCREEN_HEIGHT - 30)
        self.draw_text(f"Жизни: {self.lives}", 200, SCREEN_HEIGHT - 30)
        self.draw_text(f"Уровень: {self.level}", 400, SCREEN_HEIGHT - 30)

    def show_message(self, message, color=WHITE):
        # Показываем сообщение в центре экрана
        self.screen.fill(BLACK)
        self.draw_text(message, SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 - 18, color)
        pygame.display.flip()
        pygame.time.wait(2000)

    def run(self):
        running = True
        game_started = False

        while running:
            # Обработка событий
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE and not game_started:
                        game_started = True
                        self.ball.active = True

            # Управление
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                self.paddle.move("left")
            if keys[pygame.K_RIGHT]:
                self.paddle.move("right")

            if game_started:
                # Обновление
                self.ball.move()
                self.handle_collisions()

                # Проверка потери жизни
                if not self.ball.active:
                    self.lives -= 1
                    if self.lives <= 0:
                        self.show_message("ИГРА ОКОНЧЕНА", RED)
                        running = False
                    else:
                        self.ball.reset()
                        game_started = False
                        self.show_message(f"Жизней осталось: {self.lives}")

            # Отрисовка
            self.screen.fill(BLACK)

            # Рисование игровых объектов
            self.paddle.draw(self.screen)
            self.ball.draw(self.screen)
            for brick in self.bricks:
                brick.draw(self.screen)

            # Рисование UI
            self.draw_ui()

            # Сообщение о старте игры
            if not game_started and self.ball.active:
                self.draw_text("Нажмите ПРОБЕЛ для запуска мяча",
                               SCREEN_WIDTH // 2 - 180, SCREEN_HEIGHT // 2)

            pygame.display.flip()
            self.clock.tick(FPS)

        pygame.quit()
        sys.exit()


# Запуск игры
if __name__ == "__main__":
    game = Game()
    game.run()