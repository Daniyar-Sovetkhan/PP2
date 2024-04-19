import pygame
import sys
import random
from pygame.locals import *

# Инициализация Pygame
pygame.init()

# Определение размеров окна и его создание
WINDOW_WIDTH, WINDOW_HEIGHT = 400, 400
windowSurface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Snake')

# Определение цветов
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Начальные параметры змейки
snake = [(100, 100), (90, 100), (80, 100)]  # Начальное положение змейки
snake_direction = 'right'  # Начальное направление движения змейки
snake_speed = 10  # Начальная скорость змейки

# Начальные параметры еды
food = (random.randint(0, WINDOW_WIDTH//10 - 1) * 10, random.randint(0, WINDOW_HEIGHT//10 - 1) * 10)

# Параметры игры
level = 1  # Текущий уровень
score = 0  # Текущий счет
level_threshold = 3  # Порог для перехода на следующий уровень

# Шрифт для отображения счета и уровня
font = pygame.font.SysFont(None, 24)

# Основной игровой цикл
running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == KEYDOWN:
            # Обработка нажатий клавиш для изменения направления змейки
            if event.key == K_UP and snake_direction != 'down':
                snake_direction = 'up'
            elif event.key == K_DOWN and snake_direction != 'up':
                snake_direction = 'down'
            elif event.key == K_LEFT and snake_direction != 'right':
                snake_direction = 'left'
            elif event.key == K_RIGHT and snake_direction != 'left':
                snake_direction = 'right'

    # Обновление положения змейки в зависимости от текущего направления
    if snake_direction == 'up':
        snake.insert(0, (snake[0][0], snake[0][1] - 10))
    elif snake_direction == 'down':
        snake.insert(0, (snake[0][0], snake[0][1] + 10))
    elif snake_direction == 'left':
        snake.insert(0, (snake[0][0] - 10, snake[0][1]))
    elif snake_direction == 'right':
        snake.insert(0, (snake[0][0] + 10, snake[0][1]))

    # Проверка на столкновение с едой
    if snake[0] == food:
        score += 1
        # Генерация нового положения для еды
        food = (random.randint(0, WINDOW_WIDTH//10 - 1) * 10, random.randint(0, WINDOW_HEIGHT//10 - 1) * 10)
        while food in snake:  
            food = (random.randint(0, WINDOW_WIDTH//10 - 1) * 10, random.randint(0, WINDOW_HEIGHT//10 - 1) * 10)
    else:
        # Уменьшение длины змейки, если не было столкновения с едой
        snake.pop() 

    # Проверка на выход за границы игрового поля
    if (snake[0][0] < 0 or snake[0][0] >= WINDOW_WIDTH or
            snake[0][1] < 0 or snake[0][1] >= WINDOW_HEIGHT):
        running = False  

    # Проверка на столкновение с собственным хвостом
    if snake[0] in snake[1:]:
        running = False  

    # Проверка на переход на следующий уровень
    if score >= level_threshold * level:
        level += 1
        snake_speed += 2 

    # Отрисовка игрового поля
    windowSurface.fill(BLACK)
    for segment in snake:
        pygame.draw.rect(windowSurface, WHITE, (segment[0], segment[1], 10, 10))
    pygame.draw.rect(windowSurface, RED, (food[0], food[1], 10, 10))

    # Отображение счета и уровня
    score_text = font.render(f'Score: {score}', True, GREEN)
    level_text = font.render(f'Level: {level}', True, GREEN)
    windowSurface.blit(score_text, (10, 10))
    windowSurface.blit(level_text, (10, 30))

    # Обновление экрана
    pygame.display.update()

    # Ограничение скорости змейки
    pygame.time.Clock().tick(snake_speed)

# Завершение игры
pygame.quit()
sys.exit()
