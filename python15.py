#using for loops with else statements in python.
for i in range(7):
    print(i)
else:
    print("This is the false condition")

#In these cases, we need to identify the false condition.
#in the above case, when i becomes 7, the condition(i<7) becomes false. So, then the else statement gets executed.

for i in []:
    print(i)
else:
    print("Sorry no i.") #false as there is no i in the empty list.

for i in range(8):
    print(i)
    if (i==5):
        break
else:
    print("the else statement is executed.") #in this case the false condition is not met, so the else statement is not executed.

#In the case with while loops.
i=0
while (i<9):
    print("The number is {}".format(i))
    i+=1
else:
    print("This is the end of the loop.")   #here the loop encounters the false statement.

'''In a for loop, the else clause is executed after the loop reaches its final iteration.

In a while loop, it’s executed after the loop’s condition becomes false.

In either kind of loop, the else clause is not executed if the loop was terminated by a break.'''