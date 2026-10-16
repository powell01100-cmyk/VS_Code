students_Name= ["Alice", "Bob", "Charlie"]
for student in students_Name:
 print(student) 


 student_scores = [70, 85, 90, 50, 40, 45, 60, 49]
for score in student_scores:
        if score >=80:
            print ("Your score is impressive")
        elif score < 60:
            print ("Your score is below average")
        else:
            print ("Your score is average")



students =[
 [ "David", 70 ],
 [ "Eve", 85 ],
 [ "Frank", 90 ],
 [ "Grace", 50],
 [ "Henry", 40],
 [ "Ivy", 45],
 [ "Jack", 60],
 [ "Kate", 49],]
for student in students:
    name = student[0]
    score = student[1]
    if score >= 80:
        print ("Excellent")
    elif score >= 60:
        print ("Good")
    elif score >= 50:
        print ("Needs Improvement")
    else:
        print ("Fail")
   

User_name = input("Enter your name: ")
User_score = int(input("Enter your score: "))
User_age = int(input("Enter your age: "))
if User_score >= 80:
    result = "Excellent"
elif User_score >= 60:
    result = "Good"
elif User_score >= 50:
    result = "Needs Improvement"
else:
    result = "Fail"

print(f"{User_name}, your score is {User_score} and your result is {result}. You are {User_age} years old.")

minutes = input("Enter the number of minutes: ")
total_minutes = int(minutes)

hours = total_minutes // 60
remaining_minutes = total_minutes % 60

print(f"{total_minutes} minutes is equal to {hours} hours and {remaining_minutes} minutes.")

user_input = input("Enter the number of seconds: ")
try:
    total_seconds = int(user_input)
    
    if total_seconds < 0:
        print("Error: Please enter a positive number.")
    else:
        hours = total_seconds // 3600
        remaining_seconds_after_hours = total_seconds % 3600
        
        minutes = remaining_seconds_after_hours // 60
        seconds = remaining_seconds_after_hours % 60
        
        print(f"{total_seconds} seconds is equal to {hours} hours, {minutes} minutes, and {seconds} seconds.")
except ValueError:
    print("Error: Please enter a valid number.")

