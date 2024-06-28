#f-strings in python
#earlier method
# letter="Hey, My name is {1} and I am from {0}."
# name=input("Enter your name\n")
# country=input("Enter the country you live in\n")
# print(letter.format(name,country))  #here order matters.
# print(letter.format(country,name))  
# #or else we can supply the index within the brackets in the string. But these can be messy.
# print('\n')
# #f-strings.
# news=f"My name is {name} and I live in {country}. " #we can directly enter the variables in the string now.(f at the beginning of the string.)
# print(news)

txt="The required price for the mangoes is {price:.2f}"
print(txt.format(price=48.099999))
#same thing using f-strings
price=45.6999
text=f"The required price for the litchis is {price:.2f}"
print(text)

print(type(f"{2*60}"))  #string ans =120

#in order to print the curly brackets as it is in the program we need to use double-curly brackets.
new="Saanki"
example=f"My name is {{new}} "
print(example)