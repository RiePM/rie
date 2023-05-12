from sense_hat import SenseHat
import time, datetime

hat = SenseHat()
hat.clear()

hour_color = (0, 255, 0)
minute_color = (0, 0, 255)
second_color = (255, 0, 0)
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
    hour = t.hour
    am_pm = "AM"
    
    if hour > 12:
        hour -= 12
        am_pm = "PM"

    display_digit1(hour, 6, hour_color)
    display_digit2(hour, 5, hour_color)
    display_digit1(t.minute, 4, minute_color)
    display_digit2(t.minute, 3, minute_color)
    display_digit1(t.second, 2, second_color)
    display_digit2(t.second, 1, second_color)

    # Display AM/PM after the hour
    for x in range(0, 2):
        if am_pm[x] == 'A':
            hat.set_pixel(x + 2, 7, 0, 255, 0)
        else:
            hat.set_pixel(x + 2, 7, 255, 0, 0)




    time.sleep(0.0001)