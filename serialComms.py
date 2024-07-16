import serial
import time

# Open the serial connection (use /dev/ttyS0 if /dev/serial0 doesn't work)
ser = serial.Serial('/dev/USB0', 9600, timeout=1)
time.sleep(2)  # Wait for the connection to establish

while True:
    # Send data to Arduino
    message = 'Hello from Raspberry Pi!\n'
    ser.write(message.encode('utf-8'))
    
    # Wait for confirmation
    while True:
        if ser.in_waiting > 0:
            confirmation = ser.readline().decode('utf-8').rstrip()
            print("Arduino says:", confirmation)
            break
    
    time.sleep(1)  # Wait for 1 second before sending the next message

