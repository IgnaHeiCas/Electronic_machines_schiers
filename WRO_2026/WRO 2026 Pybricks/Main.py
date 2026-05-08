from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch, hub_menu

hub = PrimeHub()
hub.system.set_stop_button(None)
#Wenn center button gedrückt wird: Start
while Button.CENTER not in hub.buttons.pressed():
    wait(10)
hub.system.set_stop_button(Button.BLUETOOTH)
import Teil_1