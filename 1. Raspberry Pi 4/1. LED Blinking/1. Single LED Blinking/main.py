import RPi.GPIO as GPIO
import time

# Set up GPIO using BCM numbering
GPIO.setmode(GPIO.BCM)

# Set the GPIO pin number
led_pin = 18

# Set the pin as output
GPIO.setup(led_pin, GPIO.OUT)

try:
    while True:
        # Turn on the LED
        GPIO.output(led_pin, GPIO.HIGH)
        print("LED ON")
        # Wait for 1 second
        time.sleep(1)
        # Turn off the LED
        GPIO.output(led_pin, GPIO.LOW)
        print("LED OFF")
        # Wait for 1 second
        time.sleep(1)

except KeyboardInterrupt:
    # Clean up GPIO on keyboard interrupt
    GPIO.cleanup()