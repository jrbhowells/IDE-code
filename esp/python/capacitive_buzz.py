from machine import Pin, ADC, PWM, TouchPad
import time

m1 = Pin(25, Pin.OUT)
m2 = Pin(26, Pin.OUT)

t1 = TouchPad(Pin(27))
t2 = TouchPad(Pin(13))

print("CapTest")

while (True):
    m1.value(0)
    m2.value(0)
    if (t1.read() < 200):
        m1.value(1)
        print("T1: " + str(t1.read()))
    if (t2.read() < 200):
        m2.value(1)
        print("T2: " + str(t2.read()))
    time.sleep(2)
