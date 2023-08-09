"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao.

YOUR DESCRIPTION HERE
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5  # Space between bricks (in pixels). This space is used for horizontal and vertical spacing
BRICK_WIDTH = 40  # Width of a brick (in pixels)
BRICK_HEIGHT = 15  # Height of a brick (in pixels)
BRICK_ROWS = 10  # Number of rows of bricks
BRICK_COLS = 10  # Number of columns of bricks
BRICK_OFFSET = 50  # Vertical offset of the topmost brick from the window top (in pixels)
BALL_RADIUS = 10  # Radius of the ball (in pixels)
PADDLE_WIDTH = 75  # Width of the paddle (in pixels)
PADDLE_HEIGHT = 15  # Height of the paddle (in pixels)
PADDLE_OFFSET = 50  # Vertical offset of the paddle from the window bottom (in pixels)
INITIAL_Y_SPEED = 7  # Initial vertical speed for the ball
MAX_X_SPEED = 5  # Maximum initial horizontal speed for the ball


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, title='Breakout'):

        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)

        # Create a paddle
        self.paddle = GRect(paddle_width, paddle_height)
        self.paddle.filled = True
        self.window.add(self.paddle, (window_width - paddle_width) / 2, window_height - paddle_offset)

        # Center a filled ball in the graphical window
        self.ball = GOval(ball_radius * 2, ball_radius * 2)
        self.ball.filled = True
        self.window.add(self.ball, window_width / 2 - ball_radius, window_height / 2 - ball_radius)

        # Default initial velocity for the ball
        self.__dx = 0
        self.__dy = 0

        # Initialize our mouse
        self.if_start = False
        onmouseclicked(self.set_ball_v)
        onmousemoved(self.paddle_move)

        # Draw
        for i in range(brick_rows):
            for j in range(brick_cols):
                if i == 0 or i == 1:
                    color = 'red'
                elif i == 2 or i == 3:
                    color = 'orange'
                elif i == 4 or i == 5:
                    color = 'yellow'
                elif i == 6 or i == 7:
                    color = 'green'
                else:
                    color = 'blue'
                self.brick = GRect(brick_width, brick_height)
                self.brick.filled = True
                self.brick.fill_color = color
                self.brick.color = color
                self.window.add(self.brick, j * (brick_width + brick_spacing),
                                brick_offset + i * (brick_height + brick_spacing))
        self.num_bricks = brick_rows * brick_cols

    # makes the paddle moves to where the mouse is
    def paddle_move(self, mouse):
        if mouse.x <= self.paddle.width / 2:
            self.paddle.x = 0
        elif mouse.x >= self.window.width - self.paddle.width / 2:
            self.paddle.x = self.window.width - self.paddle.width
        else:
            self.paddle.x = mouse.x - self.paddle.width / 2

    # to set the velocity of the ball after the mouse clicks
    def set_ball_v(self, event):
        if not self.if_start:
            self.__dx = random.randint(1, MAX_X_SPEED)
            self.__dy = INITIAL_Y_SPEED
            if random.random() > 0.5:
                self.__dx = -self.__dx
        self.if_start = True

    # reset the ball to the very beginning position
    def reset_ball(self):
        self.window.add(self.ball, self.window.width / 2 - self.ball.width, self.window.height / 2 - self.ball.height)
        self.if_start = False
        self.__dx = 0
        self.__dy = 0

    # the getter function for the user to get the velocity of x
    def get_vx(self):
        return self.__dx

    # the getter function for the user to get the velocity of y
    def get_vy(self):
        return self.__dy

    # to set the dx to the opposite way
    def set_vx(self):
        self.__dx = -self.__dx
        return self.__dx

    # to set the dy to the opposite way
    def set_vy(self):
        self.__dy = -self.__dy
        return self.__dy

    # if the user loses all lives, the game is over
    def game_over(self):
        self.window.clear()
        background = GRect(self.window.width, self.window.height)
        background.filled = True
        label = GLabel('Game over!')
        label.font = '-60'
        label.color = 'white'
        self.window.add(background)
        self.window.add(label, x=(self.window.width-label.width)/2, y=self.window.height/2)

    # to check if all bricks are removed
    def if_all_bricks_removed(self):
        self.num_bricks -= 1
        if self.num_bricks == 0:
            return True
        else:
            return False

    # if all bricks are removed, the user wins the game
    def win(self):
        self.window.clear()
        label = GLabel('Congratulations! You win!!!')
        label.font = '-10'
        label.color = 'red'
        self.window.add(label, x=(self.window.width-label.width)/2, y=self.window.height/2)







