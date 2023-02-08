import random 
def game(comp,user):
    if comp == user:
         return  "game_draw"

    if comp == "rock":
        if user== "paper":
            return "user won"
        elif user =="scissor":
            return "comp won"  
        # else:
        #     return "game draw"    

    if comp == "paper":
        if user== "rock":
            return "comp won"
        elif user== "scissor":
            return "user won" 
        # else:
        #      return "game draw"    

    if comp == "scissor":
        if user== "rock":
            return "user won"
        elif user == "paper":
            return "comp won" 
        # else:
        #     return "game draw"    
while True:
    randomnum = random.randint(1, 3)
    if randomnum == 1:
        comp = "rock"
    elif randomnum == 2:
        comp = "paper"
    elif randomnum == 3:
        comp = "scissor"
    x = input("players chance chooose 1. Rock(1) \t 2.Paper(2)\t 3.Scissor(3):- ")
    if x == 1 or "rock":
        user = "rock"
    elif x == 2 or "paper":
        user = "paper"
    elif x == 3 or "scissor":
        user = "scissor"
    else: 
        user = "Wrong input"
    print("computer choosed :-",comp)
    print("user choosed :-",user)
    
    yo= game(comp,user)
    print(yo)
