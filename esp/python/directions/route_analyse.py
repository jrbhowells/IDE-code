'''
Program controls route analysis and guidance.
Running constantly on ESP32.

J Howells / IDE Group 1
Dyson School of Design Engineering
26/5/2022
'''

from machine import Pin, ADC, PWM
import time
import math

import gps_utils
import buzz_utils
import getter
from vec_utils import createVector, vectorMag, angleBetween, findClosest, sideOf

# Check GPS mode (DUMMY vs GPS)
if str(getter.ioGet('ide-1')) == "GPS":
    from gps_utils import GPSInit
    from gps_utils import GPSRead
else:
    from gps_utils import dummyInit as GPSInit
    from gps_utils import dummyRead as GPSRead


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

prev_loc = GPSInit()

cmd_ptr = 0
dir20 = dir100 = False

buzz_utils.alertUser("ready")

while (True):
    # Get location
    current_loc = GPSRead()

    vec_to_end = createVector(current_loc, data[0][-1])

    # If user is less than 20m from target
    if (vectorMag(vec_to_end) * 111111) < 20:
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
    motion_vec = createVector(prev_loc, current_loc)
    
    if prev_loc != current_loc:
        cmd_point = data[0][cmd_ptr]

        # If command point is behind
        if(angleBetween(motion_vec, createVector(current_loc, cmd_point)) > 160):
            dir20 = dir100 = False
            cmd_ptr += 1
            cmd_point = data[0][cmd_ptr]

        # Find distance to next command point
        dist_to_cmd = vectorMag(createVector(current_loc, cmd_point)) * 111111

        # If the next command point is the last:
        if cmd_ptr == len(data[0]):
            # Set command vector to last point
            cmd_vec = vec_to_end

        else:
            # Find coordinate closest to command point from data[1]
            close_ptr = findClosest(cmd_point, data[1]) + 1

            # Create command vector along next path
            cmd_vec = createVector(cmd_point, data[1][close_ptr])
        
        # Calculate angle between motion and command vectors
        angle = angleBetween(cmd_vec, motion_vec)

        # Calculate which side angle is on
        side = sideOf(cmd_vec, motion_vec)

        

        # If command point is < 20m ahead
        if(dist_to_cmd < 20 and dir20 == False):
            dir20 = True
            buzz_utils.directUser(side, angle)

        # If command point is 20 < D < 100m ahead
        elif(dist_to_cmd < 100 and dir100 == False):
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

        1. If cmd_point is last cmd_point,
            1. Guide user to last point

        2. Else:
            1. Find coordinate closest to command point from data[1]
            2. Create command vector: nextPoint-cmdPoint.

        3. Calculate angle between direction and command vectors (dot product)
        4. Calculate direction of turn

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
