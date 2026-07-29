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
reslut = check_prompt(prompt)
if not reslut:
    reslut = [
        {
            "status": "safe"
        }
    ]
for res in reslut:
    print(res)