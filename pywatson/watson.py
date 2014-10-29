from pywatson.answer.watson_answer import WatsonAnswer
from pywatson.question.watson_question import WatsonQuestion
import json
import requests


class Watson(object):
    """The Watson API adapter class"""

    def __init__(self, url, username, password):
        self.url = url
        self.username = username
        self.password = password

    def ask_question(self, question_text, question=None):
        """Ask Watson a question via the Question and Answer API

        :param question_text: question to ask Watson
        :type question_text: str
        :param question: if question_text is not provided, a Question object
                         representing the question to ask Watson
        :type question: WatsonQuestion
        :return: Answer
        """
        if question is not None:
            q = question.to_dict()
        else:
            q = WatsonQuestion(question_text).to_dict()
        r = requests.post(self.url + '/question', json={'question': q}, headers={
            'Accept': 'application/json',
            'X-SyncTimeout': 30
        }, auth=(self.username, self.password))
        try:
            response_json = r.json()
        except ValueError:
            raise Exception('Failed to parse response JSON')
        return WatsonAnswer(response_json)
