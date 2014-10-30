class Evidence(object):
    """

    """

    def __init__(self, metadata_map, copyright, id, terms_of_use, document, title, text, value):
        self.metadata_map = metadata_map
        self.copyright = copyright
        self.id = id
        self.terms_of_use = terms_of_use
        self.document = document
        self.title = title
        self.text = text
        self.value = value

    @classmethod
    def from_mapping(cls, evidence_mapping):
        """Create an Evidence instance from the given mapping

        :param evidence_mapping: a mapping (e.g. dict) of values provided by Watson
        :return: a new Evidence
        """
        return cls(metadata_map=MetadataMap(evidence_mapping['metadataMap']),
                   copyright=evidence_mapping['copyright'],
                   id=evidence_mapping['id'],
                   terms_of_use=evidence_mapping['termsOfUse'],
                   document=evidence_mapping['document'],
                   title=evidence_mapping['title'],
                   text=evidence_mapping['text'],
                   value=evidence_mapping['value'])


class MetadataMap(object):
    def __init__(self, originalfile, deepqaid, title, corpus_name, docno, file_name):
        pass