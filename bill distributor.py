#A group of friends goes to a restaurant. Write a program to calculate how much each person has to pay 
#if they want to split the bill equally. Also, allow a custom tip percentage.

bill=int(input("Enter the bill amount: "))
people=int(input("Enter the number of people: "))
tip_option=int(input('''
Do you want to give tip? Choose either of the default options:
1. No tip
2. Default(10%)
3. Custom\n'''))
if tip_option==1:
    print("Each person pays:", bill/people)
elif tip_option==2:
    a=bill+(0.1)*bill
    print("Each person pays:", a/people)
elif tip_option==3:
    custom=int(input("Enter the percentage of tip you want to give(=<50): "))
    if custom>50:
        print("You cant give more than 50% of bill as tip")
    else:
        a=bill+(custom/100)*bill
        print("Each person pays:", a/people)
else:
    print("Invalid option. Kindly choose from wither 1/2/3.")