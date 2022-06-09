'''
Utilities to control vibrations

J Howells / IDE Group 1
Dyson School of Design Engineering
26/5/2022
'''

import getter

# Alert users: type can = arrived, wrong, ready
def alertUser(typ):
    print('Alert: ' + typ)
    getter.ioPost('Alert: ' + typ, 'ide-terminal')

# Direct users: side = left/right, 0 < angle < 180
def directUser(side, angle):
    print('Turn ' + str(angle) + 'degrees ' + side)
    getter.ioPost('Turn ' + str(angle) + 'degrees ' + side, 'ide-terminal')
    
