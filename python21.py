#File Handling in python
f=open('myfile.txt','r')    #r - opens the file in read only mode. Even if we don't specify any mode, python automatically opens the file in read mode only as it is the default mode. If the file doesn't exist, read mode throws an error.
#in the above case, the t beside r specifies to open the file in text mode (default mode, hence no need to specify.) If we want to open a binary file(images, audio, video, pdf and executable programs) or any file as a binary file then we must open it in rb mode(binary). Now in the above case the output will come in the form of bytes.
print(f)    #No meaning to print this.
text=f.read()
# print(f.read()) #If you try to read the file again after the initial f.read(), it will return an empty string because the file pointer is at the end of the file. To read it again, you need to reset the file pointer using f.seek(0).
print(text)
f.close()

# write (w): This mode opens the file for writing only and creates a new file if the file does not exist. And if the file exists and we open it in write mode and write in it, then the previous content of the file is lost and the new content is added.
# n=open("myfile1.txt", "w")
# n.write("Hello World!\nI am learning Python Programming.")
# n.close()

# append (a): This mode opens the file for appending only and creates a new file if the file does not exist.
n=open("myfile1.txt", "a")
n.write("Hello World!\nI am learning Python Programming.\n")
n.close()


# create (x) - this mode creates a file and gives an error if the file already exists.
# use of the with open statement(No need of the close statement here.)
with open("myfile1.txt", "r") as m:
    print(m.read())
#By learning file handling, we can make and handle our own temp. database.