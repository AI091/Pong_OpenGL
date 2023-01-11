from rectangle import Rectangle
from util import generate_angle
from numpy import pi, cos, sin
from config import *


class Ball(Rectangle):
    def __init__(self):
        self.width = BALL_WIDTH
        self.length = BALL_HEIGHT
        self.velocity = BALL_VELOCITY
        self.spawn(1)

    def init_velocity(self, direction):
        theta = generate_angle(min=pi / 18, max=pi / 4)
        self.velocity_x = self.velocity * cos(theta) * direction
        self.velocity_y = self.velocity * sin(theta)

    def init_position(self):
        self.start_x = WINDOW_WIDTH / 2 - BALL_WIDTH / 2
        self.start_y = WINDOW_LENGTH / 2 - BALL_HEIGHT / 2

    def spawn(self, direction):
        self.init_velocity(direction)
        self.init_position()

    # def update(self):
    #     self.start_x = self.start_x + self.velocity_x
    #     self.start_y = self.start_y + self.velocity_y
