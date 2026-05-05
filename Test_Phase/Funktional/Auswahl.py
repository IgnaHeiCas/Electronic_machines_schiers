from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import hub_menu, wait, StopWatch

hub = PrimeHub()

# Make a menu to choose a letter. You can also use numbers.
selected = hub_menu("1", "2", "3", "4", "5")

# Based on the selection, run a program.
if selected == "1":
    import Fahren

