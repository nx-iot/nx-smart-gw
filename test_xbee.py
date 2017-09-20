#! /usr/bin/python

#from xbee import XBee, ZigBee
import serial
import time

ser = serial.Serial('/dev/ttyS1', 38400)
AI_COMMAND = ''.join(chr(x) for x in [0x7E, 0x00, 0x04, 0x08, 0x01, 0x41, 0x49, 0x6C])
SL_COMMAND  = ''.join(chr(x) for x in [0x7E, 0x00, 0x04, 0x08, 0x01, 0x53, 0x4C, 0x57])
SH_COMMAND   = ''.join(chr(x) for x in 0x7E, 0x00, 0x04, 0x08, 0x01, 0x53, 0x48, 0x5B])

ser.send(AI_COMMAND)
time.sleep(1)
while ser.inWaiting() > 0:
    print ser.read(1)


ser.send(SL_COMMAND)
time.sleep(1)
while ser.inWaiting() > 0:
    print ser.read(1)


ser.send(SH_COMMAND)
time.sleep(1)
while ser.inWaiting() > 0:
    print ser.read(1)