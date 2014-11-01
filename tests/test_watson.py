from pywatson.answer.watson_answer import WatsonAnswer
from pywatson.watson import Watson


class TestWatson:
    def test___init__(self, config):
        watson = Watson(url=config['url'], username=config['username'], password=config['password'])
        assert watson.url == config['url']
        assert watson.username == config['username']
        assert watson.password == config['password']

    def test_ask_question_basic(self, watson):
        answer = watson.ask_question('What is the Labour Code?')
        assert type(answer) is WatsonAnswer
        assert answer.raw
        assert len(answer.answers) > 0
        assert answer.synonym_list is not None
