#3 decided buzzing patterns

from machine import Pin, ADC, PWM, TouchPad
import time

m1 = Pin(25, Pin.OUT)
m2 = Pin(26, Pin.OUT)

t1 = TouchPad(Pin(27))
t2 = TouchPad(Pin(13))

m1.value(0)
m2.value(0)


def side_final(motor): 
    ## 3 pulses, 3 pulses and one long one
    ## motor is m1 or m2 depending on side
    short_buzz = 0.1
    medium_buzz = 0.7
    long_buzz = 3

    # ON 
    motor.value(1)
    print("buzz")
    time.sleep(short_buzz)
    #OFF 
    motor.value(0)
    time.sleep(short_buzz)
    #ON 
    motor.value(1)
    print("buzz")
    time.sleep(short_buzz)
    #OFF
    motor.value(0)
    time.sleep(short_buzz)
    #ON 
    motor.value(1)
    print("buzz")
    time.sleep(short_buzz)
    #OFF
    motor.value(0)
    time.sleep(short_buzz)

    #Interval 
    time.sleep(medium_buzz)

    # ON 
    motor.value(1)
    print("buzz")
    time.sleep(short_buzz)
    #OFF 
    motor.value(0)
    time.sleep(short_buzz)
    #ON 
    motor.value(1)
    print("buzz")
    time.sleep(short_buzz)
    #OFF
    motor.value(0)
    time.sleep(short_buzz)
    #ON 
    motor.value(1)
    print("buzz")
    time.sleep(short_buzz)
    #OFF
    motor.value(0)
    time.sleep(short_buzz)

    #Interval 
    time.sleep(medium_buzz)

    # ON 
    motor.value(1)
    print("buzz")
    time.sleep(short_buzz)
    #OFF 
    motor.value(0)
    time.sleep(short_buzz)
    #ON 
    motor.value(1)
    print("buzz")
    time.sleep(short_buzz)
    #OFF
    motor.value(0)
    time.sleep(short_buzz)
    #ON 
    motor.value(1)
    print("buzz")
    time.sleep(short_buzz)
    #OFF
    motor.value(0)
    time.sleep(short_buzz)

    #Interval 
    time.sleep(medium_buzz)

    #ON - HOLD
    motor.value(1)
    print("buzzzzzzzz")
    time.sleep(long_buzz)
    print("end")
    motor.value(0)
    return


def straight_final(): 
    ## 3 pulses on both sides
    global m1
    global m2
    # 3 quiz buzzes 
    short_buzz = 0.1

    
    # ON 
    print("buzz 1")
    m1.value(1)
    m2.value(1)
    time.sleep(short_buzz)
    #OFF 
    m1.value(0)
    m2.value(0)
    time.sleep(short_buzz)
    #ON 
    print("buzz 2")
    m1.value(1)
    m2.value(1)
    time.sleep(short_buzz)
    #OFF
    m1.value(0)
    m2.value(0)
    time.sleep(short_buzz)
    #ON 
    m1.value(1)
    m2.value(1)
    print("buzz 3")
    time.sleep(short_buzz)
    #OFF
    m1.value(0)
    m2.value(0)
    time.sleep(short_buzz)


def roundabout_final(motor, exit_number): 
    # 3 pulses, exit number repeated twice, long buzz
    
    short_buzz = 0.1
    medium_buzz = 0.7
    long_buzz = 3

    # ON 
    motor.value(1)
    print("buzz 1 ")
    time.sleep(short_buzz)
    #OFF 
    motor.value(0)
    time.sleep(short_buzz)
    #ON 
    motor.value(1)
    print("buzz 2")
    time.sleep(short_buzz)
    #OFF
    motor.value(0)
    time.sleep(short_buzz)
    #ON 
    motor.value(1)
    print("buzz 3")
    time.sleep(short_buzz)
    #OFF
    motor.value(0)
    time.sleep(short_buzz)

    #Interval 
    time.sleep(medium_buzz)

    for x in range(exit_number):
        # ON 
        motor.value(1)
        print("buzz")
        time.sleep(medium_buzz)

        #OFF 
        motor.value(0)
        time.sleep(medium_buzz) 

    #ON - HOLD
    motor.value(1)
    print("buzzzzzzzz")
    time.sleep(long_buzz)
    print("end")
    motor.value(0)
    return

    