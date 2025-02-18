with open("sample.txt","r") as f:
    count=len(f.readlines())
    print(f"The no.of lines in a file is {count}")