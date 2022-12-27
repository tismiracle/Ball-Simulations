
from math import radians
import pygame



screen_width = 500
screen_height = 500



pointA = {"x": 100, "y": 100, "old_x": 95, "old_y": 90}
pointB = {"x": 200, "y": 100, "old_x": 95, "old_y": 90}
radius = 10

bounce = 0.8
friction = 0.99



pygame.init()
FPS = 60 # frames per second setting
fpsClock = pygame.time.Clock()
screen = pygame.display.set_mode([screen_width, screen_height])


def if_clicked_on_ball(mouse_pos, mouse_click, ball_pos, ball_radius):

    if mouse_click[0]:
        if mouse_pos[0] > ball_pos["x"] - ball_radius and mouse_pos[0] < ball_pos["x"] + ball_radius:
        # print("clicked on x axis of ball")
            
            if mouse_pos[1] > ball_pos["y"] - ball_radius and mouse_pos[1] < ball_pos["y"] + ball_radius:
                print("clicked on ball")
                return True
            else:
                print("Not clicked")
                return False
        else:
            print("Not clicked")
            return False





def draw_distance(ball_pos, mouse_pos):
    pygame.draw.line(screen, (255, 255, 255), (ball_pos["x"], ball_pos["y"]), (mouse_pos[0], mouse_pos[1]))






mouse_pos = None
ball_clicked = False
running = True
while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    
    mouse_pos = pygame.mouse.get_pos()
    mouse_click = pygame.mouse.get_pressed()
    # mouse_pos = pygame.mouse.get_pos()
    ball_clicked = if_clicked_on_ball(mouse_pos, mouse_click, pointA, radius)
    



    # Fill the background with white
    screen.fill((0, 0, 0))

    # vecV = sub_vec((pointA["x"], pointA["y"]), (pointA["old_x"], pointA["old_y"]))
    vx = pointA["x"] - pointA["old_x"]
    vy = pointA["y"] - pointA["old_y"]


    pointA["old_x"] = pointA["x"]
    pointA["old_y"] = pointA["y"]

    if ball_clicked:
        vx = pointA["x"] - mouse_pos[0]
        vy = pointA["y"] - mouse_pos[1]
    # print(mouse_click)

    pointA["x"] += vx * friction
    pointA["y"] += vy * friction


    if pointA["x"] > screen_width - radius:
        pointA["x"] = screen_width - radius
        pointA["old_x"] = pointA["x"] + vx * bounce
    elif pointA["x"] < radius:
        pointA["x"] = radius
        pointA["old_x"] = pointA["x"] + vx * bounce

    if pointA["y"] > screen_height - radius:
        pointA["y"] = screen_width - radius
        pointA["old_y"] = pointA["y"] + vy * bounce
    elif pointA["y"] < radius:
        pointA["y"] = radius
        pointA["old_y"] = pointA["y"] + vy * bounce

    print(pointA)


    pygame.draw.circle(screen, (255,235,23), (pointA["x"], pointA["y"]), radius)

    # if_clicked = if_clicked_on_ball(mouse_pos, mouse_click, pointA, 5)


        # clicked = vel[1]

        
        
   # Flip the display
    pygame.display.flip()
    fpsClock.tick(FPS)

pygame.quit()



