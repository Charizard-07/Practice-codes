str0=input("Enter the string: ")
str1='''
1.The total number of characters in the string,
2.The string repeated 10 times,
3.The first character of the string (remember that string indices start at 0),
4.The first three characters of the string,
5.The last three characters of the string,
6.The string backwards,
7.The seventh character of the string if the string is long enough and a message otherwise,
8.The string with its first and last characters removed,
9.The string in all caps,
10.The string with every a replaced with an e,
11.The string with every letter replaced by a space
'''
print(str1)
str2=input("What operation you want to perform?(Enter serial number): ")
count=0
if str2=="1":
    for i in str0:
        count+=1
    print(count)
if str2=="2":
    for i in range(10):
        print(str0)
if str2=="3":
    print(str0[0])
if str2=="4":
    print(str0[0:3])
if str2=="5":
    print(str0[len(str0)-3:])
if str2=="6":
    print(str0[::-1])
if str2=="7":
    if len(str0)>=7:
        print(str0[6])
    else:
        print("string dosen't have enough letters")
if str2=="8":
    str3=str0[1:len(str0)-1]
    print(str3)
if str2=="9":
    str0=str0.upper()
    print(str0)
if str2=="10":
    for i in str:
        if i=="a":
            str0=str0.replace("a","e")
    print(str0)
if str2=="11":
    for i in range(len(str0)):
        if str0[i].isalpha():
            str0=str0.replace(str0[i]," ")
    print(str0)
    

    