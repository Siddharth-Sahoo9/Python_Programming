#Exercise
ques=["Which color in the traffic light means stop?\n\n A)red B)yellow C)green D)none of these.\n", "How many colors are there in the rainbow?\n\n A)5 B)7 C)8 D)9\n"]
print("\nSwagat hai aapka Kaun Banega Crorepati (KBC) mein.\n")
ans=['A', 'B']
sum=0
for i in range(len(ques)):
    print(i+1, "Question\n", ques[i])
    x=input('Enter the correct option in Capital or if you want to quit press "Q"\n')
    if(x==ans[i]):
        print("Correct answer!\n")
        sum+=1000
        print("You have won Rupees", sum)
    elif(x=='Q'):
        print("Thank you for playing!")
        break
    else:
        print("Wrong answer!\n")
        break
    input("Press any key!")     #on pressing something only the loop will move forward.(improves the presentation.)
print("Your total earnings from KBC is - Rupees", sum)
print(i)