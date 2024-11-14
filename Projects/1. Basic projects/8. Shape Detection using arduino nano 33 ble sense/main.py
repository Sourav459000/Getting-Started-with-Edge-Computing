import serial
import time
import pyttsx3

engine = pyttsx3.init()

serial_port = 'COM20'
baud_rate = 115200

ser = serial.Serial(serial_port, baud_rate, timeout=1)


def speak_shape(shape):
    # Use the text-to-speech engine to speak out the shape
    engine.say(f"The detected shape is {shape}")
    engine.runAndWait()


try:
    time.sleep(2)

    while True:
        ser.write(b'Hello from Python\n')

        if ser.in_waiting > 0:
            data = ser.readline().decode().strip()
            shape = ''

            print("Received from Arduino:", data)

            # Extract the numeric part of the string
            numeric_part = ''.join(filter(str.isdigit, data))

            # Check if the numeric part is not empty before converting to int
            if numeric_part:
                value = int(numeric_part)
                if value > 60000:
                    a = data[:-9]
                    if a == 'Circle' or a == 'Square' or a == 'Triangle' or a == 'Star':
                        speak_shape(a)
            else:
                continue

except KeyboardInterrupt:
    print("Keyboard Interrupt. Exiting...")
finally:
    ser.close()
