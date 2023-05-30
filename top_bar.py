#!/usr/bin/python3

import pygame
from datetime import datetime

pygame.init()

sysfont = pygame.font.get_default_font()
font = pygame.font.SysFont(None, 25)

BACKGROUND_COLOR = (42, 62, 140)
BLANC = (255, 255, 255)

def draw_top_bar(screen, text, screen_width):
    pygame.draw.rect(screen, BACKGROUND_COLOR, pygame.Rect(0, 0, screen_width, 50))
    left_text = font.render(text, True, BLANC)
    screen.blit(left_text, (20, 17))

    now = datetime.now()
    current_time = now.strftime("%H:%M")
    right_text = font.render(current_time, True, BLANC)
    screen.blit(right_text, (940, 17))
