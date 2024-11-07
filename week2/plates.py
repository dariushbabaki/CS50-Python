def is_valid_plate(plate):
  
    if not 2 <= len(plate) <= 6:
        return False
    
    if not plate[:2].isalpha():
        return False

    for i, char in enumerate(plate):
        if char.isdigit():
            if i < 2 or char == '0':  
                return False
            for j in range(i+1, len(plate)):
                if not plate[j].isdigit():
                    return False
            break

    return True

if __name__ == "__main__":
    plate = input("Please enter the license plate number:")
    if is_valid_plate(plate):
        print("Valid")
    else:
        print("Invalid")
