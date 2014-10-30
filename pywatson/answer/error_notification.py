class ErrorNotification(object):
    def __init__(self, error_mapping):
        self.raw = error_mapping
        self.error = error_mapping['error']
        self.text = error_mapping['text']
