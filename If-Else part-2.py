#part-2 (If-else statements in youtube channel)
#4.Get input for a number and find it is even or odd.

#num/2 is EVEN
#num!/2 is ODD

num=int(input("Enter a Number"))
if (num%2==0):
    print("Even")
else:
    print("Odd")


#5. Get input for score out of 100.
# If score is <35="Poor student"
# If score is greater than 35 but < than 70 = "Average student"
# If score is greater than 70 = "Good student"

score=int(input("Score"))
if(score<35):
    print("Poor student")

if(score>35 and score<70):
    print("Average student")

if(score>70):
    print("Good student")
    

#in python new method ...elif
score=int(input("Score"))
if(score<35):
    print("Poor student")

elif(score>35 and score<70):
    print("Average student")

else:
    print("Good student")


#to modify else part only
#above program else ku pathila elif potu greater than 70 & less than 100"Good student"
#suppose i give 101...else la "Invalid syntax"


score=int(input("SCORE"))
if(score<35):
    print("POOR STUDENT")
elif(score>35 and score<70):
    print("AVERAGE STUDENT")
elif(score>70 and score<100):
    print("GOOD STUDENT")
else:
    print("INVALID SCORE")
    



