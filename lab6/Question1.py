try:
    a=int(input("enter first number "))
    b=int(input("enter second number "))
    div=a/b
except (ZeroDivisionError,ValueError) as e:
    print(f"the error is  {e}")
finally:
    print("the division is ")
