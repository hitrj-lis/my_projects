# Economy and war

import pygame



pygame.init()

cursor = '>> : '

screen_x = 640
screen_y = 480
background_color = (0, 0, 0)

delay = 25

x = int(screen_x / 2)
y = int(screen_y / 2)
speed = 2

run = True

radius = 10
move_right = False
move_left = False
move_up = False
move_down = False

window = pygame.display.set_mode((screen_x, screen_y))
pygame.display.set_caption('Tank')

while run:

    pygame.time.delay(delay)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False
            if event.key == pygame.K_RIGHT:
                move_right = True
            if event.key == pygame.K_LEFT:
                move_left = True
            if event.key == pygame.K_UP:
                move_up = True
            if event.key == pygame.K_DOWN:
                move_down = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                move_right = False
            if event.key == pygame.K_LEFT:
                move_left = False
            if event.key == pygame.K_UP:
                move_up = False
            if event.key == pygame.K_DOWN:
                move_down = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos

    if move_right:
        x += speed
        if x > screen_x - radius:
            x = screen_x - radius
    if move_left:
        x -= speed
        if x < 0 + radius:
            x = 0 + radius
    if move_up:
        y -= speed
        if y < 0 + radius:
            y = 0 + radius
    if move_down:
        y += speed
        if y > screen_y - radius:
            y = screen_y - radius

    window.fill(background_color)
    pygame.draw.circle(window, (0, 255, 0), (x, y), radius)
    pygame.display.flip()
