from sense_hat import SenseHat
import time

sense = SenseHat()

while True:
    # Get the current time
    current_time = time.strftime("%H%M%S", time.localtime())

    # Convert each digit of the time to binary and pad with zeros
    hour_1_binary = bin(int(current_time[0]))[2:].zfill(2)
    hour_2_binary = bin(int(current_time[1]))[2:].zfill(4)
    minute_1_binary = bin(int(current_time[2]))[2:].zfill(3)
    minute_2_binary = bin(int(current_time[3]))[2:].zfill(4)
    second_1_binary = bin(int(current_time[4]))[2:].zfill(3)
    second_2_binary = bin(int(current_time[5]))[2:].zfill(4)

    # Set the LEDs on the Sense HAT to display the binary time
    for i in range(2):
        # Set the color of the LED based on the binary value for the first hour digit
        if hour_1_binary[i] == "1":
            color = (255, 0, 0)  # Red for 1
        else:
            color = (0, 0, 0)  # Off for 0
        sense.set_pixel(2*i, 0, color)

    for i in range(4):
        # Set the color of the LED based on the binary value for the second hour digit
        if hour_2_binary[i] == "1":
            color = (255, 0, 0)  # Red for 1
        else:
            color = (0, 0, 0)  # Off for 0
        sense.set_pixel(2*i+2, 0, color)

        # Set the color of the LED based on the binary value for the first minute digit
        if minute_1_binary[i] == "1":
            color = (0, 255, 0)  # Green for 1
        else:
            color = (0, 0, 0)  # Off for 0
        sense.set_pixel(2*i, 1, color)

        # Set the color of the LED based on the binary value for the second minute digit
        if minute_2_binary[i] == "1":
            color = (0, 255, 0)  # Green for 1
        else:
            color = (0, 0, 0)  # Off for 0
        sense.set_pixel(2*i+2, 1, color)

        # Set the color of the LED based on the binary value for the first second digit
        if second_1_binary[i] == "1":
            color = (0, 0, 255)  # Blue for 1
        else:
            color = (0, 0, 0)  # Off for 0
        sense.set_pixel(2*i, 2, color)

        # Set the color of the LED based on the binary value for the second second digit
        if second_2_binary[i] == "1":
            color = (0, 0, 255)  # Blue for 1
        else:
            color = (0, 0, 0)  # Off for 0
        sense.set_pixel(2*i+1, 2, color)

    # Wait for 1 second before updating the display again
    time.sleep(1)