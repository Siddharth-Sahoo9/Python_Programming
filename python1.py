#Simple Calculator using Python
# x=float(input("Enter the first number- \n"))      #here float is used as a type-casting function.
# y=float(input("Enter the second number- \n"))
# z=input("Enter the Operator- \n")
# if z=='+':
#     print("The sum of the numbers is- \n", x+y)
# elif z=='-':
#     print("The difference of the numbers is- \n", x-y)
# elif z=='*':
#     print("The product of the numbers is- \n", x*y)
# elif z=='/':
#     print("The required ans of the division is- \n", x/y)
# elif z=='//':
#     print("The required quotient is- \n", x//y)
# elif z=='%':
#     print("The required remainder is- \n", x%y)
# elif z=='**':
#     print("The required exponential ans is- \n", x**y)
# else:
#     print("Invalid Operator")

# Lesson - TypeCasting
a=1
b="5"
print(int(a)+float(b))      #here implicit typecasting is taking place. So we can add two no.s with different data-types in the number category.
print(type(a))

''' Two types of type-casting-- 
1)Explicit typecasting - type casting done by the user by giving instructions to the python interpreter.
2)Implicit typecasting - type casting done by the python interpreter itself. Python converts a smaller data type to a higher datatype to prevent data loss. ex- int to float conversion.'''
