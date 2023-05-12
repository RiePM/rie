from sense_hat import SenseHat
import time

sense = SenseHat()

while True:
    # Get the current time
    current_time = time.strftime("%H%M%S", time.localtime())

    # Convert each digit of the time to binary and pad with zeros
    hour_binary = bin(int(current_time[0:2]))[2:].zfill(4)
    minute_binary = bin(int(current_time[2:4]))[2:].zfill(4)
    second_binary = bin(int(current_time[4:6]))[2:].zfill(4)

    # Set the LEDs on the Sense HAT to display the binary time
    for i in range(4):
        # Set the color of the LED based on the binary value
        if hour_binary[i] == "1":
            color = (255, 0, 0)  # Red for 1
        else:
            color = (0, 0, 0)  # Off for 0
        sense.set_pixel(2*i+1, 0, color)

        if minute_binary[i] == "1":
            color = (0, 255, 0)  # Green for 1
        else:
            color = (0, 0, 0)  # Off for 0
        sense.set_pixel(2*i, 1, color)

        if second_binary[i] == "1":
            color = (0, 0, 255)  # Blue for 1
        else:
            color = (0, 0, 0)  # Off for 0
        sense.set_pixel(2*i+1, 2, color)

    # Wait for 1 second before updating the display again
    time.sleep(1)