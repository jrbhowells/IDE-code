import network
from machine import Pin, ADC, PWM
import time
import getter


def WifiConnect():
    led = Pin(2, Pin.OUT)

    station = network.WLAN(network.STA_IF)

    station.active(True)

    station.connect("JH-TCD", "ogler8774")

    print('Connecting WiFi... ', end="")

    while not station.isconnected():
        print("", end="")
    
    print("WiFi Connected.")
    getter.ioPost("WiFi Connected.", 'ide-terminal')

    led.value(1)
    time.sleep(1)
    led.value(0)
    time.sleep(1)
    led.value(1)
    time.sleep(1)
    led.value(0)
