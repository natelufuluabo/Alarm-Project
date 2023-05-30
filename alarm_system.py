#!/usr/bin/python3
from gpiozero import LED
import RPi.GPIO as GPIO
from time import sleep
import signal
import sys
from sms_alerts import send_text

red_led = LED(16)
yellow_led = LED(18)
door_sensor = 19

GPIO.setmode(GPIO.BCM)
GPIO.setup(door_sensor, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.add_event_detect(door_sensor, GPIO.BOTH, bouncetime=100)

def blink_lights():
	yellow_led.on()
	red_led.on()
	sleep(0.5)
	red_led.off()
	sleep(0.5)

def toggle_alarm_state(alarm_state):
	if alarm_state == "Not Armed":
		return activate_alarm(alarm_state)
	elif alarm_state == "Armed":
		alarm_state = "Not Armed"
		red_led.off()
		yellow_led.off()
		return alarm_state

def activate_alarm(alarm_state):
	if GPIO.input(door_sensor) == 0:
		send_text("Alarm failed to be activated because door opened. Make sure door is closed at the end of the delay to successfully activate alarm")
		return alarm_state
	else:
		alarm_state = "Armed"
		red_led.on()	
		send_text("Alarm activated successfully. Enjoy your outings!")
		return alarm_state

def sound_alarm(alarm_event):
	while True:
		if alarm_event.is_set():
			# Delay to give users or intruders time to enter the system code and disarm the system
			sleep(10)
			# Check to see if the system is still armed after delay before starting the alarm sound and send text message to home owner
			if alarm_event.is_set():
				send_text("Alarm triggered at home")
				while alarm_event.is_set():
					blink_lights()

def run_alarm_system(alarm_state, alarm_event):
	if GPIO.event_detected(door_sensor):
		print("Event Detected")
		print(alarm_state)
		if GPIO.input(door_sensor) == 0 and alarm_state == "Armed":
			alarm_event.set()
			return True
