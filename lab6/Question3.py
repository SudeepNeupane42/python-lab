class EmptyListError(Exception):
    pass


list1=[]
n=5
try:
    while(n):
        num=int(input("Enter a number: "))
        list1.append(num)
        n-=1
        
    if not list1:
        raise EmptyListError("Empty list error")
except (EmptyListError,ValueError) as e:
    print(e)
else:
    print(list1)
finally:
    print("this is the end of code")