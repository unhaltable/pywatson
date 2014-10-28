from pywatson.question.question import Question


class TestQuestion:
    def test___init___basic(self, questions):
        question = Question(questions[0]['questionText'])
        assert question.question_text == questions[0]['questionText']

    def test_ask_question_basic(self, watson):
        answer = watson.ask_question('What is the Labour Code?')
        assert type(answer) is Answer
