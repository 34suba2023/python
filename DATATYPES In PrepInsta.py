#INT

#user input of integer
val1=int(input("Enter any integer value:"))
print(val1)
val2=2+67j
print(val2)


#FLOAT
#user input of float
num1=float(input("Enter a float value:"))
print(num1)
num2=23.1313
print(num2)



#COMPLEX NUMBER
#user input
a=complex(input("Enter a complex number:"))
print(a)
b=3+4j
print(b)



#DICTIONARY
#creating dictionary
store=dict({'Name':'maha','contact': 9000277755,1:'id_no'})
print(store)
print(store.keys())
print(store.values())


#BOOLEAN
#Boolean in if-else conditioons
if True:
    print("I am always True")
else:
    print("I am False")

#boolean in while loop
i=1
while i==True:
    print("I am True")
    i=0




#SET(stores non-repeating values)
#user-defined set
suba=set([1,2,3,4,3,1,2,6])
print(suba)

#check fro element
if 1 in suba:
    print('True')


#LIST
#initialising a List
arr=[1,2,3,2,4,5,4]
print(arr)
print(type(arr))



#STRING (very strong data-type in python,Immutable)
sai="Beginer to Python"
print(sai)
STR=str(input("Enter the string:"))
print(STR)


#TUPLE(Like list & set| immutable| hashable whereas lists not)

num=tuple([1,2,3,4,2,4,5,1])
print(num)
print(type(num))















