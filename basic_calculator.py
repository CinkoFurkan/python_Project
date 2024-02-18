def add(a, b):
    answer = a + b
    print(str(a) + "+" + str(b) + "=" + str(answer) + "\n")


def sub(a, b):
    answer = a - b
    print(str(a) + "-" + str(b) + "=" + str(answer) + "\n")


def mul(a, b):
    answer = a * b
    print(str(a) + "*" + str(b) + "=" + str(answer) + "\n")


def div(a, b):
    answer = a / b
    print(str(a) + "/" + str(b) + "=" + str(answer) + "\n")


while True:
    print("""\
      A. Addition
      B. Subtraction
      C. Multiplication
      D. Division
      E. Exit""")

    choice = input("Input yur choice: ")

    if choice == "a" or choice == "A":
        print("Addition")
        a = int(input("input your first number: "))
        b = int(input("input your second number: "))
        add(a, b)

    elif choice == "b" or choice == "B":
        print("Subtraction")
        a = int(input("input your first number: "))
        b = int(input("input your second number: "))
        sub(a, b)

    elif choice == "c" or choice == "C":
        print("Multiplication")
        a = int(input("input your first number: "))
        b = int(input("input your second number: "))
        mul(a, b)

    elif choice == "d" or choice == "D":
        print("Division")
        a = int(input("input your first number: "))
        b = int(input("input your second number: "))

    elif choice == "e" or choice == "E":
        print("Program ended")
        quit()
