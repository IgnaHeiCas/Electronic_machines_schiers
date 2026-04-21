from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch
hub = PrimeHub()
left_motor = Motor(Port.A, profile=11, positive_direction=Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.B)

#Gyro test
drive = DriveBase(right_motor, left_motor, wheel_diameter=50, axle_track=75)

#print(motorA.angle())
#left_motor.run_angle(-1000, 1000, wait=False)
#right_motor.run_angle(1000, 1000)
#print(motorA.angle())

drive.settings(800, 1000,)
#drive.straight(360)
drive.turn(90)








