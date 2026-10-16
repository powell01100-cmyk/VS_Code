from binascii import Error


numbers=10
i = 1
while i <= numbers:
    print(f"The value of i is {i}.")
    i += 1

user_name = input("Enter your name: ")
Numbers = int(input("Enter a number: "))

if Numbers < 0:
    print("Please enter a correct number.")

else:
    for i in range(Numbers):

        print(f"Hello {user_name}! This is message number {i+1}.")

def sum_of_numbers(n):
    total = 0
    for i in range(n):
        total += i
    return total
sum = sum_of_numbers(50)
print(sum)

a =50
for i in range(a):
    print(i)







 



 
 



    