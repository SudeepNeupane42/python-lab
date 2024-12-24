# Wap to check if a given year is a leap year. A year is a leap year if it is divisible by 4 but not divisible by 100,
# or it is divisible by 400. Implement the logic using nested if statements.

year=int(input("enter a year: "))
if(year%4==0 and year%100!=0):
    print(f"the year {year} is a leap year")
else:
    print(f"the year {year} is not a leap year")
