#We learnt about the concept of virtual environment.
#A virtual environment is a tool used to isolate specific Python environments on a single machine, allowing you to work on multiple projects with different dependencies and packages without conflicts.

#In powershell or command-prompt
## Create a virtual environment
#python -m venv env_name

# '''# Activate the virtual environment (Windows)
# .\myenv\Scripts\Activate'''

# '''To set the execution policy of scripts-  Get-ExecutionPolicy
# Restricted  (this is the output)
# PS C:\C++\.vscode\Virtual Environment> Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process'''

#we can install specific versions of the packages through the syntax -- pip install pandas==1.4.4
# # Deactivate the virtual environment
# deactivate

'''# Output the list of installed packages and their versions to a file
pip freeze > requirements.txt'''

# Only "pip freeze" shows the list of packages and their versions installed in the virtual environment.

'''# Install the packages listed in the requirements.txt file(given by others ofc)
pip install -r requirements.txt'''

#How import works in python.
import math
print(math.sqrt(25))
#To use some particular functions only present within a module we can use the 'from' keyword.
from math import sqrt,pi
# now in this case the use-syntax changes.
print(sqrt(49)*pi) 

#To import all the functions and variables present within a module, we can use the '*' wildcard. However, this is generally not recommended.

from math import *
print(floor(4.5997564))
print(ceil(4.5997564))

#use of the 'as' keyword
import math as m
print(m.sqrt(100))
from math import sqrt as s, pi as p
print(s(64)*p) #or else also to expand the name of the module for better understanding.

#dir() function - this can be used to view the names of all the functions and variables defined in a module.
print(dir(math))

#we can also import different functions and variables from a different existing python file.
from python18 import a,welcome
print(a)
welcome()
#or
import python18 as pr
pr.welcome()
# or
from python18 import welcome as w
w()