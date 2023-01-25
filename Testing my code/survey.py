class AnonymousSurvey:
    """collects anonymous answers to survey questions"""

    def __init__(self, question):
        """stores a question and prepares to store responses"""
        self.question = question
        self.responses = []

    def show_question(self):
        """show the survey question"""
        print(self.question)

    def store_response(self, new_response):
        """stores a single response to a question"""
        self.responses.append(new_response)

    def show_response(self):
        """Show all responses that have been given"""
        print("Survey results:")
        for response in self.responses:
            print(f"- {response}")

