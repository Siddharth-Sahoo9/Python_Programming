# 'is' and '==' both are comparison operators.
# "==" compares the value of the two variables.
# "is" compares the exact location of the object in the memory.It returns true if the variables have the same memory location or contain constant or immutable datatypes.
#'is' operator basically compares the identity.

a=[1,2,3]
b=[1,2,3]
print(a is b) #returns false since lists are mutable
print(a == b,'\n') #returns true since they have the same face value.

x=(1,2,3)
y=(1,2,3)
print(x is y) #returns true since tuples are immutable.
print(x == y,'\n') # true as same.

p=None
q=None
print(p is q) #true as they are constants.
print(p == q) #same
print(p is None,"\n") #true

u=3
v=3
print(u is v) #constants
print(u == v,"\n") #true

s="Siddharth"
t="Siddharth"
print(s is t) #strings are constant
print(s == t) #same face value.