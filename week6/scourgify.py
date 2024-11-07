import os
import sys
import csv

def main():
    if len(sys.argv) < 3:
        print("Too few command-line arguments")
        sys.exit(1)
    elif len(sys.argv) > 3:
        print("Too many command-line arguments")
        sys.exit(1)

    input_file, output_file = sys.argv[1], sys.argv[2]

    if not os.path.isfile(input_file):
        print(f"Could not read {input_file}")
        sys.exit(1)

    if not input_file.endswith(".csv"):
        print("Not a CSV file")
        sys.exit(1)

    scourgify(input_file, output_file)

def scourgify(input_file, output_file):
    with open(input_file, "r") as csv_read_file:
        column_data = csv.DictReader(csv_read_file)
        with open(output_file, "w", newline='') as csv_write_file:
            fieldnames = ["first", "last", "house"]
            column_writer = csv.DictWriter(csv_write_file, fieldnames=fieldnames)
            column_writer.writeheader()

            for row in column_data:
                last, first = row["name"].split(",")
                house = row["house"]

                column_writer.writerow({
                    "first": first.strip(),"last": last.strip(),"house": house.strip()})

if __name__ == "__main__":
    main()
