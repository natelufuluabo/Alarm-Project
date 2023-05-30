#!/usr/bin/python3

import requests, pygame
from datetime import datetime

pygame.init()

url = "https://api.open-meteo.com/v1/forecast?latitude=45.51&longitude=-73.59&hourly=temperature_2m,cloudcover&forecast_days=1&timezone=America%2FNew_York"
response = requests.get(url)

hi = max(response.json()["hourly"]["temperature_2m"])
low = min(response.json()["hourly"]["temperature_2m"])
cloud_coverage = response.json()["hourly"]["cloudcover"]

img = pygame.image.load("weather_img.png")

def show_weather(screen):
    global hi
    global low
    global img
    global cloud_coverage
    sysfont = pygame.font.get_default_font()
    font = pygame.font.SysFont(None, 36)

    screen.blit(img, (100, 70))

    headline_text = font.render("Today Forecast", True, (42, 62, 140))
    headline_center = headline_text.get_rect()
    headline_center.center = (265, 370)
    screen.blit(headline_text, headline_center)

    hi_text = font.render("Hi: " + str(hi) + " C", True, (255, 0, 0))
    hi_center = hi_text.get_rect()
    hi_center.center = (350, 420)
    screen.blit(hi_text, hi_center)

    low_text = font.render("Low: " + str(low) + " C", True, (42, 62, 140))
    low_center = low_text.get_rect()
    low_center.center = (180, 420)
    screen.blit(low_text, low_center)

    now = datetime.now()
    current_time = now.strftime("%H")
    cloud_conditions = None

    if cloud_coverage[int(current_time)] <= 50:
        cloud_conditions = "Sunny"
    if (
        cloud_coverage[int(current_time)] > 50
        and cloud_coverage[int(current_time)] <= 80
    ):
        cloud_conditions = "Partly Cloudy"
    if (
        cloud_coverage[int(current_time)] > 80
        and cloud_coverage[int(current_time)] < 100
    ):
        cloud_conditions = "Cloudy"

    cloud_text = font.render(cloud_conditions, True, (42, 62, 140))
    cloud_center = cloud_text.get_rect()
    cloud_center.center = (265, 470)
    screen.blit(cloud_text, cloud_center)

