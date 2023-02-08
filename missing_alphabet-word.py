 print("Welcome to the round 1")

print("lets play round1")
x = input("question 1 is : i_e:")
if x == "c":
    print("I"+x+"e")
    a = print(bool("correct answer")) 
else:
  print("wrong answer")
y = input("question 2 is : ca_:")
if y == "r":
    print("c"+"a"+y)
    b =  print(bool("correct answer"))
    print("congrats! moved to 2nd round")
else:
  print("wrong answer not qualified ")
  exit()
print("welcome to 2nd round**********************************************")
print("lets play 2nd round")
if a == b:
    c = d= e= None
z = input("question 3 is : bik_:")
if z == "e":
    print("b"+"i"+"k"+z)
    print("correct answer")
    c=True
    # print(c)
else:
  print("wrong answer ")
  c=False
#   print(c)
k = input("question 4 is : d_y:")
if k == "a":
    print("d"+k+"y")
    print("correct answer")
    d=True
    # print(d)
else:
  print("wrong answer")
  d=False
#   print(d)
l = input("question 5 is : ni_ht:")
if l == "g":
    print("n"+"i"+l+"h"+"t")
    print("correct answer")
    e=True
    # print(e)
else:
  print("wrong answer")
  e=False
#   print(e)
if c & d or d & e or e & d or c & e == True:
    print("congrats! welcome to 3rd round**********************************************")
    print("lets play 3rd round")
else:
    print("its gone i say")
f = g= h= None
m = input("question 6 is : ha_ _y:")
q = input("enter other missing alphabet of same question:-")
if m and q == "p":
    print("h"+"a"+m+q+"y" )
    print("correct answer")
    f=True
    # print(c)
else:
  print("wrong answer ")
  f=False
#   print(c)
n = input("question 7 is : G_ _d:")
w = input("enter other missing alphabet of same question:-")
if n and w== "o":
    print("G"+n+w+"d")
    print("correct answer")
    g=True
    # print(d)
else:
  print("wrong answer")
  g=False
#   print(d)
o = input("question 8 is : we_ _:")
e = input("enter other missing alphabet of same question:-")
if o == "l":
    print("w"+"e"+o+e)
    print("correct answer")
    h=True
    # print(e)
else:
  print("wrong answer")
  h=False
if f == g== h == True:
    print("Damnnnnnnnn! u r the Winner")
else:
    print("almost won but in last round u have losted")
