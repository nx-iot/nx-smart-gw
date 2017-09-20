#! /usr/bin/python

#from xbee import XBee, ZigBee
import serial
import time

ser = serial.Serial('/dev/ttyS1', 38400)
COMMAND=[]
COMMAND.append(''.join(chr(x) for x in [0x7E, 0x00, 0x04, 0x08, 0x01, 0x41, 0x49, 0x6C]))
COMMAND.append(''.join(chr(x) for x in [0x7E, 0x00, 0x04, 0x08, 0x01, 0x53, 0x4C, 0x57]))
COMMAND.append(''.join(chr(x) for x in [0x7E, 0x00, 0x04, 0x08, 0x01, 0x53, 0x48, 0x5B]))

str_cmd=0


while True:
    if str_cmd < 3:
        ser.write(COMMAND[str_cmd])
        str_cmd=str_cmd+1

    time.sleep(1)
    reps=[]
    while ser.inWaiting() > 0::
        s=ser.read(1)
        reps.append(s)
        #if s = 0x
    #bytesToRead = ser.inWaiting()
    #print bytesToRead
    #reps=ser.read(100)
    print reps