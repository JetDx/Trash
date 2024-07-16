import math 
import board
import busio
from adafruit_pca9685 import PCA9685

#Basic Motor Setup
# Very cool, no use
# Initialize I2C bus
i2c = busio.I2C(board.SCL, board.SDA)

# Initialize PCA9685
pca = PCA9685(i2c)
pca.frequency = 60  # Set PWM frequency to 50Hz (standard for servos)

# Define function to set servo angle
def set_servo_angle(channel, angle):
    pulse_width = int((angle / 180.0) * 1000 + 150)  # Convert angle to pulse width, because it uses pulse width mainly. 
    pca.channels[channel].duty_cycle = int(pulse_width / (1000000 / pca.frequency * 65535))  # Convert pulse width to PWM duty cycle
    

#Wheel Pins
WheelBack = 10
WheelRight = 9
WheelLeft = 8

options = ['L', 'F', 'R']

def moveWheel(direction):
    if direction == 'L':
        print("Left")
        set_servo_angle(WheelLeft, 360*0.77)
        set_servo_angle(WheelBack, 360)
    elif direction == 'F':
        print("Forward")
        set_servo_angle(WheelLeft, 360*0.77)
        set_servo_angle(WheelRight, -360*0.77)
    elif direction == 'R':
        print("Right")
        set_servo_angle(WheelRight, 360*0.77)
        set_servo_angle(WheelBack, -360)
    else:
        print("Invalid direction")  