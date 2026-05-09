from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch, run_task, multitask

hub = PrimeHub()
#Fahren
l_motor = Motor(Port.A, profile=11, positive_direction=Direction.COUNTERCLOCKWISE)
r_motor = Motor(Port.B)
#Arme
r_arm = Motor(Port.C)
l_arm = Motor(Port.D)


drive = DriveBase(r_motor, l_motor, wheel_diameter=50, axle_track=75)
#async ist für await
async def Kalibrieren():
    #Kalibriert den Roboter Arm auf physische Limit
    await multitask(
        r_arm.run_until_stalled(-300, duty_limit=50),
        l_arm.run_until_stalled(-300, duty_limit=50)
    )
    r_arm.reset_angle(0)
    l_arm.reset_angle(0)

#Der Roboter Synchronisiert jetzt den Arm
run_task(Kalibrieren())