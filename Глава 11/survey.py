class AnonymousSurvey:
    """Сбор анонимных ответов."""

    def __init__(self, question):
        self.question = question
        self.response = []

    def show_question(self):
        """Выводит вопрос."""
        print(self.question)

    def store_response(self, new_response):
        """Сохраняет один ответ на опрос."""
        self.response.append(new_response)

    def show_result(self):
        """Выводит все полученные ответы."""
        print("Survey result: ")
        for response in self.response:
            print(f"- {response}")
