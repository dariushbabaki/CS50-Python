def convert(text):
    return text.replace(":)", "🙂").replace(":(", "🙁")

def main():
    text = input().strip() 
    result = convert(text)
    print(result)

if __name__ == "__main__":
    main()
