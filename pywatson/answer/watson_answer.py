from pywatson.answer.answer import Answer
from pywatson.answer.error_notification import ErrorNotification
from pywatson.answer.evidence import Evidence
from pywatson.answer.synonym import Synonym


class WatsonAnswer(object):
    """An answer received from Watson.

    Attributes:
      id (int): An integer that is assigned by the service
        to identify this question and its answers.
      answers (list of Answer, optional): The collection of answers
      category (str, optional): The category of the question that was submitted with the question.
        When no category was submitted with the question,
        an empty category element is returned in the response.
      error_notifications (list of ErrorNotification, optional): The collection of recoverable
        errors, if any.
      evidence_list (list of Evidence, optional): The collection of evidence used to support
        the answer(s).
      focus_list (str, optional): The collection of focus elements
        that are determined by the pipeline for the final answer.,
      lat_list (str, optional): The collection of lexical answer types (LATs)
        that the pipeline determined for the final answer.
        The WatsonQuestion.lat is submitted in the POST when the question was submitted.
        The WatsonQuestion.latlist contains the LATs that were determined by the pipeline when it processed the answer.,
      pipelineid (str, optional): The internal ID that is assigned for the final answer CAS.
        This element contains the internal CAS ID that is assigned after the question is answered.
        You can use this ID to identify the question
        with the internal data structures that Watson uses.
      qclasslist (str, optional): The container for a list of question classes
        that are determined by the pipeline for the final answer.
      status (str, optional) = ['Complete' or 'Timeout' or 'Failed']: The response status of the request.
      supplemental (string, optional): Contains more information about the answers
        for a customization of the IBM Watson processing pipeline.
        In a Watson system that is not customized, this element is not returned.
      synonym_list (list of SynonymList, optional): The collection of synonyms
        for terms in the question.
    """

    def __init__(self, answer_mapping):
        """Create a Watson Answer from the given mapping.

        :param answer_mapping: the Mapping representing a response from Watson
        :type answer_mapping: Mapping
        :return: Answer
        """
        #: ``dict``: A dict of the raw response provided by Watson
        self.raw = dict(answer_mapping)

        q = answer_mapping['question']
        self.id = q['id']
        self.category = q.get('category')
        self.pipelineid = q.get('pipelineid')
        self.status = q.get('status')
        self.supplemental = q.get('supplemental')
        self.answers = \
            list(Answer(a)
                 for a in q['answers']) \
            if 'answers' in q else None
        self.error_notifications = \
            list(ErrorNotification.from_mapping(e)
                 for e in q['errorNotifications']) \
            if 'errorNotifications' in q else None
        self.evidence_list = \
            list(Evidence.from_mapping(e)
                 for e in q['evidencelist']) \
            if 'evidencelist' in q else None
        self.focus_list = \
            list(s['value']
                 for s in q['focuslist']) \
            if 'focuslist' in q else None
        self.lat_list = \
            list(l['value']
                 for l in q['latlist']) \
            if 'latlist' in q else None
        self.qclasslist = \
            list(qc['value']
                 for qc in q['qclasslist']) \
            if 'qclasslist' in q else None
        self.synonym_list = \
            list(Synonym.from_mapping(s)
                 for s in q['synonymList']) \
            if 'synonymList' in q else None
