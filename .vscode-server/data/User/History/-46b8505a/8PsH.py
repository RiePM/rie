from sense_hat import SenseHat
import time, datetime

hat = SenseHat()
hat.clear()

hour_color = (0, 255, 0)
minute_color = (0, 0, 255)
second_color = (255, 0, 0)
#hundrefths_color = (127, 127, 0)
off = (0, 0, 0)

def display_digit1(value, row, color):
    digit1 = value // 10
    binary_str_one = "{0:04b}".format(digit1)
    for x in range(0, 4):
        if binary_str_one[x] == '1':
            hat.set_pixel(x, row, color[0], color[1], color[2])
        else:
            hat.set_pixel(x, row, off)


def display_digit2(value, row, color):
    digit2 = value % 10
    binary_str_two = "{0:04b}".format(digit2)
    for x in range(0, 4):
        if binary_str_two[x] == '1':
            hat.set_pixel(x, row, color[0], color[1], color[2])
        else:
            hat.set_pixel(x, row, off)

while True:
    t = datetime.datetime.now()
    display_digit1(t.hour, 6, hour_color)
    display_digit2(t.hour, 5, hour_color)
    display_digit1(t.minute, 4, minute_color)
    display_digit2(t.minute, 3, minute_color)
    display_digit1(t.second, 2, second_color)
    display_digit2(t.second, 1, second_color)
    time.sleep(0.0001)