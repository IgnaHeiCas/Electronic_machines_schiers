#pybricksdev run ble main.py

from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop, Axis
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch, hub_menu, run_task, multitask

hub = PrimeHub()
# === Setup ===
#Fahren
l_motor = Motor(Port.E, Direction.COUNTERCLOCKWISE, profile=5)
r_motor = Motor(Port.F, profile=5)
#Arme
vorne_arm = Motor(Port.D, positive_direction=Direction.COUNTERCLOCKWISE)
hinten_arm = Motor(Port.C, positive_direction=Direction.COUNTERCLOCKWISE)
zangen_arm = Motor(Port.A, gears=[12, 20])
#Farbsensor
farb = ColorSensor(Port.B)

drive = DriveBase(l_motor, r_motor, wheel_diameter=62.5, axle_track=196.5)

drive.use_gyro(True)

drive.settings(straight_speed=500, straight_acceleration=1000, turn_rate=300, turn_acceleration=1000)

#zange
async def halte_bloecke(laufen):

    if laufen:
        zangen_arm.dc(100)
    else:
        zangen_arm.brake()

async def zange_hoch(laufen):

    if laufen:
        zangen_arm.dc(-100)
    else:
        zangen_arm.brake()

async def zange_genau(grad):
        zangen_arm.run_angle(-800, grad)

#vorne
async def vorne_halte_oben(laufen):
    if laufen:
        vorne_arm.dc(800)
    else:
        vorne_arm.brake()

async def vorne_halte_unten(laufen):
    if laufen:
        vorne_arm.run(-800)
    else:
        vorne_arm.brake()

async def vorne_genau(x,grad):
    vorne_arm.run_angle(x, grad)

#hinten
async def hinten_halte_oben(laufen):
    if laufen:
        hinten_arm.dc(800)
    else:
        hinten_arm.brake()

async def hinten_halte_unten(laufen,x):
    if laufen:
        hinten_arm.run(x)
    else:
        hinten_arm.brake()

async def hinten_genau(grad):
    hinten_arm.run_angle(800, grad)

#messen
def reflection_messen(x):
    while x:
        print(farb.reflection())

async def batterie_messen(x):
    while x:
        print(hub.battery.voltage())
        #max 8400

async def gyro_status():
    while True:
        status = hub.imu.heading()
        print("IMU Status:", status)
        await wait(50)

#fahren
async def folge_linie_rechts(v,s,t):
    drive.reset()
    
    target = t  
    Kp = 1  
    Kd = 0.2
    eprev = 0

    while abs(drive.distance()) < s:
        refl= await farb.reflection()
        error = refl - target
        derivative = error - eprev
        
        u = (Kp * error) + (Kd * derivative)
        
        drive.drive(speed=v,turn_rate=-u)

        eprev = error
        await wait(10)

    drive.stop()

async def folge_linie_links(v,s,t):
    drive.reset()
    
    target = t
    Kp = 1  
    Kd = 0.2
    eprev = 0

    while abs(drive.distance()) < s:
        refl= await farb.reflection()
        error = refl - target
        derivative = error - eprev
        
        u = (Kp * error) + (Kd * derivative)
        
        drive.drive(speed=v,turn_rate=u)

        eprev = error
        await wait(10)

    drive.stop()

async def bis_farbe(x):
    drive.drive(30,0)

    while await farb.reflection() >= x:
        print(farb.reflection())
        await wait(10)

    drive.stop()

async def bis_farbe_oben(x):
    drive.drive(30,0)

    while await farb.reflection() <= x:
        print(farb.reflection())
        await wait(10)

    drive.stop()

async def bis_farbe_rueckwaerts(x):
    drive.drive(-30,0)

    while await farb.reflection() >= x:
        print(farb.reflection())
        await wait(10)

    drive.stop()


# === Programme ===

async def gelbe_bloecke_versorgen():
    hub.imu.reset_heading(0)
    await multitask(drive.straight(190),hinten_genau(-45))
    await bis_farbe_oben(90)
    await drive.straight(-20)
    await multitask(zange_genau(-120),vorne_halte_unten(True))
    await halte_bloecke(True)
    await wait(500)
    await vorne_halte_unten(False)
    await multitask(vorne_genau(1000,45),vorne_halte_oben(True))
    await wait(100)
    await drive.turn(60)
    drive.settings(straight_speed=1000)
    await drive.straight(640)
    drive.settings(straight_speed=500)
    await bis_farbe(30)
    await drive.straight(45)
    await drive.turn(31)
    await drive.straight(230)
    drive.use_gyro(False)
    drive.drive(500,0)
    await wait(500)
    drive.stop()
    hub.imu.reset_heading(0)
    drive.use_gyro(True)
    await vorne_halte_oben(False)
    await vorne_genau(1000,-45)
    await wait(500)
    #await halte_bloecke(False)
    #await wait(500)
    await zange_genau(80)
    await wait(500)
    await vorne_halte_oben(True)
    await wait(500)

async def blaue_bloecke_aufnehmen():
    await drive.straight(-212)#-210
    await drive.turn(-30)
    drive.settings(straight_speed=1000)
    await drive.straight(-740)#-450
    drive.settings(straight_speed=500)
    #await bis_farbe_rueckwaerts(40)
    #await drive.straight(-252)   
    await drive.turn(-60)
    await drive.straight(170)
    await bis_farbe(55)
    await drive.straight(-20)
    await vorne_halte_oben(False)
    await wait(1000)
    await vorne_halte_unten(True)
    await zange_genau(-120)
    await halte_bloecke(True)
    await wait(500)
    await vorne_halte_unten(False)
    await vorne_halte_oben(True)
    vorne_halte_oben(True)
    await wait(500)

async def spachtel_kessel_versorgen():
    await drive.turn(120)
    await drive.straight(530)
    await drive.turn(-29)
    await folge_linie_rechts(100,150,50)
    hub.imu.reset_heading(0)
    drive.settings(straight_speed=600)
    await drive.straight(395)
    drive.settings(straight_speed=500)
    #await drive.straight(545)
    await drive.turn(-90)
    await hinten_halte_unten(True,-800)
    await wait(350)
    await hinten_halte_unten(False,-800)
    await drive.straight(10)
    await drive.turn(72)
    drive.settings(straight_speed=200)
    await drive.straight(-320)
    drive.settings(straight_speed=500)
    await drive.turn(11)
    drive.settings(straight_speed=1000)
    await drive.straight(965)
    drive.settings(straight_speed=500)
    await drive.turn(50)
    await hinten_genau(120)
    await wait(500)

async def grün_weiss_aufnehmen():
    await drive.turn(68)
    await drive.straight(-390)#405
    await bis_farbe_rueckwaerts(30)
    await drive.straight(18)
    await drive.turn(73)
    await drive.straight(-90)#-75
    await hinten_halte_unten(True,-800)
    await wait(500)
    await drive.turn(-15)
    await drive.turn(30)
    await drive.turn(-15)
    await drive.straight(200)
    await drive.straight(-30)
    drive.settings(turn_acceleration=250)
    await drive.turn(105)#109
    await wait(300)
    await drive.turn(-14)#-15
    drive.settings(turn_acceleration=1000)
    await hinten_genau(160)
    await hinten_halte_unten(False,-800)
    await hinten_genau(120)
    await wait(500)
    drive.settings(straight_acceleration=250)
    await drive.straight(-400)
    drive.settings(straight_acceleration=1000)
    await hinten_halte_oben(False)
    await hinten_halte_unten(True,-800)
    await wait(400)
    await drive.turn(-75)
    await hinten_halte_unten(False,-800)
    await wait(300)
    await hinten_genau(120)
    await wait(500)
    drive.settings(straight_acceleration=250)
    await drive.straight(-190)
    drive.settings(straight_acceleration=1000)
    await hinten_halte_oben(False)
    await hinten_halte_unten(True,-800)
    await wait(500)
    await drive.turn(-15)
    #await drive.turn(30)
    #await drive.turn(-15)
    await drive.turn(50)#35

async def grün_weiss_blaue_bloecke_versorgen():
    drive.settings(straight_speed=1000)
    await drive.straight(525)
    drive.settings(straight_speed=500)
    await bis_farbe(30)
    await drive.straight(35)
    await drive.turn(-40)#-49
    drive.settings(straight_acceleration=100)
    await folge_linie_rechts(100,190,50)
    await drive.turn(-3)
    await drive.straight(180)
    drive.settings(straight_acceleration=1000)
    drive.use_gyro(False)
    drive.drive(500,0)
    await wait(500)
    drive.stop()
    hub.imu.reset_heading(0)
    drive.use_gyro(True)
    vorne_halte_oben(False)
    await vorne_genau(1000,-45)
    await wait(500)
    await halte_bloecke(False)
    await zange_genau(60)
    await wait(500)
    await zange_hoch(True)
    await wait(500)
    await zange_hoch(False)
    await multitask(vorne_genau(1000,45),vorne_halte_oben(True))
    await wait(500)
    drive.settings(straight_speed=1000)
    await drive.straight(-530)
    await drive.turn(180)
    await drive.straight(-285)
    drive.settings(straight_speed=500)
    await drive.turn(37)#36
    await drive.straight(-275)
    await hinten_halte_unten(False,-800)
    await hinten_genau(120)
    await drive.straight(170)
    await hinten_halte_unten(True,-800)
    await wait(500)
    await drive.straight(70)
    await drive.turn(-37)#-36
    await drive.straight(200)
    await drive.turn(10)
    await drive.turn(-20)
    await drive.turn(10)
    await hinten_halte_unten(False,-800)
    await hinten_genau(120)
    await wait(500)
    drive.settings(straight_acceleration=250)
    await drive.straight(-268)#275
    drive.settings(straight_acceleration=1000)
    await hinten_halte_unten(True,-150)
    await wait(800)
    await drive.straight(-20)
    await wait(500)
    await drive.straight(20)
    await wait(500)
    await hinten_halte_unten(False,-800)
    await hinten_genau(120)
    await wait(500)
    drive.settings(straight_acceleration=250)
    await drive.straight(-60)#-40
    drive.settings(straight_acceleration=1000)
    await drive.straight(180)#160
    await wait(1000)

async def gelb_blau_aufnehmen():
    #await drive.straight(100)
    await folge_linie_links(100,107,50)
    hub.imu.reset_heading(0)
    await drive.turn(50)
    drive.settings(straight_speed=1000)
    await drive.straight(750)
    drive.settings(straight_speed=500)
    await drive.turn(70)
    await drive.straight(-80)#-90
    await drive.turn(-29)#-27
    await drive.straight(-90)
    await bis_farbe_rueckwaerts(55)
    await drive.straight(-190)
    await hinten_halte_unten(True,-800)
    await wait(500)
    await drive.straight(-120)
    await hinten_genau(120)
    await wait(1000)
    await drive.straight(-140)
    await hinten_halte_unten(True,-800)
    await wait(500)

async def gelb_versorgen():
    await drive.straight(-50)
    drive.use_gyro(False)
    drive.drive(-500,0)
    await wait(1000)
    drive.stop()
    hub.imu.reset_heading(0)
    drive.use_gyro(True)
    await drive.straight(85)
    await drive.turn(-160)
    drive.settings(straight_speed=1000)
    await drive.straight(-580)
    drive.settings(straight_speed=500)
    await drive.turn(237)#235
    await vorne_genau(30,-60)
    await wait(500)
    await vorne_halte_unten(True)
    hinten_halte_unten(True,-800)
    await zange_genau(-120)
    await wait(1000)
    await drive.straight(410)
    await drive.turn(28)#29
    await drive.straight(505)#485
    #await bis_farbe(40)
    #await drive.straight(20)
    await drive.turn(-15)
    await folge_linie_links(100,200,50)
    hub.imu.reset_heading(0)
    await drive.straight(-160)
    await drive.turn(-90)
    await drive.straight(-110)
    hinten_halte_unten(False,-800)
    
async def kelle_versorgen():
    await drive.straight(10)
    await hinten_halte_oben(True)
    await wait(1000)
    await drive.straight(150)
    await hinten_halte_unten(True,-800)
    await wait(500)
    await drive.straight(20)
    await drive.turn(99)
    drive.settings(straight_speed=1000)
    await drive.straight(570)
    drive.settings(straight_speed=500)
    await drive.turn(-15)
    await folge_linie_links(100,160,50)
    await bis_farbe(40)
    await drive.turn(-15)
    await drive.straight(40)
    await drive.straight(-40)
    await drive.turn(15)
    await vorne_halte_oben(True)
    await wait(400)
    await drive.straight(-30)

async def blaue_versorgen():
    drive.settings(straight_acceleration=250,turn_acceleration=250)
    await drive.turn(-75)
    await wait(300)
    await drive.turn(15)
    await hinten_halte_oben(True)
    await wait(500)
    await drive.straight(-510)
    await bis_farbe_rueckwaerts(40)
    await drive.turn(63)
    await drive.straight(-250)#-245
    await hinten_halte_unten(True,-150)
    await wait(800)
    await drive.straight(-25)#-20
    await wait(500)
    await drive.straight(20)
    await wait(500)
    await hinten_halte_oben(True)
    await wait(500)
    await drive.straight(-62)#-72
    await wait(100000)

async def main_programme():
    hub.imu.settings(heading_correction=360)
    await gelbe_bloecke_versorgen()
    await blaue_bloecke_aufnehmen()
    await spachtel_kessel_versorgen()
    await grün_weiss_aufnehmen()
    await grün_weiss_blaue_bloecke_versorgen()
    await gelb_blau_aufnehmen()
    await gelb_versorgen()
    await kelle_versorgen()
    await blaue_versorgen()

async def main():
    await multitask(
        gyro_status(),
        main_programme(),
        race=True
    )


run_task(main())












