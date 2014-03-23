from os.path import abspath, join, dirname
import sys
import argparse

sys.path.append(abspath(dirname(__file__)))

from answer import Reading, find

parser = argparse.ArgumentParser()

parser.add_argument("filepath")

args = parser.parse_args()

readings  = []

with open(args.filepath) as f:
    for line in f:
        x,y,distance = line.split(" ")
        readings.append(Reading(float(x), float(y), float(distance)))

for possible_location  in find(readings):
    possible_x, possible_y = possible_location

    print "{x}, {y}".format(x=float(possible_x), y=float(possible_y))
