from machine import Pin, ADC, PWM, TouchPad
import time
import getter

m1 = Pin(25, Pin.OUT)
m2 = Pin(26, Pin.OUT)

def p1():
    pass

def p2():
    pass

def p3():
    pass

def p4():
    pass

def p5():
    pass

value = oldVal = RoldVal = str(getter.ioGetWithID('buzz-test'))

while (True):
    value = str(getter.ioGetWithID('buzz-test'))

    if oldVal != value and oldVal != RoldVal:
        if value == 1:
            p1()
        elif value == 2:
            p2()
        elif value == 3:
            p3()
        elif value == 4:
            p4()
        elif value == 5:
            p5()

    RoldVal = oldVal
    oldVal = value
    value = str(getter.ioGetWithID('buzz-test'))