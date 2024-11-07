amount_due = 50
total_paid = 0

while total_paid < amount_due:
    print(f"Amount Due: {amount_due - total_paid}")
    
    while True:
        try:
            a = int(input("Next coin (5, 10, or 25): ").strip())
            if a in [5, 10, 25]:
                total_paid += a
                break
            else:
                print(f"Amount Due: {amount_due}")
                print(f"{a} is invalid, please try again.")
        except ValueError:
            print(f"Amount Due: {amount_due}")
            print("Invalid input, please enter a valid coin value (5, 10, or 25).")

if total_paid == amount_due:
    print(f"Change Owed: 0")
else:
    print(f"Change Owed: {total_paid - amount_due}")
