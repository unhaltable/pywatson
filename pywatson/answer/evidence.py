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
        return cls(metadata_map=MetadataMap.from_mapping(evidence_mapping['metadataMap']),
                   copyright=evidence_mapping['copyright'],
                   id=evidence_mapping['id'],
                   terms_of_use=evidence_mapping['termsOfUse'],
                   document=evidence_mapping['document'],
                   title=evidence_mapping['title'],
                   text=evidence_mapping['text'],
                   value=evidence_mapping['value'])


class MetadataMap(object):
    """Additional metadata about an Evidence passage

    """

    def __init__(self, originalfile, deepqaid, title, corpus_name, docno, file_name):
        """Initialize this MetadataMap with the given attributes.

        :param originalfile:
        :param deepqaid:
        :param title:
        :param corpus_name:
        :param docno:
        :param file_name:
        :return:
        """
        self.originalfile = originalfile
        self.deepqaid = deepqaid
        self.title = title
        self.corpus_name = corpus_name
        self.docno = docno
        self.file_name = file_name

    @classmethod
    def from_mapping(cls, metadata_mapping):
        return cls(originalfile=metadata_mapping['originalfile'],
                   deepqaid=metadata_mapping['deepqaid'],
                   title=metadata_mapping['title'],
                   corpus_name=metadata_mapping['corpusName'],
                   docno=metadata_mapping['DOCNO'],
                   file_name=metadata_mapping['fileName'])
