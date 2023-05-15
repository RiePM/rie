from sense_hat import SenseHat, ACTION_PRESSED, ACTION_HELD, ACTION_RELEASED
import time, datetime

hat = SenseHat()
hat.clear()

#Vis start tekst: Husk at ud-udkommentere:
#hat.show_message("Programmet starter")


day_color = (255, 0, 0)
hour_color = (0, 255, 0)
minute_color = (0, 0, 255)
second_color = (255, 0, 0)
off = (0, 0, 0)

#Sørg for at uret kører ved start:
cur_clock = "3col24formClock"

# Metode til at konvertere til binary
def display_binary(value, row, color):
    binary_str = "{0:08b}".format(value)
    for x in range(0, 8):
        if binary_str[x] == '1':
            hat.set_pixel(x, row, color[0], color[1], color[2])
        else:
            hat.set_pixel(x, row, off)

def pushed_up(event):
    global cur_clock
    if event.action == ACTION_RELEASED:
        cur_clock = "up"
        hat.clear()

def pushed_down(event):
    global cur_clock
    if event.action == ACTION_RELEASED:
        cur_clock = "down"
        hat.clear()

def pushed_left(event):
    global cur_clock
    if event.action == ACTION_RELEASED:
        cur_clock = "3col12formClock"
        hat.clear()

def pushed_right(event):
    global cur_clock
    if event.action == ACTION_RELEASED:
        cur_clock = "3col24formClock"
        hat.clear()


hat.stick.direction_up = pushed_up
hat.stick.direction_down = pushed_down
hat.stick.direction_left = pushed_left
hat.stick.direction_right = pushed_right

hat.clear()


while True:
    t = datetime.datetime.now()

    if cur_clock == "3col12formClock":
        hour = t.hour
        if hour > 12:
            hour -= 12
        display_binary(hour, 7, hour_color)
        display_binary(t.minute, 6, minute_color)
        display_binary(t.second, 5, second_color)
        time.sleep(0.0001)


    if cur_clock == "3col24formClock":            
        display_binary(t.hour, 3, hour_color)
        display_binary(t.minute, 4, minute_color)
        display_binary(t.second, 5, second_color)
        time.sleep(0.0001)



    

