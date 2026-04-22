from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch, runt_task, multitask

hub = PrimeHub()

rechter_arm = motor(Port.C, Direction.#je nachdem, [Zahnräder ] [ Zahnräder])
linker_arm = motor(Port.D, Direction.#je nachdem, [Zahnräder ] [ Zahnräder])

#Ein bisschen eine unnötige Motoren einstellen
def r_config.control.limits(speed, acceleration, kraft):
    rechter_arm(speed, acceleraction, kraft)
def l_config.control.limits(speed, acceleration, kraft):
    linker_arm(speed, acceleration, kraft)

#async ist für await
async def Kalibrieren():
    #Kalibriert den Roboter Arm auf physische Limit
    await rechter_arm.run_until_stalled(-300, duty_limit=50)
    rechter_arm.reset_angle(0)

#Der Roboter Synchronisiert jetzt den Arm
run_task(Kalibrieren())
#Einstellen des Motoren
r_config(1000, 10, 1000)
#Roboter Arm bewegen
rechter_arm.run_angle( )
