from rectangle import Rectangle
from util import generate_angle
from numpy import pi , cos , sin

WINDOW_WIDTH = 800
WINDOW_LENGTH = 600
BALL_WIDTH = 20
BALL_HEIGHT = 20
BALL_VELOCITY = 10


class Ball(Rectangle):
    def __init__(self, width, length, velocity):
        self.width = width 
        self.length = length
        self.velocity = velocity
        self.spawn(1)

    def init_velocity(self ,direction ): 
        theta = generate_angle(min=pi/18 , max =pi/4 )
        self.velocity_x = self.velocity * cos(theta) * direction 
        self.velocity_y = self.velocity  * sin(theta)

    def init_position(self): 
        self.start_x =  WINDOW_WIDTH / 2 - BALL_WIDTH / 2
        self.start_y =  WINDOW_LENGTH / 2 - BALL_HEIGHT / 2

    def spawn(self , direction): 
        self.init_velocity(direction)
        self.init_position()


 