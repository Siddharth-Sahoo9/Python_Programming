#Tuple
tup=(1,2,3,4,50,6,7,8,9,5,6,5,9,5, "sunny", True )
print(type(tup), tup)
tup0=(1)
print(type(tup0)) #this shows class is int
tup1=(1,)
print(type(tup1)) #this shows class is tuple

#Tuples and strings are immutable.
# tup[0]=2  #this shows an error(dissimilar to lists)
print(tup[0])
print(tup[len(tup)-1])
print(tup[len(tup)-2])

if 'sunny' in tup:
    print("yes")
#slicing
print(tup[0:10:2])

#Tuple manipulations.
#we can convert a tuple to a list, make changes in it and can again convert it back to a tuple.
countries=("India", "Italy", "Russia", "Pakistan", "UK", "Poland")
temp=list(countries)
temp.append("USA")
temp.pop(3) #removes(deletes) the value at the supplied index.
countries=tuple(temp)
print(countries)

#we can directly concatenate two tuples without converting them to lists.
new=tup+countries
print(new)

#count method
print(tup.count(5))
print(list(tup).count(5))   #works for list as well.

#index()-method -- first occurence index.(raises value error if element is not present in the tuple.)
print(tup.index(5))
print(tup.index(5,10,14)) #index of (element, start , end) - slices the tuple first, then checks for the first occurence index.

#length method (same)
print(len(new))
