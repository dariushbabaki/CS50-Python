def main():
    plate = input("Plate: ").strip()
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    s = str(s)
    if 2 <= len(s) <= 6 and s[0].isalpha() and s[1].isalpha():
        num_count = 0
        for ch in s:
            if ch.isalpha():
                continue
            elif ch.isdigit() and num_count == 0:
                num_count += 1
            elif ch.isdigit() and num_count > 0:
                return False
            else:
                return False
        return True
    return False

if __name__ == "__main__":
    main()
