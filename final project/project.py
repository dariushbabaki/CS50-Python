import random

def main():
    print("\n" ,"The game of mud or nonsense","\n")
    choice = input("Guess which hand the ball is in (left or right): ").strip()
    print()
    try:
        choice = guess_hand(choice)
        result, hidden_hand = check_guess(choice)
        if result:
            print(f"Congratulations! You guessed right. The ball was in {hidden_hand}")
        else:
            print(f"Wrong! The ball was in {hidden_hand}")
    except ValueError as e:
        print(e)
        
def hide_ball():
    return random.choice(["left", "right"])

def guess_hand(choice):
    if choice.lower() not in ["left", "right"]:
        raise ValueError("Guess should be 'left' or 'right' ")
    return choice.lower()

def check_guess(choice):
    hidden_hand = hide_ball()
    return choice == hidden_hand, hidden_hand

if __name__ == "__main__":
    main()
