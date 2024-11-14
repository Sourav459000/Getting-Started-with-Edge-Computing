import Adafruit_DHT
import RPi.GPIO as GPIO
import time

# Set up the GPIO mode
GPIO.setmode(GPIO.BCM)

# Set the sensor type and the GPIO pin it’s connected to
DHT_SENSOR = Adafruit_DHT.DHT11
DHT_PIN = 14  # GPIO pin for DHT11 sensor (Pin 8 on Raspberry Pi)
BUZZER_PIN = 15  # GPIO pin for Buzzer (Pin 10 on Raspberry Pi)

# Set up the buzzer pin as an output
GPIO.setup(BUZZER_PIN, GPIO.OUT)

# Temperature threshold (in Celsius) for triggering the buzzer
TEMP_THRESHOLD = 30  # You can change this value based on your requirement
HUM_THRESHOLD = 60

try:
    while True:
        # Read humidity and temperature from the sensor
        humidity, temperature = Adafruit_DHT.read(DHT_SENSOR, DHT_PIN)

        if humidity is not None and temperature is not None:
            print(f"Temp: {temperature}°C  Humidity: {humidity}%")
            
            # Check if the temperature exceeds the threshold
            if temperature > TEMP_THRESHOLD or humidity > HUM_THRESHOLD:
                print("Temperature or Humidity exceeded threshold! Triggering buzzer...")
                GPIO.output(BUZZER_PIN, GPIO.HIGH)  # Turn on the buzzer
                time.sleep(1)  # Buzzer sound duration
                GPIO.output(BUZZER_PIN, GPIO.LOW)   # Turn off the buzzer
        else:
            print("Failed to retrieve data from the sensor")

        # Wait before repeating
        time.sleep(2)

except KeyboardInterrupt:
    print("Program stopped by user")

finally:
    GPIO.cleanup()  # Clean up GPIO pins

