import Adafruit_DHT
import time

# Set the sensor type and the GPIO pin it's connected to
DHT_SENSOR = Adafruit_DHT.DHT11
DHT_PIN = 14  # Change to GPIO 14 (Pin 8 on Raspberry Pi)

try:
    while True:
        # Read humidity and temperature
        humidity, temperature = Adafruit_DHT.read(DHT_SENSOR, DHT_PIN)

        if humidity is not None and temperature is not None:
            print(f"Temp: {temperature}°C  Humidity: {humidity}%")
        else:
            print("Failed to retrieve data from the sensor")

        # Wait before repeating
        time.sleep(2)

except KeyboardInterrupt:
    print("Program stopped by user")
