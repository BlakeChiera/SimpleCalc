if __name__ == "__main__":

    x = int(input("Number 1: "))
    y = int(input("Number 2: "))
    op = input("operator: ")

    if op == "x":
        print(x*y)
    elif op == "/":
        print(x/y)
    elif op == "+":
        print(x+y)
    elif op == "-":
        print(x-y)
