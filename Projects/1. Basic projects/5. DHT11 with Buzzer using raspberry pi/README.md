**Title:**  
DHT11 Sensor with Buzzer for Raspberry Pi (Temperature & Humidity Threshold)

**Requirements:**
- Raspberry Pi 4 Model B (or any Raspberry Pi model)
- DHT11 Sensor
- Buzzer
- GPIO Pins 14 and 15 (for DHT11 and Buzzer, respectively)
- Python 3.x installed
- Adafruit_DHT library installed (`pip install Adafruit_DHT`)
- RPi.GPIO library installed (`sudo apt-get install python-rpi.gpio python3-rpi.gpio`)

**Procedure:**
1. **Setup Hardware:**
   - Connect the **DHT11 sensor** to GPIO pin 14 (Pin 8) on the Raspberry Pi.
   - Connect the **Buzzer** to GPIO pin 15 (Pin 10) on the Raspberry Pi.
   - Ensure proper wiring for the **VCC** and **GND** pins of the DHT11 sensor.
   - Refer to the [Raspberry Pi GPIO Pinout Diagram](https://www.raspberrypi.com/documentation/computers/images/GPIO-Pinout-Diagram-2.png) for further reference.

2. **Install Required Libraries:**
   - Open the terminal on your Raspberry Pi.
   - Install the **Adafruit_DHT** library by running the following command:
     ```bash
     pip install Adafruit_DHT
     ```
   - Install the **RPi.GPIO** library by running:
     ```bash
     sudo apt-get install python-rpi.gpio python3-rpi.gpio
     ```

3. **Download the Code:**
   - Create a new Python file on your Raspberry Pi using your preferred text editor (e.g., Nano, Vim, Thonny).

4. **Run the Code:**
   - Save the Python file with a name like `main.py`.
   - Open the terminal and navigate to the directory where the Python file is located.
   - Run the Python script using the following command:
     ```bash
     python3 main.py
     ```
   - The script will continuously check the temperature and humidity. If the temperature exceeds 30°C or the humidity exceeds 60%, the buzzer will sound for 1 second.
   - Press `Ctrl + C` to stop the script.

**Conclusion:**
This README provides step-by-step instructions for setting up and running a Python script to monitor temperature and humidity using a DHT11 sensor on the Raspberry Pi. If either the temperature or humidity exceeds a threshold, a buzzer is triggered. By following these steps, you can create a simple monitoring system with a buzzer alert for specific environmental conditions.