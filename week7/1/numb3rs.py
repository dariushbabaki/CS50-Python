import re
import sys

def main():
    print(validate(input("IPv4 Address: ").strip()))


def validate(ip):
    try:
       list_numbers = ip.split(".", maxsplit=3)
       for number in list_numbers:
            if int(number) > 255 or len(list_number) < 4:
                return False

    except ValueError:
        return False
    else:
        return True


if __name__ == "__main__":
    main()
