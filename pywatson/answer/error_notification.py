class ErrorNotification(object):
    def __init__(self, error, text):
        self.error = error
        self.text = text

    @classmethod
    def from_mapping(cls, error_mapping):
        return cls(error=error_mapping['error'],
                   text=error_mapping['text'])
