#!/usr/bin/env python
"""
get3gSignal.py

Get 3g signal strength from usb connected device

   Copyright (C) 2014  Bluerhodfa Consulting Ltd

    This program is free software; you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation; either version 2 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License along
    with this program; if not, write to the Free Software Foundation, Inc.,
    51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

"""
from __future__ import division
import subprocess
import os
import sys
import serial
import time


# Define dBm constants in list format
#
#  Marginal Levels of -95dBm or lower.
#  Workable under most conditions. Levels of -85dBm to -95dBm.
#  Good Levels between -75dBm and -85dBm
#  Excellent Levels above -75dBm

dBm = {'0': 113,
       '1': 111,
       '2': 109,
       '3': 107,
       '4': 105,
       '5': 103,
       '6': 101,
       '7': 99,
       '8': 97,
       '9': 95,
       '10': 93,
       '11': 91,
       '12': 89,
       '13': 87,
       '14': 85,
       '15': 83,
       '16': 81,
       '17': 79,
       '18': 77,
       '19': 75,
       '20': 73,
       '21': 71,
       '22': 69,
       '23': 67,
       '24': 65,
       '25': 63,
       '26': 61,
       '27': 59,
       '28': 57,
       '29': 55,
       '30': 53,
       '31': 51,
       '99': ' which is not known or not detectable with no'
       }

sigQuality = {'0': 'poor',
              '1': 'poor',
              '2': 'poor',
              '3': 'poor',
              '4': 'poor',
              '5': 'poor',
              '6': 'poor',
              '7': 'poor',
              '8': 'poor',
              '9': 'poor',
              '10': 'workable',
              '11': 'workable',
              '12': 'workable',
              '13': 'workable',
              '14': 'workable',
              '15': 'good',
              '16': 'good',
              '17': 'good',
              '18': 'good',
              '19': 'good',
              '20': 'excellent',
              '21': 'excellent',
              '22': 'excellent',
              '22': 'excellent',
              '23': 'excellent',
              '24': 'excellent',
              '25': 'excellent',
              '26': 'excellent',
              '27': 'excellent',
              '28': 'excellent',
              '29': 'excellent',
              '30': 'excellent',
              '31': 'excellent',
              '99': 'disconnected'

              }


def detectModem(device):

    try:
        os.stat(device)

    except OSError as e:
        print "I/O Error({0}): {1}".format(e.errno, e.strerror)
        print "Check that 3g dongle is inserted and try running this program again"
        raise


def pollSerial(device):
    ser = serial.Serial(device, 9600, timeout=0)
    ser.close()
    ser.open()
    ser.write("AT+CSQ\r")
    time.sleep(3)
    ser.readline()
    read_val = ser.read(11)
# we expect to recieve +CSQ: [n]n,nn in read_val
    val = read_val[read_val.find(':')+1:read_val.find(',')].strip()
    pct = int(val) / 32 * 100
    print "Receieving a signal at -" + str(dBm[val]) + "dbm" + " which is " + str(pct) + "% and " + str(sigQuality[val])
    ser.close()


# confirm we have a modem connected before we start
detectModem("/dev/cu.ZTEUSBModem_")

# let's go
pollSerial("/dev/cu.ZTEUSBModem_")
