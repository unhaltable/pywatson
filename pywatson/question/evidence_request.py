class EvidenceRequest(object):
    """Include this with a Question to request evidence from Watson"""

    def __init__(self, items=3, profile=False):
        self.items = items
        self.profile = profile

    def __eq__(self, other):
        """Return True iff self is equivalent to other

        :param other: an EvidenceRequest
        :return: True or False
        """
        if self is other:
            return True

        if not isinstance(other, EvidenceRequest):
            return False
        if self.items != other.items:
            return False
        if self.profile != other.profile:
            return False

        return True
