import pygame
import os

pygame.init()
pygame.mixer.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Music Player with Keyboard Controls")

music_dir = "/Users/sateya2022/Desktop/muzika"
music_files = [f for f in os.listdir(music_dir) if f.endswith(".mp3")]
current_track = 0

pygame.mixer.music.load(os.path.join(music_dir, music_files[current_track]))

def play_music():
    pygame.mixer.music.play()

def stop_music():
    pygame.mixer.music.stop()

def next_track():
    global current_track
    current_track = (current_track + 1) % len(music_files)
    pygame.mixer.music.load(os.path.join(music_dir, music_files[current_track]))
    play_music()

def previous_track():
    global current_track
    current_track = (current_track - 1) % len(music_files)
    pygame.mixer.music.load(os.path.join(music_dir, music_files[current_track]))
    play_music()

# Здесь добавлена функция play_music() для начала воспроизведения музыки
play_music()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if pygame.mixer.music.get_busy():
                    stop_music()
                else:
                    play_music()
            elif event.key == pygame.K_RIGHT:
                next_track()
            elif event.key == pygame.K_LEFT:
                previous_track()

    screen.fill(BLACK)
    pygame.display.flip()

pygame.quit()
