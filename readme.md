General 
---
All code for achiving the answers is found in the answer.py files in corisponding question directorys.  Commands to meet the gemeral requirements of file path arguments and output to stdout are called cmd.py again in each corrisponding question directory

To test run the command 
    python -munittest tests

Q1 - Finding the source
----
Requires Sympy

uses the solve function to make the system of equation more explicate and easier to understand.  

Q3 - Following the pointers
----
Reduces pointer links to their simplest form. a->b->c can be reduced to a->c.  Then checks for circular pointers.  a->b->c->a reduces and checks for to a->a 

Q4 - String manipulation
----
Requires cython for canswer.py

The in place requirement makes this solution a little more complicated.  The immutable nature of string require us to drop down to C where we can treat strings as a character array.  

A pure python solutions is given in answers.py in the q4 folder.  This answer may not achive the requirement of _in place_.  Another solution which is implemented in cython is found in the fild canswer.pyx

Other solutions may include 

1. Use bytearray in place of strings throughout the program.  I didn't know if this put the solution outside of the requirements specified.  
2. Skip _in place_ requirement and allow new string objects two be returned.  

Q5 - Spiral printing
----
Turned into a decient OO based solution.  