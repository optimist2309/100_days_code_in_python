"""
How to read multiple values from input in single line.
"""

a, b = [int(x) for x in input("enter 2 numbers:-").split()]
print("First Number is ", a)
print("Second Number is ", b)
"""
For Above code we need to separate values using space. 
We can separate values using space Below is the example.  
"""
c, d = [int(x) for x in input("enter 2 numbers:-").split(",")]
print("First Number is ", c)
print("Second Number is ", d)
