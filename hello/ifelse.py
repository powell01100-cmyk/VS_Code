user_name = input("Enter your name: ")
Numbers = int(input("Enter a number: "))
if Numbers > 0:
    for i in range(Numbers):
        print(f"Hello {user_name}! This is message number {i+1}.")
else:
    print("Please enter a correct number.")

Pass = int(input("Enter your score: "))

if Pass >= 60:
    print("You have passed the exam.")
elif Pass >= 50:
    print("You have passed the exam but you need to retake it.")
elif Pass < 40:
    print("You have failed the exam and you cannot retake it.")
else:
    print("You have failed the exam ")

fail = int(input("Enter your score: "))

if fail <= 40:
    print ("You have failed but you try again.")
elif fail >= 80:
 print("You have passed the exam and you can achieve more prizes.")
elif fail >= 60:
    print( "You have passed the exam and you have a great score.")
elif fail >= 50:
    print("You have passed the exam exactly ")
else: 
    print("You have failed the exam and you cannot retake it.")



