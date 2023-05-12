from sense_hat import SenseHat, ACTION_PRESSED, ACTION_HELD, ACTION_RELEASED
import time, datetime

hat = SenseHat()

green = (0, 255, 0)
blue = (0, 0, 255)
red = (255, 0, 0)
yellow = (0,255,255)
white = (255, 255, 255)
black = (0,0,0)

cur_color = black

def pushed_up(event):
    global cur_color
    if event.action == ACTION_RELEASED:
        cur_color = green

def pushed_down(event):
    global cur_color
    if event.action == ACTION_RELEASED:
        cur_color = red

def pushed_left(event):
    global cur_color
    if event.action == ACTION_RELEASED:
        cur_color = yellow

def pushed_right(event):
    global cur_color
    if event.action == ACTION_RELEASED:
        cur_color = blue

def pushed_middle(event):
    global cur_color
    if event.action == ACTION_RELEASED:
        cur_color = white

def pushed_any(event):
    global cur_color
    if event.action == ACTION_HELD:
        cur_color = black


hat.stick.direction_up = pushed_up
hat.stick.direction_down = pushed_down
hat.stick.direction_left = pushed_left
hat.stick.direction_right = pushed_right
hat.stick.direction_middle = pushed_middle

hat.stick.direction_any = pushed_any

hat.clear()

while True:
    hat.reset(cur_color)