# **Shape Detection using Arduino Nano 33 BLE Sense**

This project demonstrates **shape detection** using a model trained on **Edge Impulse** and deployed on the **Arduino Nano 33 BLE Sense**. The model classifies shapes into four classes:

1. **Circle**
2. **Square**
3. **Star**
4. **Triangle**

The `main.py` Python script allows real-time shape detection with voice feedback for each detected shape.

### **Edge Impulse Project Link**
- Access the project on Edge Impulse here: [Edge Impulse Shape Detection Project](https://studio.edgeimpulse.com/public/371256/live)

## **Project Structure**

- **Data**
    - `shape-detection-export.zip`: Contains the training data used to develop the model.
  
- **Deployment**
    - `shape-detection-arduino-1.0.5.zip`: A ready-to-use Arduino deployment package with the classifier.

- **Models**
    - `shape-detection-classifier-keras-h5-model.zip`: Model file in Keras H5 format for further model customization and retraining.
    - `shape-detection-classifier-tensorflow-lite-float32-model.lite`: Model optimized for TensorFlow Lite with float32 precision.
    - `shape-detection-classifier-tensorflow-lite-int8-quantized-model.lite`: Quantized TensorFlow Lite model optimized for efficiency with int8 precision.
    - `shape-detection-classifier-tensorflow-savedmodel-model.zip`: TensorFlow SavedModel format, suitable for deployment in environments supporting the TensorFlow SavedModel standard.

- **Python Script**
    - `main.py`: Python script for accessing Arduino shape detection results and providing voice feedback for detected shapes.

## **Requirements**

- **Hardware**: 
    - Arduino Nano 33 BLE Sense
    - Micro USB cable for connecting to the Arduino IDE
- **Software**:
    - Arduino IDE with Edge Impulse library installed (`Install the Edge Impulse Arduino Library` from Arduino Library Manager)
    - Edge Impulse account (for model retraining or dataset modifications)
    - Python 3.x
    - `pyttsx3` library for text-to-speech (`pip install pyttsx3`)
    - `pyserial` library for serial communication (`pip install pyserial`)

## **Model Deployment Options**

### **Option 1: Using Arduino Deployment**

1. **Prepare Hardware**:
    - Connect the Arduino Nano 33 BLE Sense to your computer using a USB cable.

2. **Upload the Sketch**:
    - Unzip the **`shape-detection-arduino-1.0.5.zip`** file and open the sketch in the Arduino IDE.
    - Ensure that you have selected the **Arduino Nano 33 BLE Sense** board and the correct port under **Tools** in the Arduino IDE.
    - Upload the sketch to the Arduino Nano 33 BLE Sense by selecting **Upload**.

3. **Run Shape Detection**:
    - Once the sketch is uploaded, the device will start using the trained model to detect shapes in real-time.
    - Open the **Serial Monitor** (set the baud rate to `9600` if necessary) to observe the real-time classification results, where shape events will be categorized into one of the four classes: **Circle, Square, Star,** or **Triangle**.

### **Option 2: Using Python Script for Voice Feedback**

1. **Connect to Serial Port**:
    - Ensure the Arduino Nano 33 BLE Sense is connected to your computer, and check the assigned **COM port** (e.g., `COM20` for Windows or `/dev/ttyUSB0` for Linux).

2. **Run `main.py` Script**:
    - Open a terminal and navigate to the directory containing `main.py`.
    - Execute the script using the following command:
      ```bash
      python main.py
      ```

3. **Shape Detection with Voice Feedback**:
    - When a shape is detected, the script reads the shape from the Arduino’s serial output.
    - The detected shape will be printed in the terminal and spoken aloud using a text-to-speech engine.
    - This provides an audio output for each detected shape, helping visually impaired users or offering hands-free feedback.

4. **Stopping the Script**:
    - To stop the script, use `Ctrl+C` to terminate the program.

## **Conclusion**

This **Shape Detection** project enables real-time classification of shape data collected from the Arduino Nano 33 BLE Sense using a machine learning model trained on **Edge Impulse**. The Python script (`main.py`) enhances the project by providing real-time voice feedback for each detected shape, supporting four classes: **Circle, Square, Star,** and **Triangle**. 

For additional customization or retraining, you can import the `shape-detection-export.zip` dataset into the Edge Impulse platform and modify the project as required.