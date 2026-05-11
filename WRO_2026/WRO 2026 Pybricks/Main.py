from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch, hub_menu, run_task, multitask

hub = PrimeHub()
# === Setup ===
#Fahren
l_motor = Motor(Port.A, profile=4, positive_direction=Direction.COUNTERCLOCKWISE)
r_motor = Motor(Port.B, profile=4)
#Arme
hoch_arm = Motor(Port.E, profile=4)
zangen_arm = Motor(Port.F, profile=4, gears=[12, 20])

drive = DriveBase(r_motor, l_motor, wheel_diameter=50, axle_track=75)

drive.settings(straight_speed=800, straight_acceleration=1000, turn_rate=800, turn_acceleration=500)

async def Kalibrieren(): #async ist für await und multitask
    #Kalibriert den Roboter Arm auf physische Limit
    await multitask(
        hoch_arm.run_until_stalled(-300, duty_limit=50),
        zangen_arm.run_until_stalled(-300, duty_limit=50)
    )
    hoch_arm.reset_angle(0)
    zangen_arm.reset_angle(0)

def halte_blöcke(laufen):
    if laufen:
        zangen_arm.run(200)
    else:
        zangen_arm.brake()


# === Programme ===
def gelbe_bausteine():
    drive.settings(straight_speed=800, straight_acceleration=100, turn_rate=800, turn_acceleration=100)
    drive.straight(350)
    drive.straight(-50)
    zangen_arm.track_target(190)
    hoch_arm.run_until_stalled(800)
    halte_blöcke(True)
    Kalibrieren()

def aus_gelbe_steine_fahren():
    drive.straight(-235)
    drive.turn(90)
    drive.straight(-250)
    drive.settings(straight_speed=400)
    #vlt
    #drive.straight(30)
    #drive.settings(straight_speed=800)
    drive.straight(2080)
    drive.turn(-90)
    drive.straight(-75)
    zangen_arm.track_target(159)

def bauklotz_1():
    drive.straight(-150)
    drive.straight(130)
    drive.turn(87)
    drive.straight(1000)
    drive.turn(-87)
    drive.straight(-240)
    drive.straight(850)
    drive.straight(-50)
    drive.turn(15)
    zangen_arm.track_target(128)
    drive.turn(-15)
    drive.straight(190)
    drive.turn(-89)
    drive.straight(800)
    zangen_arm.track_target(151)
    halte_blöcke(False)

# === hier laufen lassen ===
Kalibrieren()
gelbe_bausteine()
aus_gelbe_steine_fahren()
bauklotz_1()

