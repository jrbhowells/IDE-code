import network
from machine import Pin, SoftI2C, UART
from micropyGPS import MicropyGPS
import time
import initpy
import getter

initpy.WifiConnect()

file = 'capacitive_buzz.py'

print(file)

execfile(file)