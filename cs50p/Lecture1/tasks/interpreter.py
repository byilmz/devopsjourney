interpreter = input("Expression: ")
x, y, z = interpreter.split()
x = float(x)
z = float(z)

match y:
    case "+":
        result = x + z
    case "-":
        result = x - z
    case "*":
        result = x * z
    case "/":
        if z != 0:
            result = x / z
        else:
            print("Error: Division by zero")
            exit()
    case _:
        print("Error: Invalid operator")
        exit()

print(f"{result:.1f}")
