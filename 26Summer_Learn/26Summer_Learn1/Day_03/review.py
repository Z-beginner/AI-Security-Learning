class KeywordMatcher:
    def __init__(self, keywords):
        self.keywords = keywords
    def match(self, prompt):
        matched_keywords = []
        for keyword in self.keywords:
            if keyword in prompt:
                matched_keywords.append(keyword)
        return matched_keywords
matcher = KeywordMatcher(
    [
        "jailbreak",
        "password"
    ]
)
prompt = input()
class RiskEngine:
    def __init__(self, risk_rules):
        self.risk_rules = risk_rules
    def calculate_risk(self, matched_keywords):
        risk = 0
        for matched_keyword in matched_keywords:
            risk = risk + self.risk_rules[matched_keyword]
        if risk >= 5:
            risk_level = "high"
        else:
            risk_level = "low"
        return {"risk": risk, "level": risk_level}
risk_rules1 = {
    "jailbreak":5,
    "password":2
}
risk_rules = RiskEngine(risk_rules1)
matched_key = matcher.match(prompt)
risk_calculate = risk_rules.calculate_risk(matched_key)
risk = risk_calculate["risk"]
level = risk_calculate["level"]
print(risk)
print(level)
#报错后检查发现问题如下：
#由于risk_rules1是dic，忘记把它放入RiskEngine中，导致程序无法正常运行
#与初始化记混，matched_keywords带上了self