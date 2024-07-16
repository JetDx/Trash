from adafruit_servokit import ServoKit
kit = ServoKit(channels=16)
import time 

#Define Angle Storages 
left_hand_x_var = 0
left_hand_y_var = 0
left_hand_gripper_var = 0 

#Define Servo Channels
left_hand_x = 0
left_hand_y = 1 
left_hand_gripper = 2

#Use Action
def move_servo(servo, angle):
    if servo == left_hand_x_var:
        servoToMove = left_hand_x
    elif servo == left_hand_y_var:
        servoToMove = left_hand_y
    elif servo == left_hand_gripper_var:
        servoToMove = left_hand_gripper
    else:
        pass
    print("Identified Servo as ", servoToMove, " Moving to ", angle)
    kit.servo[servoToMove].angle = angle 
    time.sleep(1)
    print("Servo Moved")
    return "Servo Moved"

#Determine Action. 
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
   
   
#TEST
# move_servo(left_hand_x_var, 180)
# move_servo(left_hand_x_var, 90)
# move_servo(left_hand_x_var, 0)
# move_servo(left_hand_x_var, 180)
# move_servo(left_hand_x_var, 0)


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