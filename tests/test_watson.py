from pywatson.answer.answer import Answer
from pywatson.watson import Watson


class TestWatson:
    def test_ask_question_basic(self, watson):
        answer = watson.ask_question('What is the Labour Code?')
        assert type(answer) is Answer
