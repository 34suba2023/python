#Method 1 Using simple iteration

num=int(input("Enter a number:"))
temp=num
rev=0
while temp>0:
   rem=temp%10
   rev=(rev*10)+rem
   temp=temp//10
if num==rev:
    print("Palindrome")
else:
    print("Not a palindrome")

#Method 2 using String slicing

num=131
rev=int(str(num)[::-1])
if num==rev:
    print('Palindrome')
else:
    print('not palindrome')


#Method 3 using Recursion

def recurnum(num,rev):
  if num==0:
      return rev

  rem=int(num%10)
  rev=(rev*10)+rem

  return recurnum(int(num/10),rev)

num=1229
rev=0
rev=recurnum(num,rev)

print(str(num) + " is:", end="")
print("palindrome") if rev==num else print("Not palindrome")


#Method 4 using character match
# srt[i]!=str[len(str)-i-1]  if yes then its not a palindrome

def checkpalindrome(str):


  for i in range(0,len(str)):
    if str[i]!=str[len(str)-i-1]:
        return False

  return True

#main function

s="kayak"

print("Palindrome") if checkpalindrome(s) else print("Not Palindrome")


















