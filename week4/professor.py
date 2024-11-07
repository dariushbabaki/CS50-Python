import random

def get_level():
    level = 0
    while level not in [1, 2, 3]:
        try:
            level = int(input("Enter your level (1, 2, or 3): "))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 3.")
    return level

def generate_integer(level):
    score = 0
    for x in range(10):
        if level == 1:
            number1 = random.randint(0, 10)
            number2 = random.randint(0, 10)
        elif level == 2:
            number1 = random.randint(10, 99)
            number2 = random.randint(10, 99)
        elif level == 3:
            number1 = random.randint(100, 999)
            number2 = random.randint(100, 999)
        else:
            raise ValueError("Invalid level")

        number3 = number1 + number2

        try:
            user_input = int(input(f"{number1} + {number2} = "))
            if user_input == number3:
                score += 1
            else:
                print("EEE")
                for attempt in range(2):
                    user_input = int(input(f"{number1} + {number2} = "))
                    if user_input == number3:
                        score += 1
                        break
                else:
                    print(f"{number1} + {number2} = {number3}")
        except ValueError:
            print("Invalid input. Please enter a number.")

    return score

def main():
    level = get_level()
    score = generate_integer(level)
    print(f"Score: {score}")

if __name__ == "__main__":
    main()
