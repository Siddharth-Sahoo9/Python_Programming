# #To print double-quotes in the output
# name='My name is "Siddharth Sahoo"'
# print(name)

# #Multi-Line String
# string='''hey how are u doing ?\
# I am fine dear.
# I heard that you got an A+ in your 2nd semester exam.
# Yeah bro! I kinda worked hard for it.
# Nice to hear that.'''
# print(string)

# # In python, string is like an array of characters.(LIKE AN)
# #Indexing in strings.
# print(name[0])
# print(name[1])
# print(name[2])

# #Using for-loop
# for i in string:    #prints also the spaces and the new-line characters.
#     print(i)
# print('\n')
# #Length of a string using len() func.
# print(len(name))
# #string-slicing
# print(name[:10:1])
# print(name[::])
# print(name[0:-10])  #-ve index--> -10 equivalent to len(name)-10. 
# print(name[-1:-29:-1])
# print(name[-28])
# print(name[-1])
# print(name[-28:-10])    #every -ve index is interpreted as mentioned above.

#Strings are immutable. The func.s that follow make a copy of the string (new) and then edit it. Makes new string, doesn't change the existing string.
a="!!!! SuNnY !!!!!!!"
print(a.upper())
print(a.lower())
print(a.rstrip("!"))    #removes the trailing characters.(repeating)
b="Sunny is a nice boy. Sunny is currently living in Rourkela. 10"
print(b.replace("Sunny", "Swaraj")) #replaces

#split() function - Converts the string(copy) to the form of a list breaking the string at the points where the passed character is present.
print(b.split(" "))
#capitalize() func.-converts only the first letter of the string to uppercase and rest letters to lowercase.
print(b.capitalize())

#center() func.- adds space(default-can change) at the beginning of the string to make the length of the entire string equal to the passed argument.
print(b.center(70))

#count() func.
print(b.count(" "))

#endswith()/startswith() func.s- returns boolean data.
print(a.endswith("!!!"))
print(b.endswith("a",0,10))
print("\n")
print(b.startswith("Sunny"))

#find() func.- returns the index of the first occurence of the passed argument. Else returns -1.
print(b.find("is"))
print(b.find("ins"))

#index() func. - similar to the find func. except it raises a error when the required string is not found.
print(b.index("is"))
# print(b.index("iss"))

#isalnum() func.- only alpha-numeric characters. Not even space is considered.
b1="SunnyisaniceboySunnyiscurrentlylivinginRourkela10"
b2="SunnyisaniceboySunnyiscurrentlylivinginRourkela"
print(b1.isalnum())
print(a.isalnum())

#isalpha() func. - evident by it's name.
print(b1.isalpha())
print(b2.isalpha())

#islower()/isupper() func.-checks if all the letters of the string are in lowercase/uppercase or not.
print("\n")
c="i study in nit rourkela.\n"
d="I LIVE IN HOSTEL THERE."
print(b2.islower())
print(c.islower())
print(d.isupper())

#isprintable() func. - boolean return - tells whether the string has printable characters or not. Non-printable characters include new-line characters "\n".
print("\n")
print(d.isprintable())
print(c.isprintable())

#isspace() func. - evident by it's name.
e="     "
print(c.isspace())
print(e.isspace())

print("\n")
d1="He Is A Very Good Person"

#istitle() func. - returns true iff the first letter of each word of the string is capitalized (title case), else returns false.
print(c.istitle())
print(d1.istitle())

#swapcase() func.- lowercase <--> uppercase
print(d1.swapcase())

#title() func. - converts to title case.
print(c.title())

