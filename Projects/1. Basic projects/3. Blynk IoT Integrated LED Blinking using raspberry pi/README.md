## **LED Blinking with Blynk IoT**

This project demonstrates how to control an LED connected to a Raspberry Pi using a **virtual push button** in the **Blynk IoT app**.

### **Requirements:**
- **Raspberry Pi 4 Model B** (or any Raspberry Pi model)
- **LED** connected to a GPIO pin (for example, GPIO 15)
- **Blynk IoT App** (Installed on your smartphone)
- **Python 3.x** installed on the Raspberry Pi
- **Blynk Library for Python** installed

### **Setup:**

#### 1. **Hardware Connections:**
   - **Anode** of the LED to **GPIO 15 (Pin 10)** on the Raspberry Pi
   - **Cathode** of the LED to **Ground (GND)** on the Raspberry Pi

   **Note:** Use a **220Ω resistor** in series with the LED to limit the current and prevent damage to the Raspberry Pi.

#### 2. **Install Dependencies:**

   First, make sure you have Python 3.x and the necessary libraries installed on your Raspberry Pi.

   - **Install Blynk Library for Python:**
     ```bash
     cd /home/pi
     git clone https://github.com/vshymanskyy/blynk-library-python
     ```

   - **Install RPi.GPIO Library:**
     ```bash
     sudo pip3 install RPi.GPIO
     ```

#### 3. **Create Blynk Project:**
   - Open the **Blynk IoT App** on your smartphone.
   - Create a new project and choose **Raspberry Pi** as the device.
   - Add a **Push Button** widget in the Blynk app:
     - Set the **Virtual Pin (V0)** for the Push Button widget.
     - The button in the app will control the state of the LED connected to the Raspberry Pi.

   - Obtain your **Blynk Auth Token** from the app (you’ll need this to connect the Raspberry Pi to the app).

### **Running the Code:**

1. Clone or download this repository onto your Raspberry Pi.
2. Replace the **Blynk Auth Token** in the code with your personal **Blynk Auth Token**.
3. Run the Python script:

   ```bash
   python3 main.py
   ```

   The LED will blink on and off based on the state of the Push Button in the Blynk app.

### **How It Works:**

- The **Push Button widget** in the Blynk app sends signals to the Raspberry Pi via a virtual pin.
- When the button is pressed, the Raspberry Pi will turn on the LED, and when the button is released, the LED will turn off.
- The Raspberry Pi continuously listens for button presses and responds by controlling the LED.

### **Conclusion:**

This project demonstrates how to use the **Blynk IoT app** to control a simple **LED blinking** circuit on the **Raspberry Pi** using a virtual push button. This can be expanded to more complex IoT projects, controlling multiple devices or integrating with additional sensors.