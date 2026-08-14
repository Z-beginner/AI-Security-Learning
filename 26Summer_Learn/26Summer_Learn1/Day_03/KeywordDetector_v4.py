class KeywordDetector:
    def __init__(self, keywords, risk_score):
        self.keywords = keywords
        self.risk_score = risk_score
        self.scan_count = 0
    def analyze(self, prompt):
        self.scan_count = self.scan_count + 1
        matched_keywords = []
        for word in self.keywords:
            if word in prompt:
                matched_keywords.append(word)
        score = 0
        for word in matched_keywords:
            score = score + self.risk_score[word]
        if score >= 5:
            level = "high"
        elif score >= 1:
            level = "medium"
        else:
            level = "low"
        result = {
            "matched_keywords": matched_keywords,
            "risk_score": score,
            "risk_level": level
        }
        return result
keywords = [
    "jailbreak",
    "system prompt",
    "password"
]
risk_score = {
    "jailbreak": 5,
    "system prompt": 3,
    "password": 2
}
detector = KeywordDetector(keywords,risk_score)
prompt = input()
result = detector.analyze(prompt)
print(result)