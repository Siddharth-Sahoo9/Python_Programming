l=[55,1, 95, 62, 1,2,4,6,1]
print(l)
#reverse method 
l.reverse()
print(l)
#Append method
l.append(7)
print(l)
#Sorting methods
l.sort()    #ascending order
print(l)
l.sort(reverse=True)    #descending order.
print(l)
#determine the index.
print(l.index(1)) #first appearance index of 1.
#count method
print(l.count(1))

#in this case list l will also change as m is a refernce of l.
m=l
m[0]=0
print("\n",l)

#But in this case l will not change, when we will use the copy method.
m=l.copy()
m[0]=1
print("\n",l)
#insert method
l.insert(5,100)
print(l)
#extend method
n=[0.1,0.2,100,959,2000,5.6]
k=l+n   #lists get concatenated.
print(k)    #in this l doesn't 
l.extend(n)
print(l)