with open("sample.txt","a") as f:
    string="\n Append Line"
    f.writelines(string)
    print("File append succesfully")