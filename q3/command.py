from os.path import abspath, join, dirname
import sys
import argparse
sys.path.append(abspath(dirname(__file__)))
from answer import flatten_chains, number_cycles

parser = argparse.ArgumentParser()

parser.add_argument("filepath")

args = parser.parse_args()

node_list = []

with open(args.filepath) as f:
    for line in f:
        node_list.append(line)

print number_cycles(flatten_chains(node_list))
