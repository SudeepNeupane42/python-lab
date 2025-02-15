# 4. Write a Python program that takes a list of numbers and a target number as input. Use enumeration to find the index of the first occurrence of the target number. If the target number is not found, print -1.

numbers = [13,14,25,67,83,45,2,1,5,3,4,7,6,8,9,13,24,16,27,12,11,15,7]
target = int(input("Enter the target number: "))

for index, number in enumerate(numbers):
    if target == number:
        print(f"The index of target is {index}")
        break
    if index == len(numbers)-1:
        print("-1")
        