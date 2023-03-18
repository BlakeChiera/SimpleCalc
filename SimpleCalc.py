if __name__ == "__main__":
    print("hello, world")

    x = int(input("x: "))
    y = int(input("y: "))
    op = input("operator: ")

    if op == "x":
        print(x*y)
    elif op == "/":
        print(x/y)
    elif op == "+":
        print(x+y)
    elif op == "-":
        print(x-y)
