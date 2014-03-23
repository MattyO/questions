General 
---
All code for achiving the answers is found in the answer.py files in corisponding question directories.  Commands to meet the gemeral requirements of file path arguments and output to stdout are called command.py again in each corrisponding question directory

To run the command

	>> python [question_number]/command.py [question_number]/[*.txt]
    >> python q1/command.py q1/data.txt
    
To test run the command 

    >>python -munittest tests
    

Q1 - Finding the source
----
Requires Sympy

uses the solve function to make the system of equation more explicate and easier to understand.  

Q3 - Following the pointers
----
Reduces pointer links to their simplest form. a->b->c can be reduced to a->c.  Then checks for circular pointers.  Reduce a->b->c->a  and checks for to a->a 

Q4 - String manipulation
----
Requires cython for canswer.py

command.py uses the canswer solution

The in place requirement makes this solution a little more complicated.  The immutable nature of strings require us to drop down to C where we can treat strings as a character array.  

A pure python solutions is given in answers.py in the q4 folder.  This answer may not achive the requirement of _in place_.  Another solution which is implemented in cython is found in the file canswer.pyx

Other solutions may include 

1. Use bytearray in place of strings throughout the program.  I didn't know if this puts the solution outside of the requirements specified.
2. Skip _in place_ requirement and allow new string objects to be returned.  

The side-effectly nature of a in place solution would make me think twice about implementing it in a larger system.  The C / cython makes it hard to maintain and much more prone to errors.  If a performance gain is the driving influence I would recommend looking for other lower-fruit kind of places.  


Q5 - Spiral printing
----
Turned into a decient OO based solution.  

The enumerate functions returns a generator for performance and consistencey with the standard enumerate stdlib function.  Use with care as it is prone to the constrains of all other python generators.  