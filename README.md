DBDM : Closure Algorithm for Functional Dependencies
====================================================

SLOWIK Agnieszka
PHILIBERT Manon


Content
=======

readme.txt : this file
results.csv : raw results
plot.png : figure depicting results

/* to be completed with the list of your source files, */
/* feel free to add relevant supplementary material */
/* prevent yourselves from adding binaries or the originaly provided examples */


Open questions
==============

4.1 Justifications of data structures
-------------------------------------
Attributes are stored as chars or integers according to the form of the original input.
Sets of attributes are implemented with Python "set" collection because it provides a constant time access and insertion
as well as the functions typical for a set in the mathematical sense (intersection, union, difference) which are crucial for computing a closure.
A functional dependency is stored in a dictionary "frozenset" -> "frozenset". We use dictionary to be able to capture relations between the attributes (to access the dependent ones by  and for the constant time access and insertion.
"Frozenset" is a hashable equivalent of "set" collection therefore it can be used as a key in a dictionary.
Set of fds is implemented as a set of dictionaries.

In the "construct_indices" function I implement "count" and "lista" (used the word "lista" instead of "list" because "list" is a special name in Python)
with a dictionary tuple containing fd -> integer. I used a tuple because we don't want to make any changes to fds, just count the size of a key set for every one of them.
"Lista" is a dictionary mapping each attribute A -> to a list of tuples containing fds W - > Z such that W contains A.

4.2 Strategy for Choose A
-------------------------
Choose A is implemented by a loop which iterates through all the attributes in the "update"
and removes them from the set at every step. The iterations are over when there are no more elements in the "update".


4.3 Find the bug
-------------------------
The corner case for Closure_improved is the input fd with the empty left side.
In that case we don't construct the "lista" for this fd and skip it - while according to the FDs rules if the left side is empty
we can access the right side from every set of attributes.

6.1 Interestingness of generate
-------------------------------

6.2 Setup and methodology
-------------------------

6.3 Analysis
------------


Additional comments
===================

/* if any */