class NegativeNumberError(Exception):
    pass


try:
    a=int(input("Enter a positive number: "))
    if a<0:
        raise NegativeNumberError("Negative Number Error Occured")
except NegativeNumberError as e:
    print(e)
finally:
    print("end of program")