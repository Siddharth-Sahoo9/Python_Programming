#os module in python.
import os
if not os.path.exists("OS module/data"):
    os.mkdir("OS module/data")
# for i in range(1,6):  #Do This to make folders inside a folder 
#     os.mkdir(f"OS module/data/Day {i}")

#To rename the prepared folders.
# for i in range(1,6):  
#     os.rename(f"OS module/data/Day {i}", f"OS module/data/Tutorial {i}")    #(original file name, renamed file name) - syntax

folders=os.listdir("OS module/data")    #prints the list of folders(things) present within the specified folder.
print(folders)
for folder in folders:
    print(folder)
for folder in folders:
    print(folder)
    print(os.listdir(f"OS module/data/{folder}"))

#os.system() - to run the commands.
# print(os.system('date')) - #this prints the date and also allows to set the date.
# print(os.system('notepad'))     #this statement opens up the notepad in our local device.

#to get the current working directory
print(os.getcwd())
#to change the current working directory - 
os.chdir("\C++\.vscode\OS module")
print(os.getcwd())

#os.rmdir() - deletes an empty directory
#os.remove() - removes a file.
