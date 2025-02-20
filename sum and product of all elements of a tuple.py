#Given a tuple of numbers, write a program to calculate the sum and product of all the elements.
lst1=[]
while True:
    num=int(input("Enter the number: "))
    lst1.append(num)
    ch=input("Want to add more quantities? ")
    if ch.lower()=="no":
        break
tup1=tuple(lst1)
print(tup1)
add=0
mul=1
for i in tup1:
    add+=i
    mul*=i
print(add,"is the addition of all numbers given by you")
print(mul,"is the multiplication of all numbers given by you")




