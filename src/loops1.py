# Loops - iter

import sys

list = [1,2,3,4]
it = iter(list) # this builds an iterator object
#print (next(it)) #prints next available element in iterator

#Iterator object can be traversed using regular for statement
for x in it:
   print (x, end=" ")
   
print()
   
#or using next() function
it = iter(list) # this builds an iterator object

while True:
   try:
      print (next(it), end=" ")
   except StopIteration:
      sys.exit() #you have to import sys module for this