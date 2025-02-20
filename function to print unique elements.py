#Write a function unique_elements(lst) that returns a new list containing only the unique elements from the input list lst.
def unique_elements(lst):
    lst2 = []  
    for i in lst:
        if i not in lst2:  
            lst2.append(i)  
    return lst2
lst = input("Enter list elements separated by comma: ").split(',')
lst2=[]
for i in lst:
    lst2.append(int(i))
print(unique_elements(lst2))


        
                 

