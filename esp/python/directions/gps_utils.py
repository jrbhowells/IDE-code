'''
Utilities to control GPS module

J Howells / IDE Group 1
Dyson School of Design Engineering
26/5/2022
'''

import getter

# Return handler
def handleReturn():
    global pts
    global ptr

    getter.ioPostWithCo(ptr/len(pts) * 100, pts[ptr], 'ide-progress')

# Initialise GPS
def GPSInit():
    pass

# Read GPS data and return [lat, lon]
def GPSRead():
    global pts
    global ptr
    '''INCOMPLETE'''
    handleReturn()

# Dummy initialise GPS
def dummyInit():
    global pts
    global ptr
    global value
    global oldVal

    value = oldVal = str(getter.ioGetWithID('ide-dummy-advance'))

    ptr = 1

    with open('sample-cycle.txt', 'r') as f:
        pts = f.readlines()
        f.close()
    
    for i in range(len(pts)):
        pts[i] = pts[i].replace('\n','')
        pts[i] = pts[i].replace('[','')
        pts[i] = pts[i].replace(']','')
        pts[i] = pts[i].split(',')

        for j in range(len(pts[i])):
            pts[i][j] = float(pts[i][j])
    
    handleReturn()
    
    return pts[0]


# Return dummy [lat, lon] object from sample-cycle.txt
def dummyRead():
    global pts
    global ptr
    global value
    global oldVal

    value = str(getter.ioGetWithID('ide-dummy-advance'))

    if oldVal != value:
        ptr += 1
        handleReturn()

    oldVal = value

    return pts[ptr]
