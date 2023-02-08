*********kindly create data.txt file and edit in code accordingly**********

*********kindly download or add your own music and add locations of it on                                         code**********

*********my drive link for audio download  audio downloads ****



 # To drink water  after every 60 minutes

# To perform eye exercise after every 45 minutes
# To eat after every 30 minutes.
# Adjust time and locations in code accordingly

print("hellooo")
name=input("enter your name:-")
print("remainder !!!!!!!!!!!!!!!")
print("please drink some water")

from pygame import mixer
import time
content= time.asctime(time.localtime(time.time()))
mixer.init()
    
def exitfuncto():       
        print("Enter exit to exit from whole program")
        print("For continue process type continue ")
        # print("Delaying giving  input takes as no")
        query = input("")   
        if query == 'exit':
            mixer.music.stop()
            print(f"Okay {name}! ,exited ")
            exit()
        elif query == 'continue':
            print(f"Okay {name}! lets continue")
        else:
            print(f"hey {name} enter valid input")

while True:
    mixer.music.load("D:\Visual Studio\Python\practise_codes\Projects\water_exercise\music\Jism2.mp3")
    mixer.music.set_volume(0.2)
    mixer.music.play(-1)
    print("please enter drank if u have completed drinking water")
    query = input("")   
    content= time.asctime(time.localtime(time.time()))
    
    if query == 'drank':
        mixer.music.pause() 
        with open("D:\Visual Studio\Python\practise_codes\Projects\water_exercise\data.txt",'a') as f:
            f.write(f"\n\nuser name is:- {name}")
            f.write("\nyou have drunk water at:- ")
            f.write(content)
        print("Thank you for water, I will remind you after 10s")
        exitfuncto()
        time.sleep(10)
    else:
        mixer.music.set_volume(0.6)
        mixer.music.play(-1)
        while query!='drank':
            print("please enter valid input to hold alarm ")
            mixer.music.play(-1)
            query = input("")
        content= time.asctime(time.localtime(time.time()))
        mixer.music.pause() 
        with open("D:\Visual Studio\Python\practise_codes\Projects\water_exercise\data.txt",'a') as f:
            f.write(f"\nuser name is:- {name}")
            f.write("\nyou have drunk water at:- ")
            f.write(content)
        print("Thank you, I will remind you after 10s")
        exitfuncto()
        time.sleep(10)  

    print("please enter eydone after doing some exercise:- ")
    mixer.music.load("D:\Visual Studio\Python\practise_codes\Projects\water_exercise\music\Vivo.mp3")
    mixer.music.set_volume(0.3)
    mixer.music.play(-1)    
    query = input("")   
    content= time.asctime(time.localtime(time.time()))

    if query == 'eydone':
        mixer.music.pause() 
        with open("D:\Visual Studio\Python\practise_codes\Projects\water_exercise\data.txt",'a') as f:
            f.write("\nyou have done exercise at:- ")
            f.write(content)
        print("Thank you, I will remind you after 20s")
        exitfuncto()
        time.sleep(20)
    else:
        mixer.music.set_volume(0.6)
        mixer.music.play(-1)
        while query!='eydone':
            print("please enter valid input to hold alarm ")
            mixer.music.play(-1)
            query = input("")
        content= time.asctime(time.localtime(time.time()))
        mixer.music.pause() 
        with open("D:\Visual Studio\Python\practise_codes\Projects\water_exercise\data.txt",'a') as f:
            f.write("\nyou have done exercise at :- ")
            f.write(content)
        print("Thank you, I will remind you after 20s")
        exitfuncto()
        time.sleep(20)  

    print("please enter eat after eating some snacks:- ")
    mixer.music.load("D:\Visual Studio\Python\practise_codes\Projects\water_exercise\music\Andro.mp3")
    mixer.music.set_volume(0.3)
    mixer.music.play(-1)    
    query = input("")   
    content= time.asctime(time.localtime(time.time()))

    if query == 'eat':
        mixer.music.pause() 
        with open("D:\Visual Studio\Python\practise_codes\Projects\water_exercise\data.txt",'a') as f:
            f.write("\nyou have ate snacks at:- ")
            f.write(content)
        print("Thank you, I will remind you  after 30s")
        exitfuncto()
        time.sleep(30)
    else:
        mixer.music.set_volume(0.6)
        mixer.music.play(-1)
        while query!='eat':
            print("please enter valid input to hold alarm ")
            mixer.music.play(-1)
            query = input("")
        content= time.asctime(time.localtime(time.time()))
        mixer.music.pause() 
        with open("D:\Visual Studio\Python\practise_codes\Projects\water_exercise\data.txt",'a') as f:
            f.write("\nyou have ate snacks at :- ")
            f.write(content)
        print("Thank you, I will remind you after 30s")
        exitfuncto()
        time.sleep(30)  
