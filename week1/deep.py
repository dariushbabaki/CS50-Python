def check_input(user_input):

  user_input = user_input.lower()

  user_input = user_input.strip()

  if user_input == "42" or user_input == "forty-two" or user_input == "forty two":
    return 'Yes'
  else:
    return 'No'

user_input = input("Please enter a number: ")

result = check_input(user_input)
print(result)
