#Short-hand if-else statements.
'''used especially when you want to assign a value to a variable based on a condition.'''
a=303
b=3303
print("a") if a>b else print("=") if a==b else print("b")   #this reads from left to right
print('9') if a>b else ""   #else do nothing.
c=9 if a>b else 0 
print(c)

#Python automatically detects the data-type of a variable.
#Linter - bugs and stylistic errors.

#enumerate function in python. - it gets the index along with the value of the element present in a list,tuple or string and stores it in the form of a tuple.
new=[78,98,10,1,56,85,94,13]
for index,mark in enumerate(new):   #index,mark is the order - first is index
    if(index==1):
        print("Siddharth, you did awesome in the test. ", mark)
        continue
    print(mark)

for v in enumerate(new):   
    print(v)
print(type(v))      #here,the output type is 'tuple'

#we can also change the start value of the index using the following syntax.
fruit={"apple", "banana", "strawberry", "Litchi", "Custard apple", "orange"}
for i,m in enumerate(fruit,start=1):    #start=1
    print(f"{i} - {m}")

