#!/usr/bin/python3

import pygame
from class_button import Button

pygame.init()

BACKGROUND_COLOR = (42, 62, 140)
BLANC = (255, 255, 255)

button_1 = Button(550, 135, 100, 125, "1", BACKGROUND_COLOR, BLANC)
button_4 = Button(550, 247.5, 100, 125, "4", BACKGROUND_COLOR, BLANC)
button_7 = Button(550, 360, 100, 125, "7", BACKGROUND_COLOR, BLANC)
button_x = Button(550, 472.5, 100, 125, "x", BACKGROUND_COLOR, BLANC)

button_2 = Button(687, 135, 100, 126, "2", BACKGROUND_COLOR, BLANC)
button_5 = Button(687, 247.5, 100, 126, "5", BACKGROUND_COLOR, BLANC)
button_8 = Button(687, 360, 100, 126, "8", BACKGROUND_COLOR, BLANC)
button_0 = Button(687, 472.5, 100, 126, "0", BACKGROUND_COLOR, BLANC)

button_3 = Button(825, 135, 100, 125, "3", BACKGROUND_COLOR, BLANC)
button_6 = Button(825, 247.5, 100, 125, "6", BACKGROUND_COLOR, BLANC)
button_9 = Button(825, 360, 100, 125, "9", BACKGROUND_COLOR, BLANC)
button_back = Button(825, 472.5, 100, 125, "<", BACKGROUND_COLOR, BLANC)


def update_code_input(codeInput, value):
    if len(codeInput) <= 3:
        return codeInput + value
    return codeInput

def update_input_area_text(inputAreaText):
    if len(inputAreaText) <= 3:
        return inputAreaText + "*"
    return inputAreaText

def clear_code_input():
    return ""

def correct_code_input(codeInput):
    return codeInput[:-1]

def correct_input_area_text(inputAreaText):
    return inputAreaText[:-1]

def draw_keypad(screen, inputAreaText):
    sysfont = pygame.font.get_default_font()
    font = pygame.font.SysFont(None, 36)

    #Code to draw the code input area
    pygame.draw.rect(screen, (42, 62, 140), pygame.Rect(550, 70, 400, 52.5))
    inputText = font.render(inputAreaText, True, (255, 255, 255))
    inputArea = inputText.get_rect()
    inputArea.center = (550 + 400 / 2, 70 + 52.5 / 2)
    screen.blit(inputText, inputArea)

    #Code to draw keypad buttons
    button_1.draw_button(screen)
    button_4.draw_button(screen)
    button_7.draw_button(screen)
    button_x.draw_button(screen)
    
    button_2.draw_button(screen)
    button_5.draw_button(screen)
    button_8.draw_button(screen)
    button_0.draw_button(screen)
    
    button_3.draw_button(screen)
    button_6.draw_button(screen)
    button_9.draw_button(screen)
    button_back.draw_button(screen)
