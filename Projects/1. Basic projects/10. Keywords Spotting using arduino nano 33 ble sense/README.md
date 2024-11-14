# **Keyword Spotting using Arduino Nano 33 BLE Sense**

This project implements **keyword spotting** on the **Arduino Nano 33 BLE Sense** to recognize specific voice commands in real-time. The model is trained to detect **5 keywords**: **computer, sourav, ok mit, mitadt,** and **unknown**.

### **Edge Impulse Project Link**
- Access the project on Edge Impulse here: [Edge Impulse Keyword Spotting Project](https://studio.edgeimpulse.com/public/381326/live)

## **Project Structure**

- **Data**
    - `keyword-spotting-data-export.zip`: Contains the dataset of audio recordings used to train the keyword spotting model.

- **Deployment**
    - `keyword-spotting-arduino-1.0.5.zip`: Arduino deployment package for the keyword spotting model.

- **Models**
    - `keyword-spotting-classifier-keras-h5-model.zip`: Model file in Keras H5 format for further customization or retraining.
    - `keyword-spotting-classifier-tensorflow-lite-float32-model.lite`: Model optimized for TensorFlow Lite with float32 precision.
    - `keyword-spotting-classifier-tensorflow-lite-int8-quantized-model.lite`: Quantized TensorFlow Lite model optimized for efficiency with int8 precision.
    - `keyword-spotting-classifier-tensorflow-savedmodel-model.zip`: Model in TensorFlow SavedModel format, suitable for various deployment environments.

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
    - Unzip the **`keyword-spotting-arduino-1.0.5.zip`** file and open the Arduino sketch in the Arduino IDE.
    - Ensure the **Arduino Nano 33 BLE Sense** board and correct port are selected under **Tools** in the Arduino IDE.
    - Upload the sketch to the Arduino Nano 33 BLE Sense.

3. **Run Keyword Spotting**:
    - After uploading, the device will begin detecting keywords based on audio input.
    - Open the **Serial Monitor** to view real-time classification results. It should display one of the detected keywords: **computer, sourav, ok mit, mitadt,** or **unknown** when a matching audio command is recognized.

4. **Optional Python Serial Interface**:
    - To access results through Python, refer to the serial communication setup in the **Shape Detection** project README.

## **Conclusion**

This **Keyword Spotting** project enables real-time detection of specific voice commands on the **Arduino Nano 33 BLE Sense**. The model was developed with **Edge Impulse** for efficient audio classification. To customize the keywords, import `keyword-spotting-data-export.zip` into Edge Impulse and retrain the model.