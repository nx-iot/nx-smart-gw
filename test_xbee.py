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
        print COMMAND[str_cmd]
        ser.write(COMMAND[str_cmd])
        str_cmd=str_cmd+1

    time.sleep(1)
    reps=[]
    start_b=0
    start_c=0
    stop=True
    while stop:
        s=ser.read(1)
        if s=0x7e:
            resps=[]
            start_b=1
            start_c=0
        else if start_b=1:
            start_b=2
        else if start_b=2:
            start_b=s
        else if start_b+1<start_c:
            start_c=start_c+1 
            stop=False
            start_b=0
            start_c=0    
        reps.append(s)
        #if s = 0x
    #bytesToRead = ser.inWaiting()
    #print bytesToRead
    #reps=ser.read(100)
    print reps