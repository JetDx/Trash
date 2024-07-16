import time 
from gpiozero import LineSensor
from gpiozero import Servo


#SETUP 

#I'm just going to assume that its in Pin 4, 5, 6, 7, 8 like above 
s1 = LineSensor(4)
s2 = LineSensor(5)
s3 = LineSensor(6)
s4 = LineSensor(7)
s5 = LineSensor(8)

#Servo Pins 
m1 = Servo(9)
m2 = Servo(10)
m3 = Servo(11)

s1_state = 0
s2_state = 0
s3_state = 0
s4_state = 0
s5_state = 0

def update_s1_state(state):
    global s1_state
    s1_state = state

def update_s2_state(state):
    global s2_state
    s2_state = state

def update_s3_state(state):
    global s3_state
    s3_state = state

def update_s4_state(state):
    global s4_state
    s4_state = state

def update_s5_state(state):
    global s5_state
    s5_state = state

#The Functions baby
s1.when_line = lambda: update_s1_state(1)
s1.when_no_line = lambda: update_s1_state(0)
s2.when_line = lambda: update_s2_state(1)
s2.when_no_line = lambda: update_s2_state(0)
s3.when_line = lambda: update_s3_state(1)
s3.when_no_line = lambda: update_s3_state(0)
s4.when_line = lambda: update_s4_state(1)
s4.when_no_line = lambda: update_s4_state(0)
s5.when_line = lambda: update_s5_state(1)
s5.when_no_line = lambda: update_s5_state(0)

def checkLine(motorfr, motorfl, motorb): #Three wheel setup. 
    ##POSITIVE RIGHT/NEGATIVE LEFT
    ##TURN LEFT
    if (s1_state == 1) and (s2_state == 0) and (s3_state == 0) and (s4_state == 0) and (s5_state == 0):
        m1.value(-0.3)
        m2.value(-0.3)
        m3.value(-0.3)
    elif (s1_state == 1) and (s2_state == 1) and (s3_state == 0) and (s4_state == 0) and (s5_state == 0):
        m1.value(-0.2)
        m2.value(-0.2)
        m3.value(-0.2)
    elif (s1_state == 1) and (s2_state == 1) and (s3_state == 1) and (s4_state == 0) and (s5_state == 0):
        m1.value(-0.1)
        m2.value(-0.1)
        m3.value(-0.1)
    elif (s1_state == 0) and (s2_state == 1) and (s3_state == 1) and (s4_state == 0) and (s5_state == 0):
        m1.value(-0.05)
        m2.value(-0.05)
        m3.value(-0.05)     
    ##FORWARD
    elif (s1_state == 0) and (s2_state == 0) and (s3_state == 1) and (s4_state == 0) and (s5_state == 0):
        m1.value(-0.3)
        m2.value(0.3)
        m3.value(0.1)    
    ##TURN RIGHT 
    elif (s1_state == 0) and (s2_state == 0) and (s3_state == 0) and (s4_state == 0) and (s5_state == 1):
        m1.value(0.3)
        m2.value(0.3)
        m3.value(0.3)
    elif (s1_state == 0) and (s2_state == 0) and (s3_state == 0) and (s4_state == 1) and (s5_state == 1):
        m1.value(0.2)
        m2.value(0.2)
        m3.value(0.2)
    elif (s1_state == 0) and (s2_state == 0) and (s3_state == 1) and (s4_state == 1) and (s5_state == 1):
        m1.value(0.1)
        m2.value(0.1)
        m3.value(0.1)
    elif (s1_state == 0) and (s2_state == 0) and (s3_state == 1) and (s4_state == 1) and (s5_state == 0):
        m1.value(0.05)
        m2.value(0.05)
        m3.value(0.05)
    else:
        m1.value(0)
        m2.value(0)
        m3.value(0)
    return "Done"
        