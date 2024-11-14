## **DHT11 Sensor with Blynk IoT**

This project demonstrates how to read temperature and humidity data from a **DHT11 sensor** and display it in the **Blynk IoT app** using virtual pins.

### **Requirements:**
- **Raspberry Pi 4 Model B** (or any Raspberry Pi model)
- **DHT11 sensor** (Temperature and Humidity sensor)
- **Blynk IoT App** (Installed on your smartphone)
- **Python 3.x** installed on the Raspberry Pi
- **Blynk Library for Python** installed
- **Adafruit_DHT Library** installed for reading DHT11 data

### **Setup:**

#### 1. **Hardware Connections:**
   - **VCC** pin of DHT11 to **5V** (Pin 2) on Raspberry Pi
   - **GND** pin of DHT11 to **Ground** (Pin 6) on Raspberry Pi
   - **DATA** pin of DHT11 to **GPIO 14 (Pin 8)** on Raspberry Pi

   **Note:** You may need to add a **pull-up resistor (10kΩ)** between the **DATA** pin and **5V** to stabilize the signal.

#### 2. **Install Dependencies:**

   First, make sure you have Python 3.x and the necessary libraries installed on your Raspberry Pi.

   - **Install Adafruit_DHT Library:**
     ```bash
     sudo pip3 install Adafruit_DHT
     ```

   - **Install Blynk Library for Python:**
     ```bash
     cd /home/pi
     git clone https://github.com/vshymanskyy/blynk-library-python
     ```

#### 3. **Create Blynk Project:**
   - Open the **Blynk IoT App** on your smartphone.
   - Create a new project and choose **Raspberry Pi** as the device.
   - Add two **Value Display** widgets in the Blynk app:
     - **V0**: To display temperature
     - **V1**: To display humidity
   - Obtain your **Blynk Auth Token** from the app (you’ll need this to connect the Raspberry Pi to the app).

### **Running the Code:**

1. Clone or download this repository onto your Raspberry Pi.
2. Replace the **Blynk Auth Token** in the code with your personal **Blynk Auth Token**.
3. Run the Python script:

   ```bash
   python3 main.py
   ```

   The script will read temperature and humidity data from the DHT11 sensor and send it to the Blynk app, where the data will be displayed in real-time.

### **Conclusion:**

This project allows you to monitor **temperature** and **humidity** from a **DHT11 sensor** using the **Blynk IoT app**. The values will be updated in real-time in the app as the Raspberry Pi reads data from the sensor. You can further extend this project by adding additional sensors or integrating alerts based on sensor readings.