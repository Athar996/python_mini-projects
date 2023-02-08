 x=int(input("enter a random num from 1 to 8 :-"))

tuple1=(1,2,6,7,8,3,4,5)
list2=tuple(tuple1)
length=len(tuple1)
mid=int(length/2)
if (x in tuple1):
    print("creating 2 halves of tuple1 are ")
    first_half=tuple1[:mid]
    second_half=tuple1[mid:]
    print("1st half is ",first_half)
    print("2nd half is ",second_half)
    if (x in first_half):
        print("it is in first half so divide that ")
        tuple1=first_half
        length=len(tuple1)
        mid=int(length/2)
        inner_first_half=first_half[:mid]
        print("1st half is ",inner_first_half)
        inner_second_half=first_half[mid:]
        print("2nd half is ",inner_second_half) 
        if (x in inner_first_half ):
            print("num is at index of",list2.index(x))
        elif(x in inner_second_half ):
            print("num is at index of",list2.index(x))
        else:
            print("Something is wrong Try agian")
       
    else:
        print("it is in second half")
        tuple1=second_half
        length=len(tuple1)
        mid=int(length/2)
        inner_first_half=second_half[:mid]
        print("1st half is ",inner_first_half) 
        inner_second_half=second_half[mid:]
        print("2nd half is ",inner_second_half) 
        if (x in inner_first_half ):
            print(list2.index(x)) 
        elif(x in inner_second_half ):
            print(list2.index(x))
        else:
            print("Something is wrong try again")
else:
    print("Game Over !!!")
