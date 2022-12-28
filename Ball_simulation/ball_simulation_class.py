
from math import radians
import pygame
import random



screen_width = 500
screen_height = 500



pygame.init()
FPS = 50 # frames per second setting
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

class Ball():
    """
    function order:
    1. save_previous_position
    2. move
    3. update v
    """
    def __init__(self, x, y, vx, vy, ball_friction, bounce, radius, name, color = (255, 255, 255), old_x = 0, old_y = 0, gravity = 0):
        """ gravity = 0 is no gravity
        bounce is only 0-1 value
        friction is only 0-1 value        
        """
        self.name = name
        self.vx = vx
        self.vy = vy
        self.x = x
        self.y = y
        self.old_x = x
        self.old_y = y
        self.radius = radius
        self.color = color
        self.friction = ball_friction
        self.bounce = bounce
        self.gravity = gravity

    def save_previous_position(self):
        self.old_x = self.x
        self.old_y = self.y

    def move(self):
        self.x += self.vx * self.friction
        self.y += self.vy * self.friction
        self.y += self.gravity

    def update_v(self):
        self.vx = self.x - self.old_x
        self.vy = self.y - self.old_y

    def collision_line(self, surf):
        pygame.draw.line(surf, (243,23,23), (self.x, self.y), (self.x + self.vx, self.y + self.vy), 3)

    def check_if_out_of_borders(self, screen_width, screen_height):
        if self.x > screen_width - self.radius:
            self.x = screen_width - self.radius
            # self.x = self.old_x
            self.vx *= -1 * self.bounce            
        
            
        elif self.x < self.radius:
            self.x = self.radius
            # self.x = self.old_x just in case
            self.vx *= -1 * self.bounce            
          
            

        if self.y > screen_height - self.radius:
            self.y = screen_height - self.radius
            # self.y = self.old_y just in case
            self.vy *= -1 * self.bounce            
           
            
        elif self.y < self.radius:
            self.y = self.radius
            # self.y = self.old_y just in case
            self.vy *= -1 * self.bounce

    def highlight_ends(self, surf):
        pygame.draw.circle(surf, (255, 0, 255), (self.x + self.radius, self.y), 1)
        pygame.draw.circle(surf, (255, 0, 255), (self.x - self.radius, self.y), 1)

    def collide(self, objects):
        for obj in objects:
            if self.name == objects[obj].name:
                continue
            else:
                #check if collide on both axis
                if self.x + self.radius >= objects[obj].x - objects[obj].radius and self.x - self.radius <= objects[obj].x + objects[obj].radius:
                    if self.y + self.radius >= objects[obj].y - objects[obj].radius and self.y - self.radius <= objects[obj].y + objects[obj].radius:
                        print("collision")
                        #gdy wektory są zwrócone w tą samą stronę                       
                        
                        self.x = self.old_x                        
                        self.vx *= self.bounce
                        objects[obj].vx += self.vx
                        
                                
           
            

mouse_pos = None
ball_clicked = False
running = True

balls = {}

ball1 = Ball(random.randint(10, 400), random.randint(10, 400), random.randint(0, 100), random.randint(0, 100), 0.98, 0.9, 10, "ball1", gravity=4, color=(random.randint(1,254), random.randint(1,254), random.randint(1,254)))
# ball1 = Ball(200, 200, 0, 0, 1, 1, 10, "ball1", gravity=0)
balls[ball1.name] = ball1

ball2 = Ball(random.randint(10, 400), random.randint(10, 400), random.randint(0, 100), random.randint(0, 100), 0.98, 0.9, 10, "ball2", gravity=4, color=(random.randint(1,254),random.randint(1,254),random.randint(1,254)))
# ball2 = Ball(100, 100, 0, 0, 1, 1, 10, "ball2", gravity=0)
balls[ball2.name] = ball2

ball3 = Ball(random.randint(10, 400), random.randint(10, 400), random.randint(0, 100), random.randint(0, 100), 0.98, 0.9, 10, "ball3", gravity=4, color=(random.randint(1,254),random.randint(1,254),random.randint(1,254)))
# ball2 = Ball(100, 100, 0, 0, 1, 1, 10, "ball2", gravity=0)
balls[ball3.name] = ball3

ball4 = Ball(random.randint(10, 400), random.randint(10, 400), random.randint(0, 100), random.randint(0, 100), 0.98, 0.9, 10, "ball4", gravity=4, color=(random.randint(1,254),random.randint(1,254),random.randint(1,254)))
# ball2 = Ball(100, 100, 0, 0, 1, 1, 10, "ball2", gravity=0)
balls[ball4.name] = ball4



while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    
    mouse_pos = pygame.mouse.get_pos()
    mouse_click = pygame.mouse.get_pressed()
    # mouse_pos = pygame.mouse.get_pos()
    # ball_clicked = if_clicked_on_ball(mouse_pos, mouse_click, pointA, radius)
    screen.fill((0, 0, 0))
    
    for ball in balls:
        balls[ball].save_previous_position()   
        balls[ball].move()  
        balls[ball].update_v() 
        
        balls[ball].collide(balls)
    

        # print(ball.vx, ball.vy, ball.x, ball.y, ball.old_x, ball.old_y, ball.radius, ball.color, ball.friction, ball.bounce)


        balls[ball].check_if_out_of_borders(screen_width, screen_height)
        pygame.draw.circle(screen, balls[ball].color, (balls[ball].x, balls[ball].y), balls[ball].radius)
        balls[ball].highlight_ends(screen)
        balls[ball].collision_line(screen)

       
        
   # Flip the display
    pygame.display.flip()
    fpsClock.tick(FPS)

pygame.quit()



