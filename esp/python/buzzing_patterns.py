from machine import Pin, ADC, PWM, TouchPad
import time

m1 = Pin(25, Pin.OUT)
m2 = Pin(26, Pin.OUT)

t1 = TouchPad(Pin(27))
t2 = TouchPad(Pin(13))

print("CapTest")
short_buzz = 50
medium_buzz = 100
long_buzz = 200

m1.value(0)

def side_1(): 
    ## 3 pulses, 3 pulses and one long one

    # ON 
    m1.value(1)
    print("buzz")
    time.sleep(short_buzz)
    #OFF 
    m1.value(0)
    time.sleep(short_buzz)
    #ON 
    m1.value(1)
    print("buzz")
    time.sleep(short_buzz)
    #OFF
    m1.value(0)
    time.sleep(short_buzz)
    #ON 
    m1.value(1)
    print("buzz")
    time.sleep(short_buzz)
    #OFF
    m1.value(0)
    time.sleep(short_buzz)

    # ON 
    m1.value(1)
    print("buzz")
    time.sleep(short_buzz)
    #OFF 
    m1.value(0)
    time.sleep(short_buzz)
    #ON 
    m1.value(1)
    print("buzz")
    time.sleep(short_buzz)
    #OFF
    m1.value(0)
    time.sleep(short_buzz)
    #ON 
    m1.value(0)
    time.sleep(short_buzz)
    #OFF
    m1.value(0)
    time.sleep(short_buzz)


    # ON 
    m1.value(1)
    print("buzz")
    time.sleep(short_buzz)
    #OFF 
    m1.value(0)
    time.sleep(short_buzz)
    #ON 
    m1.value(1)
    print("buzz")
    time.sleep(short_buzz)
    #OFF
    m1.value(0)
    time.sleep(short_buzz)
    #ON 
    m1.value(0)
    time.sleep(short_buzz)
    #OFF
    m1.value(0)
    time.sleep(short_buzz)

    #ON - HOLD
    m1.value(1)
    print("buzzzzzzzz")
    time.sleep(long_buzz)
    m1.value(0)


def side_2(): 
    ## 3 medium buzzes and one long one

    # ON 
    m1.value(1)
    print("buzz")
    time.sleep(medium_buzz)

    #OFF 
    m1.value(0)
    time.sleep(medium_buzz)

    #ON 
    m1.value(1)
    print("buzz")
    time.sleep(medium_buzz)

    #OFF
    m1.value(0)
    time.sleep(medium_buzz)

    #ON 
    m1.value(0)
    time.sleep(medium_buzz)

    #OFF
    m1.value(0)
    time.sleep(medium_buzz)

    #ON - HOLD
    m1.value(1)
    print("buzzzzzzzz")
    time.sleep(long_buzz)
    m1.value(0)


def side_3(): 
    ## 2 long buzzes


    #ON 
    m1.value(1)
    print("buzz")
    time.sleep(long_buzz)

    #OFF
    m1.value(0)
    time.sleep(medium_buzz)

    #ON 
    m1.value(1)
    rint("buzz")
    time.sleep(long_buzz)

    #OFF
    m1.value(0)
    time.sleep(medium_buzz)

    #ON - HOLD
    m1.value(1)
    print("buzzzzzzzz")
    time.sleep(long_buzz)
    m1.value(0)

def side_4(): 
    ## 3 long buzzes

    # ON 
    m1.value(1)
    print("buzz")
    time.sleep(long_buzz)

    #OFF 
    m1.value(0)
    time.sleep(medium_buzz)

    #ON 
    m1.value(1)
    print("buzz")
    time.sleep(long_buzz)

    #OFF
    m1.value(0)
    time.sleep(medium_buzz)

    #ON 
    m1.value(1)
    rint("buzz")
    time.sleep(long_buzz)

    #OFF
    m1.value(0)
    time.sleep(medium_buzz)

    #ON - HOLD
    m1.value(1)
    print("buzzzzzzzz")
    time.sleep(long_buzz)
    m1.value(0)

def side_5 (): 
    ## triple buzzes getting faster


    # speed = short buzz
    # ON 
    m1.value(1)
    print("buzz")
    time.sleep(short_buzz)

    #OFF 
    m1.value(0)
    time.sleep(short_buzz)

    #ON 
    m1.value(1)
    print("buzz")
    time.sleep(short_buzz)

    #OFF
    m1.value(0)
    time.sleep(short_buzz)

    #ON 
    m1.value(1)
    rint("buzz")
    time.sleep(short_buzz)

    #OFF
    m1.value(0)
    time.sleep(short_buzz)

    
    #speed x2 

    # ON 
    m1.value(1)
    print("buzz")
    time.sleep(short_buzz/2)

    #OFF 
    m1.value(0)
    time.sleep(short_buzz/2)

    #ON 
    m1.value(1)
    print("buzz")
    time.sleep(short_buzz/2)

    #OFF
    m1.value(0)
    time.sleep(short_buzz/2)

    #ON 
    m1.value(1)
    rint("buzz")
    time.sleep(short_buzz/2)

    #OFF
    m1.value(0)
    time.sleep(short_buzz/2)

      #speed x3

    # ON 
    m1.value(1)
    print("buzz")
    time.sleep(short_buzz/3)

    #OFF 
    m1.value(0)
    time.sleep(short_buzz/3)

    #ON 
    m1.value(1)
    print("buzz")
    time.sleep(short_buzz/3)

    #OFF
    m1.value(0)
    time.sleep(short_buzz/3)

    #ON 
    m1.value(1)
    rint("buzz")
    time.sleep(short_buzz/3)

    #OFF
    m1.value(0)
    time.sleep(short_buzz/3)
    

    # speed x4 

    # ON 
    m1.value(1)
    print("buzz")
    time.sleep(short_buzz/4)

    #OFF 
    m1.value(0)
    time.sleep(short_buzz/4)

    #ON 
    m1.value(1)
    print("buzz")
    time.sleep(short_buzz/4)

    #OFF
    m1.value(0)
    time.sleep(short_buzz/4)

    #ON 
    m1.value(1)
    rint("buzz")
    time.sleep(short_buzz/4)

    #OFF
    m1.value(0)
    time.sleep(short_buzz/4)    

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


    ## time.sleep() = delay 
    ## make each pattern a function 