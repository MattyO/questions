from os.path import abspath, join, dirname
import sys
import argparse
sys.path.append(abspath(dirname(__file__)))

import pyximport; 
pyximport.install()

from canswer import ireplace 

parser = argparse.ArgumentParser()

parser.add_argument("filepath")

args = parser.parse_args()

file_contents = ""
with open(args.filepath) as f:
    #strip off new line that r.read adds
    file_contents =f.read().rstrip("\n")
ireplace(file_contents)
print file_contents

