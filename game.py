from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

from ball import Ball

from util import line_collesion


WINDOW_WIDTH = 800
WINDOW_LENGTH = 600
ACCELARATION = 0.001

class Game:
    def __init__(
        self,
        right_paddle,
        left_paddle,
        ball,
        window_length=WINDOW_LENGTH,
        window_width=WINDOW_WIDTH,
    ):
        self.right_paddle = right_paddle
        self.left_paddle = left_paddle
        self.ball = ball
        self.player_one_score = 0
        self.player_two_score = 0
        self.window_length = window_length
        self.window_width = window_width

    def collides_with_roof(self):
        if (
            self.ball.start_y + self.ball.length >= self.window_length
            or self.ball.start_y < 0
        ):
            return True
        return False

    def collides_right_paddle(self):
        if line_collesion(
            self.ball.start_x +  self.ball.velocity_x,
            self.ball.start_x + self.ball.width +  self.ball.velocity_x,
            self.right_paddle.start_x,
            self.right_paddle.start_x + self.right_paddle.width,
        ) and line_collesion(
            self.ball.start_y + self.ball.velocity_y,
            self.ball.start_y + self.ball.length + self.ball.velocity_y,
            self.right_paddle.start_y,
            self.right_paddle.start_y + self.right_paddle.length,
        ):
            return True
        return False

    def collides_left_paddle(self):
        if line_collesion(
            self.ball.start_x + self.ball.velocity_x,
            self.ball.start_x + self.ball.width+ self.ball.velocity_x,
            self.left_paddle.start_x,
            self.left_paddle.start_x + self.left_paddle.width,
        ) and line_collesion(
            self.ball.start_y + self.ball.velocity_y,
            self.ball.start_y + self.ball.length + self.ball.velocity_y,
            self.left_paddle.start_y,
            self.left_paddle.start_y + self.left_paddle.length,
        ):
            return True
        return False

    def collides_right_screen(self):
        if self.ball.start_x + self.ball.width >= self.window_width:
            return True
        return False

    def collides_left_screen(self):
        if self.ball.start_x < 0:
            return True
        return False

    def render(self): 
        self.right_paddle.draw()
        self.left_paddle.draw()
        self.ball.draw()

    def update_ball(self): 
        self.ball.start_x += self.ball.velocity_x
        self.ball.start_y += self.ball.velocity_y 
        self.ball.velocity_x += (ACCELARATION) if self.ball.velocity_x > 0 else -ACCELARATION  #speedup the game as time goes on


    def play(self):

        self.render()

        if self.collides_with_roof():
            self.ball.velocity_y = -1 * self.ball.velocity_y

        if self.collides_right_paddle():
            self.ball.velocity_x = -1 * self.ball.velocity_x

        if self.collides_left_paddle():
            self.ball.velocity_x = -1 * self.ball.velocity_x

        elif self.collides_right_screen():
            self.player_one_score += 1 
            self.ball.spawn(1)
            print(self)

        
        elif  self.collides_left_screen():
            self.player_two_score += 1 
            self.ball.spawn(-1)
            print(self)
        
        self.update_ball()


    def __str__(self) -> str:
        return f"{self.player_one_score} | {self.player_two_score}"

