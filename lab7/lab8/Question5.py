with open("sample.txt","r") as f:
    count=0
    context=f.read()
    content=context.split()
    count +=len(content)
    print(count)