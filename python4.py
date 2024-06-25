import os   #os module
os.system("python --version")

#Match-Case Statements. - similar to the switch-case statements used in C/C++ except here break statements are not used.
# x=int(input("Enter the no. of your choice.\n"))
# match x:
#     case 0:
#         print("The given number is zero\n")
#     case 2:
#         print("The given number is the smallest prime number.\n")
#     case 10:
#         print("The supplied number is ten on ten!\n")
#     case _ if(x%2!=0): #_ represents the default case inside which we can use if statements as well.
#         print("It is an odd number.\n")
#     case _:
#         print("It is an even number except 2 and 10.\n")

#For-loops in python programming.
# name=input("Enter your name here -\n")
# for i in name:
#     if(i==" "):
#         print("This is the white-space.")
#     else:
#         print(i)

# colors=['red', 'yellow', 'green', 'blue', 'black']
# for x in colors:
#     for i in x:
#         print(i)
#     print('\n')

#range func.
for i in range(1,11,2):
    print(i/2, end=' ')
print('\n')
#While-loops.
# j=0
# while(j<=5):
#     j=int(input("Enter the number of your choice.:-\n"))
#     print("The current number is ", j)
# print("Done with the loop.")

#Decrementing while-loops. (Be wary of the infinite while loops.)
#using else with while-loop. - when the while loop condition becomes false or it ends the else statement is executed.
x=-5
while(x>0):
    print(x)
    x-=1
else:
    print("I am out of the loop")

#There is no do-while loop in python. Do-while loop runs atleast once.
#Do-while loop first runs the loop body irrespective whether the condition is true or not, and then it will again run the loop if and only if the condition is true else not.

#After learning break-continue statements in python, try to emulate the do-while loop.

#Emulation of do-while loop without using break-continue statements by writing the loop body twice once inside the loop and once outside the loop.

y=int(input("Enter the number\n"))
print(y)
while(y<=20):
    y=int(input("Enter the number\n"))
    print(y)