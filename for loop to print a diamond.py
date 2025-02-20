#Use for loops to print a diamond 
x=input("What element you wanna use as diamond? ")
num1=int(input("Enter how high you want the diamond: "))
if num1%2==0:
    print("As the input is even, it will be a pseudo diamond")
    a=((num1)//2)
    for i in range(0,a):
        print(" "*(a-i),x*(2*i+1))
    for i in range(a,0,-1):
        print(" "*(a-(i-1)),x*(2*i-1))
else:
    a=((num1+1)//2)
    b=((num1-1)//2)
    for i in range(0,a):
        print(" "*(b-i),x*(2*i+1))
    for i in range(b,0,-1):
        print(" "*(b-(i-1)),x*(2*i-1))
