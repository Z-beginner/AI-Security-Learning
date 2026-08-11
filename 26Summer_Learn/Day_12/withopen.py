import json

with open('user_info.json', 'r') as file:
    user_info = json.load(file)
    print(user_info)