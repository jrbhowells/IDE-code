import network
from machine import Pin, SoftI2C, UART
import time
import initpy
import math

import gps_utils
import buzz_utils
import getter
from vec_utils import createVector, vectorMag, angleBetween, findClosest, sideOf

initpy.WifiConnect()

file = 'route_analyse.py'

print(file)
getter.ioPost('File: ' + file, 'ide-terminal')

execfile(file)