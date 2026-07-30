class KeywordDetector:
    def __init__(self, keywords):
        self.keywords = keywords
    def detect(self,prompt):
        matched = []
        for word in self.keywords:
            if word in prompt:
                matched.append(word)
        return matched
    def risk_level(self,prompt):
        score = 0
        risk_score = {"jailbreak": 5, "system prompt": 3, "password": 2}
        for word in self.keywords:
            if word in prompt:
                score = score + risk_score[word]
        return score
detector = KeywordDetector(
    [
        "jailbreak",
        "system prompt",
        "password"
    ]
)
prompt = input()
result = detector.detect(prompt)
score = detector.risk_level(prompt)
print("matched_keywords:",result)
print("risk_score",score)
if score >=5:
    print("risk_level:high")
elif score >=3:
    print("risk_level:medium")
else:
    print("risk_level:low")