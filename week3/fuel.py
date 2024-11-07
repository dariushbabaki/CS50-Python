def calculate_fuel_percentage():
    while True:
        try:
            fraction = input("Enter the fraction representing the amount of fuel (in the form of x/y): ")
            numerator, denominator = map(int, fraction.split('/'))
            if denominator == 0 or numerator > denominator:
                print("The entered fraction is invalid. Please enter again.")
                continue
            percentage = round(numerator / denominator * 100)
            
            if percentage <= 1: 
                print("E")
                return
            elif percentage >= 99:
                print("F")
                return
            else:
                print(f"{percentage}%")
                return
        except ValueError:
            print("Please enter a correct fraction.")

if __name__ == "__main__":
    calculate_fuel_percentage()
