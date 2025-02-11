class InvalidAgeError(Exception):
    pass


try:
    age=int(input("Enter your age: "))
    if(age<0 or age>120):
        raise InvalidAgeError("Invalid age eror occured")
except (ValueError, InvalidAgeError) as e:
    print(e)
else:
    print(f"Your age is {age}")
finally:
    print("this is the end of code")