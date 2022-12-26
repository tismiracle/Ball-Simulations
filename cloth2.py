import math
import pygame
import numpy as np


screen_width = 500
screen_height = 500



pointA = {"x": 100, "y": 100, "old_x": 95, "old_y": 90}

friction = 0.9888888

# vecV = {"x": 0, "y": -5}
#vx = 0
#vy = 5

pygame.init()
FPS = 60 # frames per second setting
fpsClock = pygame.time.Clock()
screen = pygame.display.set_mode([screen_width, screen_height])



running = True
while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background with white
    screen.fill((0, 0, 0))

    # vecV = sub_vec((pointA["x"], pointA["y"]), (pointA["old_x"], pointA["old_y"]))

    vx = pointA["x"] - pointA["old_x"]
    vy = pointA["y"] - pointA["old_y"]

    pointA["old_x"] = pointA["x"]
    pointA["old_y"] = pointA["y"]

    pointA["x"] += vx * friction
    pointA["y"] += vy * friction


    if pointA["x"] > screen_width - 5:
        pointA["x"] = screen_width - 5
        pointA["old_x"] = pointA["x"] + vx
    elif pointA["x"] < 5:
        pointA["x"] = 5
        pointA["old_x"] = pointA["x"] + vx

    if pointA["y"] > screen_height - 5:
        pointA["y"] = screen_width - 5
        pointA["old_y"] = pointA["y"] + vy
    elif pointA["y"] < 5:
        pointA["y"] = 5
        pointA["old_y"] = pointA["y"] + vy


    pygame.draw.circle(screen, (255,235,23), (pointA["x"], pointA["y"]), 5)

    # vx = pointA["x"] - pointA["old_x"]
    # vy = pointA["y"] - pointA["old_y"]
    # pointA = check_if_out_of_borders(pointA, vecV)
   # Flip the display
    pygame.display.flip()
    fpsClock.tick(FPS)

pygame.quit()



