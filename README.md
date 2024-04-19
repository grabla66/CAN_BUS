The python script, can_from_csv.py, is run from a Raspberry Pi4 Model B, but should work on all Pi models.

It is written around the inno-maker USB2CAN device. This device is connected to the Pi via a single USB lead.

Install python3-can
$ sudo apt install python3-can

For useful debug tools
$ sudo apt-get install can-utils

Note: If the Race Technology Dash4Pro is the only device on the CAN bus, then you must turn Silent Mode off on the D4P otherwise this will not work. CAN requires at least one active device present for frames to be ackowledged. Silent mode is turned off using the Dash4Pro designer program.

combe.csv file contains the run data taken from the car from the first run off at Castle Combe circuit in October 2023.

March 3rd 2024.dbc file is the DBC file that needs loading in to the Dash4Pro designer to define the frames being received.

To execute the code, with the Dash4Pro connected to the USB2CAN board, and with 12V present on the Dash4Pro:

run sudo python3 can_from_csv.py

The program opens the combe.csv file, and line by line writes the contents as frames to the Dash4Pro over CAN.
