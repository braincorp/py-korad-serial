#!/usr/bin/python

import argparse
from koradserial import KoradSerial
import time


def enablePowerSupply(powerOn=True):
    with KoradSerial('/dev/ttyACM0') as ps:
        ps.output.on() if powerOn == True else ps.output.off()
    with KoradSerial('/dev/ttyACM0') as ps:
        print("V: {}V".format(ps.channels[0].output_voltage))
        print("I: {}A".format(ps.channels[0].output_current))

def printPowerSupplyInfo():
    with KoradSerial('/dev/ttyACM0') as ps:
        print("Model: ", ps.model)
        print("Status: ", ps.status)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Basic Power supply control script")
    parser.add_argument("--info", action="store_true", default=False, help="Print power supply information")
    parser.add_argument("--on", action="store_true", help="Enable the power supply")
    parser.add_argument("--off", action="store_true", help="Disable the power supply")

    args = parser.parse_args()

    if args.info or not (args.on or args.off):
        printPowerSupplyInfo()
    elif args.on:
        enablePowerSupply(True)
    elif args.off:
        enablePowerSupply(False)
    else:
        parser.print_help()
    
