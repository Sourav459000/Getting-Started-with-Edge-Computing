**Title:**  
Blinking LED Code for Raspberry Pi 4 Model B

**Requirements:**
- Raspberry Pi 4 Model B
- LED from Grove Kit (connected to GPIO pin 18)
- Raspbian OS installed on Raspberry Pi
- Python 3.x installed
- RPi.GPIO library installed (`pip install RPi.GPIO`)

**Procedure:**
1. **Setup Hardware:**
   - Connect the LED from the Grove Kit to GPIO pin 18 on the Raspberry Pi 4 Model B. Ensure proper connections and polarity. ![GPIO Pinout Reference](https://www.raspberrypi.com/documentation/computers/images/GPIO-Pinout-Diagram-2.png)
   
2. **Install Required Libraries:**
   - Open the terminal on your Raspberry Pi.
   - Install the RPi.GPIO library by running the following command:
     ```
     pip install RPi.GPIO
     ```

3. **Download the Blinking LED Code:**
   - Create a new Python file on your Raspberry Pi using your preferred text editor (e.g., Nano, Vim, Thonny).
   - Copy and paste the code from main.py.

4. **Run the Code:**
   - Save the Python file with an appropriate name, for example, `blink_led.py`.
   - Open the terminal and navigate to the directory where the Python file is located.
   - Run the Python script.
   - The LED connected to GPIO pin 18 should start blinking at one-second intervals.
   - Press `Ctrl + C` to stop the script and exit.

**Conclusion:**
This README provides a step-by-step guide to set up and run a Python script on the Raspberry Pi 4 Model B to blink an LED connected to GPIO pin 18 using the RPi.GPIO library. Following these instructions, you can easily create simple LED blinking projects on your Raspberry Pi.