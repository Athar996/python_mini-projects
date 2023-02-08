******create a file with score.txt and 

paste the location of file in code accordingly***********

 f = open('D:\Visual Studio\python\score.txt','r')

data = f.read()
dataint = int(data)
print("previous highscore was:-",dataint)
# f = open('D:\Visual Studio\python\score.txt','r')
newint = int(input("enter score for now as a proxy"))
print(newint)
newstring = str(newint)

if dataint>newint:
    print("new score not beaten the high score")
    f = open('D:\Visual Studio\python\score.txt','r')
    f.close()
else:
    print("new high score is:- ",newstring)
    print("congrats!,you have beaten the highscore")  
    f = open('D:\Visual Studio\python\score.txt','w')
    f.write(newstring)
f.close()
