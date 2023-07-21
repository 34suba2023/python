#9 For Loop with Examples Part 1
#Q1. Get input for number a and b. Print the number btw a & b.


a=int(input())
b=int(input())
for i in range(a+1,b):
   print(i)

#Q2. Print even number between 1 to 10.

for i in range (1,11):
   if(i%2==0):
       print(i)

#Q3. Count the number of Even & Odd numbers between 1 to 10.

Even_count=0
Odd_count=0
for i in range(1,11):
    if(i%2==0):
        Even_count =Even_count+1
    else:
       Odd_count = Odd_count+1
print(Even_count)
print(Odd_count)

#Q4. Count the number which are divisible by 3 & 5. Range 1-100.

count=0
for i in range(1,101):
   if(i%3==0 and i%5==0):
       count = count+1
print(count)
