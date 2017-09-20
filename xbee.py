import XBee, ZigBee
import serial

ser = serial.Serial('/dev/ttyS1', 38400)

# Use an XBee 802.15.4 device
xbee = XBee(ser)
# To use with an XBee ZigBee device, replace with:
# xbee = ZigBee(ser)

# Set remote DIO pin 2 to low (mode 4)
#xbee.remote_at(
 #   dest_addr=b'\x56\x78',
  #  command='D2',
   # parameter=b'\x04')

#xbee.remote_at(
 #   dest_addr=b'\x56\x78',
  #  command='WR')

while True:
    try:
        data = xbee.wait_read_frame() #Get data for later use
        print data # To check what comes in before processing / parsing (already buggered up)
        #addr = repr(data ['source_addr_long']) # Working sort of, but with @y... issue in results
        #file = open('/media/log/senslog.txt','a')
        #value = float(((data['samples'])[0])['adc-0'])
        #num = (value * 3.0) / 1023.0
        #file.write(datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S') + ' ' + str(addr) + ' ' + str(value) + ' ' + str(num) + '\n')
        #print str(datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S') + ' ' + str(addr) + ' ' + str(value) + ' ' + str(num) + '\n')
        #file.close()

    except KeyboardInterrupt:
        break