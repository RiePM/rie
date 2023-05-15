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

def pushed_up(event):
    global cur_clock
    if event.action == ACTION_RELEASED:
        hat.clear()
        time.sleep(0.5)
        cur_clock = "6col24formClock"

def pushed_down(event):
    global cur_clock
    if event.action == ACTION_RELEASED:
        hat.clear()
        time.sleep(0.5)
        cur_clock = "6col12formClock"

def pushed_left(event):
    global cur_clock
    if event.action == ACTION_RELEASED:
        hat.clear()
        time.sleep(0.5)
        cur_clock = "3col12formClock"

def pushed_right(event):
    global cur_clock
    if event.action == ACTION_RELEASED:
        hat.clear()
        time.sleep(0.5)
        cur_clock = "3col24formClock"

def pushed_any(event):
    if event.action == ACTION_PRESSED:
        hat.clear()

hat.stick.direction_up = pushed_up
hat.stick.direction_down = pushed_down
hat.stick.direction_left = pushed_left
hat.stick.direction_right = pushed_right
hat.stick.direction_any = pushed_any
hat.clear()


while True:
    t = datetime.datetime.now()

    if cur_clock == "3col12formClock":
        hour = t.hour
        am_pm = "AM"
        if hour > 12:
            hour -= 12
            am_pm = "PM"
        display_binary(hour, 0, hour_color)
        display_binary(t.minute, 1, minute_color)
        display_binary(t.second, 2, second_color)


    #Sæt AM eller PM:
        if am_pm == 'AM':
        # A
            hat.set_pixel(7, 7, 0, 155, 155)
            hat.set_pixel(1, 7, 0, 155, 155)
            hat.set_pixel(2, 7, 0, 155, 155)
            hat.set_pixel(0, 6, 0, 155, 155)
            hat.set_pixel(1, 6, 0, 155, 155)
            hat.set_pixel(2, 6, 0, 155, 155)
            # hat.set_pixel(1, 5, 0, 155, 155)
            # hat.set_pixel(0, 5, 0, 155, 155)
            # M
            # hat.set_pixel(3, 3, 0, 155, 155)
            # hat.set_pixel(2, 3, 0, 155, 155)
            # hat.set_pixel(1, 3, 0, 155, 155)
            # hat.set_pixel(0, 3, 0, 155, 155)
            # hat.set_pixel(2, 2, 0, 155, 155)
            # hat.set_pixel(3, 1, 0, 155, 155)
            # hat.set_pixel(2, 1, 0, 155, 155)
            # hat.set_pixel(0, 1, 0, 155, 155)
            # hat.set_pixel(1, 1, 0, 155, 155)
        else:
            # P
            hat.set_pixel(7, 3, 0, 155, 155)
            hat.set_pixel(7, 2, 0, 155, 155)
            hat.set_pixel(7, 1, 0, 155, 155)
            hat.set_pixel(7, 0, 0, 155, 155)
            hat.set_pixel(6, 3, 0, 155, 155)
            hat.set_pixel(6, 1, 0, 155, 155)
            hat.set_pixel(5, 3, 0, 155, 155)
            hat.set_pixel(5, 2, 0, 155, 155)
            hat.set_pixel(5, 1, 0, 155, 155)
            # M
            hat.set_pixel(3, 3, 0, 155, 155)
            hat.set_pixel(3, 2, 0, 155, 155)
            hat.set_pixel(3, 1, 0, 155, 155)
            hat.set_pixel(3, 0, 0, 155, 155)
            hat.set_pixel(2, 2, 0, 155, 155)
            hat.set_pixel(1, 3, 0, 155, 155)
            hat.set_pixel(1, 2, 0, 155, 155)
            hat.set_pixel(1, 0, 0, 155, 155)
            hat.set_pixel(1, 1, 0, 155, 155)

   
        

        time.sleep(0.0001)


    if cur_clock == "3col24formClock":            
        display_binary(t.hour, 3, hour_color)
        display_binary(t.minute, 4, minute_color)
        display_binary(t.second, 5, second_color)
        time.sleep(0.0001)


    if cur_clock == "6col12formClock":
        hour = t.hour
        am_pm = "AM"
        #Sæt max værdi 12 på hour:   
        if hour > 12:
            hour -= 12
            am_pm = "PM"

        display_digit1(hour, 6, hour_color)
        display_digit2(hour, 5, hour_color)
        display_digit1(t.minute, 4, minute_color)
        display_digit2(t.minute, 3, minute_color)
        display_digit1(t.second, 2, second_color)
        display_digit2(t.second, 1, second_color)

        #Sæt AM eller PM:
        if am_pm == 'AM':
        # A
            hat.set_pixel(5, 7, 0, 155, 155)
            hat.set_pixel(6, 7, 0, 155, 155)
            hat.set_pixel(7, 7, 0, 155, 155)
            hat.set_pixel(4, 6, 0, 155, 155)
            hat.set_pixel(6, 6, 0, 155, 155)
            hat.set_pixel(5, 5, 0, 155, 155)
            hat.set_pixel(6, 5, 0, 155, 155)
            hat.set_pixel(7, 5, 0, 155, 155)
            # M
            hat.set_pixel(4, 3, 0, 155, 155)
            hat.set_pixel(5, 3, 0, 155, 155)
            hat.set_pixel(6, 3, 0, 155, 155)
            hat.set_pixel(7, 3, 0, 155, 155)
            hat.set_pixel(5, 2, 0, 155, 155)
            hat.set_pixel(4, 1, 0, 155, 155)
            hat.set_pixel(5, 1, 0, 155, 155)
            hat.set_pixel(6, 1, 0, 155, 155)
            hat.set_pixel(7, 1, 0, 155, 155)
        else:
            # P
            hat.set_pixel(4, 7, 0, 155, 155)
            hat.set_pixel(5, 7, 0, 155, 155)
            hat.set_pixel(6, 7, 0, 155, 155)
            hat.set_pixel(7, 7, 0, 155, 155)
            hat.set_pixel(4, 6, 0, 155, 155)
            hat.set_pixel(6, 6, 0, 155, 155)
            hat.set_pixel(4, 5, 0, 155, 155)
            hat.set_pixel(5, 5, 0, 155, 155)
            hat.set_pixel(6, 5, 0, 155, 155)
            # M
            hat.set_pixel(4, 3, 0, 155, 155)
            hat.set_pixel(5, 3, 0, 155, 155)
            hat.set_pixel(6, 3, 0, 155, 155)
            hat.set_pixel(7, 3, 0, 155, 155)
            hat.set_pixel(5, 2, 0, 155, 155)
            hat.set_pixel(4, 1, 0, 155, 155)
            hat.set_pixel(5, 1, 0, 155, 155)
            hat.set_pixel(6, 1, 0, 155, 155)
            hat.set_pixel(7, 1, 0, 155, 155)       
        time.sleep(0.0001)


    if cur_clock == "6col24formClock":
        display_digit1(t.hour, 6, hour_color)
        display_digit2(t.hour, 5, hour_color)
        display_digit1(t.minute, 4, minute_color)
        display_digit2(t.minute, 3, minute_color)
        display_digit1(t.second, 2, second_color)
        display_digit2(t.second, 1, second_color)
        time.sleep(0.0001)
    

