#Function arguments in python.
#There are 4 types of function arguments that we can provide in--
#These are default, keyword, variable length and required.

def average(a=5,b=7):       #here 5 and 7 are the default arguments.
    avg=(a+b)/2
    return avg

print(average(6,10))
print(average())        #In case no argument is passed, the default argument works.
#working of the default arguments.
print(average(6))   #a=5, b from default
print(average(b=10))   #a from default

print(average(b=99,a=44)) #This is the ex. of keyword arg. where the order doesn't matter.

def name(fname, mname="Kumar", lname="Sahoo"):  #as here the fname is not specified, it becomes the required argument- means we need to supply the fname atleast. 
    print('Hello, ', fname, mname, lname)

name('Siddharth',"Manohar", "Kumar")

#Variable-length arguments.
def newAverage(*numbers):   #takes the input numbers as a tuple.(variable-length)
    print(type(numbers))
    sum=0
    for i in numbers:
        sum+=i
    print('The required average of the numbers is: - ', sum/len(numbers))   #len()- no.of elements in the tuple.

newAverage(1,2,3,4,56,7,8,9,10,50)

#Keyword arguments - works as a dictionary.
def name(**name):   #takes name as a key-value pairs (dictionary)
    print(type(name))
    print('Hello, ', name["fname"], name["mname"], name["lname"])   #substances inside the square brac.s are the keys. Values need to be supplied during the function call.

name(lname="sahoo", mname="vajpayee", fname="sunny") #The values are supplied in any random order.

# if we use two return statements in a function, then only the first return func. is taken into account.

