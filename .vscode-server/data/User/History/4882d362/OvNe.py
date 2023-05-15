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
