from pywatson.answer.answer import Answer
from pywatson.watson import Watson


class TestWatson:
    def test___init__(self, config):
        watson = Watson(url=config['url'], username=config['username'], password=config['password'])
        assert watson.url == config['url']
        assert watson.username == config['username']
        assert watson.password == config['password']

    def test_ask_question_basic(self, watson):
        answer = watson.ask_question('What is the Labour Code?')
        assert type(answer) is Answer
