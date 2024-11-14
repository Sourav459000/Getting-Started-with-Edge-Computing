# **Color Detection using Arduino Nano 33 BLE Sense**

This project implements **color detection** on the **Arduino Nano 33 BLE Sense** to classify colors in real-time. The model is trained to detect **4 colors**: **Blue, Green, Red,** and **White**.

### **Edge Impulse Project Link**
- Access the project on Edge Impulse here: [Edge Impulse Color Detection Project](https://studio.edgeimpulse.com/public/367725/live)

## **Project Structure**

- **Data**
    - `color-detection-data-export.zip`: Contains the dataset used to train the color detection model.

- **Deployment**
    - `color-detection-arduino-1.0.5.zip`: Arduino deployment package for the color detection model.

- **Models**
    - `color-detection-classifier-keras-h5-model.zip`: Model file in Keras H5 format for further customization or retraining.
    - `color-detection-classifier-tensorflow-lite-float32-model.lite`: Model optimized for TensorFlow Lite with float32 precision.
    - `color-detection-classifier-tensorflow-lite-int8-quantized-model.lite`: Quantized TensorFlow Lite model optimized for efficiency with int8 precision.
    - `color-detection-classifier-tensorflow-savedmodel-model.zip`: Model in TensorFlow SavedModel format, suitable for various deployment environments.

## **Requirements**

- **Hardware**:
    - Arduino Nano 33 BLE Sense
    - Micro USB cable for connecting to the Arduino IDE
- **Software**:
    - Arduino IDE with the Edge Impulse library installed (`Install the Edge Impulse Arduino Library` from Arduino Library Manager)
    - Edge Impulse account (for model retraining or dataset modifications)

## **Model Deployment Instructions**

### **Using Arduino Deployment**

1. **Prepare Hardware**:
    - Connect the Arduino Nano 33 BLE Sense to your computer with a USB cable.

2. **Upload the Sketch**:
    - Unzip the **`color-detection-arduino-1.0.5.zip`** file and open the Arduino sketch in the Arduino IDE.
    - Ensure the **Arduino Nano 33 BLE Sense** board and correct port are selected under **Tools** in the Arduino IDE.
    - Upload the sketch to the Arduino Nano 33 BLE Sense.

3. **Run Color Detection**:
    - Once uploaded, the device will begin detecting colors based on its sensor input.
    - Open the **Serial Monitor** in the Arduino IDE to view real-time classification results. The monitor will display one of the detected colors: **Blue, Green, Red,** or **White**.

4. **Optional Python Serial Interface**:
    - If you wish to access results through Python, refer to the serial communication setup in the **Shape Detection** project README.

## **Conclusion**

This **Color Detection** project enables real-time color classification on the **Arduino Nano 33 BLE Sense** using Edge Impulse’s machine learning platform. To customize the colors or add additional classes, import `color-detection-data-export.zip` into Edge Impulse and retrain the model.