import re

def main():
    print(convert(input("Hours: ")))

def convert(s):
    pattern = r"^(\d{1,2})(?::(\d{2}))? (AM|PM) to (\d{1,2})(?::(\d{2}))? (AM|PM)$"
    
    match = re.match(pattern, s)
    if not match:
        raise ValueError("Invalid input format")
    
    h1, m1, period1, h2, m2, period2 = match.groups()
    
    h1, m1 = int(h1), int(m1 or 0)
    h2, m2 = int(h2), int(m2 or 0)
    
    if not (1 <= h1 <= 12) or not (0 <= m1 < 60) or not (1 <= h2 <= 12) or not (0 <= m2 < 60):
        raise ValueError("Invalid time values")
    
    t1 = to_24_hour(h1, m1, period1)
    t2 = to_24_hour(h2, m2, period2)
    
    return f"{t1} to {t2}"

def to_24_hour(hour, minute, period):
    if period == "PM" and hour != 12:
        hour += 12
    elif period == "AM" and hour == 12:
        hour = 0
    return f"{hour:02}:{minute:02}"

if __name__ == "__main__":
    main()
