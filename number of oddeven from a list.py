#Given a list of numbers, write a program to count how many of them are even and how many are odd.
lst1=[]
count1=0
count2=0
while True:
    num=int(input("Enter the number: "))
    lst1.append(num)
    ch=input("Want to add more quantities? ")
    if ch=="no":
        break
print(lst1)
for i in lst1:
    if i%2==0:
        count1=count1+1
    else:
        count2=count2+1
print("number of even numbers in the list are",count1)
print("number of odd numbers in the list are",count2)

