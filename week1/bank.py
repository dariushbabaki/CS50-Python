user_input = input("Please enter a greeting: ")

user_input_cleaned = user_input.strip().lower()

if user_input_cleaned.startswith("hello"):
    print("$0")
elif user_input_cleaned.startswith("h"):
    print("$20")
else:
    print("$100")
