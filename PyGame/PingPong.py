import pygame
import sys
import random

# Инициализация Pygame
pygame.init()

# Константы игры
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 100, 255)
RED = (255, 50, 50)
GREEN = (50, 255, 100)


class Paddle:
    """Класс для ракетки игрока"""

    def __init__(self, x, y, width, height, color, is_ai=False):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.speed = 7
        self.is_ai = is_ai  # Является ли ракетка компьютерным игроком
        self.score = 0

    def move(self, direction, ball=None):
        """Движение ракетки"""
        if self.is_ai and ball:
            # AI логика: следует за мячом с некоторой случайностью
            if random.random() > 0.1:  # 90% времени следует за мячом
                if ball.rect.centery < self.rect.centery - 10:
                    direction = "up"
                elif ball.rect.centery > self.rect.centery + 10:
                    direction = "down"
                else:
                    direction = None

        if direction == "up" and self.rect.top > 0:
            self.rect.y -= self.speed
        if direction == "down" and self.rect.bottom < SCREEN_HEIGHT:
            self.rect.y += self.speed

    def draw(self, screen):
        """Отрисовка ракетки"""
        pygame.draw.rect(screen, self.color, self.rect)
        # Добавляем небольшой градиент для красоты
        pygame.draw.rect(screen, WHITE, self.rect, 2)

    def reset_position(self):
        """Сброс позиции ракетки"""
        self.rect.y = SCREEN_HEIGHT // 2 - self.rect.height // 2


class Ball:
    """Класс для мяча"""

    def __init__(self, x, y, size):
        self.rect = pygame.Rect(x, y, size, size)
        self.color = WHITE
        self.dx = 5 * random.choice([-1, 1])  # Случайное начальное направление
        self.dy = 5 * random.choice([-1, 1])
        self.speed_increase = 1.05  # Увеличение скорости после отскока
        self.max_speed = 12

    def move(self):
        """Движение мяча"""
        self.rect.x += self.dx
        self.rect.y += self.dy

        # Отскок от верхней и нижней стенок
        if self.rect.top <= 0 or self.rect.bottom >= SCREEN_HEIGHT:
            self.dy *= -1
            # Добавляем звуковой эффект (если бы был)

    def reset(self):
        """Сброс мяча в центр"""
        self.rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        self.dx = 5 * random.choice([-1, 1])
        self.dy = 5 * random.choice([-1, 1])

    def draw(self, screen):
        """Отрисовка мяча"""
        pygame.draw.ellipse(screen, self.color, self.rect)
        # Добавляем свечение
        pygame.draw.ellipse(screen, (200, 200, 255), self.rect, 2)

    def increase_speed(self):
        """Увеличение скорости мяча"""
        if abs(self.dx) < self.max_speed:
            self.dx *= self.speed_increase
        if abs(self.dy) < self.max_speed:
            self.dy *= self.speed_increase


class Game:
    """Основной класс игры"""

    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Pong Game")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 36)
        self.large_font = pygame.font.Font(None, 72)

        # Создание игровых объектов
        paddle_width = 15
        paddle_height = 100
        ball_size = 15

        # Игрок 1 (слева) - управляется игроком
        self.player1 = Paddle(50, SCREEN_HEIGHT // 2 - paddle_height // 2,
                              paddle_width, paddle_height, BLUE)

        # Игрок 2 (справа) - компьютер
        self.player2 = Paddle(SCREEN_WIDTH - 50 - paddle_width,
                              SCREEN_HEIGHT // 2 - paddle_height // 2,
                              paddle_width, paddle_height, RED, is_ai=True)

        # Мяч
        self.ball = Ball(SCREEN_WIDTH // 2 - ball_size // 2,
                         SCREEN_HEIGHT // 2 - ball_size // 2, ball_size)

        self.game_state = "playing"  # playing, paused, game_over

    def handle_collisions(self):
        """Обработка столкновений"""
        # Столкновение с ракетками
        if self.ball.rect.colliderect(self.player1.rect) and self.ball.dx < 0:
            self.ball.dx *= -1
            self.ball.increase_speed()
            # Небольшое изменение угла в зависимости от места удара
            hit_pos = (self.ball.rect.centery - self.player1.rect.centery) / (self.player1.rect.height / 2)
            self.ball.dy = hit_pos * 6

        if self.ball.rect.colliderect(self.player2.rect) and self.ball.dx > 0:
            self.ball.dx *= -1
            self.ball.increase_speed()
            # Небольшое изменение угла в зависимости от места удара
            hit_pos = (self.ball.rect.centery - self.player2.rect.centery) / (self.player2.rect.height / 2)
            self.ball.dy = hit_pos * 6

        # Проверка забития гола
        if self.ball.rect.left <= 0:
            self.player2.score += 1
            self.reset_round()

        if self.ball.rect.right >= SCREEN_WIDTH:
            self.player1.score += 1
            self.reset_round()

    def reset_round(self):
        """Сброс раунда после гола"""
        self.ball.reset()
        self.player1.reset_position()
        self.player2.reset_position()

        # Проверка на победу
        if self.player1.score >= 5 or self.player2.score >= 5:
            self.game_state = "game_over"

    def draw_scoreboard(self):
        """Отрисовка таблицы счета"""
        # Фон для таблицы счета
        score_bg = pygame.Rect(SCREEN_WIDTH // 2 - 100, 10, 200, 50)
        pygame.draw.rect(self.screen, (30, 30, 30), score_bg)
        pygame.draw.rect(self.screen, WHITE, score_bg, 2)

        # Счет игроков
        score_text = f"{self.player1.score} - {self.player2.score}"
        score_surface = self.font.render(score_text, True, WHITE)
        self.screen.blit(score_surface, (SCREEN_WIDTH // 2 - score_surface.get_width() // 2, 25))

        # Имена игроков
        player1_text = self.font.render("Player 1", True, BLUE)
        player2_text = self.font.render("Player 2", True, RED)

        self.screen.blit(player1_text, (50, 20))
        self.screen.blit(player2_text, (SCREEN_WIDTH - 50 - player2_text.get_width(), 20))

    def draw_center_line(self):
        """Отрисовка центральной линии"""
        for y in range(0, SCREEN_HEIGHT, 30):
            pygame.draw.rect(self.screen, WHITE, (SCREEN_WIDTH // 2 - 2, y, 4, 15))

    def draw_game_over(self):
        """Отрисовка экрана окончания игры"""
        # Полупрозрачный фон
        overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        overlay.set_alpha(180)
        overlay.fill(BLACK)
        self.screen.blit(overlay, (0, 0))

        # Текст победы
        if self.player1.score > self.player2.score:
            winner_text = "Player 1 Wins!"
            color = BLUE
        else:
            winner_text = "Player 2 Wins!"
            color = RED

        winner_surface = self.large_font.render(winner_text, True, color)
        self.screen.blit(winner_surface,
                         (SCREEN_WIDTH // 2 - winner_surface.get_width() // 2,
                          SCREEN_HEIGHT // 2 - 50))

        # Финальный счет
        final_score = f"Final Score: {self.player1.score} - {self.player2.score}"
        score_surface = self.font.render(final_score, True, WHITE)
        self.screen.blit(score_surface,
                         (SCREEN_WIDTH // 2 - score_surface.get_width() // 2,
                          SCREEN_HEIGHT // 2 + 20))

        # Инструкция для рестарта
        restart_text = "Press R to Restart or Q to Quit"
        restart_surface = self.font.render(restart_text, True, GREEN)
        self.screen.blit(restart_surface,
                         (SCREEN_WIDTH // 2 - restart_surface.get_width() // 2,
                          SCREEN_HEIGHT // 2 + 80))

    def restart_game(self):
        """Перезапуск игры"""
        self.player1.score = 0
        self.player2.score = 0
        self.reset_round()
        self.game_state = "playing"

    def run(self):
        """Основной игровой цикл"""
        running = True

        while running:
            # Обработка событий
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p and self.game_state == "playing":
                        self.game_state = "paused"
                    elif event.key == pygame.K_p and self.game_state == "paused":
                        self.game_state = "playing"
                    elif event.key == pygame.K_r and self.game_state == "game_over":
                        self.restart_game()
                    elif event.key == pygame.K_q:
                        running = False

            if self.game_state == "playing":
                # Управление
                keys = pygame.key.get_pressed()
                if keys[pygame.K_w]:
                    self.player1.move("up")
                if keys[pygame.K_s]:
                    self.player1.move("down")

                # Движение AI
                self.player2.move(None, self.ball)

                # Обновление игры
                self.ball.move()
                self.handle_collisions()

            # Отрисовка
            self.screen.fill(BLACK)

            # Игровые элементы
            self.draw_center_line()
            self.player1.draw(self.screen)
            self.player2.draw(self.screen)
            self.ball.draw(self.screen)
            self.draw_scoreboard()

            # Состояния игры
            if self.game_state == "paused":
                pause_text = self.large_font.render("PAUSED", True, WHITE)
                self.screen.blit(pause_text,
                                 (SCREEN_WIDTH // 2 - pause_text.get_width() // 2,
                                  SCREEN_HEIGHT // 2 - pause_text.get_height() // 2))

            if self.game_state == "game_over":
                self.draw_game_over()

            pygame.display.flip()
            self.clock.tick(FPS)

        pygame.quit()
        sys.exit()


# Запуск игры
if __name__ == "__main__":
    game = Game()
    game.run()