from datetime import date, timedelta
import sys
import inflect

def main():
    birthday_str = input("Enter your birth date (YYYY-MM-DD): ")
    birthday = parse_date(birthday_str)
    minutes = calculate_minutes(birthday)
    print_minutes_in_words(minutes)

def parse_date(birthday_str):
    try:
        year, month, day = map(int, birthday_str.split("-"))
        return date(year, month, day)
    except ValueError:
        sys.exit("Invalid date format")

def calculate_minutes(birthday):
    today = date.today()
    difference = today - birthday
    minutes = difference.total_seconds() / 60
    return round(minutes)

def print_minutes_in_words(minutes):
    p = inflect.engine()
    minutes_in_words = p.number_to_words(minutes, andword="")
    print(minutes_in_words.capitalize(), "minutes")

if __name__ == "__main__":
    main()
