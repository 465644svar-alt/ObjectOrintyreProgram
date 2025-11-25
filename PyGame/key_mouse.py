import pygame
import time

pygame.init()

window_size = (full_width, full_height) = (800, 800)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("Тестовый проект")

# Загрузка изображений
image1 = pygame.image.load('logopy.png')
image_rect1 = image1.get_rect()

image2 = pygame.image.load("pycharm.png")
image_rect2 = image2.get_rect()

# Установка начальных позиций
image_rect1.center = (full_width // 4, full_height // 2)
image_rect2.center = (3 * full_width // 4, full_height // 2)

run = True
speed = 15
clock = pygame.time.Clock()

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # Управление мышью для первого объекта
    mouseX, mouseY = pygame.mouse.get_pos()
    image_rect1.x = mouseX - image_rect1.width // 2
    image_rect1.y = mouseY - image_rect1.height // 2

    # Управление клавиатурой для второго объекта
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        image_rect2.x -= speed
    if keys[pygame.K_RIGHT]:
        image_rect2.x += speed
    if keys[pygame.K_UP]:
        image_rect2.y -= speed
    if keys[pygame.K_DOWN]:
        image_rect2.y += speed

    # Проверка столкновения
    if image_rect1.colliderect(image_rect2):
        print("Произошло столкновение!")
        # Можно добавить визуальное отображение столкновения
        # Например, временно изменить цвет фона
        screen.fill((255, 0, 0))  # Красный фон при столкновении
        pygame.display.flip()
        time.sleep(0.5)  # Короткая пауза для визуального эффекта

    # Отрисовка
    screen.fill((50, 0, 50))  # Возвращаем обычный цвет фона
    screen.blit(image1, image_rect1)
    screen.blit(image2, image_rect2)
    pygame.display.flip()

    # Ограничение FPS
    clock.tick(60)

pygame.quit()