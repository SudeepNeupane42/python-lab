# this is just example

a = ["Geeks", "for", "Geeks"]

# Iterating list using enumerate to get both index and element
for i, name in enumerate(a):
    print(f"Index {i}: {name}")

# Converting to a list of tuples
print(list(enumerate(a)))