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

drive.settings(straight_speed=1000, straight_acceleration=1000, turn_rate=600, turn_acceleration=1000)

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
        zangen_arm.dc(1000)
    else:
        zangen_arm.brake()

def hoch_genau(grad):
    hoch_arm.run_angle(1000, grad)

# === Programme ===
def gelbe_bausteine():
    hoch()
    drive.straight(195)
    drive.straight(-35)
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
    drive.turn(-90)
    drive.straight(557)
    drive.turn(90)
    drive.straight(-134)
    drive.straight(474)
    drive.straight(-27)
    drive.turn(-15)
    hoch()
    drive.turn(15)
    drive.straight(105)
    drive.turn(89)
    drive.straight(443)
    wait(100)
    hoch_genau(-30)
    halte_bloecke(False)
    zange_hoch()
    hoch_genau(16.5)
    wait(50)

def grüne_steine():
    drive.straight(-800)
    hoch_arm.run_until_stalled(-800)
    drive.straight(-90)
    drive.straight(336)
    drive.turn(-105)
    drive.turn(15)
    hoch_arm.run_until_stalled(800)
    drive.straight(-475)
    hoch_arm.run_until_stalled(-800)
    drive.straight(-133)
    drive.straight(61)
    drive.turn(83)
    hoch_arm.run_until_stalled(800)
    hoch_genau(-30)
    drive.straight(-295)
    hoch_arm.run_until_stalled(-800)

def weisse_steine():
    drive.straight(500)
    drive.turn(83)


# === hier laufen lassen ===
hoch()
zange_hoch()
gelbe_bausteine()
aus_gelbe_steine_fahren()
bauklotz_1()
grüne_steine()





