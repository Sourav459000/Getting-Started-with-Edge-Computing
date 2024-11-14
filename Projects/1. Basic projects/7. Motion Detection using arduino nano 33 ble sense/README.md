# **Motion Detection using Arduino Nano 33 BLE Sense**

This project demonstrates a **motion detection** system using **Edge Impulse** and the **Arduino Nano 33 BLE Sense**. The model classifies motion data captured by the onboard sensors of the Arduino Nano 33 BLE Sense into four motion classes:

1. **Circular**
2. **Ideal** (no significant motion)
3. **Left-Right**
4. **Up-Down**

### **Edge Impulse Project Link**
- Access the project on Edge Impulse here: [Edge Impulse Motion Detection Project](https://studio.edgeimpulse.com/public/360393/live)

## **Project Structure**

- **Data**
    - `motion-detection-export.zip`: Contains the training data used to develop the model.
  
- **Deployment**
    - `motion-detection-arduino-1.0.5.zip`: A ready-to-use Arduino deployment package with the classifier.

- **Models**
    - `motion-detection-classifier-keras-h5-model.zip`: Model file in Keras H5 format for further model customization and retraining.
    - `motion-detection-classifier-tensorflow-lite-float32-model.lite`: Model optimized for TensorFlow Lite with float32 precision.
    - `motion-detection-classifier-tensorflow-lite-int8-quantized-model.lite`: Quantized TensorFlow Lite model optimized for efficiency with int8 precision.
    - `motion-detection-classifier-tensorflow-savedmodel-model.zip`: TensorFlow SavedModel format, suitable for deployment in environments supporting the TensorFlow SavedModel standard.

## **Requirements**

- **Hardware**: 
    - Arduino Nano 33 BLE Sense
    - Micro USB cable for connecting to the Arduino IDE
- **Software**:
    - Arduino IDE with Edge Impulse library installed (`Install the Edge Impulse Arduino Library` from Arduino Library Manager)
    - Edge Impulse account (for model retraining or dataset modifications)
  
## **Model Deployment Options**

### **Option 1: Using Arduino Deployment**

1. **Prepare Hardware**:
    - Connect the Arduino Nano 33 BLE Sense to your computer using a USB cable.

2. **Upload the Sketch**:
    - Unzip the **`motion-detection-arduino-1.0.5.zip`** file and open the sketch in the Arduino IDE.
    - Ensure that you have selected the **Arduino Nano 33 BLE Sense** board and the correct port under **Tools** in the Arduino IDE.
    - Upload the sketch to the Arduino Nano 33 BLE Sense by selecting **Upload**.

3. **Run Motion Detection**:
    - Once the sketch is uploaded, the device will start using the trained model to detect and classify motion in real-time.
    - Open the **Serial Monitor** (set the baud rate to `9600` if necessary) to observe the real-time classification results as the device detects different types of motion.

### **Option 2: Using TensorFlow Lite Models**

1. **TensorFlow Lite Float32 Model**:
    - Use `motion-detection-classifier-tensorflow-lite-float32-model.lite` if you need higher precision.
  
2. **TensorFlow Lite Quantized Model**:
    - Use `motion-detection-classifier-tensorflow-lite-int8-quantized-model.lite` for resource-constrained applications requiring lower latency and reduced memory footprint.
  
3. **Execute the Model on Device**:
    - If you choose to deploy a TensorFlow Lite model, refer to the Edge Impulse documentation to integrate the `.lite` model into custom firmware or an application.

### **Option 3: Using TensorFlow SavedModel**

1. **SavedModel Usage**:
    - Download and unzip the `motion-detection-classifier-tensorflow-savedmodel-model.zip` file.
    - Integrate this model into Python-based or other TensorFlow-supported applications for further experimentation or deployment in environments compatible with TensorFlow.

## **Conclusion**

This **Motion Detection** project enables real-time classification of motion data collected from the Arduino Nano 33 BLE Sense using a machine learning model trained on the **Edge Impulse** platform. The project structure provides flexibility with various deployment options suitable for different environments and constraints.

For additional customization or retraining, you can import the `motion-detection-export.zip` dataset into the Edge Impulse platform and modify the project as required.