with open('C:/projects/referat.txt', 'r', encoding='utf-8') as f:
    content = f.read().replace("\n"," ").replace(".","!")
    with open('C:/projects/referat2.txt', 'w', encoding='utf-8') as f:
        f.write(content)
    print(content)
    print(len(content))
    words= content.split(" ")
    print(words)
    print(len(words))

    