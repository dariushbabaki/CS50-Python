import sys
import csv
from tabulate import tabulate

def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python pizza.py <filename.csv>")
    
    filename = sys.argv[1]
    if not filename.endswith('.csv'):
        sys.exit("Error: File must end with .csv")
    
    try:
        with open(filename, newline='') as csvfile:
            reader = csv.reader(csvfile)
            data = list(reader)
            print(tabulate(data[1:], headers=data[0], tablefmt="grid"))

    except FileNotFoundError:
        sys.exit(f"Error: File '{filename}' not found")

if __name__ == "__main__":
    main()
