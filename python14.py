#Python dictionaries. - mapping through a combination of key value pairs.These are ordered.
dict={
    "Siddharth":"Human Being",
    "Spoon": "Object", "Daffodil":"Flower"
}
print(dict["Siddharth"])
dic={
    12:"sunny",
    15:"shubham",
    18:"sanchita",
    20:"Arpita"
}
# print(dic[20])
# print(dict)

# #To access the values, there are two methods.
# print(dic[12])
# print(dic.get(12))
# But if the key is not present the first method throws an error.But the second method prints None in that case.

#In order to access all the keys.
# print(dict.keys())
# #In order to access all the values
# for key in dict.keys(): #prints the values in an ordered manner.
#     print(f"The value corresponding to the key {key} is {dict[key]}")
# print(dic.values())

# #to access the key-value pairs of the dictionary.
# print(dic.items())  #This is iterable.
# print(type(dic.items()))
# for key,value in dic.items():
#     print(f"The corresponding value for the key {key} is {value}")


#Update method
dict.update(dic)    #similar to sets but ordered.
print(dict)
#clear() method - to empty the dict.
dic.clear()
print(dic)
#to make an empty dictionary - we have seen it during sets.
empt={}
print(empt)
#pop() method - to remove a particular key-value pair.
dict.pop('Siddharth')
print(dict)
#popitem() - to remove the last key-value pair.
dict.popitem()
print(dict)
#del keyword - to delete the entire dict.
ep={12:50, 15:60}
del ep
# print(ep)   #This throws an error as now ep doesn't exist.
#to delete a particular key-value pair using del.
ep1={"Sanchita":"girl", "Ashwani":"boy","BK":"trans"}
del ep1["Sanchita"]
ep1["Arpita"]="girl"    #to add a entry, we can use this.
print(ep1)

#try not to name a dict. as dict as it is a keyword.
#dict. comprehension
newdict={x:x**3 for x in range(5)}
print(newdict)

#always try to learn new things, by typing in google python_(topic)_documentation.