import pygame
from random import randrange

RES = 600
SIZE = 50

x, y = randrange(0, RES, SIZE), randrange(0, RES, SIZE)
apple = randrange(0, RES, SIZE), randrange(0, RES, SIZE)
dirs = {'W': True, 'S': True,'A': True,'D': True} # словарь для разрешения движения всех клавиш
length = 1
snake = [(x, y)]
dx, dy = 0, 0
score = 0
fps = 6

pygame.init()
sc = pygame.display.set_mode([RES, RES])
clock = pygame.time.Clock()
font_score = pygame.font.SysFont('Arial', 26, bold=True)

while True:
    sc.fill(pygame.Color('Black'))
    # drawing snake
    [(pygame.draw.rect(sc, pygame.Color('green'), (i, j, SIZE - 2, SIZE - 2))) for i, j in snake]
    pygame.draw.rect(sc, pygame.Color('red'), (*apple, SIZE, SIZE))
    render_score = font_score.render(f'SCORE: {score}', 1, pygame.Color('orange'))
    sc.blit(render_score, (5, 5))

    # движение змеи
    x += dx * SIZE
    y += dy * SIZE
    snake.append((x, y)) # каждый шаг змейки добавляем в список координат
    snake = snake[- length:] # делаем срез для того чтобы змейка была не бесконечной
    # учим кушать яблоко
    if snake[-1] == apple:
        apple = randrange(0, RES,SIZE), randrange(0, RES, SIZE)
        length += 1
        score += 1 # счет
        fps += 1
# проигрываем - вышли за предел поля или съели себя
    if x < 0 or x > RES - SIZE or y < 0 > RES - SIZE or len(snake) != len(set(snake)):
        while True:
            render_end = font_score.render('GAME OVER', 1, pygame.Color('orange'))
            sc.blit(render_end, (RES // 2 - 200, RES // 3))
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()

    pygame.display.flip()
    clock.tick(fps)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    # control прописываем управление для змейки
    key = pygame.key.get_pressed()
    if key[pygame.K_w] and dirs ['W']:
        dx, dy = 0, -1
        dirs = {'W': True, 'S': False, 'A': True, 'D': True}
    if key[pygame.K_s] and dirs ['S']:
        dx, dy = 0, 1
        dirs = {'W': False, 'S': True, 'A': True, 'D': True}
    if key[pygame.K_a] and dirs ['A']:
        dx, dy = -1, 0
        dirs = {'W': True, 'S': True, 'A': True, 'D': False}
    if key[pygame.K_d] and dirs ['D']:
        dx, dy = 1, 0
        dirs = {'W': True, 'S': True, 'A': False, 'D': True}
