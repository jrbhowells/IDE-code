import network
from machine import Pin, ADC, PWM
import time


def WifiConnect():
    led = Pin(2, Pin.OUT)

    station = network.WLAN(network.STA_IF)

    station.active(True)

    station.connect("JH-TCD", "ogler8774")

    while not station.isconnected():
        print(".", end="")

    led.value(1)
    time.sleep(1)
    led.value(0)
    time.sleep(1)
    led.value(1)
    time.sleep(1)
    led.value(0)
