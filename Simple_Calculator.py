name=input("Hey,whats your name :-")

print(f"Hii {name}!,Hope your having good day")
greet=input()
print("lets do some calculations!")
def calc():
    try:
        num1 = int(input("enter num1:-"))
        num2 = int(input("enter num2:-"))
    except Exception as e :
        print(e)
        print("exit! next time enter numbers ")
        # calc()
        exit()
    op="operation are \n +  addition \n -  subtraction \n *  multiplication \n ** cube   \n /  divide \n %  modulo \n choose operations\n  "
    print(op)
    opera = input()
    # def opera():
    if opera=='+':
                    res = num1+num2
                    print(f"output of {num1} {opera} {num2} = {res} ")
    elif opera=='-':
                    res = num1-num2
                    print(f"output of {num1} {opera} {num2} = {res} ")
    elif opera=='*':
                    res = num1*num2
                    print(f"output of {num1} {opera} {num2} = {res} ")
    elif opera=='**':
                    res = num1**num2
                    print(f"output of {num1} {opera} {num2} = {res} ")
    elif opera=='/':
                    res = num1/num2
                    print(f"output of {num1} {opera} {num2} = {res} ")
    elif opera=='%':
                    res = num1%num2
                    print(f"output of {num1} {opera} {num2} = {res} ")
    else:
                    print("invalid operations enter again")
                    # print(input(op))
                    # opera()

calc()
while True:
    a=input("do you want to continue ? yes/no:- ")
    if a=="yes":
      calc()
    elif a=="no":
        print("Exit Done...")
        break
    else:
        print("enter proper answer ")
