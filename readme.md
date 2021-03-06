General 
---
All code for achieving the answers is found in the answer.py files in corresponding question directories.  Commands to meet the general requirements of file path arguments and output to stdout are called command.py again in each corresponding question directory

To run the command

	>> python [question_number]/command.py [question_number]/[*.txt]
    >> python q1/command.py q1/data.txt
    
To test run the command 

    >>python -munittest tests
    

Install
----
1. Create virtualenv
2. activate virtualenv
2. install requirements.txt
3. follow run directions above

####Requirements
* tested under python 2.7
* sympy
* cython
 
1 - Finding the source
----
Requires Sympy

Given two points with radi find the intercection of the resulting circles.  

Uses the [solve](http://docs.sympy.org/dev/modules/solvers/solvers.html#sympy.solvers.solvers.solve) function to make the system of equation more explicate and easier to understand.  

From an engineering and user experience perspective using [shapely](https://pypi.python.org/pypi/Shapely) and providing a visual solutions would probibly be more useful.  Shapely however can only describe circles as LinearRings that are made up of a collection of points.  Solutions may not exist if rings come to a single perfect mathamatical intersection and solutions for two points will not be an exact mathamatical solution.  But an approximate visual solution is probibly better for the use case of finding things in a coordinate system.  Approximate visual solutions would also guard against error in distances measured(close points are better than no points).  Shapely would allow for overlay of maps and other contextual data.

Q3 - Following the pointers
----
Given a list of pointers find how many cycles(where a pointers eventually points back to itself) there are.  

Reduces pointer links to their simplest form. a->b->c can be reduced to a->c.  Then checks for circular pointers.  Reduce a->b->c->a  and checks for to a->a 

Q4 - String manipulation
----
Requires cython for canswer.py

Replace concecative letters and spaces in a string __in place__

command.py uses the canswer solution

The in place requirement makes this solution a little more complicated.  The immutable nature of strings require us to drop down to C where we can treat strings as a character array.  

A pure python solutions is given in answers.py in the q4 folder.  This answer may not achieve the requirement of _in place_.  Another solution which is implemented in cython is found in the file canswer.pyx

Other solutions may include 

1. Use [bytearray](http://docs.python.org/3.1/library/functions.html#bytearray) in place of strings throughout the program.  I didn't know if this puts the solution outside of the requirements specified.
2. Skip _in place_ requirement and allow new string objects to be returned.  

The side-effectly nature of a in place solution would make me think twice about implementing it in a larger system.  The C / cython makes it hard to maintain and is much more prone to errors.  If a performance gain is the driving influence I would recommend looking for other lower-fruit kind of places.  


Q5 - Spiral printing
----
Print a two dimensional array in a clockwise spiral to its center

1 2 3
4 5 6
7 8 9

prints to 1 2 3 6 9 8 7 4 5

Turned into a decent OO based solution.  

The enumerate functions returns a generator for performance and consistency with the standard enumerate stdlib function.  Use with care as it is prone to the constraints of all other python generators.
