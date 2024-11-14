**Title:**  
- DHT11 Sensor with Raspberry Pi

**Requirements:**
- Raspberry Pi 4 Model B (or any Raspberry Pi model)
- DHT11 Sensor
- Python 3.x installed
- Adafruit_DHT library installed (`pip install Adafruit_DHT`)

**Procedure:**

1. **Setup Hardware:**
   - Connect the **VCC** pin of the DHT11 sensor to **5V** on the Raspberry Pi.
   - Connect the **GND** pin of the DHT11 sensor to **Ground** on the Raspberry Pi.
   - Connect the **SIG** pin of the DHT11 sensor to **GPIO 14 (Pin 8)** on the Raspberry Pi.
   - Refer to the [Raspberry Pi GPIO Pinout Diagram](https://www.raspberrypi.com/documentation/computers/images/GPIO-Pinout-Diagram-2.png) for further reference.

2. **Install Dependencies:**
   - Open the terminal on your Raspberry Pi.
   - Install the **Adafruit_DHT** library by running the following command:
     ```bash
     pip install Adafruit_DHT
     ```

3. **Download the Code:**
   - Clone or download this repository.
   - Create a new Python file on your Raspberry Pi using your preferred text editor (e.g., Nano, Vim, Thonny).

4. **Run the Code:**
   - Save the Python file with a name like `main.py`.
   - Open the terminal and navigate to the directory where the Python file is located.
   - Run the Python script using the following command:
     ```bash
     python3 main.py
     ```
   - The script will continuously display the temperature (°C) and humidity (%) every 2 seconds.
   - Press `Ctrl + C` to stop the script.

**Conclusion:**
This README provides step-by-step instructions for setting up and running a Python script to read temperature and humidity data from a DHT11 sensor on the Raspberry Pi. Following these instructions, you can monitor environmental conditions using your Raspberry Pi.