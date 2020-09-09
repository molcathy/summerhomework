integer = False

while not integer:
    n = input("Enter A number: ")
    isfloat = False
    for c in n:
        if c == ".":
            print("float")
            isfloat = True
            break
    if isfloat != True:
        print(n)
        integer = True