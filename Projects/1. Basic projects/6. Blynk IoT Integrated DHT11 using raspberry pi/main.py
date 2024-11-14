import Adafruit_DHT
import BlynkLib
import time

# Initialize Blynk with your Auth Token
BLYNK_AUTH_TOKEN = 'Your_Blynk_Auth_Token'
blynk = BlynkLib.Blynk(BLYNK_AUTH_TOKEN)

# Set up the DHT11 sensor
DHT_SENSOR = Adafruit_DHT.DHT11
DHT_PIN = 14  # GPIO pin for DHT11 sensor (Pin 8 on Raspberry Pi)

# Function to send data to Blynk
def send_data_to_blynk():
    # Read temperature and humidity from DHT11 sensor
    humidity, temperature = Adafruit_DHT.read(DHT_SENSOR, DHT_PIN)
    
    if humidity is not None and temperature is not None:
        # Send temperature to Virtual Pin V0
        blynk.virtual_write(0, temperature)
        
        # Send humidity to Virtual Pin V1
        blynk.virtual_write(1, humidity)
        
        print(f"Temp: {temperature}°C  Humidity: {humidity}%")
    else:
        print("Failed to retrieve data from the sensor")

# Main loop
while True:
    send_data_to_blynk()
    
    # Run Blynk virtual writes in the background
    blynk.run()
    
    # Wait for 2 seconds before reading data again
    time.sleep(2)
