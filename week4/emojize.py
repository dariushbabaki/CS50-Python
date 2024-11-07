import emoji

def emojize_text(text):
  return emoji.emojize(text, language='alias')

if __name__ == "__main__":
  text = input("Enter your text: ")
  emojized_text = emojize_text(text)
  print(emojized_text)
