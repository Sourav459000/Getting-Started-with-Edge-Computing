# **Object Detection using Arduino Nano 33 BLE Sense**

This project uses the **Arduino Nano 33 BLE Sense** to classify different objects in real-time. The model has been trained to detect **5 classes**: **Chair, Bench, Mouse, Mobile,** and **Watch**.

### **Edge Impulse Project Link**
- Access the project on Edge Impulse here: [Edge Impulse Object Detection Project](https://studio.edgeimpulse.com/public/374600/live)

## **Project Structure**

- **Data**
    - `object-detection-data-export.zip`: Contains the dataset used for training the object detection model.

- **Deployment**
    - `object-detection-arduino-1.0.5.zip`: Arduino deployment package for the object detection model.

- **Models**
    - `object-detection-classifier-keras-h5-model.zip`: Model in Keras H5 format, useful for further training or model tweaking.
    - `object-detection-classifier-tensorflow-lite-float32-model.lite`: Float32 TensorFlow Lite model optimized for the Arduino Nano 33 BLE Sense.
    - `object-detection-classifier-tensorflow-lite-int8-quantized-model.lite`: Int8 quantized TensorFlow Lite model, efficient for embedded deployment.
    - `object-detection-classifier-tensorflow-savedmodel-model.zip`: TensorFlow SavedModel version for additional deployment environments.

## **Requirements**

- **Hardware**:
    - Arduino Nano 33 BLE Sense
    - USB cable for connecting to the Arduino IDE
- **Software**:
    - Arduino IDE with Edge Impulse library installed (search for `Edge Impulse Arduino Library` in the Library Manager)
    - Edge Impulse account (for re-training or data management)

## **Model Deployment Instructions**

### **Using Arduino Deployment**

1. **Connect Hardware**:
    - Connect the Arduino Nano 33 BLE Sense to your computer via USB.

2. **Upload the Arduino Sketch**:
    - Unzip the **`object-detection-arduino-1.0.5.zip`** file and open the Arduino sketch in the Arduino IDE.
    - Select the **Arduino Nano 33 BLE Sense** board and the correct port in the Arduino IDE under **Tools**.
    - Upload the sketch to the Arduino Nano 33 BLE Sense.

3. **Run Object Detection**:
    - After uploading, the device will begin recognizing objects.
    - Open the **Serial Monitor** in the Arduino IDE to see real-time classification results. You will see one of the following classes: **Chair, Bench, Mouse, Mobile,** or **Watch**.

4. **Optional Python Serial Interface**:
    - For serial communication with Python, refer to the setup used in the **Shape Detection** project README for guidance.

## **Conclusion**

This **Object Detection** project brings real-time object recognition to the Arduino Nano 33 BLE Sense. To retrain or adjust object classes, import `object-detection-data-export.zip` into Edge Impulse, modify as needed, and deploy.