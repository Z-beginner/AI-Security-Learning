Prompt = input()
length = len(Prompt)
if length == 0 or 'hack'in Prompt or 'attack'in Prompt or 'ignore'in Prompt or length >100:
    print('danger')
else:
    print("safe")