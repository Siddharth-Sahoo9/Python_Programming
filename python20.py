'''if "__name__ == "__main__" in Python
The if __name__ == "__main__" idiom is a common pattern used in Python scripts to determine whether the script is being run directly or being imported as a module into another script.

In Python, the __name__ variable is a built-in variable that is automatically set to the name of the current module. When a Python script is run directly, the __name__ variable is set to the string __main__ When the script is imported as a module into another script, the __name__ variable is set to the name of the module.'''
# import python19
# print(python19.sum(9,10))

#OS module in python
# import os

#Local and Global variable and use of the global keyword.
x=10 #global variable

def my_function():
    y=5 #local variable - only accessible within the function and is destroyed once the function gets executed.
    global x
    x=5 #used the global keyword - this will change the value of our global x.

my_function()
print(x)    #once the above function is executed the value of the global variable is changed to 5 instead of 10 (done using the global keyword). If we don't execute the func. using the above statement then the value of the var. x is set to 10 only.
# print(y) #this throws an error as y is a local var. and hence cannot be accessed outside the function.

'''It's important to note that it's generally considered good practice to avoid modifying global variables from within functions, as it can lead to unexpected behavior and make your code harder to debug.'''
