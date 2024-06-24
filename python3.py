#if-else statements.
# a=int(input("Enter your current age:- \n"))
# #The operators used in the following are called conditional-operators.
# print(a>18)
# print(a<=18)
# print(a==18)
# print(a!=18)
# if(a>18):
#     print("You are an adult now and you may drive.")
# else:
#     print("You are a minor now and hence you cannot drive.")

#To run file in the terminal--> write python file_name.py and press enter.
#using elif-statements
# b=int(input("Enter the price of Apple\n"))
# c=int(input("Enter your budget\n"))
# if(b-c<0):
#     print("You can buy more than 1kg of apples.")
# elif(b-c==0):
#     print("You can buy 1kg of apples.")
# else:               #Nested if-else statements.
#     if(b-c>10):
#         print("You need to save money ASAP")
#     else:
#         print("No rush for now, you can buy it later!")

#EXERCISE-2
import time
#epoch - it is the point where the time starts and is platform-dependent.
print(time.gmtime(0))   #func. to get the epoch (GreenWich Mean Time (gm))
timestamp=time.strftime('%H:%M:%S')     #Get the local time from your device.
print(timestamp)
x=int(time.strftime('%H'))
y=int(time.strftime('%M'))
z=int(time.strftime('%S'))
print(x)
print(y)
print(z)
#Greeting the user using time-module.
if(x>=0 and x<12):
    print("Good Morning Sir!")
elif(x>=12 and x<16):
    print("Good Afternoon Sir!")
elif(x>=16 and x<22):
    print("Good Evening Sir!")
else:
    print("Good Night Sir!")



   