#Find the Length of a List without Using len()
lst1=[]
count=0
while True:
    num=int(input("Enter the number: "))
    lst1.append(num)
    ch=input("Want to add more quantities?(y/no) ")
    if ch=="no":
        break
print(lst1)
for i in lst1:
    count+=1
print("The length of the list is",count)
