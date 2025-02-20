#You are a teacher grading students exams.Based on the total marks scored, assign a grade
print('''
Marks >= 90: A
Marks >=75 : B
Marks >= 50: C
Marks < 50: Fail
''')
marks=[]
str1=''
grades=[]
while True:
    num=int(input("Enter the number: "))
    marks.append(num)
    ch=input("Want to add more quantities?(y/no) ")
    if ch=="no":
        break
print("the marks of the students are:",marks)
for i in marks:
    if i>=90:
        str1='A'
    elif i>=75:
        str1='B'
    elif i>=50:
        str1='C'
    else:
        str1='Fail'
    grades.append(str1)
print("grades of the students are:",grades)
    


