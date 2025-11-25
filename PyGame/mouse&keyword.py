import pygame
import time
pygame.init()

window_size =(full_width, full_height) = (800,800)
screen =pygame.display.set_mode(window_size)
pygame.display.set_caption("Тестовый проект")

image1 = pygame.image.load('logopy.png')
image_rect1 = image1.get_rect()

image2 = pygame.image.load("pycharm.png")
image_rect2 = image2.get_rect()

run = True
speed = 5
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEMOTION:
            mouseX, mouseY = pygame.mouse.get_pos()
            image_rect1.x = mouseX -50
            image_rect1.y = mouseY -50
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        image_rect2.x -= speed
    if keys[pygame.K_RIGHT]:
        image_rect2.x += speed
    if keys[pygame.K_UP]:
        image_rect2.y -= speed
    if keys[pygame.K_DOWN]:
        image_rect2.y += speed


    if image_rect1.colliderect(image_rect2):
        print("Произошло столкновение")
        time.sleep(1)


    screen.fill((50,0,50))
    screen.blit(image1, image_rect1)
    screen.blit(image2, image_rect2)
    pygame.display.flip()


pygame.quit()