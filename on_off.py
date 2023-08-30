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
        # Turn on the relay
        GPIO.output(relay_pin, GPIO.HIGH)
        print("Relay turned on")
        time.sleep(2)  # Wait for 2 seconds

        # Turn off the relay
        GPIO.output(relay_pin, GPIO.LOW)
        print("Relay turned off")
        time.sleep(2)  # Wait for 2 seconds

except KeyboardInterrupt:
    # Clean up GPIO settings on program exit
    GPIO.cleanup()
