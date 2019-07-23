#from random import choice
from collections import Counter
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

#Weighted random choice

professions = ["scientist", 
               "philosopher", 
               "engineer", 
               "priest", 
               "programmer"]
probabilities = [0.2, 0.05, 0.3, 0.15, 0.3]

c = Counter()
for _ in range(1000):
    profession = choice(professions, p=probabilities)
    c[profession] += 1
    
print(c)
s = sum(c.values())
for el in c:
    c[el] /= s
print(c)
