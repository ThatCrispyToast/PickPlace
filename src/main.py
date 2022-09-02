import time
from adafruit_motorkit import MotorKit
from adafruit_motor import stepper

kit = MotorKit()

def release():
    kit.stepper1.release()
    kit.stepper2.release()

for i in range(200):
    kit.stepper1.onestep()


release()