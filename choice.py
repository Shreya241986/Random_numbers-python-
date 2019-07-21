#from random import choice
from numpy.random import choice
possible_destinations = ["Berlin","Hamburg","Munich","Amsterdam","London","Paris","Zurich","Heidelburg","Strasbuorg","Ausgburg","Milan","Rome"]
#print(choice(possible_destinations))

"""Alternative way"""
print(choice(possible_destinations))

#With the help of the parameter "size" we can create a numpy.ndarray with choice values:

x1 = choice(possible_destinations, size=3)
print(x1)
x2 = choice(possible_destinations, size=(3, 4))
print(x2)

"""To avoid repition in choices use replace = False"""
x3 = choice(possible_destinations, size=(3, 4),replace = False)
print("\n",x3)
