#############################################################################################################
## Date        :  2024.04.16
## Environment :  Hardware            ----------------------  Raspberry Pi 4
##                SYstem of RPI       ----------------------  2022-04-04-raspbian-buster-full.img 64 bit
##                Version of Python   ----------------------  Python 3.7.3(Default in the system)
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
    with can.Bus(interface='socketcan', channel='can0') as bus:
        rpm = 6000
        rpm_rate = 203
        candata = [0x03,0xe7,0,0,0,0,0,2]
        hrpm = 0
        lrpm = 0
        gear = 3 #2 is neutral
        gear_rate = 1
        try:
            while True:
                eff_frame1 = can.Message(arbitration_id=0x600, data=[hrpm, lrpm, 0,0,0,0,0, gear], is_extended_id = False)

                print(eff_frame1)
                bus.send(eff_frame1)
                time.sleep(0.1)

                rpm = rpm + rpm_rate
                if rpm > 7200 or rpm < 6000:
                    rpm_rate = rpm_rate * -1
                    gear = gear + gear_rate
                    if gear<4 or gear >7:
                        gear_rate = gear_rate * -1

                hexrpm=hex(rpm)
                if rpm>4095:
                    hrpm=int(hexrpm[2:4],16)
                    lrpm=int(hexrpm[4:6],16)
                else:
                    hrpm=int(hexrpm[2:3],16)
                    lrpm=int(hexrpm[3:5],16)

        except KeyboardInterrupt:
            pass

if __name__ == '__main__':
    can_test()


