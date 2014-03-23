from os.path import abspath, join, dirname
import sys
sys.path.append(abspath(dirname(__file__)))

import argparse

from answer import create_grid, enumerate_clockwise

parser = argparse.ArgumentParser()

parser.add_argument("filepath")

args = parser.parse_args()

grid = None
with open(args.filepath) as f:
    grid = create_grid(f.read())

print ' '.join(map(lambda position: position.value, enumerate_clockwise(grid)))

