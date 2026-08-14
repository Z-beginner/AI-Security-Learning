class KeywordDetector:
    def __init__(self, keywords):
        self.keywords = keywords
    def detect(self,prompt):
        for word in self.keywords:
            if word in prompt:
                print('发现关键词',word)
detector = KeywordDetector(
    [
        "jailbreak",
        "system prompt",
        "password"
    ]
)
prompt = input()
detector.detect(prompt)