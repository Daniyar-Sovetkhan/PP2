import pygame
import sys

# Инициализация Pygame
pygame.init()

# Создание окна
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("My Pygame Window")

# Основной цикл программы
while True:
    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Отрисовка на экране
    screen.fill((255, 255, 255))  # Белый фон
    font = pygame.font.SysFont(None, 36)  # Шрифт
    text = font.render("Hello, Pygame!", True, (0, 0, 0))  # Текст
    screen.blit(text, (300, 250))  # Рисуем текст на экране
    pygame.display.flip()  # Обновление экрана
