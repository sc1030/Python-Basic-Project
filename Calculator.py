num1 = int(input("Enter First Number: "))
num2 = int(input("Enter Second Number: "))
op = input("Enter Operator (+ , - , * , / , %): ")

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "*":
    print(num1 * num2)
elif op == "/":
    if num2 != 0:
        print(num1 / num2)
    else:
        print("Error: Division by zero")
elif op == "%":
    if num2 != 0:
        print(num1 % num2)
    else:
        print("Error: Division by zero")
else:
    print(" Invalid operation! ")