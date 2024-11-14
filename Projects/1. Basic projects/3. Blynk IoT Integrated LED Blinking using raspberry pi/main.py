import time
import RPi.GPIO as GPIO
import BlynkLib

# Set up GPIO
LED_PIN = 15  # GPIO pin for LED (Pin 15 on Raspberry Pi)

# Disable GPIO warnings
GPIO.setwarnings(False)

# Blynk Authentication Token (Replace with your own)
BLYNK_AUTH_TOKEN = 'jShSSQ5vq3-kCoIhr2xDMBdlcVMFaXul'

# Set up Blynk connection
blynk = BlynkLib.Blynk(BLYNK_AUTH_TOKEN)

# Blynk Virtual Pin for Push Button
VIRTUAL_PIN_BUTTON = 0  # Virtual Pin V0 for Push Button

# Set up the GPIO mode and LED pin
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)

# Function to control LED based on button state
@blynk.on(VIRTUAL_PIN_BUTTON)
def button_pressed(value):
    if value == '1':  # Button pressed
        print("Button pressed, turning on LED")
        GPIO.output(LED_PIN, GPIO.HIGH)  # Turn on LED
    else:  # Button released
        print("Button released, turning off LED")
        GPIO.output(LED_PIN, GPIO.LOW)   # Turn off LED

# Run Blynk's event loop
try:
    while True:
        blynk.run()  # Keeps the connection to Blynk alive
        time.sleep(0.1)  # Sleep to avoid high CPU usage
except KeyboardInterrupt:
    print("Program stopped by user")
finally:
    GPIO.cleanup()  # Clean up GPIO on exit
