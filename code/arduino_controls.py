__author__ = 'astha'

import serial
import time

PORT = 'COM5'
BAUDRATE = 115200

def send_go_forward_fast():
    ser = serial.Serial(PORT, BAUDRATE) # putty
    for i in range(3):
        ser.write('f')

def send_go_forward_mod():
    ser = serial.Serial(PORT,BAUDRATE)
    for i in range(3):
        ser.write('m')

def send_go_forward_slow():
    ser = serial.Serial(PORT,BAUDRATE)
    for i in range(3):
        ser.write('s')

def stop_moving():
    ser = serial.Serial(PORT,BAUDRATE)
    for i in range(3):
        ser.write('h')

def halt():
    ser = serial.Serial(PORT,BAUDRATE)
    ser.write('h')
    ser.close()
