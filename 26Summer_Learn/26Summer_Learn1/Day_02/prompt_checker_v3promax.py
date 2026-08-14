def check_prompt(prompt):
    attack_rules = {
        "hack": "high",
        "attack": "medium",
        "ignore": "medium"
    }
    report = []
    for keyword in attack_rules:
        if keyword in prompt:
            report.append(
                {
                    "keyword": keyword,
                    "risk": attack_rules[keyword]
                }
             )
    return report
prompt = input('请输入文本：')
result = check_prompt(prompt)
if not result:
    result = [
        {
            "risk": "safe"
        }
    ]
for res in result:
    print(res)
risk_level = {
        "safe": 0,
        "medium": 1,
        "high": 2
    }
max_risk = 'safe'
for resl in result:
    risk = resl['risk']
    if risk_level[risk] > risk_level[max_risk]:
        max_risk = risk
print('Max risk:',max_risk)