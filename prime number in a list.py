#Gives prime numbers from a given list of numbers
lst1=[]
lst2=[]
while True:
    num=int(input("Enter the number: "))
    lst1.append(num)
    ch=input("Want to add more quantities?(y/no) ")
    if ch=="no":
        break
prime_checker=False
for i in lst1:
    if int(i)<=1:
        prime_checker=False 
    elif int(i)==2:
        prime_checker=True      
    else:
        for j in range(2,i):
            if int(i)%int(j)==0:
                prime_checker=False
                break
            else:
                prime_checker=True            
    if prime_checker==True:
        lst2.append(i)
print("The original list is:",lst1)
print("The list contating prime numbers is:",lst2)