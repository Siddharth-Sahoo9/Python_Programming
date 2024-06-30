#Exception/Error Handling - to prevent the unnecessary halting of the program due to errors. (By the use of try-except statements.)
# x=input("Enter the number: \n")
# print(f"The multiplication table of {x} is :-\n")

# try:
#     for i in range(1,11):
#         print(f"{int(x)} X {i} = {int(x)*i}")
# except Exception as e:  #Exception is a keyword which means errors.
#     print(e)            #This print the error as a string. If you want to print something else when the error is encountered,you can use the following.
# # except:
# #     print("Invalid Input")

# print("Some imp lines of code.")
# print("End of the program")

# #We can also handle specific and multiple errors at the same time. For example - 
# try:
#     y=int(input("Enter the required number here :\n"))
#     a=[6,3]
#     print(a[y])
# except ValueError:
#     print("The entered value is not an integer.")
# except IndexError:
#     print("Invalid Index")

#Finally keyword in python - anything wriiten under it always gets executed.
#It's real use-case is when we write functions. - when a function has returned a value, the statements below it usually don't get executed. Here, we can use the finally keyword.

def func1():
    try:
        l1=[1,3,4,6,9]
        x=int(input("Enter the index:- \n"))
        print(l1[x])
        return 1
    except:
        print("Some error has occured.")
        return 0
    finally:
        print("I am always executed.")

y=func1()
print(y)