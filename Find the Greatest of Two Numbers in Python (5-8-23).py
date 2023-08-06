#Method 1: Find the Greatest of Two Numbers in Python

num1=int(input("Enter a number1:"))
num2=int(input("Enter a number2:"))
if num1>num2:
   print("True")

else:
    print("False")



#Method 2: Using Ternary Operator

num1,num2=30,40
print((num1 if num1>num2 else num2))


#Method 3: Using inbuilt max() Function

num1,num2=50,100
print(max(num1,num2))
