from pathlib import Path
import json

def load_json(path):
    if path.exists():
        user_info = json.loads(path.read_text())
    else:
        user_info = {}
    if 'username' in user_info and 'sex' in user_info and 'fav_number' in user_info:
        greet_user(user_info)
    else:
        username = input('Please enter your name:')
        sex = input('Please enter your sex:')
        fav_number = input('Please enter your favorite number:')
        user_info = {
            'username': username,
            'sex': sex,
            'fav_number': fav_number
        }
        contents = json.dumps(user_info)
        path.write_text(contents)
        print(f'welcome,{username},I will remember your favorite number')
def greet_user(user_information):
    print(f"welcome back,{user_information['username']},I had remembered your favorite number")
load_json(Path('user_info.json'))