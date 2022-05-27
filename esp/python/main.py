import network
from machine import Pin, SoftI2C, UART
from micropyGPS import MicropyGPS
import time
import initpy

initpy.Wifi_Connect()

file = 'gps.py'

print(file)

execfile(file)