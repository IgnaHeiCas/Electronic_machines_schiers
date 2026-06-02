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
#Farbsensor
l_farb = ColorSensor(Port.C)
r_farb = ColorSensor(Port.E)
drive = DriveBase(r_motor, l_motor, wheel_diameter=62.5, axle_track=196.5)

drive.settings(straight_speed=1000, straight_acceleration=1000, turn_rate=600, turn_acceleration=1000)

def hoch(): #async ist für await und multitask
    #Kalibriert den Roboter Arm auf physische Limit
    hoch_arm.run_until_stalled(800)
    hoch_arm.reset_angle(0)

def zange_hoch(): 
    #Kalibriert den Roboter Arm auf physische Limit
    zangen_arm.run_until_stalled(-1000, duty_limit=100),
    zangen_arm.reset_angle(0)

def zange_genau(grad):
        zangen_arm.run_angle(-800, grad),

def halte_bloecke(laufen):
    if laufen:
        zangen_arm.dc(100)
    else:
        zangen_arm.brake()

def halte_oben(laufen):
    if laufen:
        hoch_arm.dc(800)
    else:
        hoch_arm.brake()

def halte_unten(laufen):
    if laufen:
        hoch_arm.run(-800)
    else:
        hoch_arm.brake()

def hoch_genau(grad):
    hoch_arm.run_angle(800, grad)

def bis_gruen():
   while l_farb.reflection() >= 94 or r_farb.reflection() >= 94:
        drive.straight(3)
    #else:
        #drive.stop()

# === Programme ===
def start():
    hoch()
    drive.settings(straight_speed=300)
    drive.straight(195)
    drive.straight(-19)
    hoch_arm.run_until_stalled(-800)
    halte_unten(True)
    drive.settings(straight_speed=800)
    wait(50)
    zangen_arm.run_until_stalled(800)

def gelbe_bloecke_aufnehmen():
    halte_bloecke(True)
    halte_unten(False)
    hoch_arm.run_until_stalled(800)
    halte_oben(True)
    drive.straight(-90)
    drive.turn(-90)
    drive.straight(-140)
    #vlt
    #drive.straight(30)
    #drive.settings(straight_speed=800)
    drive.straight(500)
    drive.reset()
    drive.turn(1)
    drive.straight(600)
    drive.turn(90)
    drive.straight(-47)
    halte_oben(False)
    hoch_arm.run(-800)
    wait(1000)

def bei_kessel():
    halte_unten(True)
    drive.straight(-60)
    hoch_arm.run_until_stalled(-1000)
    drive.straight(20)
    hoch_arm.run_until_stalled(-1000)
    drive.straight(-34)
    halte_unten(False)
    drive.straight(75)
    hoch_arm.run_until_stalled(1000)
    hoch_genau(-35)
    wait(100)
    #hoch_genau(7)
    drive.turn(-86)#90
    drive.straight(550)
    drive.straight(-30)
    drive.turn(86)#88
    hoch_arm.run_until_stalled(-1000)
    wait(500)
    drive.straight(-120)
    drive.straight(440)
    drive.straight(-27)
    drive.turn(-15)
    hoch()
    halte_oben(True)
    drive.turn(15)
    drive.straight(112)
    drive.turn(90)
    drive.settings(straight_speed=300)
    drive.straight(430)
    wait(100)
    halte_oben(False)
    hoch_arm.run_until_stalled(-800)

def gelbe_bauklötze_versorgt():
    halte_bloecke(False)
    zange_genau(40)
    wait(500)
    zangen_arm.run_until_stalled(800, duty_limit=100)
    wait(500)
    zange_genau(40)
    zangen_arm.run_until_stalled(-800, duty_limit=100)
    hoch_arm.run_until_stalled(800)

def grüne_steine_aufnehmen():
    halte_oben(True)
    drive.settings(straight_speed=800)
    drive.straight(-400)
    halte_oben(False)
    drive.reset()
    drive.turn(-1)
    hoch_genau(-22)
    drive.straight(-380)
    hoch_arm.run_until_stalled(-800)
    halte_unten(True)
    drive.straight(-90)
    drive.straight(336)
    drive.turn(-110)
    #drive.turn(40)
    drive.turn(20)
    halte_unten(False)

def weisse_steine_im_käfig():
    hoch_arm.run_until_stalled(800)
    halte_oben(True)
    drive.straight(-360)
    halte_oben(False)
    hoch_genau(-30)
    drive.turn(68)
    drive.straight(-300)

def grün_weiss_abliefern():
    hoch_arm.run_until_stalled(-800)
    drive.straight(-10)
    halte_unten(True)
    drive.straight(288)
    drive.turn(-68)
    drive.straight(380)
    drive.turn(-90)
    drive.straight(-392)
    drive.settings(straight_speed=300)
    #drive.straight(17)
    drive.turn(-45)
    halte_unten(False)
    hoch_genau(7)
    drive.straight(-90) 
    drive.straight(20)
    #halte_unten(False)
    hoch_arm.run_until_stalled(800) 
    hoch_genau(-30)
    drive.straight(110)
    drive.straight(-10)
    hoch_arm.run_until_stalled(-800)
    halte_unten(True)
    wait(1000)
    drive.straight(-100)
    drive.straight(125)
    drive.turn(42)
    #drive.straight(-55)
    halte_unten(False)
    hoch_arm.run_until_stalled(800)
    drive.straight(-117)

def blaue_steine_im_käfig():
    drive.settings(straight_speed=800)
    drive.straight(315)
    drive.turn(135)
    drive.straight(-305)
    drive.turn(43)
    hoch_genau(-20)
    drive.straight(-175)
    hoch_arm.run_until_stalled(-800)
    halte_unten(True)
    drive.straight(-85)
    drive.straight(336)
    drive.turn(110)
    drive.turn(-20)
    halte_unten(False)
    hoch_arm.run_until_stalled(800)
    halte_oben(True)
    drive.straight(-455)
    halte_oben(False)
    hoch_arm.run_until_stalled(-800)
    halte_unten(True)
    drive.straight(-100)
    drive.straight(50)
    halte_unten(False)
    hoch_arm.run_until_stalled(800)
    hoch_genau(-27)
    drive.turn(-86)

def gelbe_im_käfig():
    drive.straight(-300)
    hoch_arm.run_until_stalled(-800)
    halte_unten(True)
    drive.straight(-10)
    drive.straight(295)
    drive.turn(86)
    drive.straight(-65)
    drive.straight(400)
    drive.reset()
    drive.turn(-2)
    drive.straight(210)

def gelbe_versorgen():
    zange_genau(-100)
    drive.turn(-50)
    drive.straight(295)
    l_motor.run_angle(speed=300, rotation_angle=200)
    drive.straight(200)
    l_motor.run_angle(speed=300, rotation_angle=45)
    drive.straight(585)
    halte_unten(False)
    drive.straight(-410)
    drive.turn(90)
    drive.straight(-215)
    hoch_genau(14)
    wait(1000)
  
def dreieckskelle_versorgt():
    drive.straight(215)
    drive.turn(-90)
    drive.straight(410)
    drive.turn(-20)
    drive.straight(200)
    drive.turn(40)
    drive.straight(320)
    #drive.turn(55)
    #drive.straight(-362)
    #hoch_genau(20)
    
def blaue_bloecke_aufnehmen():
    drive.straight(362)
    drive.turn(-25)
    hoch_arm.run_until_stalled(-800)
    drive.straight(-400)
    #drive.straight(-142)
    #drive.turn(-90)
    #drive.straight(206)
    #drive.straight(-28)
    #hoch_arm.run_until_stalled(-800)
    #halte_unten(True)
    #wait(50)
    #zangen_arm.run_until_stalled(800)
    #halte_bloecke(True)
    #halte_unten(False)

def fertig():
    hoch_arm.run_until_stalled(800)
    halte_oben(True)
    drive.straight(153)
    drive.settings(straight_speed=300)
    bis_gruen()
    drive.settings(straight_speed=800)
    drive.straight(28)
    drive.straight(-72)
    drive.turn(-90)
    drive.straight(-150)
    drive.straight(500)
    drive.reset()
    drive.settings(straight_speed=300)
    drive.straight(536)
    halte_oben(False)
    hoch_arm.run_until_stalled(-800)
    halte_bloecke(False)
    zange_hoch()


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
grün_weiss_abliefern()
blaue_steine_im_käfig()
gelbe_im_käfig()
gelbe_versorgen()
dreieckskelle_versorgt()
#blaue_bloecke_aufnehmen()
#neu