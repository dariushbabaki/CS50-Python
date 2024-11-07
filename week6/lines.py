import sys
import os

def main():
    if len(sys.argv) < 2:
        print("Too few command-line arguments")
        sys.exit(1)
    elif len(sys.argv) > 2:
        print("Too many command-line arguments")
        sys.exit(1)
    elif not os.path.isfile(sys.argv[1]):
        print("File does not exist")
        sys.exit(1)
    elif not sys.argv[1].endswith(".py"):
        print("Not a Python file")
        sys.exit(1)
    else:
        print(counter(sys.argv[1]))

def counter(python_file):
    rline = 0
    with open(python_file, "r") as lines:
        tlines = list(enumerate(lines.readlines(), start=1))

        for nline, line in tlines:
            if line.strip().startswith("#") or line.strip() == "" or line.isspace():
                rline += 1
        return len(tlines) - rline

if __name__ == "__main__":
    main()
