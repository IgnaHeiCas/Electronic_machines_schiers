from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop, Axis
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = PrimeHub(top_side=Axis.Z, front_side=Axis.X)
#Motor
left_motor = Motor(Port.A, profile=11, positive_direction=Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.B)
drive = DriveBase(right_motor, left_motor, wheel_diameter=50, axle_track=75)

#Gyro
def gyro_turn(degrees):
    hub.imu.reset_heading(0)
    
    if degrees > 0:
        while hub.imu.heading() < degrees:
            drive.drive(0, 30)
    else:
        while hub.imu.heading() > degrees:
            drive.drive(0, -30)
    
    drive.stop()

gyro_turn(90)

