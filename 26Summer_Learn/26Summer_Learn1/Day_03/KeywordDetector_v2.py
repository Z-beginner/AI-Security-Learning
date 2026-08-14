class KeywordDetector:
    def __init__(self, keywords):
        self.keywords = keywords
    def detect(self,prompt):
        r = []
        for word in self.keywords:
            if word in prompt:
                r.append(word)
        return r
detector = KeywordDetector(
    [
        "jailbreak",
        "system prompt",
        "password"
    ]
)
prompt = input()
result = detector.detect(prompt)
print(result)