def add(a, b):
    return a+b


def sub(a, b):
    return a-b


def mult(a, b):
    return a*b


def div(a, b):
    return a/b


def power(a, b):
    return a**b


a = int(input("Enter your first number: "))
req = input("Enter oprator (+ , - , * , / , ** ): ")
b = int(input("Enter your second number: "))

if req == "+":
    result = add(a, b)
elif req == "-":
    result = sub(a, b)
elif req == "*":
    result = mult(a, b)
elif req == "/":
    result = div(a, b)
elif req == "**":
    result = power(a, b)
else:
    print("Invalid operator")

    result = None

print("Answer is: ", result)
