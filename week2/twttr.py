def remove_vowels(text):

  vowels = "AEIOUaeiou"
  no_vowels = ""
  for char in text:
    if char not in vowels:
      no_vowels += char
  return no_vowels

if __name__ == "__main__":
  text = input("Enter your text:")
  result = remove_vowels(text)
  print("text without vowels:", result)
