#factorial using while loop
mul=1
num=int(input("Enter the number whose factorial you want to know: "))
while num>=1:
    mul=num*mul
    num=num-1
print(mul)


