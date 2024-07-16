from adafruit_servokit import ServoKit
kit = ServoKit(channels=16)

while True:
  kit.servo[0].angle = 180
  kit.servo[0].angle = 0
