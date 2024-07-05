# #How to raise custom errors in python ? - by using the raise keyword.
# a=int(input("Enter any value between 5 and 9\n"))
# if(a<5 or a>9):
#     raise ValueError("Value should be between 5 and 9")
# print(a)

#To build - when we type quit above, the error is not raised.

import random
import string 
#Secret-Code Language.
x=int(input("Enter 0 to encode the message and 1 to decode the message - \n"))
if x!=0 and x!=1:   #here and will be used - view the code properly.
    raise ValueError('Enter either 0 or 1 based upon the choice.')
if(x==0):
    str1=input("Enter the string to be encoded. - \n")
    if(len(str1)<3):
        print(str1[::-1])
    else:
        characters=string.ascii_letters+string.digits
        begin_chars=''.join(random.choice(characters) for i in range(3))
        end_chars=''.join(random.choice(characters) for i in range(3))
        y=str1[0]
        str1=str1[1:]+y
        encoded=begin_chars+str1+end_chars
        print(encoded)
else:
    str2=input("Enter the string to be decoded - \n")
    if len(str2)<3:
        print(str2[::-1])
    else:
        w=str2[3:-3]
        z=w[-1]
        decoded=z+w[:-1]
        print(decoded)
    
