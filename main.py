#!/usr/bin/env python3
from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_B, SpeedPercent, MoveTank
from ev3dev2.sensor import INPUT_1
from ev3dev2.sensor.lego import TouchSensor
from ev3dev2.led import Leds


from ev3dev2.sound import Sound

sound = Sound()
sound.speak('Welcome to the E V 3 dev project!')
sound.speak('Hi Tim id like to drive')

#!/usr/bin/env python3
# so that script can be run from Brickman

from ev3dev.ev3 import *
from time import sleep


#text to speech
Sound.speak('Hello, my name is E V 3!').wait()
m = LargeMotor('outC')
m2 = LargeMotor('outB')

m.run_to_rel_pos(position_sp=-3600, speed_sp=900, stop_action="hold")
m2.run_to_rel_pos(position_sp=-3600, speed_sp=900, stop_action="hold")

sleep(5)   # Give the motor time to move
m.run_to_rel_pos(position_sp=36000, speed_sp=900, stop_action="hold")
m2.run_to_rel_pos(position_sp=36000, speed_sp=900, stop_action="hold")
sleep(5)   # Give the motor time to move