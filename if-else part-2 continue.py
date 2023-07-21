#6.Make a mini calculator
# Get input for 2 numbers a and b
# Get input from user whether to add/sub/mul/div
# If user selects add the two number and print the result.

a=int(input("A:"))
b=int(input("B:"))
operator=input("add/sub/mul/div:")
if(operator=="add"):
    print(a+b)
elif(operator=="sub"):
    print(a-b)
elif(operator=="mul"):
    print(a*b)
elif(operator=="div"):
    print(a/b)
else:
    print("Invalid Operation")

