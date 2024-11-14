import RPi.GPIO as GPIO
import time

# Set up GPIO using BCM numbering
GPIO.setmode(GPIO.BCM)

# Set the GPIO pin numbers for the LEDs
led_pin1 = 18
led_pin2 = 17

# Set the pins as output
GPIO.setup(led_pin1, GPIO.OUT)
GPIO.setup(led_pin2, GPIO.OUT)

try:
    while True:
        # Turn on the first LED
        GPIO.output(led_pin1, GPIO.HIGH)
        # Turn off the second LED
        GPIO.output(led_pin2, GPIO.LOW)
        # Wait for 1 second
        time.sleep(1)
        
        # Turn off the first LED
        GPIO.output(led_pin1, GPIO.LOW)
        # Turn on the second LED
        GPIO.output(led_pin2, GPIO.HIGH)
        # Wait for 1 second
        time.sleep(1)

except KeyboardInterrupt:
    # Clean up GPIO on keyboard interrupt
    GPIO.cleanup()

