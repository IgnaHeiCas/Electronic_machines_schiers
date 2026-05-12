from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch, hub_menu, run_task, multitask

hub = PrimeHub()
# === Setup ===
#Fahren
l_motor = Motor(Port.A, positive_direction=Direction.COUNTERCLOCKWISE, profile=5)
r_motor = Motor(Port.B, profile=5)
#Arme
hoch_arm = Motor(Port.F, positive_direction=Direction.COUNTERCLOCKWISE)
zangen_arm = Motor(Port.D, gears=[12, 20])

drive = DriveBase(r_motor, l_motor, wheel_diameter=62.5, axle_track=196.5)

drive.settings(straight_speed=1000, straight_acceleration=500, turn_rate=500, turn_acceleration=500)

def hoch(): #async ist für await und multitask
    #Kalibriert den Roboter Arm auf physische Limit
    hoch_arm.run_until_stalled(800)
    hoch_arm.reset_angle(0)

def zange_hoch(): 

    #Kalibriert den Roboter Arm auf physische Limit
    zangen_arm.run_until_stalled(-800, duty_limit=100),
    zangen_arm.reset_angle(0)

def halte_bloecke(laufen):
    if laufen:
        zangen_arm.run(800)
    else:
        zangen_arm.brake()

# === Programme ===
def gelbe_bausteine():
    hoch()
    drive.straight(195)
    drive.straight(-25)
    hoch_arm.run(-200)
    wait(50)
    zangen_arm.run_until_stalled(200)

def aus_gelbe_steine_fahren():
    halte_bloecke(True)

    hoch()
    drive.straight(-130)
    drive.turn(-90)
    drive.straight(-140)
    drive.settings(straight_speed=400)
    #vlt
    #drive.straight(30)
    #drive.settings(straight_speed=800)
    drive.straight(1100)
    drive.turn(90)
    drive.straight(-42)
    hoch_arm.run_until_stalled(-1000)

def bauklotz_1():
    drive.straight(-83)
    drive.straight(72.5)
    drive.turn(-87)
    drive.straight(557)
    drive.turn(87)
    drive.straight(-134)
    drive.straight(474)
    drive.straight(-27)
    drive.turn(-15)
    hoch_arm.run_until_stalled(800)
    drive.turn(15)
    drive.straight(105)
    drive.turn(89)
    drive.straight(443)
    hoch_arm.track_target(151)
    wait(100)
    halte_bloecke(False)
    zangen_arm.run_until_stalled(800)
    hoch_arm.run_until_stalled(800)
    wait(50)

def grüne_steine():
    drive.straight(-1260)
    hoch_arm.track_target(191)
    drive.straight(-140)
    drive.straight(610)
    drive.turn(105)
    drive.turn(-15)
    hoch_arm.track_target(128)
    multitask (drive.straight(-850), hoch_arm.track_target(190))



# === hier laufen lassen ===
#hoch()
#zange_hoch()
#gelbe_bausteine()
#aus_gelbe_steine_fahren()
#bauklotz_1()
hoch_arm.run(100)