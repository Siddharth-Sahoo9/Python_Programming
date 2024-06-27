#Introduction to lists in python.
marks=[3,5,6,"Sunny", True]
# print(marks)
# print(marks[0])
# print(marks[1])
# print(marks[2])
# print(marks[3])
# print(marks[4])
print(type(marks))  #class gets printed as everything in python is a object and objects have a class.
print('\n')
print(marks[-3])    #negative indexing
print(marks[len(marks)-3]) #-ve equivalent to this. Same as in case of strings.
print(marks[5-3])
print(marks[2])

#in-keyword
# x=int(input("Enter the value to be checked\n"))  #considers only one data-type.
# if x in marks:
#     print("Yes, it is present.")
# else:
#     print("No, it is absent.")

#same case applies for strings as well.
if "unny" in "sunny":
    print("yes")

#slicing- same as strings
print(marks)
print(marks[1:-1])  #5-1=4 , so it will print upto 4-1=3
print(marks[::2])   #step. here it is marks[0:len(marks):2]
print(marks[-1:-6:-1])
print(marks[-5:len(marks):1])

#List Comprehension - creating lists from other iterables like lists, strings, tuples, etc.
lst=[i*i for i in range(5)]
print(lst)
names=['sunny', 'monty', 'guddu', 'sanchita', 'arpita', 'dinesh', 'tanisha']
names_1=[ i for i in names if "a" in i]
print(names_1)