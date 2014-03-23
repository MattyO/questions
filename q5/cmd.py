from answer import create_grid, enumerate_clockwise
import argparse

parser = argparse.ArgumentParser()

argparse.parser.add_argument("filepath")

argparse.parse()
args = parser.parse_args()

with open(args.filepath) as f:
    create_grid(f.read())
    print ''.join(list(enumerate_clockwise(grid)), ' '):

