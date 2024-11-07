vowels = ["a" , "e" , "i" , "o" , "u"]

def main():
    text = str(input("enter your text: ").strip())
    print(f"Silent_Letters: {shorten (text)}")
    
def shorten (word):
    silent_letters = ""
    for x in word:
        if x.lower() not in vowels:
            silent_letters += x
            
    return silent_letters
    
if __name__ == "__main__":
    main()
