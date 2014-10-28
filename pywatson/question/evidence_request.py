class EvidenceRequest(object):
    """Include this with a Question to request evidence from Watson"""

    def __init__(self, items=3, profile=False):
        self.items = items
        self.profile = profile

    def __eq__(self, other):
        return False
