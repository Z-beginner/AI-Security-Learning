'''
attack_keywords = [
    "hack",
    "attack",
    "ignore"
]
'''
attack_rules = {
    "hack": "high",
    "attack": "medium",
    "ignore": "medium"
}
detected_keywords = []
prompt = input('请输入文本：')
for keyword in attack_rules:
    if keyword in prompt:
        detected_keywords.append(keyword)
if detected_keywords:
    print('attack detected:')
    for detected_keyword in detected_keywords:
        print('keyword:', detected_keyword, "\nrisk:",attack_rules[detected_keyword])
else:
    print('safe')