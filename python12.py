#DOC-STRINGS AND PEP-8 (Interview topics)
#Python doc-strings are the string literals that appear right after the definition of a function, method, class or module.
def square(a):
    print(a)
    '''Takes in a number a, returns the square of a'''  #this text is not a comment, it is a doc-string. If we write some operation just above the doc-string like print(n), it will no longer remain a doc-string.
    return a**2
print(square(5))
print(square.__doc__)   #method to print the doc-string.(parse)--when no doc-string it displays none.

#chaning comments cannot change the program, but on changing doc-strings the program may change.

#PEP - PEP stands for Python Enhancement Proposal. It is a document that provides guidelines and best practices on how to write a python code.

#The Zen of Python -- this poem appears when we type import this in the terminal. It is the 'easter egg' in python.(hidden message or feature)


#Recursions in python - calling a function within itself.(Recursion is the process of defining something in terms of itself.)
#for example - factorial
#factorial(n) = n* factorial(n-1)
def factorial(n):
    if(n==0 or n==1):
        return 1
    else:
        return n*factorial(n-1)
print(factorial(5))
print(factorial(4))
print(factorial(3))

#Quick quiz of fibonacci
def fibonacci(n):
    '''fibonacci sequence'''
    if(n==0):
        return 0
    elif(n==1):
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
print(fibonacci(6))
