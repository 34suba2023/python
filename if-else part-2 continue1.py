#7.Get a inpu for score percentage. Only if the percentage is greater than 70,
# get input for his name, department and location. Then print you are eligible.
#If not print you are nor eligible.


score=int(input("score percentage ?:"))
if(score>=70):
    name = input("Enter your name:")
    age = int(input("Enter your age:"))
    location = input("Enter your location:")
    print("You are eligible")
else:
    print("You are not eligible")




