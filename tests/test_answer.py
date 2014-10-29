from pywatson.answer.watson_answer import WatsonAnswer


class TestAnswer(object):
    """Unit tests for the WatsonQuestion class"""

    def test___init___complete(self, answers):
        """WatsonAnswer is constructed properly with all parameters provided"""
        answer = WatsonAnswer(answers[0])

        assert answer.raw == answers[0]
