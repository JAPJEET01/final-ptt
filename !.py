import RPi.GPIO as GPIO
import time

# Set the GPIO mode to BCM numbering
GPIO.setmode(GPIO.BCM)

# Define the GPIO pin number
relay_pin = 17  # Change this to the actual GPIO pin number you're using

# Set up the GPIO pin as an output
GPIO.setup(relay_pin, GPIO.OUT)

try:
    while True:
        # Wait for user input
        action = input("Press 'on' to turn on the relay, 'off' to turn off, or 'exit' to quit: ")

        if action == 'on':
            GPIO.output(relay_pin, GPIO.HIGH)
            print("Relay turned on")

        elif action == 'off':
            GPIO.output(relay_pin, GPIO.LOW)
            print("Relay turned off")

        elif action == 'exit':
            break  # Exit the loop if the user wants to quit

except KeyboardInterrupt:
    pass  # Allow the script to be interrupted with Ctrl+C

finally:
    # Clean up GPIO settings on program exit
    GPIO.cleanup()
