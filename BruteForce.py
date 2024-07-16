import board
import busio
import time
from adafruit_pca9685 import PCA9685

# Initialize I2C bus
i2c = busio.I2C(board.SCL, board.SDA)

# Initialize PCA9685
pca = PCA9685(i2c)
pca.frequency = 60  # Set PWM frequency to 50Hz (standard for servos)

# Define servo channels for each hand
left_hand_x = 0
left_hand_y = 1
left_hand_z = 2
left_hand_gripper = 3


#Variables to store their current angle
left_hand_x_var = 0
left_hand_y_var = 0
left_hand_z_var = 0
left_hand_gripper_var = 0

#Initial Loc of the Servo
left_hand_loc_start_x = 0

#Variables to store their loc 
left_hand_x_loc = [left_hand_loc_start_x, 0]
left_hand_y_loc = [left_hand_loc_start_x, 40]
left_hand_z_loc = [left_hand_loc_start_x, 80]
left_hand_gripper_loc = [left_hand_loc_start_x, 80]


# Define function to set servo angle
def set_servo_angle(channel, angle):
    pulse_width = int(150 + (angle / 180.0) * (600 - 150)) # Convert angle to pulse width, because it uses pulse width mainly. 
    #pca.channels[channel].duty_cycle = int(pulse_width / (1000000 / pca.frequency * 65535))  # Convert pulse width to PWM duty cycle
    pca.channels[channel].duty_cycle = pulse_width
    time.sleep(1)
    return "Moved!"
    
#Move Servo but we store the angle so its easily accessible    
def move_servo(servo, angle):
    if servo == left_hand_x:
        left_hand_x_var = angle
    elif servo == left_hand_y:
        left_hand_y_var = angle
    elif servo == left_hand_z:
        left_hand_z_var = angle
    elif servo == left_hand_gripper:
        left_hand_gripper_var = angle
    else:
        pass
    set_servo_angle(servo, angle)
    return "Servo Moved"

#Accept Action. 
def interpet_data(mLResult):
    if mLResult == "Metal":
        #Action
        return [-10, 0]
    elif mLResult == "Non-Magnetic Metal":
        #Action
        return [-5, 0]
    elif mLResult == "Plastic":
        #Action
        return  [0, 0]
    elif mLResult == "Paper":
        #Action
        return [5, 0]
    elif mLResult == "Leaf":
        #Action
        return [10, 0 ]
    elif mLResult == "Wet Leaf":
        #Action
        return [10, 0]
    else:
        return #Lead 
    
    
    
###BRUTE FORCE###

##ACTUAL ANGLE = FOR FIRST FOUR APART FROM CENTRE| X = 33.122 , Y = 113.75
#Caculated here: https://www.symbolab.com/geometry/angles-calculator#
#MOVE TO MOST LEFT 
move_servo(left_hand_gripper, 180)
move_servo(left_hand_x, -15.827)
move_servo(left_hand_y, 113.75) #Y needs to be calibrated to see how it moves 
move_servo(left_hand_gripper, 0)
#MOV TO TRASH
move_servo(left_hand_x, 0)
move_servo(left_hand_y, 0)
#MOVE TO SECOND LEFT 
move_servo(left_hand_gripper, 180)
move_servo(left_hand_x, -15.827)
move_servo(left_hand_y, 360-111.18)
move_servo(left_hand_gripper, 0)
#MOV TO TRASH
move_servo(left_hand_x, 0)
move_servo(left_hand_y, 0)
#MOVE TO MIDDLE
move_servo(left_hand_gripper, 180)
move_servo(left_hand_x, 56.64)
move_servo(left_hand_y, 66.73)
move_servo(left_hand_gripper, 0)
#MOV TO TRASH
move_servo(left_hand_x, 0)
move_servo(left_hand_y, 0)
#MOVE TO SECOND RIGHT
move_servo(left_hand_gripper, 180)
move_servo(left_hand_x, 15.827)
move_servo(left_hand_y, 111.18)
move_servo(left_hand_gripper, 0)
#MOV TO TRASH
move_servo(left_hand_x, 0)
move_servo(left_hand_y, 0)
#MOVE TO MOST RIGHT
move_servo(left_hand_gripper, 180)
move_servo(left_hand_x, 15.827)
move_servo(left_hand_y, 180-113.75)
move_servo(left_hand_gripper, 0)
#MOV TO TRASH
move_servo(left_hand_x, 0)
move_servo(left_hand_y, 0)
move_servo(left_hand_gripper, 180)

