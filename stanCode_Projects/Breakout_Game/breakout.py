"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

YOUR DESCRIPTION HERE
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 5  # 100 frames per second
NUM_LIVES = 3  # Number of attempts


def main():
    graphics = BreakoutGraphics()

    # Add the animation loop here!
    ball = graphics.ball
    window = graphics.window
    lives = NUM_LIVES
    while True:
        pause(FRAME_RATE)
        # to get the starting random velocity of the ball
        dx = graphics.get_vx()
        dy = graphics.get_vy()
        ball.move(dx, dy)
        obj_1 = window.get_object_at(ball.x, ball.y)
        obj_2 = window.get_object_at(ball.x, (ball.y + ball.height))
        obj_3 = window.get_object_at((ball.x + ball.width), ball.y)
        obj_4 = window.get_object_at((ball.x + ball.width), (ball.y + ball.height))
        # to make the ball bounce back while reaching the edge of window
        if ball.x <= 0 or ball.x > (window.width - ball.width):
            graphics.set_vx()
        if ball.y <= 0:
            graphics.set_vy()
        # if the ball touch the bottom of the window, the number of lives deducted 1
        # and the ball return to the middle of the window
        if ball.y >= (window.height - ball.height):
            graphics.reset_ball()
            lives -= 1
            # if the number of lives goes to 0, the game is over
            if lives == 0:
                graphics.game_over()
                break
        # if the ball touches the paddle, it bounces back
        if obj_1 is not None:
            if obj_1 == graphics.paddle:
                if dy > 0:
                    graphics.set_vy()
            # if the ball touches the brick, the brick is removed and the ball bounce back
            # if all bricks are removed, the user wins the game
            else:
                window.remove(obj_1)
                graphics.set_vy()
                if graphics.if_all_bricks_removed():
                    graphics.win()
                    break
        elif obj_2 is not None:
            if obj_2 == graphics.paddle:
                if dy > 0:
                    graphics.set_vy()
            else:
                window.remove(obj_2)
                graphics.set_vy()
                if graphics.if_all_bricks_removed():
                    graphics.win()
                    break
        elif obj_3 is not None:
            if obj_3 == graphics.paddle:
                if dy > 0:
                    graphics.set_vy()
            else:
                window.remove(obj_3)
                graphics.set_vy()
                if graphics.if_all_bricks_removed():
                    graphics.win()
                    break
        elif obj_4 is not None:
            if obj_4 == graphics.paddle:
                if dy > 0:
                    graphics.set_vy()
            else:
                window.remove(obj_4)
                graphics.set_vy()
                if graphics.if_all_bricks_removed():
                    graphics.win()
                    break


if __name__ == '__main__':
    main()
