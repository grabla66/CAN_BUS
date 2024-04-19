#############################################################################################################
## Date        :  2024.04.17
## Environment :  Hardware            -- Raspberry Pi 4
##                SYstem of RPI       -- Debian GNU/Linux 12 (bookworm)
##                Version of Python   -- Python 3.7.3(Default in the system)
##                Kernel              -- Linux 6.6.20+rpt-rpi-v8
##                Architecture        -- arm64
## Toinstall dependencies:
## sudo pip3 install python-can
#############################################################################################################
import os
import can
import time

def can_test():
    #Set CAN0 speed to 1M bps
    os.system('sudo ifconfig can0 down')
    os.system('sudo ip link set can0 type can bitrate 1000000 loopback off')
    os.system("sudo ifconfig can0 txqueuelen 1000")
    os.system('sudo ifconfig can0 up')

    with open('/home/grahamb/combe.csv',newline='') as f:
        print("Reading csv and sending data over can")
        with can.Bus(interface='socketcan', channel='can0') as bus:
            try:
                while True:
                    r = f.readline()
                    if r == '':
                        f.close()
                        print("EOF reached, closing the file")
                        break
                    d1=r.split(',') #seperate all the values
                    eff_frame1 = can.Message(arbitration_id=0x600, data=[int(d1[1]), int(d1[2]), int(d1[3]), int(d1[4]), int(d1[5]), int(d1[6]), int(d1[7]), 2+int(d1[8])],is_extended_id=False)
                    eff_frame4 = can.Message(arbitration_id=0x603, data=[int(d1[10]),int(d1[11]),int(d1[12]),int(d1[13]),int(d1[14]),int(d1[15]),int(d1[16]),int(d1[17])],is_extended_id=False)
                    eff_frame6 = can.Message(arbitration_id=0x605, data=[int(d1[19]),int(d1[20]),int(d1[21]),int(d1[22]),int(d1[23]),int(d1[24]),int(d1[25]),int(d1[26])],is_extended_id=False)
                    eff_frame8 = can.Message(arbitration_id=0x607, data=[int(d1[28]),int(d1[29]),int(d1[30]),int(d1[31]),int(d1[32]),int(d1[33]),int(d1[34]),int(d1[35])],is_extended_id=False)
                    eff_frame9 = can.Message(arbitration_id=0x608, data=[int(d1[37]),int(d1[38]),int(d1[39]),int(d1[40]),int(d1[41]),int(d1[42]),int(d1[43]),int(d1[44])],is_extended_id=False)
                    eff_frame10= can.Message(arbitration_id=0x609, data=[int(d1[46]),int(d1[47]),int(d1[48]),int(d1[49]),int(d1[50]),int(d1[51]),int(d1[52]),int(d1[53])],is_extended_id=False)

                    print(eff_frame1)
                    print(eff_frame4)
                    print(eff_frame6)
                    print(eff_frame8)
                    print(eff_frame9)
                    print(eff_frame10)

                    bus.send(eff_frame1)
                    bus.send(eff_frame4)
                    bus.send(eff_frame6)
                    bus.send(eff_frame8)
                    bus.send(eff_frame9)
                    bus.send(eff_frame10)
                    time.sleep(0.05) #data is exported from lifeview at 20Hz

            except KeyboardInterrupt:
                pass

try:
    while True:
        can_test()
except KeyboardInterrupt:
    pass



