# a company gives a discount based on the following conditions:
# 1 purchase amount greater than $10000: 20% discount
# 1 purchase amount between $5000 and $10000: 10% discount
# 1 purchase amount less than $5000: No discount
# write a python program to calculate the final price after applying the discount.

amt=int(input("Enter the purchase amount: "))
    
if(amt>10000):
    print(f"your purchase amount is {amt-(0.2*amt)}")
elif(amt>=5000 and amt<10000):
    print(f"your purchase amount is {amt-(0.1*amt)}")

else:
    print(f"your purchase amount is {amt}")
