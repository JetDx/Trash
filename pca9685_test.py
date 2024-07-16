import time
import board
import busio
from adafruit_pca9685 import PCA9685

# Initialize the I2C bus
i2c = busio.I2C(board.SCL, board.SDA)

# Create the PCA9685 class instance
pca = PCA9685(i2c)
pca.frequency = 60

# Function to convert angle in degrees to PWM pulse length
def angle_to_pulse(angle):
    # Assuming 0-180 degrees maps to 150-600 pulse length
    pulse = int(150 + (angle / 180.0) * (600 - 150))
    return pulse

try:
    while True:
        # Move servo connected to channel 0

        # Move to 0 degrees
        print("Moving to 0 degrees")
        pca.channels[0].duty_cycle = angle_to_pulse(0)
        time.sleep(1)

        # Move to 90 degrees
        print("Moving to 90 degrees")
        pca.channels[0].duty_cycle = angle_to_pulse(90)
        time.sleep(1)

        # Move to 180 degrees
        print("Moving to 180 degrees")
        pca.channels[0].duty_cycle = angle_to_pulse(180)
        time.sleep(1)

except KeyboardInterrupt:
    # Turn off all channels on keyboard interrupt
    for i in range(16):
        pca.channels[i].duty_cycle = 0
    print("Program interrupted and exited")
