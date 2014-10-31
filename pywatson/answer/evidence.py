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

    def __init__(self,
                 originalfile,
                 deepqaid,
                 title,
                 corpus_name,
                 docno,
                 corpus_plus_docno,
                 file_name,
                 metadata_mapping=None):
        """Initialize this MetadataMap with the given attributes.

        :param originalfile:
        :param deepqaid:
        :param title:
        :param corpus_name:
        :param docno:
        :param corpus_plus_docno:
        :param file_name:
        :param metadata_mapping:
        :return:
        """
        self.originalfile = originalfile
        self.deepqaid = deepqaid
        self.title = title
        self.corpus_name = corpus_name
        self.docno = docno
        self.corpus_plus_docno = corpus_plus_docno
        self.file_name = file_name

        self.raw = metadata_mapping

    @classmethod
    def from_mapping(cls, metadata_mapping):
        return cls(originalfile=metadata_mapping.get('originalfile', None),
                   deepqaid=metadata_mapping.get('deepqaid', None),
                   title=metadata_mapping.get('title', None),
                   corpus_name=metadata_mapping.get('corpusName', None),
                   docno=metadata_mapping.get('DOCNO', None),
                   corpus_plus_docno=metadata_mapping.get('CorpusPlusDocno', None),
                   file_name=metadata_mapping.get('fileName', None),
                   metadata_mapping=metadata_mapping)
