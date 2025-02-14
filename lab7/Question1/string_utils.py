def reverse_string(str):
    return str[::-1]

def count_vowels(str):
    string=str.lower()
    vowels="aeiou"
    count=0
    for s in string:
        if s in vowels:
            count+=1
    return count 

if __name__== '__main__':
    print(count_vowels("rabin is gay"))
