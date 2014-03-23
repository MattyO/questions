from sympy.abc import x, y
from sympy.solvers import solve
import math
from collections import namedtuple

Reading = namedtuple("Reading", ['x', 'y', 'distance'])

def distance(reading_one, reading_two):
    return math.sqrt((reading_two.x - reading_one.x)**2 + (reading_two.y - reading_one.y)**2)

def find(readings):
    points = []
    first_two_readings = readings[:2]
    radi_sum = sum(map(lambda reading: reading.distance,first_two_readings))

    if distance(*first_two_readings)  <= radi_sum:
        function_list = [ (x-reading.x)**2 + (y-reading.y)**2 - reading.distance**2
                            for reading in readings ]
        points = solve(function_list, x,y)

    return points


