from pywatson.util.map_initializable import MapInitializable


class SynSetSynonym(MapInitializable):
    def __init__(self, is_chosen, value, weight):
        self.is_chosen = is_chosen
        self.value = value
        self.weight = weight

    @classmethod
    def from_mapping(cls, syn_mapping):
        return cls(is_chosen=syn_mapping['isChosen'],
                   value=syn_mapping['value'],
                   weight=syn_mapping['weight'])


class SynSet(MapInitializable):
    def __init__(self, name, synonyms=()):
        self.name = name
        self.synonyms = tuple(synonyms)

    @classmethod
    def from_mapping(cls, synset_mapping):
        return cls(name=synset_mapping[0]['name'],
                   synonyms=(SynSetSynonym.from_mapping(s) for s in synset_mapping[0]['synonym']))


class Synonym(MapInitializable):
    def __init__(self, part_of_speech, lemma, value, syn_set):
        self.part_of_speech = part_of_speech
        self.lemma = lemma
        self.value = value
        self.syn_set = syn_set

    @classmethod
    def from_mapping(cls, synonym_mapping):
        return cls(part_of_speech=synonym_mapping['partOfSpeech'],
                   lemma=synonym_mapping['lemma'],
                   value=synonym_mapping['value'],
                   syn_set=SynSet.from_mapping(synonym_mapping['synSet']))
