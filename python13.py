#sets in python - doesn't accept repeated values. These are unordered and unchangeable. Hence, specific elements cannot be accessed using random index numbers. 
# s={2,4,6,2,8}
# print(s)
# info={"Sunny", False, 19,5.5, "Love", None}
# print(info)
# print(type(info))

# sunny={}    #This makes an empty dictionary.
# print(type(sunny))
# #In order to make an empty set, we can use the following
# sahoo=set()
# print(type(sahoo))

# #To access the elements of a list in any random order.
# for value in info:
#     print(value)

#set methods in python

#Union method
s1={1,2,3,4,5}
s2={5,6,9,18}
print(s1.union(s2))
print(s1,s2) #s1 and s2 don't change here.

#update method
s1.update(s2)
print(s1)

#Intersection method
print(s1.intersection(s2))  #prints the common items.

#Intersection update method
cities={"delhi", "mumbai", "rourkela", "kolkata", "chennai"}
cities2={"delhi", "kolkata", "tokyo", "kabul", "katra"}
# cities.intersection_update(cities2)
print(cities)   #only common items will be present in cities, rest items will be removed.

#symmetric difference - the values that are not common.((A union B) minus (A intersection B))

print(cities.symmetric_difference(cities2))
print(cities,"\n",cities2)
cities.symmetric_difference_update(cities2) #when you print this statement as it is , the output will be none. so always print this and the following.(in every update method.)
print(cities)

#difference and difference update method (A-B)
cities={"delhi", "mumbai", "rourkela", "kolkata", "chennai"}
cities2={"delhi", "kolkata", "tokyo", "kabul", "katra"}
print("\n")
print(cities.difference(cities2))

#disjoint sets - having no value in common.
cities3={"NewYork", "Peru"}
print(cities.isdisjoint(cities2))   #checks
print(cities.isdisjoint(cities3))

#superset method - if all elements of B are present in A, then A is called the superset of B.
cities4={"rourkela", "chennai"}
print(cities.issuperset(cities2))   #checks
print(cities.issuperset(cities4))

#subset method
print(cities4.issubset(cities))

#add method - to add one element 
cities.add("Helsinki")
print(cities)
#update method - to add multiple elements(we have seen above)

#to remove/ delete elements
cities.remove("rourkela")
print(cities)
cities.discard("delhi") #doesn't raise an error when the element to delete is not present in the set. whereas remove raises an error.
print(cities)

#pop method - deletes any random value.
item=cities.pop()
print(cities)
print(item)

#del - keyword to delete the entire set. When try to print the set afterwards it raises a nameerror.
del cities
# print(cities)

#clear method - clears(deletes) all the items from the list and returns an empty set.
cities2.clear()
print(cities2)

#to check if a item is present in a set.
if "delhi" in cities4:
    print("Yes, it is present.")
else:
    print("No, it is not present.")