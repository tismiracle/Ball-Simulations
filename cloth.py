import math
import pygame
import numpy as np


gravitation = 10


def vector_length(start_pos, end_pos):
    x = int(end_pos[0]) - int(start_pos[0])
    y = int(end_pos[1]) - int(end_pos[1])
    #print(x, y)
    length = math.sqrt(x**2+y**2)
    return int(length)

def calculate_length_of_new_vec(vec_length, grav):
    return int(math.sqrt(vec_length**2 - grav**2))

def calculate_x(vec_len, new_vec_len):
    return vec_len - new_vec_len

def calculate_y(end_pos_y, grav):
    return end_pos_y + grav

A = np.array([[250, 10], [400, 10]])
#pygame.Vector2(A[1],[2])
#Vector2(x, y) -> Vector2
pygame.init()
FPS = 20 # frames per second setting
fpsClock = pygame.time.Clock()
screen = pygame.display.set_mode([500, 500])

running = True
while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background with white
    screen.fill((0, 0, 0))

    # Draw a solid blue circle in the center
    #pygame.draw.circle(screen, (0, 0, 255), (250, 250), 75)
    #print(A[0][0],A[0][1])

    vec_len = vector_length(A[0],A[1])
    new_vec_len = calculate_length_of_new_vec(vec_len, gravitation)
    x = vec_len - new_vec_len
    y = calculate_y(A[1][1], gravitation)
    print(x, y)
    A[1] = [x, y]

    
    pygame.draw.line(screen, (255,255,255), A[0], A[1])
    
   # Flip the display
    pygame.display.flip()
    fpsClock.tick(FPS)


# Done! Time to quit.
pygame.quit()

