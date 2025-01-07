# 7. Write a function that takes variable number of arguments and returns their sum.
def add(*args):
    return sum(args)

print(add(2,6,9,4))
print(add(5,8,2,9,5,7))
