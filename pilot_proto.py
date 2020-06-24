import time
import csv
import pandas as pd
import serial
import subprocess as cmd
import os

ser = serial.Serial(port = '/dev/tty.usbserial-1430', baudrate = 9600, parity = serial.PARITY_NONE, stopbits = serial.STOPBITS_ONE, bytesize = serial.EIGHTBITS, timeout = 1)
iter = 0

masterlog = open('master.csv', 'w')
mw = csv.writer(masterlog)
weight = -1
prev_weight = -1
UNIT_WEIGHT = 0.1

while 1:
    prev_weight = weight
    ser.write(b'W\r')
    weight_str = str(ser.readline())[2:9]
    if('.' in weight_str):
        iter += 1
        weight = float(weight_str)
        if (weight != prev_weight) :
            row = [time.ctime()+',', weight, round(weight/UNIT_WEIGHT)]
            mw.writerow(row)
        print(weight)
        time.sleep(1)

    if (iter%300 == 0):
        #cp = cmd.run("git add .", check=True, shell=True)
        #cp = cmd.run("git commit -m " + time.ctime(), check=True, shell=True)
        #cp = cmd.run("git push -u origin master -f", check=True, shell=True)
