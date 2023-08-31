n=int(input("Enter num:"))
temp=n
rev=0
while n>0:
    rem=n%10
    rev=(rev*10)+rem
    n=n//10
print("The given num is {} and reverse num is {}".format(temp,rev))
