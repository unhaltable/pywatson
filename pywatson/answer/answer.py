class Answer(object):
    def __init__(self, answer_mapping):
        self.pipeline = answer_mapping['pipeline']
        self.confidence = answer_mapping['confidence']
        self.id = answer_mapping['id']
        self.text = answer_mapping['text']
