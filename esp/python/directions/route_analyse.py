'''
Program controls route analysis and guidance.
Running constantly on ESP32.

J Howells / IDE Group 1
Dyson School of Design Engineering
26/5/2022
'''

# from machine import Pin, ADC, PWM
import time
import math

from matplotlib.pyplot import close
import gps_utils
import buzz_utils
from vec_utils import createVector, vectorMag, distanceTo, angleBetween, findClosest

with open("directions.txt", 'r') as file:
    data = file.read()
    file.close()

data = data.split("]],[[")

for i in range(2):

    data[i] = data[i].split("],[")

    for j in range(len(data[i])):
        data[i][j] = data[i][j].replace("[", "")
        data[i][j] = data[i][j].replace("]", "")
        data[i][j] = data[i][j].split(",")

        for k in range(len(data[i][j])):
            data[i][j][k] = float(data[i][j][k])

gps_utils.GPSInit()
prev_loc = gps_utils.GPSRead()

cmd_ptr = 0
dir20 = dir100 = False

buzz_utils.alert("ready")

while (True):
    # Get location
    current_loc = gps_utils.GPSRead()

    # If user is less than 20m from target
    if (vectorMag(createVector(data[0][-1], current_loc)) < 20):
        buzz_utils.alertUser("arrived")
        break

    '''
    This functionality is not yet complete

    # If user is more than 20m from correct path
    if (distanceTo(data[0], current_loc) > 20):
        buzz_utils.alertUser("wrong")
        time.sleep(20)
    '''

    # Create user's direction vector
    motion_vec = createVector(current_loc, prev_loc)

    # Find distance to next command point
    dist = vectorMag(createVector(data[1][cmd_ptr], current_loc))
    
    if (dist < 100):
        # Find coordinate closest to command point from data[1]
        close_ptr = findClosest(data[0][cmd_ptr], data[1])

        # If the closest point is the last point:
        if (close_ptr == len(data[1])):
            # Create command vector to last point
            cmd_vec = createVector(data[1][-1], current_loc)

        else:
            # Create command vector along next path
            cmd_vec = createVector(data[1][close_ptr+1], data[0][cmd_ptr])
        
        # Find distance to next command point
        dist = vectorMag(cmd_vec)
        
        # Calculate angle between motion and command vectors
        angle = angleBetween(motion_vec, cmd_vec)

        # Calculate which side angle is on
        '''###########'''

    # If command point is behind
    if(angle > 160):
        dir20 = dir100 = False
        cmd_ptr += 1

    # If command point is < 20m ahead
    elif(dist < 20 and dir20 == False):
        dir20 = True
        buzz_utils.directUser(side, angle)

    # If command point is 20 < D < 100m ahead
    elif(dist < 100 and dir100 == False):
        dir100 = True
        buzz_utils.directUser(side, angle)

    # Save current as previous location
    prev_loc = current_loc


'''
THEORY:

0. Get current location

1. If user is less than 20m from target, end guidance and alert with alert({string}"arrived")

2. If user is more than 20m from correct path, alert user using alert({string}"wrong")

3. Create user direction vector: Location-prevLocation

4. Find distance to next command point

    4.0. If user is less than 100m from command point
        1. Find coordinate closest to command point from data[1]

        2. If closest point == last point,
            1. Guide user to last point

        3. Else:
            1. Create command vector: nextPoint-cmdPoint.
            2. Calculate angle between direction and command vectors (dot product)

    4.1. If user is past command point (angle to command point > 160deg):
        1. Set dir100 = dir20 = False
        2. Ddvance pointer to next command point

    4.2. If user is within 20m of next command point and dir20 == False,
        1. Direct user using function direct({string}side, {int}angle)
        2. set dir20 = True

    4.3. If user is between 100m and 20m of next command point and dir100 == False,
        1. Direct user using function direct({string}side, {int}angle)
        2. set dir100 = True

'''
