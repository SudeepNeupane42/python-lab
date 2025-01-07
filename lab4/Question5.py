# 5. Write a function that greets a user. If no name is provided, it should greet with a default name.
def greet(name="ram"):
    print(f"welcome {name}")
    
name=input("Enter your name: ")
greet(name)