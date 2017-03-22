print ("Hello Python!")

counter = 100          # An integer assignment
miles   = 1000.0       # A floating point
name    = "John"       # A string

print (counter)
print (miles)
print (name)
print ()




# two examples of assignment which could cause confusion.
a=1
b=2

# in this case b is assigned a+b where a is the original value (1) 
# not the newly assigned value (2) from b on the LHS
a, b = b, a + b

print (a)
print (b)
print ()


a=1
b=2

a = b
b = a + b

print (a)
print (b)
