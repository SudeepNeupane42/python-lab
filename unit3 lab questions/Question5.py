str=input("Enter a string: ")
list1=[]
for i in str:
    if i in list1:
        print(i)
        break
    else:
        list1.append(i)