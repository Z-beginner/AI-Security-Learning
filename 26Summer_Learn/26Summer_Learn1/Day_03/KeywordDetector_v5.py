class KeywordMatcher:
    def __init__(self, keywords):
        self.keywords = keywords
    def match(self, prompt):
        matched = []
        for keyword in self.keywords:
            if keyword in prompt:
                matched.append(keyword)
        return matched
class RiskEngine:
    def __init__(self, risk_score_stander):
        self.risk_score_stander = risk_score_stander
    def calculate(self, matched):
        score = 0
        for word in matched:
            score = score + self.risk_score_stander[word]
        if score >= 5:
            level = "high"
        elif score >= 1:
            level = "medium"
        else:
            level = "low"
        return {
            "risk_score": score,
            "risk_level": level
        }
prompt = input()
matcher = KeywordMatcher(
    [
        "jailbreak",
        "system prompt",
        "password"
    ]
)
risk_score_stander = {
    "jailbreak": 5,
    "system prompt": 3,
    "password":2
}
matched = matcher.match(prompt)
engine = RiskEngine(risk_score_stander)
result = engine.calculate(matched)
print(matched)
print(result)