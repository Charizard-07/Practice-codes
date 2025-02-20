#Finding Palindromes in a List
lst1=[]
lst2=[]
while True:
    wor=(input("Enter letter: "))
    lst1.append(wor)
    ch=input("Want to add more quantities? ")
    if ch.lower()=="no":
        break
print("The original list is",lst1)
for i in lst1:
    if i.lower() == i.lower()[::-1]:
        lst2.append(i)
print("The palindrome list is",lst2)