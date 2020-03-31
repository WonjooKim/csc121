import arcade

screen_wid = 1000
screen_hei = 600


def draw_bird(x, y):
    arcade.draw_arc_outline(x, y, 20, 20, (34, 48, 254), 0, 90)
    arcade.draw_arc_outline(x+40, y, 20, 20, (34, 48, 254), 90, 180)

def draw_church(x, y):
    arcade.draw_lrtb_rectangle_filled(x, x+200, y+200, y, (171, 105, 53))
    arcade.draw_triangle_filled(x+100, y+350, x, y+200, x+200, y+200, (255, 0, 0))
    arcade.draw_lrtb_rectangle_filled(x+95, x+105, y+400, y+340, (197, 178, 141))
    arcade.draw_lrtb_rectangle_filled(x+80, x+120, y+380, y+375, (197, 178, 141))
    arcade.draw_lrtb_rectangle_filled(x+50, x+150, y+150, y, (38, 254, 34))
    arcade.draw_line(x+100, y, x+100, y+150, arcade.color.WOOD_BROWN, 2)

def draw_church_window(x, y):
    arcade.draw_lrtb_rectangle_filled(x+150, x+250, y+380, y+360, (230, 244, 0))
    arcade.draw_line(x+200, y+360, x+200, y+380, arcade.color.WOOD_BROWN, 1.5)
    arcade.draw_line(x+150, y+370, x+250, y+370, arcade.color.WOOD_BROWN, 1.5)
    arcade.draw_text("Belhaven Church", x+150, y+390, arcade.color.BLACK, 11.5)

def draw_tree(x, y):
    arcade.draw_lrtb_rectangle_filled(x, x+40, y+120, y, arcade.color.DARK_BROWN)
    arcade.draw_circle_filled(x-10, y+140, 60, (81, 132, 86))
    arcade.draw_circle_filled(x+20, y+200, 60, (81, 132, 86))
    arcade.draw_circle_filled(x+50, y+140, 60, (81, 132, 86))

def draw_apple(x, y):
    arcade.draw_circle_filled(x-15, y+150, 10, (247, 15, 0))
    arcade.draw_line(x-17, y+155, x-10, y+164,(174, 124, 33), 4)
    arcade.draw_circle_filled(x+40, y+190, 10, (247, 15, 0))
    arcade.draw_line(x+38, y+195, x+45, y+204,(174, 124, 33), 4)

def draw_flower(x, y):
    arcade.draw_line(x, y, x, y+20, (54, 192, 67), 1.5)
    arcade.draw_circle_filled(x, y+25, 5, (241, 248, 95))


def on_draw(delta_time):
    arcade.start_render()

    # ground is 1/3 and it's color is green
    arcade.draw_lrtb_rectangle_filled(0, screen_wid, 150, 0, (80, 114, 61))
    arcade.draw_arc_filled(300, 150, 600, 100, (80, 114, 61), 0, 180)

    #draw birds

    draw_bird(on_draw.bird_x1, 560)
    draw_bird(on_draw.bird_x2, 450)
    draw_bird(on_draw.bird_x3, 500)
    on_draw.bird_x1 -= 10
    on_draw.bird_x2 += 20
    on_draw.bird_x3 -= 25

    #draw church
    draw_church(100, 100)
    draw_church_window(0, -30)

    draw_tree(600, 150)
    draw_tree(850, 60)

    draw_apple(600, on_draw.apple_y1)
    draw_apple(850, on_draw.apple_y2)

    if on_draw.apple_y1 == -100:
        on_draw.apple_y1 == -100
    else :
        on_draw.apple_y1 -= 25

    if on_draw.apple_y2 == -70:
        on_draw.apple_y2 == -70
    else :
        on_draw.apple_y2 -= 5

    draw_flower(550, 100)
    draw_flower(590, 100)
    draw_flower(580, 80)
    draw_flower(500, 90)
    draw_flower(530, 120)
    draw_flower(540, 95)
    draw_flower(560, 125)
    draw_flower(520, 90)
    draw_flower(553, 80)


on_draw.bird_x1 = 50 
on_draw.bird_x2 = 450
on_draw.bird_x3 = 570
on_draw.apple_y1 = 150
on_draw.apple_y2 = 60


def main():
    arcade.open_window(screen_wid, screen_hei, "lab3_example")
    # Background color is light blue
    arcade.set_background_color((102, 227, 205))

    arcade.schedule(on_draw, 1/250)
    arcade.run()

main()


