class AnonymousSurvey:
    def __init__(self, question):
        self.question = question
        self.responses = set()
    def show_question(self):
        print(self.question)
    def store_response(self, new_response):
        self.responses.add(new_response)
    def show_results(self):
        print("Survey results:")
        for response in self.responses:
            print(f"-{response}")

#只是通过简单的集合来升级以下
#没有其他的什么意义