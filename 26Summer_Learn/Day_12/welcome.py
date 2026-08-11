from pathlib import Path
import json

path = Path('welcome.json')
if path.exists():
    contents = path.read_text()
    username = json.loads(contents)
    print(f'welcome back,{username}')
else:
    username = input('please enter your name:')
    contents = json.dumps(username)
    path.write_text(contents)
    print(f'welcome,{username},I will remember you next time')