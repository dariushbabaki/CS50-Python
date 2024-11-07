def main():
    while True:
        try:
            fraction = str(input("Fraction: ").strip())
            print(gauge(convert(fraction)))
            break
        except (ValueError, ZeroDivisionError, UnboundLocalError):
            print("Invalid input. Please enter a fraction in the form X/Y.")
            continue

def convert(fraction):
    try:
        x, y = fraction.split("/")
        x, y = int(x), int(y)
        if x > y or y == 0:
            raise ValueError("Invalid fraction: X must be less than or equal to Y, and Y cannot be zero.")
        return (x / y) * 100
    except (ValueError, TypeError):
        raise ValueError("Invalid input. Please enter a fraction in the form X/Y.")

def gauge(percentage):
    if percentage >= 99:
        return "F"
    elif percentage <= 1:
        return "E"
    else:
        return f"{percentage:.0f}%"

if __name__ == "__main__":
    main()
