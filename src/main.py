import time
from adafruit_motorkit import MotorKit
from adafruit_motor import stepper

kit = MotorKit()

# print(kit.motor1.throttle)

for i in range(200):
    kit.stepper1.onestep()
# for i in range(100):
#     kit.stepper1.onestep()