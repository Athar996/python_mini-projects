import random
compchoose= random.randint(1,10)
str="wrong guess ,use hints"
print("comp chooses 1 num u have to enter numb untill it matches and gives hints")
for i in range(4):
    x= int(input("hey user guesss the number from the 1 to 10 :-"))
    if(x==compchoose):
        print("congo!,you are correct")
        exit()
    elif(x!=compchoose):
        print(str)        
        if i==0:
            print("hint1")      
            if compchoose%2==0:
                print("might be a even")           
            else:
                print("might be a odd") 
        elif i==1:
            print("hint2")
            if compchoose<4:
                print("num is less then 4 ")
            else:
                print("num is greater then 4 ")
        elif i==2:
            print("hint3")
            if compchoose<7:
                print("num is less then 7 ")
            else:
                print("num is greater then 7 ")           
        elif i>2:
            print("Dumb! ,No more hints,Game lost")

    
        ********************other way **************************

n = 8
chances= 10
yo = 1
while(chances>0):
    print("numbers range from 1 to 10")
    print(f"chances left are:- {chances}")
    chances=chances-1
    guess= int(input("enter the number to check whether it matches or not:-"))
    if guess ==n:
        print("you won")
        x =chances
        left = 10 -x
        print(f"you took {left} chances to crack the number")
        exit()
    elif guess<n:
        print("need to increment guess number  ")
    elif guess>n:
        print("need to decrement the guess number   ")
