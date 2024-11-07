import re
import sys

def main():
    print(parse(input("HTML: ")))

def parse(s):
    address = re.search(r"https?://(www\.)?youtube\.com/embed/(.+?)(?=\")", s)
    if address:
        user_name = address.group(2)
        return f"https://youtu.be/{user_name}"
        
if __name__ == "__main__":
    main()
