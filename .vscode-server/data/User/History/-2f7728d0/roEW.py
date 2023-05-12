from sense_hat import SenseHat
import time, datetime

hat = SenseHat()

hour_color = (0, 255, 0)
minute_color = (0, 0, 255)
second_color = (255, 0, 0)
off = (0, 0, 0)

hat.clear()

def display_binary(value, row, color):
    binary_str = "{0:08b}".format(value)
    for x in range(0, 8):
        if binary_str[x] == '1':
            hat.set_pixel(x, row, color[0], color[1], color[2])
        else:
            hat.set_pixel(x, row, off)

while True:
    t = datetime.datetime.now()
    display_binary(t.hour, 3, hour_color)
    display_binary(t.minute, 4, minute_color)
    time.sleep(0.0001)