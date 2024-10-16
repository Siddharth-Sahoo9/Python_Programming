#Readline Method
f=open("myfile1.txt", "r")
i=0
while True:
    i=i+1
    line=f.readline()
    if not line:
        print(type(line))
        break
    # print(line)
    m1=line.split(",")[0]
    m2=line.split(",")[1]
    m3=line.split(",")[2]
    print(f"The marks of student {i} in Maths is {m1} ")
    print(f"The marks of student {i} in Physics is {m2} ")
    print(f"The marks of student {i} in Chemistry is {m3} ")
f.close()

#Writelines method
# f=open("myfile2.txt", "w")
# lines=["line1\n", "line2\n","line3\n"]
# f.writelines(lines)
# f.close()

#Write - Another method to carry out writelines- when we have large number of lines, then we can automate the process of adding the new-line characters.
f=open("myfile2.txt", "w")
lines=["My name is Siddharth Sahoo" , "I live in Rourkela. ", "I study at NIT Rourkela."]
for line in lines:
    f.write(line+"\n")
f.close()