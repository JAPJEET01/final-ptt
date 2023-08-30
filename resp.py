import RPi.GPIO as GPIO
import socket

GPIO.setmode(GPIO.BCM)
gpio_pin = 17  # Change this to the actual GPIO pin number you're using
GPIO.setup(gpio_pin, GPIO.OUT)

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(('0.0.0.0', 12356))  # Change the port if needed

while True:
    data, _ = server_socket.recvfrom(1024)
    if data == b'high':
        GPIO.output(gpio_pin, GPIO.HIGH)
    elif data == b'low':
        GPIO.output(gpio_pin, GPIO.LOW)
