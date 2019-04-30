#!/usr/bin/python

import argparse
from koradserial import KoradSerial
import time


def enablePowerSupply(device, powerOn=True):
    with KoradSerial(device) as ps:
        ps.output.on() if powerOn == True else ps.output.off()
    with KoradSerial('/dev/ttyACM0') as ps:
        print("V: {}V".format(ps.channels[0].output_voltage))
        print("I: {}A".format(ps.channels[0].output_current))

def printPowerSupplyInfo(device):
    with KoradSerial(device) as ps:
        print("Model: {}".format(ps.model))
        print("Status: {}".format(ps.status))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Basic Power supply control script")
    parser.add_argument("-d", "--device", nargs='+', default=['/dev/ttyACM0'], help="Power supply device")
    parser.add_argument("--info", action="store_true", default=False, help="Print power supply information")
    parser.add_argument("--on", action="store_true", help="Enable the power supply")
    parser.add_argument("--off", action="store_true", help="Disable the power supply")

    args = parser.parse_args()

    if args.info:
        printPowerSupplyInfo(args.device[0])
    elif args.on:
        enablePowerSupply(args.device[0], True)
    elif args.off:
        enablePowerSupply(args.device[0], False)
    else:
        parser.print_help()
    
