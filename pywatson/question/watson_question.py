from pywatson.question.evidence_request import EvidenceRequest
from pywatson.util.dictable import Dictable


class WatsonQuestion(Dictable):
    """A question to ask Watson"""

    def __init__(self,
                 question_text,
                 answer_assertion=None,
                 category=None,
                 context=None,
                 evidence_request=None,
                 filters=(),
                 formatted_answer=None,
                 items=None,
                 lat=None,
                 passthru=None,
                 synonym_list=()):
        """Create this Question with the given parameters.

        See `IBM Watson Developer Cloud`_ for more details

        .. _`IBM Watson Developer Cloud`: http://www.ibm.com/smarterplanet/us/en/ibmwatson/developercloud/apis/#!/Question_Answer/question

        :param question_text: the text of the question to be answered
        :type question_text: str
        :param answer_assertion:
        :type answer_assertion: str
        :param category:
        :type category: str
        :param context:
        :type context: str
        :param evidence_request:
        :type evidence_request: EvidenceRequest
        :param filters:
        :type filters: Iterable of Filter
        :param formatted_answer:
        :type formatted_answer: bool
        :param items:
        :type items: int
        :param lat:
        :type lat: str
        :param passthru:
        :type passthru: str
        :param synonym_list:
        :type synonym_list: Iterable of str
        :return: Question
        """
        self.question_text = question_text
        self.answer_assertion = answer_assertion
        self.category = category
        self.context = context
        self.evidence_request = evidence_request
        self.filters = filters
        self.formatted_answer = formatted_answer
        self.items = items
        self.lat = lat
        self.passthru = passthru
        self.synonym_list = synonym_list

    def __eq__(self, other):
        return False
