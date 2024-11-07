months = {
    "January": 1, "February": 2, "March": 3, "April": 4,
    "May": 5, "June": 6, "July": 7, "August": 8,
    "September": 9, "October": 10, "November": 11, "December": 12
}

while True:
    user_input = input("Please enter the date in the format MM/DD/YYYY.")
    
    if "/" in user_input:
        user_input1 = user_input.strip()
        new_input = user_input1.split("/")
        x = new_input[0]
        y = new_input[1]
        
        if x in months.keys():
            continue
        if int(y) > 31:
            continue
        if int(x) < 13:
            print(f"{new_input[2]}-{int(x):02}-{int(y):02}")
            break

    elif "," in user_input:
        new_input = user_input.replace("," , " ").split('  ')
        y = new_input[1]
        if y in months.keys():
            continue
        if int(y) >31:
            continue
        if new_input[0] in months.keys():
            print(f"{new_input[2]}-{months[new_input[0]]:02}-{int(new_input[1]):02}")
            break
