# 3. Write a function multiply that multiplies two numbers, but can also accept and multiply strings.

def multiply(a,b):
    if(isinstance(a,str)and isinstance(b,str)):
        return a+b
    else:
        return a*b
    
print(multiply('sirifiri','sudeep'))