
from math import sqrt, asin, acos
import pygame
import random



screen_width = 500
screen_height = 500



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
        #rewrite it to fit the physics collisions
        if self.x > screen_width - self.radius:
            self.x = screen_width - self.radius
            self.x = self.old_x
            self.vx *= -1 * self.bounce            
        
            
        elif self.x < self.radius:
            self.x = self.radius
            self.x = self.old_x
            self.vx *= -1 * self.bounce            
          
            

        if self.y > screen_height - self.radius:
            self.y = screen_height - self.radius
            self.y = self.old_y
            self.vy *= -1 * self.bounce            
           
            
        elif self.y < self.radius:
            self.y = self.radius
            self.y = self.old_y
            self.vy *= -1 * self.bounce

    def highlight_ends(self, surf):
        pygame.draw.circle(surf, (255, 0, 255), (self.x + self.radius, self.y), 1)
        pygame.draw.circle(surf, (255, 0, 255), (self.x - self.radius, self.y), 1)


    
    def collide(self, objects):
        
        #C:\Users\rylko\Documents\Simulations\Simulations\Ball_simulation\obliczanie prędkości obiektów.jpg
        for obj in objects:
            if self.name == objects[obj].name:
                continue
            else:
                #different collision algorythm 
                dist = sqrt((self.x - objects[obj].x)**2 + (self.y - objects[obj].y)**2)
                sum_of_radii = self.radius + objects[obj].radius

                if dist <= sum_of_radii:
                        print("collision")
                        print(self.vx, self.vy)
                        [print(objects[obj].vx, objects[obj].vy)]

                        # angle = asin()

                        #check only for X axis
                        self.x = self.old_x
                        # objects[obj].x = objects[obj].old_x
                        # old_vx = self.vx
                        # old_vy = self.vy
                        # old_obj_vx = objects[obj].vx
                        # old_obj_vy = objects[obj].vy

                        distance = sqrt((self.x - objects[obj].x)**2 + (self.y - objects[obj].y)**2)

                        #normal
                        normalized_x = (objects[obj].x - self.x) / distance
                        normalized_y = (objects[obj].y - self.y) / distance 

                        #tangent
                        tan_x = -normalized_y
                        tan_y = normalized_x

                        #dot product tangent
                        dpTan1 = self.vx * tan_x + self.vy * tan_y
                        dpTan2 = objects[obj].vx * tan_x + objects[obj].vy * tan_y

                        #dot product normal
                        dpNorm1 = self.vx * normalized_x + self.vy * normalized_y
                        dpNorm2 = objects[obj].vx * normalized_x + objects[obj].vy * normalized_y

                        #conservation of momentum
                        momentum1 = (dpNorm1 * (1 - 1) + 2 * 1 * dpNorm2) / (1 + 1)
                        momentum2 = (dpNorm2 * (1 - 1) + 2 * 1 * dpNorm1) / (1 + 1)

                        #update ball velocities
                        self.vx = tan_x * dpTan1 + normalized_x * momentum1
                        self.vy = tan_y * dpTan1 + normalized_y * momentum1
                        objects[obj].vx = tan_x * dpTan2 + normalized_x * momentum2
                        objects[obj].vy = tan_y * dpTan2 + normalized_y * momentum2
                            
                                
           
            

mouse_pos = None
ball_clicked = False
running = True

balls = {}

#random forces on X and Y axis
ball1 = Ball(random.randint(10, 400), random.randint(10, 400), random.randint(10, 40), random.randint(10, 40), 0.98, 0.9, 30, "ball1", gravity=0, color=(random.randint(1,254), random.randint(1,254), random.randint(1,254)))

balls[ball1.name] = ball1

ball2 = Ball(random.randint(10, 400), random.randint(10, 400), random.randint(10, 40), random.randint(10, 40), 0.98, 0.9, 30, "ball2", gravity=0, color=(random.randint(1,254),random.randint(1,254),random.randint(1,254)))

balls[ball2.name] = ball2


#only on X axis
# ball3 = Ball(100, 320, random.randint(10, 40), 0, 0.98, 0.9, 30, "ball3", gravity=0, color=(random.randint(1,254),random.randint(1,254),random.randint(1,254)))

# balls[ball3.name] = ball3

# ball4 = Ball(300, 300, 0, 0, 0.98, 0.9, 30, "ball4", gravity=0, color=(random.randint(1,254),random.randint(1,254),random.randint(1,254)))

# balls[ball4.name] = ball4

#only on Y axis
# ball5 = Ball(161, 30, 0, 30, 0.98, 0.9, 30, "ball5", gravity=5, color=(random.randint(1,254),random.randint(1,254),random.randint(1,254)))
# balls[ball5.name] = ball5

# ball6 = Ball(160, 600, 0, 0, 0.98, 0.9, 30, "ball6", gravity=5, color=(random.randint(1,254),random.randint(1,254),random.randint(1,254)))
# balls[ball6.name] = ball6



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



