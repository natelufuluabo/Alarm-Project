#!/usr/bin/python3

import pygame
import sys
import threading
from time import sleep
from top_bar import draw_top_bar
from arm_disarm_button import cancel_button, arm_disarm_button_1, arm_disarm_button_2, update_arm_disarm_button, validate_code
from keypad import correct_input_area_text, correct_code_input, clear_code_input, update_input_area_text, update_code_input, draw_keypad,button_1, button_4, button_7, button_x, button_2, button_3, button_5, button_6, button_8, button_9, button_0, button_back
from alarm_system import toggle_alarm_state, run_alarm_system, sound_alarm
from modal import draw_modal
from weather_conditions import show_weather

pygame.init()

screen_width = 1000
screen_height = 600
INTERFACE_BACKGROUND = (255, 255, 255)
screen = pygame.display.set_mode([screen_width, screen_height])

alarm_event = threading.Event()

alarm_state = "Not Armed"
system_text = "System Ready, "
system_code = "1234"
codeInput = ""
inputAreaText = ""

keypad_on_screen = False
modal_on_screen = False
time = 10

def run_gui():
    global alarm_state
    global system_text
    global system_code
    global codeInput
    global inputAreaText
    global keypad_on_screen
    global modal_on_screen
    global time
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x_pos, mouse_y_pos = pygame.mouse.get_pos()
            if button_1.isOverButton((mouse_x_pos, mouse_y_pos)) and keypad_on_screen:
                codeInput = update_code_input(codeInput, button_1.text)
                inputAreaText = update_input_area_text(inputAreaText)
            if button_2.isOverButton((mouse_x_pos, mouse_y_pos)) and keypad_on_screen:
                codeInput = update_code_input(codeInput, button_2.text)
                inputAreaText = update_input_area_text(inputAreaText)
            if button_3.isOverButton((mouse_x_pos, mouse_y_pos)) and keypad_on_screen:
                codeInput = update_code_input(codeInput, button_3.text)
                inputAreaText = update_input_area_text(inputAreaText)
            if button_4.isOverButton((mouse_x_pos, mouse_y_pos)) and keypad_on_screen:
                codeInput = update_code_input(codeInput, button_4.text)
                inputAreaText = update_input_area_text(inputAreaText)
            if button_5.isOverButton((mouse_x_pos, mouse_y_pos)) and keypad_on_screen:
                codeInput = update_code_input(codeInput, button_5.text)
                inputAreaText = update_input_area_text(inputAreaText)
            if button_6.isOverButton((mouse_x_pos, mouse_y_pos)) and keypad_on_screen:
                codeInput = update_code_input(codeInput, button_6.text)
                inputAreaText = update_input_area_text(inputAreaText)
            if button_7.isOverButton((mouse_x_pos, mouse_y_pos)) and keypad_on_screen:
                codeInput = update_code_input(codeInput, button_7.text)
                inputAreaText = update_input_area_text(inputAreaText)
            if button_8.isOverButton((mouse_x_pos, mouse_y_pos)) and keypad_on_screen:
                codeInput = update_code_input(codeInput, button_8.text)
                inputAreaText = update_input_area_text(inputAreaText)
            if button_9.isOverButton((mouse_x_pos, mouse_y_pos)) and keypad_on_screen:
                codeInput = update_code_input(codeInput, button_9.text)
                inputAreaText = update_input_area_text(inputAreaText)
            if button_0.isOverButton((mouse_x_pos, mouse_y_pos)) and keypad_on_screen:
                codeInput = update_code_input(codeInput, button_0.text)
                inputAreaText = update_input_area_text(inputAreaText)
            if button_back.isOverButton((mouse_x_pos, mouse_y_pos)) and keypad_on_screen:
                codeInput = correct_code_input(codeInput)
                inputAreaText = correct_input_area_text(inputAreaText)
            if button_x.isOverButton((mouse_x_pos, mouse_y_pos)) and keypad_on_screen: 
                codeInput = clear_code_input()
                inputAreaText = clear_code_input()
            if arm_disarm_button_1.isOverButton((mouse_x_pos, mouse_y_pos)) and keypad_on_screen == False:
                update_arm_disarm_button(alarm_state)
                keypad_on_screen = True
            if arm_disarm_button_2.isOverButton((mouse_x_pos, mouse_y_pos)) and keypad_on_screen:
                if validate_code(system_code, codeInput):
                    if alarm_state == "Armed":
                        alarm_state = toggle_alarm_state(alarm_state)
                        alarm_event.clear()
                        update_arm_disarm_button(alarm_state)
                        codeInput = clear_code_input()
                        inputAreaText = clear_code_input()
                        keypad_on_screen = False
                    elif alarm_state == "Not Armed":
                        modal_on_screen = True
                else:
                    codeInput = clear_code_input()
                    inputAreaText = clear_code_input()
            if cancel_button.isOverButton((mouse_x_pos, mouse_y_pos)):
                keypad_on_screen = False
    
    screen.fill(INTERFACE_BACKGROUND)
    # Draw keypad on screen for user to enter code
    # to arm or disarm the alarm system
    if keypad_on_screen:
        if alarm_state == "Armed":
            text = "Enter code to disarm system"
            draw_top_bar(screen, text, screen_width)
            draw_keypad(screen, inputAreaText)
            arm_disarm_button_2.draw_button(screen)
            cancel_button.draw_button(screen)
        elif alarm_state == "Not Armed":
            text = "Enter code to arm system"
            draw_top_bar(screen, text, screen_width)
            draw_keypad(screen, inputAreaText)
            arm_disarm_button_2.draw_button(screen)
            cancel_button.draw_button(screen)
            if modal_on_screen:
                draw_modal(screen, screen_width, time)
                sleep(1)
                time = time - 1
                if time == 0:
                    alarm_state = toggle_alarm_state(alarm_state)
                    update_arm_disarm_button(alarm_state)
                    codeInput = clear_code_input()
                    inputAreaText = clear_code_input()
                    keypad_on_screen = False
                    modal_on_screen = False
                    time = 10
    # Draw main screen with weather condition
    else:
        show_weather(screen)
        draw_top_bar(screen, system_text + alarm_state, screen_width)
        arm_disarm_button_1.draw_button(screen)
    
    pygame.display.update()

sound_alarm_thread = threading.Thread(target=sound_alarm, args=(alarm_event,))
sound_alarm_thread.daemon = True
sound_alarm_thread.start()

while True: 
    run_gui()
    if run_alarm_system(alarm_state, alarm_event):
        alarm_event.set()
    
