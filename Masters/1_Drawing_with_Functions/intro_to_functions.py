import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# define your draw functions
def grass():
    arcade.draw_lrtb_rectangle_filled(0, SCREEN_WIDTH, SCREEN_HEIGHT / 3, 0, arcade.color.GREEN)

def bridge():
    arcade.draw_circle_outline(400, 175, 100, arcade.color.BROWN, 25)
    arcade.draw_circle_outline(400, 175, 95, arcade.color.BROWN, 25)
    arcade.draw_circle_outline(400, 175, 90, arcade.color.BROWN, 25)

def river():
    arcade.draw_rectangle_filled(400, 160, 100, 80, arcade.color.BLUE)
    arcade.draw_arc_filled(450, 120, 100, 50, arcade.color.BLUE, 180, 360)
    arcade.draw_rectangle_filled(500, 100, 100, 60, arcade.color.BLUE)

def main():
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Drawing with Functions")
    arcade.set_background_color(arcade.color.DARK_BLUE)
    arcade.start_render()

   # call your draw functions
    bridge()
    grass()
    river()

    # Finish and run
    arcade.finish_render()
    arcade.run()


# Call the main function to get the program started.
main()