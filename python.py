import pandas
#I am a B.Tech student at NIT Rourkela. This is a single-line comment
'''This is the multi-line comment
As we know from here, it can take as many lines as required by us.'''
print("Hey I am a \"good boy\".")   #Escape-sequence to use double quote inside the string.--\""
print(17*13)
x=7
y=8
print(x*y)
print("My branch is \nElectronics and Communication Engineering")
print("hey", 68,"\n78", 100 , sep="~", end="")  #By default the end value is always the new-line escape sequence
print("Siddharth")
a=None
b="NIT Rourkela"
print(a, "\nThe type of a is-", type(a))        #type function
print(b, "\nThe type of b is-", type(b))        #type function
c=complex(6,5)                                  #complex datatype
print(c,type(c))
list=[7,8,121,True, "Sunny", "Sanchita", "Ashwani", 1.1, [1,"sahoo"]]
print(list)             #Lists are Mutable
tuple1=("Honey", "Nutter", 1.05, "Moom", True, False,(1.9, "sunny"))
print(tuple1)           #Tuples are immutable

#Dictionary is the mapped data-type where key-value pairs exist.
dict1={"name":"Sunny","age":20,"Phone Number":9827345715, "canVote":True}
print(dict1)
# In Python, everything is a object.---Remember this.

#Floor Division by // -- returns the Quotient
# Modulo operator by % -- returns the remainder
# Exponential Operator -- **
print(5//2)
print(5%2)
print(2.5**5)
