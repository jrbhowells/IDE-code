from machine import Pin, SoftI2C, UART
from micropyGPS import MicropyGPS
import time
'''from ssd1306 import SSD1306_I2C''' 

def main():
    uart = UART(1, rx=17, tx=16, baudrate=9600, bits=8, parity=None, stop=1, timeout=5000, rxbuf=1024)
    gps = MicropyGPS()
    '''i2c = SoftI2C(scl=Pin(22), sda=Pin(21), freq=400000) 
    oled = SSD1306_I2C(128, 64, i2c, addr=0x3C)
    '''
    led = Pin(2, Pin.OUT)
    
    while True:
        buf = uart.readline()
        try: print(buf)
        except: print('no_print_buf')

        try:
            for char in buf:
                gps.update(chr(char))  # Note the conversion to to chr, UART outputs ints normally

            print('UTC Timestamp:', gps.timestamp)
            print('Date:', gps.date_string('long'))
            print('Satellites:', gps.satellites_in_use)
            print('Altitude:', gps.altitude)
            print('Latitude:', gps.latitude)
            print('Longitude:', gps.longitude_string())
            print('Horizontal Dilution of Precision:', gps.hdop)
            print()
            
            '''oled.fill(0)
            oled.text('Date:{}'.format(gps.date_string('s_mdy')),0,0)
            oled.text('Sat:{}'.format(gps.satellites_in_use),0,10)
            oled.text('Alt:{}'.format(gps.altitude),0,20)
            oled.text('{}'.format(gps.latitude_string()),0,35)
            oled.text('{}'.format(gps.longitude_string()),0,45)
            oled.show()'''
        
        except:
            print("Error")
            time.sleep(1)
            
        led.value(not led.value())

        
# def startGPSthread():
#     _thread.start_new_thread(main, ())

if __name__ == "__main__":
  print('...running main, GPS testing')
  main()