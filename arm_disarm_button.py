#!/usr/bin/python3

import pygame
from class_button import Button

pygame.init()

GREEN = (97, 235, 52)
RED = (235, 52, 58)
NOIR = (0, 0, 0)
BLANC = (255, 255, 255)

def update_arm_disarm_button(alarm_state):
    if alarm_state == "Not Armed":
        arm_disarm_button_1.text = "ARM"
        arm_disarm_button_2.text = "ARM"
        arm_disarm_button_1.fillColor = GREEN
        arm_disarm_button_2.fillColor = GREEN
    elif alarm_state == "Armed":
        arm_disarm_button_1.text = "DISARM"
        arm_disarm_button_2.text = "DISARM"
        arm_disarm_button_1.fillColor = RED
        arm_disarm_button_2.fillColor = RED

def validate_code(system_code, code_input):
    if system_code == code_input:
        return True
    return False

arm_disarm_button_1 = Button(625, 200, 250, 250, "ARM", GREEN, NOIR)
arm_disarm_button_2 = Button(125, 200, 250, 250, "ARM", GREEN, NOIR)
cancel_button = Button(125, 475, 50, 250, "Cancel", RED, BLANC)
