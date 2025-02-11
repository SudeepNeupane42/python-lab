i=0
try:
    while(i<3):
        num=int(input("Enter a number between 1 to 10: "))
        if(num>=10 or num<1):
            print("the number was not  between 1 to 10")
            i+=1
        else:
            break
    if i==3:
        raise ValueError("number not between 1 to 10 error occured")
except ValueError as e:
    print(e) 