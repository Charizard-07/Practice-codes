#Write a program that asks the user how many Fibonacci numbers to print and then prints that many
num1 = int(input("How many Fibonacci numbers to print?: "))
a,b=1,1
print("Here is your Fibonacci series:")
for i in range(num1):
    print(a,end="," if i < num1-1 else "\n")
    a,b=b,a+b

