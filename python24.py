# Map, Filter and Reduce
def cube(x):
    return x**3
l=[1,2,3,4,5,6,7,8,9,10]
newl=[]
for item in l:
    newl.append(cube(item))
print(newl)

# or we can here use the map method
newl2=list(map(cube,l))
newl2a=map(cube,l)
print(newl2)
print(newl2a)

# Filter Function - either returns true or false and based on that the iterable elements are filtered.
x=int(input("Enter the number after which the list is to be filtered\n"))
def filter_func(a):
    return a>x
# newl3=list(filter(filter_func,l))
newl3=list(filter(lambda a: a>x,l))
newl3b=filter(lambda a: a>x,l)
print(newl3)
print(newl3b)

# Map and Filter are higher order functions as they take other functions as inputs.

#Reduce Function - this function needs to be imported from functools.
from functools import reduce as rd
newl4=rd(lambda p,q:p+q, l)
print(newl4,"\n", type(newl4))

