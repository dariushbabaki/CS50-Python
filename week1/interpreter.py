expression = input("Enter an arithmetic expression:")

operator = None
for op in ['+', '-', '*', '/']:
    if op in expression:
        operator = op
        break

if operator is None:
    print("The operator is invalid")
else:
    
    try:
        x, z = expression.split(operator)
        
        x = int(x)
        z = int(z)

        if operator == '+':
            result = x + z
        elif operator == '-':
            result = x - z
        elif operator == '*':
            result = x * z
        elif operator == '/':
            if z != 0:
                result = x / z
            else:
                result = "Division by zero is not possible"
        
        if isinstance(result, (int, float)):
            print(f"result {round(float(result), 1)}")
        else:
            print(result)

    except ValueError:
        print("The input format is incorrect. Please enter a valid integer")
