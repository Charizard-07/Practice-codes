#Kaun banega crorepati game
print("KAUN BANEGA CROREPATI")
ch=0
mul=0
lst1=[
    "Who was the first Prime Minister of India?",
    "Which planet is known as the Red Planet?",
    "What is the capital of France?",
    "Which is the longest river in the world?",
    "In which year did India gain independence?"
    ]
lst2=["a","c","a","b","d"]
while ch<=4:
    print(lst1[ch])
    if ch==0:
        print("a.jawahar lal nehru\nb.Indira gandhi\nc.Rajendra prasad\nd.Mahatma gandhi")
    elif ch==1:
        print("a.Venus\nb.Earth\nc.Mars\nd.Saturn")
    elif ch==2:
        print("a.paris\nb.Marseille\nc.Nice\nd.Lyon")
    elif ch==3:
        print("a.amazon\nb.Nile\nc.ganga\nd.brahmputra")
    elif ch==4:
        print("a.1946\nb.1949\nc.1948\nd.1947")
    x=input("Enter your answer: ")
    if x.lower() == lst2[ch]:
        mul=mul+2000000
        print("Congratulations, correct answer! You won this round.")
        ch += 1 
    else:
        print("Wrong answer! Game over.")
        break  
print("you won",mul,"rupees")    
        
        
        





    







    