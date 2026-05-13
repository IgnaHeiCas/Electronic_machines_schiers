from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop, Axis
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

def halte_oben(laufen):
    if laufen:
        hoch_arm.dc(1000)
    else:
        hoch_arm.brake()

def halte_unten(laufen):
    if laufen:
        hoch_arm.dc(-1000)
    else:
        hoch_arm.brake()

def hoch_genau(grad):
    hoch_arm.run_angle(1000, grad)

# === Programme ===
def start():
    hoch()
    drive.straight(180)
    drive.straight(-25)
    hoch_arm.run(-200)
    wait(50)
    zangen_arm.run_until_stalled(800)

def gelbe_bloecke_aufnehmen():
    halte_bloecke(True)
    hoch_arm.run_until_stalled(800)
    drive.straight(-140)
    drive.turn(-90)
    drive.straight(-140)
    #vlt
    #drive.straight(30)
    #drive.settings(straight_speed=800)
    drive.straight(1100)
    drive.turn(90)
    drive.straight(-42)
    hoch_arm.run_until_stalled(-1000)

def bei_kessel():
    drive.straight(-83)
    drive.straight(72.5)
    drive.turn(-90)
    drive.straight(557)
    drive.turn(90)
    #drive.straight(-134)
    drive.straight(340)
    drive.straight(-27)
    drive.turn(-15)
    hoch()
    drive.turn(15)
    drive.straight(140)
    drive.turn(89)
    drive.settings(straight_speed=300)
    drive.straight(443)
    wait(100)
    hoch_genau(-30)

def gelbe_bauklötze_versorgt():
    halte_bloecke(False)
    zange_hoch()
    #hoch_genau(18)
    wait(50)

def grüne_steine_aufnehmen():
    drive.settings(straight_speed=1000)
    drive.straight(-780)
    hoch_arm.run_until_stalled(-800)
    halte_unten(True)
    drive.straight(-90)
    drive.straight(336)
    drive.turn(-100)
    drive.turn(10)
    halte_unten(False)

def weisse_steine_im_käfig():
    hoch_arm.run_until_stalled(800)
    halte_oben(True)
    drive.straight(-447)
    halte_oben(False)
    drive.turn(83)
    hoch_genau(-33)
    drive.straight(-300)
    hoch_arm.run_until_stalled(-800)
    halte_unten(True)

def grün_weiss_abliefern():
    drive.straight(278)
    drive.turn(-83)
    drive.straight(493)
    drive.turn(-90)
    halte_unten(True)
    drive.straight(-423)
    drive.straight(42)
    halte_unten(False)
    drive.turn(-48)
    drive.turn(4)
    drive.straight(-108)
    hoch_arm.run_until_stalled(800)
    drive.straight(115)
    hoch_arm.run_until_stalled(-800)
    drive.straight(-95)
    drive.straight(95)
    drive.turn(44)
    halte_unten(True)
    drive.straight(-61)
    drive.straight(78)
    hoch_arm.run_until_stalled(800)

def blaue_steine_im_käfig():
    drive.straight(-61)
    drive.straight(-61)
    drive.straight(-61)

def gelbe_im_käfig():
    drive.straight(-61)

def gelbe_versorgen():
    drive.straight(50)
    drive.turn(-70)
    drive.straight(-230)
    drive.turn(-15)
    drive.straight(-222)
    drive.turn(-6)
    drive.straight(-334)
    drive.straight(83)
    drive.turn(-90)
    drive.straight(-267)
    hoch_arm.run_until_stalled(800)

def dreieckskelle_versorgt():
    drive.straight(306)
    drive.turn(90)
    drive.straight(50)
    drive.straight(50)

def fertig():
    drive.straight(-61)


# === hier laufen lassen ===
#print("Es fehlen noch:" + 8400 - hub.battery.voltage() + "von 8400")
hoch()
zange_hoch()
start()
gelbe_bloecke_aufnehmen()
bei_kessel()
gelbe_bauklötze_versorgt()
grüne_steine_aufnehmen()
weisse_steine_im_käfig()




