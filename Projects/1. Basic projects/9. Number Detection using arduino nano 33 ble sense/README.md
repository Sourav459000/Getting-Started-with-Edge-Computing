# **Number Detection using Arduino Nano 33 BLE Sense**

This project enables real-time **number detection** on the **Arduino Nano 33 BLE Sense**, classifying handwritten numbers into **10 classes (0 to 9)** using a machine learning model trained with **Edge Impulse**.

### **Edge Impulse Project Link**
- Access the project on Edge Impulse here: [Edge Impulse Number Detection Project](https://studio.edgeimpulse.com/public/558992/live)

## **Project Structure**

- **Data**
    - `number-detection-export.zip`: Contains the dataset used to develop the number detection model.

- **Deployment**
    - `number-detection-arduino-1.0.5.zip`: Arduino deployment package for the number detection model.

- **Models**
    - `number-detection-classifier-keras-h5-model.zip`: Model file in Keras H5 format for further customization or retraining.
    - `number-detection-classifier-tensorflow-lite-float32-model.lite`: Model optimized for TensorFlow Lite with float32 precision.
    - `number-detection-classifier-tensorflow-lite-int8-quantized-model.lite`: Quantized TensorFlow Lite model optimized for efficiency with int8 precision.
    - `number-detection-classifier-tensorflow-savedmodel-model.zip`: Model in TensorFlow SavedModel format, suitable for various deployment environments.

## **Requirements**

- **Hardware**:
    - Arduino Nano 33 BLE Sense
    - Micro USB cable for connecting to the Arduino IDE
- **Software**:
    - Arduino IDE with Edge Impulse library installed (`Install the Edge Impulse Arduino Library` from Arduino Library Manager)
    - Edge Impulse account (for model retraining or dataset modifications)

## **Model Deployment Instructions**

### **Using Arduino Deployment**

1. **Prepare Hardware**:
    - Connect the Arduino Nano 33 BLE Sense to your computer with a USB cable.

2. **Upload the Sketch**:
    - Unzip the **`number-detection-arduino-1.0.5.zip`** file and open the Arduino sketch in the Arduino IDE.
    - Ensure the **Arduino Nano 33 BLE Sense** board and correct port are selected under **Tools** in the Arduino IDE.
    - Upload the sketch to the Arduino Nano 33 BLE Sense.

3. **Run Number Detection**:
    - After uploading, the device will begin classifying numbers in real-time based on sensor inputs.
    - Open the **Serial Monitor** (ensure the baud rate is set to `9600` if necessary) to view real-time classification results as one of the numbers between **0 to 9**.

4. **Optional Python Serial Interface**:
    - If you want to access classification results through Python, refer to the serial communication setup in the **Shape Detection** project README.

## **Conclusion**

The **Number Detection** project classifies numbers from **0 to 9** using a model deployed on the **Arduino Nano 33 BLE Sense**. The model was developed with **Edge Impulse** for efficient and lightweight real-time number classification. For further customization, import `number-detection-export.zip` into Edge Impulse to retrain the model or add more classes.