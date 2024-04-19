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

music_dir = "/Users/sovetkhandaniyar/Downloads"


music_files = [f for f in os.listdir(music_dir) if f.endswith(".mp3")]

current_track = 0

pygame.mixer.music.load(os.path.join(music_dir, music_files[current_track]))

def play_music():
    pygame.mixer.music.play()
    print(pygame.mixer.music.get_busy())

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
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                play_music()
                print(pygame.mixer.music.get_busy())  
            elif event.key == pygame.K_s:
                stop_music()
            elif event.key == pygame.K_n:
                next_track()
            elif event.key == pygame.K_b:
                previous_track()

    screen.fill(BLACK)
    pygame.display.flip()

pygame.quit()

