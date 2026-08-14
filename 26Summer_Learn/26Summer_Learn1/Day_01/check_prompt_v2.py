prompt = input()
def check_prompt(prompt):
    length = len(prompt)
    if length == 0:
        return 'empty input'
    if 'hack'in prompt:
        return 'attack keyword: hack'
    if 'attack'in prompt:
        return 'attack keyword: attack'
    if 'ignore'in prompt:
        return 'attack keyword: ignore'
    else:
        return 'safe'
result = check_prompt(prompt)
print(result)