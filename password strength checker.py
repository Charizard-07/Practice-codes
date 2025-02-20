#Write a program that takes a password as input and checks whether it is strong
print('''A password is strong if:
1. It is at least 8 characters long.     
2. It contains both uppercase and lowercase characters.
3. It contains at least one digit.
4. No space
''')
password = input("Enter your password: ")
if len(password)>=8:
    if ' ' in password:
        print("No space can be in password. Please try again")
    else:
        up= False
        low= False
        dig= False
        for i in password:
            if i.isupper():
                up=True
            elif i.islower():
                low=True
            elif i.isdigit():
                dig=True
        if up==True and low==True and dig==True:
            print("Your password is strong")
        else:
            print("Password is weak")
else:
    print("Password is weak")
