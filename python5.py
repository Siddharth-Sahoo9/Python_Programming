# #break-continue statements in python.
# for i in range(15):
#     if(i==10):
#         break
#     print("5 X ", i+1, "=", 5*(i+1))
# print('Loop ko chodkar nikal gaya apun')

# print('\n')

# for i in range(15):
#     if(i==10):
#         print('Iteration ko chodkar nikal gaya apun')
#         continue
#     print("5 X ", i+1, "=", 5*(i+1))

# #Emulation of do-while loop (also 'exit-controlled' loop) now.

# while (True):
#     x=int(input("Enter the number of your choice: -"))
#     print(x)
#     if not (x>=50):     #use of not against if.
#         break

# Functions in Python.
def calculateGmean( a, b):
    gmean=(a*b)**0.5
    return gmean

def isGreater(a,b):
    if(a>b):
        print("The first number is greater.")
    elif (a==b):
        print("Both the numbers are equal.")
    else:
        print("The second number is greater.")

def isLesser(a,b):
    pass                #used when you intend to complete the func. body at a later stage.

print("Enter two numbers: ")
p=int(input())
q=int(input())
print(calculateGmean(p,q))
isGreater(p,q)




