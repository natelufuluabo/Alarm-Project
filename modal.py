#!/usr/bin/python3

import pygame
from time import sleep

pygame.init()

def draw_modal(screen, screen_width, time):
    sysfont = pygame.font.get_default_font()
    font = pygame.font.SysFont(None, 36)
    x_pos = 300
    y_pos = 225
    width = 400
    height = 150
    pygame.draw.rect(screen, (0, 0, 0, 0.36), pygame.Rect(x_pos, y_pos, width,height))
    textBtn = font.render("System will be armed in " + str(time), True, (255, 255, 255))
    rectBtn = textBtn.get_rect()
    rectBtn.center = (x_pos + width / 2, y_pos + height / 2)
    screen.blit(textBtn, rectBtn)