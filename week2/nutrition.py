def get_calories(fruit_name):
    fruit_calories = {
        'apple': 130, 'avocado': 50, 'banana': 110, 'cantaloupe': 50,
        'grapefruit': 60, 'grapes': 90, 'honeydew': 50, 'kiwifruit': 90,
        'nectarine': 60, 'lime': 20, 'lemon': 15, 'pear': 100, 'peach': 60,
        'orange': 80, 'strawberries': 50, 'plums': 70, 'pineapple': 50,
        'watermelon': 80, 'tangerine': 50, 'sweet cherries': 100
    }
    
    fruit_name = fruit_name.lower()
    
    if fruit_name in fruit_calories:
        return fruit_calories[fruit_name]
    else:
        return None

fruit = input("Enter the name of a fruit: ")

calories = get_calories(fruit)
if calories is not None:
    print(f"A serving of {fruit} contains {calories} calories.")
else:
    print("Fruit not found in the database.")
