import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# define your draw functions
def grass():
    arcade.draw_lrtb_rectangle_filled(0, SCREEN_WIDTH, SCREEN_HEIGHT / 3, 0, arcade.color.WHITE)

def bridge():
    arcade.draw_circle_outline(400, 175, 100, arcade.color.BROWN, 25)
    arcade.draw_circle_outline(400, 175, 95, arcade.color.BROWN, 25)
    arcade.draw_circle_outline(400, 175, 90, arcade.color.BROWN, 25)
    arcade.draw_arc_outline(400, 175, 125, 125, arcade.color.BROWN, 250, 360, 13, 145)
    arcade.draw_line(340, 240, 320, 270, arcade.color.BROWN, 5)
    arcade.draw_line(460, 240, 480, 270, arcade.color.BROWN, 5)
    arcade.draw_line(365, 260, 350, 290, arcade.color.BROWN, 5)
    arcade.draw_line(435, 260, 450, 290, arcade.color.BROWN, 5)
    arcade.draw_line(400, 275, 400, 300, arcade.color.BROWN, 5)

def river():
    arcade.draw_rectangle_filled(400, 160, 100, 80, arcade.color.BLUE)
    arcade.draw_arc_filled(450, 120, 100, 50, arcade.color.BLUE, 180, 360)
    arcade.draw_rectangle_filled(500, 100, 100, 60, arcade.color.BLUE)
    arcade.draw_arc_filled(550, 80, 100, 50, arcade.color.BLUE, 270, 540)
    arcade.draw_rectangle_filled(600, 40, 100, 80, arcade.color.BLUE)

def tree():
    arcade.draw_rectangle_filled(150, 150, 75, 75, arcade.color.BROWN)
    arcade.draw_triangle_filled(75, 160, 225, 160, 150, 250, arcade.color.DARK_GREEN)
    arcade.draw_triangle_filled(75, 210, 225, 210, 150, 300, arcade.color.DARK_GREEN)
    arcade.draw_triangle_filled(75, 260, 225, 260, 150, 350, arcade.color.DARK_GREEN)
    point_list = ((140, 345),
                  (130, 355),
                  (142, 355),
                  (150, 370),
                  (158, 355),
                  (170, 355),
                  (160, 345))
    arcade.draw_polygon_filled(point_list, arcade.color.YELLOW)
    point_list = ((160, 345),
                  (165, 330),
                  (150, 340),
                  (135, 330),
                  (140, 345))
    arcade.draw_polygon_filled(point_list, arcade.color.YELLOW)

def moon():
    arcade.draw_circle_filled(650, 450, 70, arcade.color.PASTEL_GRAY)
    arcade.draw_circle_filled(677, 490, 12, arcade.color.DIM_GRAY)
    arcade.draw_circle_filled(620, 460, 15, arcade.color.DIM_GRAY)
    arcade.draw_circle_filled(697, 419, 20, arcade.color.DIM_GRAY)
    arcade.draw_circle_filled(615, 405, 18, arcade.color.DIM_GRAY)
    arcade.draw_circle_outline(650, 450, 71, arcade.color.DARK_BLUE, 40)
    arcade.draw_circle_outline(650, 450, 77, arcade.color.DARK_BLUE, 40)

def snowman():
    arcade.draw_circle_filled(650, 200, 40, arcade.color.GHOST_WHITE)
    arcade.draw_circle_filled(650, 240, 33.3, arcade.color.GHOST_WHITE)
    arcade.draw_circle_filled(650, 280, 26.6, arcade.color.GHOST_WHITE)
    arcade.draw_circle_filled(640, 287, 3.3, arcade.color.BLACK)
    arcade.draw_circle_filled(660, 287, 3.3, arcade.color.BLACK)
    arcade.draw_triangle_filled(650, 284, 650, 276, 630, 280, arcade.color.ORANGE)

def snow():
    arcade.draw_circle_filled(x, y, 3, arcade.color.WHITE)

def on_draw(delta_time):
    global snow1, snow2, snow3, snow4, snow5, snow6, snow7, snow8, snow9, snow10, snow11,snow12, snow13, snow14, snow15, snow16, snow17, snow18, snow19, snow20

    arcade.start_render()


    bridge()
    grass()
    river()
    tree()
    moon()
    snowman()
    snow(snow1, snow11)
    snow(snow2, snow12)
    snow(snow3, snow13)
    snow(snow4, snow14)
    snow(snow5, snow15)
    snow(snow6, snow16)
    snow(snow7, snow17)
    snow(snow8, snow18)
    snow(snow9, snow19)
    snow(snow10, snow20)

    snow1 -= 1
    snow2 -= 1
    snow3 -= 1
    snow4 -= 1
    snow5 -= 1
    snow6 -= 1
    snow7 -= 1
    snow8 -= 1
    snow9 -= 1
    snow10 -= 1

    snow11 -= 2
    snow12 -= 2
    snow13 -= 2
    snow14 -= 2
    snow15 -= 2
    snow16 -= 2
    snow17 -= 2
    snow18 -= 2
    snow19 -= 2
    snow20 -= 2

snow1 = 100
snow2 = 150




def main():
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Drawing with Functions")
    arcade.set_background_color(arcade.color.DARK_BLUE)
    arcade.start_render()

   # call your draw functions
    bridge()
    grass()
    river()
    tree()
    moon()
    snowman()
    snow()

    # Finish and run
    arcade.finish_render()
    arcade.run()


# Call the main function to get the program started.
main()