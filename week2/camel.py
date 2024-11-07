def camel_to_snake(camel_case_string):

  snake_case_string = ""
  for char in camel_case_string:
    if char.isupper():
      
      snake_case_string += "_" + char.lower()
    else:
      snake_case_string += char
      
  return snake_case_string[1:] if snake_case_string[0] == "_" else snake_case_string

if __name__ == "__main__":
  camel_case_input = input("Please enter a variable name in camelCase format: ")
  snake_case_output = camel_to_snake(camel_case_input)
  print("Variable name in snake_case format: ", snake_case_output)
