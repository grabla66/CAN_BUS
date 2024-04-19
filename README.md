The python code is run from a Raspberry Pi4 Model B, but should work on all Pi models.
It uses python-can to send data over CAN bus using a inno-maker USB2CAN device.
If the Race Technology Dash4Pro is the only device on the CAN bus, then you must turn Silent Mode off on the D4P otherwise this will not work. CAN requires at least one active device present for frames to be ackowledged. 
The combe.csv file contains the run data taken from the car from the run off at Castle Combe circuit in October 2023.
The March 3rd 2024.dbc file is the DBC file that needs loading in to the Dash4Pro to define the frames being received.

run sudo python3 can_from_csv.py

The program opens the combe.csv file, and line by line writes the contents as frames to the Dash4Pro over CAN.
