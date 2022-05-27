import network
from machine import Pin, ADC, PWM
import time


def Wifi_Connect():
    led = Pin(2, Pin.OUT)

    station = network.WLAN(network.STA_IF)

    station.active(True)

    station.connect("JH-TCD", "ogler8774")

    time.sleep(3)

    if (station.isconnected()):
        led.value(1)
        time.sleep(1)
        led.value(0)
        time.sleep(1)
        led.value(1)
        time.sleep(1)
        led.value(0)
    else:
        led.value(1)
        time.sleep(5)
        led.value(0)
