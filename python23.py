#Additional File handling Operations - Seek() and Tell() functions.

#1) Seek Function.
with open("myfile2.txt", "r") as f:
    print(type(f))
    #Move to the 10th byte in the file.
    f.seek(11)
    #Read the next 5 bytes
    data=f.read(9)
    print(data)

    #2) Tell Function
    # tell function tells us where the pointer is or upto how many bytes we have seeked collectively till that point.
    print(f.tell())

#3) Truncate Method - Truncates the file data to the number of bytes specified.
with open("sample.txt","w") as g:
    g.write("Hello World!")
    g.truncate(5)
with open("sample.txt","r") as g:
    data1=g.read()
    print(data1)

#Lambda Functions-used when we need one-liners, and when we need to pass functions as arguments.
#Lambda Functions are small anonymous functions wiyhout name.
double=lambda x: x*2
cube=lambda x:x**3
average=lambda x,y,z:(x+y+z)/3
print(double(2))
print(cube(2))
print(average(2,3,4))

def appl(fx,value):
    return 6+fx(value)

print(appl(cube,2))
print(appl(lambda x:x**2,2))
