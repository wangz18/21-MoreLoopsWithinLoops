"""
This project demonstrates NESTED LOOPS (i.e., loops within loops)
in the context of TWO-DIMENSIONAL GRAPHICS.

Authors: David Mutchler, Valerie Galluzzi, Mark Hays, Amanda Stouder,
         their colleagues and Zhiyu Wang.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

import rosegraphics as rg


def main():
    """ Calls the other functions to test them. """
    run_test_draw_upside_down_wall()


def run_test_draw_upside_down_wall():
    """ Tests the    draw_upside_down_wall    function. """
    # Tests 1 and 2 are ALREADY DONE (here).
    window = rg.RoseWindow(550, 300, 'Upside-down wall, Tests 1 and 2')

    rectangle = rg.Rectangle(rg.Point(125, 230), rg.Point(155, 250))
    draw_upside_down_wall(rectangle, 8, window)

    rectangle = rg.Rectangle(rg.Point(375, 175), rg.Point(425, 225))
    draw_upside_down_wall(rectangle, 4, window)

    window.close_on_mouse_click()


def draw_upside_down_wall(rectangle, n, window):
    """
    See   MoreWalls.pdf   in this project for pictures that may
    help you better understand the following specification:

    Draws an "upside-down wall" on the given window, where:
      -- The BOTTOM of the wall is a single "brick"
            that is the given rg.Rectangle.
      -- There are n rows in the wall.
      -- Each row is a row of "bricks" that are the same size
            as the given rg.Rectangle.
      -- Each row has one more brick than the row below it.
      -- Each row is centered on the bottom row.

    Preconditions:
      :type rectangle: rg.Rectangle
      :type n: int
      :type window: rg.RoseWindow
    and n is nonnegative.
    """
    # ------------------------------------------------------------------
    # TODO: 2. Implement and test this function.
    #     Some tests are already written for you (above).
    # ------------------------------------------------------------------
    original_corner1_x = rectangle.corner_1.x
    original_corner2_x = rectangle.corner_2.x
    original_corner1_y = rectangle.corner_1.y
    original_corner2_y = rectangle.corner_2.y
    dx = original_corner1_x - original_corner2_x
    dy = original_corner2_y - original_corner1_y

    x1 = original_corner1_x
    x2 = original_corner2_x
    y1 = original_corner1_y
    y2 = original_corner2_y

    Corner1 = rg.Point(x1, y1)
    Corner2 = rg.Point(x2, y2)

    for k in range(1,n+1):
        for j in range(k):
            new_rectangle = rg.Rectangle(Corner1,Corner2)
            new_rectangle.attach_to(window)
            window.render(.1)
            Corner1.x = Corner1.x + dx
            Corner2.x = Corner2.x + dx
        Corner1.x = original_corner1_x - (dx / 2)*k
        Corner2.x = original_corner2_x - (dx / 2)*k
        Corner1.y = Corner1.y - dy
        Corner2.y = Corner2.y - dy


# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------
main()
