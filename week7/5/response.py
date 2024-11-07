from validators import email

def validate_email():
    user_email = input("Please enter your email address: ")
    if email(user_email):
        print("Valid")
    else:
        print("Invalid")

if __name__ == "__main__":
    validate_email()
