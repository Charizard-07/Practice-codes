#A library stores a list of books and their status (whether they are available or checked out). 
#Write a program that searches for a book by its title and tells if it is available.
print("There are total 16 books. Kindly write the book name")
book_name=input("Enter the book name: ")
lst1=[
("book1","available"),
("book2","checked out"),
("book3","available"),
("book4","checked out"),
("book5","available"),
("book6","checked out"),
("book7","available"),
("book8","checked out"),
("book9","available"),
("book10","available"),
("book11","checked out"),
("book12","available"),
("book13","available"),
("book14","checked out"),
("book15","available"),
("book16","checked out")
]
book_found=False                               #initially assume the book is not found
for i in lst1:
    if i[0]==book_name:
        book_found=True                        #as when book is find, it becomes true 
        if i[1].lower()=="checked out":
            print(i[0],"is checked out")
        elif i[1].lower()=="available":
            print(i[0],"is available")
            print("You can issue it. Have a nice day!!!")
if book_found==False:                          #if the book found doesnt become true in the whole loop, it means the book isnt in database
    print("Sorry the book is not in our database")

