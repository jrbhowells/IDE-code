from machine import Pin, ADC, PWM, TouchPad
import time

m1 = Pin(25, Pin.OUT)
m2 = Pin(26, Pin.OUT)

t1 = TouchPad(Pin(27))
t2 = TouchPad(Pin(13))

m1.value(0)

####### SIDE ####### 

def side_1(): 
    global m1
    global m2
    ## 3 pulses, 3 pulses and one long one
    short_buzz = 0.1
    medium_buzz = 0.7
    long_buzz = 3

    time.sleep(5)

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

    #Interval 
    time.sleep(medium_buzz)

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

    #Interval 
    time.sleep(medium_buzz)

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

    #Interval 
    time.sleep(medium_buzz)

    #ON - HOLD
    m1.value(1)
    print("buzzzzzzzz")
    time.sleep(long_buzz)
    print("end")
    m1.value(0)
    return

def side_2(): 
    global m1
    global m2
    ## 3 medium buzzes and one long one
    medium_buzz = 0.7
    long_buzz = 3

    time.sleep(5)

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
    m1.value(1)
    print("buzz")
    time.sleep(medium_buzz)

    #OFF
    m1.value(0)
    time.sleep(medium_buzz)

    #ON - HOLD
    m1.value(1)
    print("buzzzzzzzz")
    time.sleep(long_buzz)
    m1.value(0)
    print("end")
    return

def side_3(): 
    global m1
    global m2
    ## 2 long buzzes
    long_buzz = 3
    medium_buzz = 0.7 
    time.sleep(5)

    #ON 
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

    #ON - HOLD
    m1.value(1)
    print("buzzzzzzzz")
    time.sleep(long_buzz)
    m1.value(0)
    return

def side_4(): 
    global m1
    global m2
    ## 3 long buzzes
    medium_buzz = 0.7
    long_buzz = 3

    time.sleep(2)
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
    print("buzz")
    time.sleep(long_buzz)

    #OFF
    m1.value(0)
    time.sleep(medium_buzz)

    #ON - HOLD
    m1.value(1)
    print("buzzzzzzzz")
    time.sleep(long_buzz)
    m1.value(0)
    return

def side_5 (): 
    global m1
    global m2
    ## triple buzzes getting faster
    short_buzz = 0.5
    medium_buzz = 0.7
    time.sleep(5)
    # speed = short buzz
    # ON
    m1.value(1)
    print("on")
    time.sleep(short_buzz)

    #OFF 
    m1.value(0)
    print("off")
    time.sleep(short_buzz)

    #ON 
    m1.value(1)
    print("on")
    time.sleep(short_buzz)

    #OFF
    m1.value(0)
    print("off")
    time.sleep(short_buzz)

    #ON 
    m1.value(1)
    print("on")
    time.sleep(short_buzz)

    #OFF
    m1.value(0)
    print("off")
    time.sleep(short_buzz)


    #Interval 
    time.sleep(medium_buzz)
    
    #speed x2 

    # ON 
    m1.value(1)
    print("on")
    time.sleep(short_buzz/2)

    #OFF 
    m1.value(0)
    print("off")
    time.sleep(short_buzz/2)

    #ON 
    m1.value(1)
    print("on")
    time.sleep(short_buzz/2)

    #OFF
    m1.value(0)
    print("off")
    time.sleep(short_buzz/2)

    #ON 
    m1.value(1)
    print("on")
    time.sleep(short_buzz/2)

    #OFF
    m1.value(0)
    print("off")
    time.sleep(short_buzz/2)

    #Interval 
    time.sleep(medium_buzz)

    #speed x3

    # ON 
    m1.value(1)
    print("on")
    time.sleep(short_buzz/3)

    #OFF 
    m1.value(0)
    print("off")
    time.sleep(short_buzz/3)

    #ON 
    m1.value(1)
    print("on")
    time.sleep(short_buzz/3)

    #OFF
    m1.value(0)
    print("off")
    time.sleep(short_buzz/3)

    #ON 
    m1.value(1)
    print("on")
    time.sleep(short_buzz/3)

    #OFF
    m1.value(0)
    print("off")
    time.sleep(short_buzz/3)

    #Interval 
    time.sleep(medium_buzz)
    

    # speed x4 

    # ON 
    m1.value(1)
    print("on")
    time.sleep(short_buzz/4)

    #OFF 
    m1.value(0)
    print("off")
    time.sleep(short_buzz/4)

    #ON 
    m1.value(1)
    print("on")
    time.sleep(short_buzz/4)

    #OFF
    m1.value(0)
    print("off")
    time.sleep(short_buzz/4)

    # ON 
    m1.value(1)
    print("on")
    time.sleep(short_buzz/4)

    #OFF 
    m1.value(0)
    print("off")
    time.sleep(short_buzz/4)

    #ON 
    m1.value(1)
    print("on")
    time.sleep(short_buzz/4)

    #OFF
    m1.value(0)
    print("off")
    time.sleep(short_buzz/4)

    # ON 
    m1.value(1)
    print("on")
    time.sleep(short_buzz/4)

    #OFF 
    m1.value(0)
    print("off")
    time.sleep(short_buzz/4)

    #ON 
    m1.value(1)
    print("on")
    time.sleep(short_buzz/4)

    #OFF
    m1.value(0)
    print("off")
    time.sleep(short_buzz/4)

    #ON 
    m1.value(1)
    print("on")
    time.sleep(short_buzz/4)

    #OFF
    m1.value(0)
    print("off") 
    time.sleep(short_buzz/4)    
    print("end")
    return


####### STRAIGHT ####### 

def straight_1():
    global m1
    global m2
    #long buzz on both sides
    long_buzz = 3
    short_buzz = 0.1

    time.sleep(5)
    #ON 
    print("on")
    m1.value(1)
    m2.value(1)
    time.sleep(long_buzz)

    #OFF 
    print("off")
    m1.value(0)
    m2.value(0)
    time.sleep(short_buzz)
    return

def straight_2():
    global m1
    global m2
    # 3 quiz buzzes 
    short_buzz = 0.1

    time.sleep(5)
    # ON 
    print("buzz 1 ")
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

def straight_3():
    global m1
    global m2
    ## 2 long buzzes
    long_buzz = 3
    medium_buzz = 0.7 

    time.sleep(5)
    #ON 
    print("on")
    m1.value(1)
    m2.value(1)
    time.sleep(long_buzz)

    #OFF
    print("off")
    m1.value(0)
    m2.value(0)
    time.sleep(medium_buzz)

    #ON 
    print("on")
    m1.value(1)
    m2.value(1)
    time.sleep(long_buzz)

    #OFF
    print("off")
    m1.value(0)
    m2.value(0)
    time.sleep(medium_buzz)
    return
   

###### ROUNDABOUT ###### 

def roundabout_1():
    global m1
    global m2

    short_buzz = 0.1
    medium_buzz = 0.7
    long_buzz = 3

    time.sleep(7)

    # ON 
    m1.value(1)
    print("buzz 1 ")
    time.sleep(short_buzz)
    #OFF 
    m1.value(0)
    time.sleep(short_buzz)
    #ON 
    m1.value(1)
    print("buzz 2")
    time.sleep(short_buzz)
    #OFF
    m1.value(0)
    time.sleep(short_buzz)
    #ON 
    m1.value(1)
    print("buzz 3")
    time.sleep(short_buzz)
    #OFF
    m1.value(0)
    time.sleep(short_buzz)

    #Interval 
    time.sleep(medium_buzz)


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

    #ON - HOLD
    m1.value(1)
    print("buzzzzzzzz")
    time.sleep(long_buzz)
    print("end")
    m1.value(0)
    return

def roundabout_2(): 
    global m1
    global m2
    ## speeds up as you get closer to the turn
    short_buzz = 0.7
    long_buzz = 3

    time.sleep(5)

    # speed = short buzz
    # ON 
    m1.value(1)
    print("on")
    time.sleep(short_buzz)

    #OFF 
    m1.value(0)
    print("off")
    time.sleep(long_buzz)

    #ON 
    m1.value(1)
    print("on")
    time.sleep(short_buzz)

    #OFF
    m1.value(0)
    print("off")
    time.sleep(long_buzz/2)

    #ON 
    m1.value(1)
    print("on")
    time.sleep(short_buzz)

    #OFF
    m1.value(0)
    print("off")
    time.sleep(long_buzz/3)

    #ON 
    m1.value(1)
    print("on")
    time.sleep(short_buzz)

    #OFF
    m1.value(0)
    print("off")
    time.sleep(long_buzz/4)


    # ON 
    m1.value(1)
    print("on")
    time.sleep(short_buzz)

    #OFF 
    m1.value(0)
    print("off")
    time.sleep(long_buzz/5)

    #ON 
    m1.value(1)
    print("on")
    time.sleep(short_buzz)

    #OFF
    m1.value(0)
    print("off")
    time.sleep(long_buzz/6)
    return

def roundabout_3():
    global m1
    global m2
    #no no yes

    time.sleep(8)
    medium_buzz = 0.7
    short_buzz = 0.1
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

    # ON 
    m1.value(1)
    print("buzz 1 ")
    time.sleep(short_buzz)
    #OFF 
    m1.value(0)
    time.sleep(short_buzz)
    #ON 
    m1.value(1)
    print("buzz 2")
    time.sleep(short_buzz)
    #OFF
    m1.value(0)
    time.sleep(short_buzz)
    #ON 
    m1.value(1)
    print("buzz 3")
    time.sleep(short_buzz)
    #OFF
    m1.value(0)
    time.sleep(short_buzz)

    # ON 
    m1.value(1)
    print("buzz 1 ")
    time.sleep(short_buzz)
    #OFF 
    m1.value(0)
    time.sleep(short_buzz)
    #ON 
    m1.value(1)
    print("buzz 2")
    time.sleep(short_buzz)
    #OFF
    m1.value(0)
    time.sleep(short_buzz)
    #ON 
    m1.value(1)
    print("buzz 3")
    time.sleep(short_buzz)
    #OFF
    m1.value(0)
    time.sleep(short_buzz)
    return

def roundabout_4(): 
    global m1
    global m2
    #repeat number of turns three times then hold 
    short_buzz = 0.3
    medium_buzz = 1
    long_buzz = 4

    time.sleep(5)
    
    # ON 
    m1.value(1)
    print("buzz 1 ")
    time.sleep(short_buzz)
    #OFF 
    m1.value(0)
    time.sleep(short_buzz)
    #ON 
    m1.value(1)
    print("buzz 2")
    time.sleep(short_buzz)
    #OFF
    m1.value(0)
    time.sleep(short_buzz)
    #ON 
    m1.value(1)
    print("buzz 3")
    time.sleep(short_buzz)
    #OFF
    m1.value(0)
    time.sleep(short_buzz)

    #interval
    print("wait")
    time.sleep(medium_buzz)

    # ON 
    m1.value(1)
    print("buzz 1 ")
    time.sleep(short_buzz)
    #OFF 
    m1.value(0)
    time.sleep(short_buzz)
    #ON 
    m1.value(1)
    print("buzz 2")
    time.sleep(short_buzz)
    #OFF
    m1.value(0)
    time.sleep(short_buzz)
    #ON 
    m1.value(1)
    print("buzz 3")
    time.sleep(short_buzz)
    #OFF
    m1.value(0)
    time.sleep(short_buzz)

    #interval
    print("wait")
    time.sleep(medium_buzz)

    # ON 
    m1.value(1)
    print("buzz 1 ")
    time.sleep(short_buzz)
    #OFF 
    m1.value(0)
    time.sleep(short_buzz)
    #ON 
    m1.value(1)
    print("buzz 2")
    time.sleep(short_buzz)
    #OFF
    m1.value(0)
    time.sleep(short_buzz)
    #ON 
    m1.value(1)
    print("buzz 3")
    time.sleep(short_buzz)
    #OFF
    m1.value(0)
    time.sleep(short_buzz)

    #interval
    print("wait")
    time.sleep(medium_buzz)

    #HOLD 
    m1.value(1)
    print("buzzzzz")
    time.sleep(long_buzz)
    m1.value(0)
    return


    
    
    
    ## time.sleep() = delay 
    ## make each pattern a function 