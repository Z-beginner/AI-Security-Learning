import json
def load_prompt(prompt):
    with open("config/keywords.json", "r") as file:
       data = json.load(file)
    return data
detected_prompt = []
score = 0
prompt = input('Enter a prompt: ')
for d_p in load_prompt('prompt_injection'):
    if d_p in prompt:
        detected_prompt.append(d_p)
        score = score + 1
if score == 0:
    level = "low"
elif score == 1:
    level = "medium"
else :
    level = "high"
print("prompt:",prompt)
print("matched_keywords:",detected_prompt)
print( "risk_score:",score)
print("risk_level:",level)