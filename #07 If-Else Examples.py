# (15.05.2023)

#practice - day 1(24.05,23)

#8.Get input for salary and age.
#
#
#

sal=int(input("Enter sal:"))
age=int(input("Enter age:"))
if(sal>=20000 or age<=25):
    loan=int(input("Loan:"))
    if(loan>50000):
        print("Maximun loan amount is 50000")
    else:
        print("You are eligible for loan")
        
else:
    print("You are not eligible for loan")
        
     
   
