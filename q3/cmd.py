from answer import Reading, find
import argparse

parser = argparse.ArgumentParser()

argparse.parser.add_argument("filepath")

argparse.parse()
args = parser.parse_args()

readings = []

with open(args.filepath) as f:
    for line in f:
        x,y,distance = line.split(' ')
        readings.append(Reading(x,y,distance))

for possible_x, possible_y in find(readings)
    print possible_x, possible_y
