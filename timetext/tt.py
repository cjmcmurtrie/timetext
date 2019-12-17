from itertools import product
from timetext.db import DB
from timetext.parse import text_to_concepts, text_to_concepts_spacy_batch


class Timetext(object):

    def __init__(self, project_name):
        self.db = DB(project_name)

    def populate(self, relations):
        for relation in relations:
            self.db.insert_relation(relation)

    def parse_and_populate(self, timed_texts, mode='tokens'):
        if mode == 'tokens':
            relations = set()
            for time, text in timed_texts:
                relations.update(time_text_to_coccur_rows(time, text))
        elif mode == 'spacy':
            relations = time_text_to_coccur_batch(timed_texts)
        self.db.insert_relations(relations)

    def analyse(self, concept):
        pass


def time_text_to_coccur_batch(timed_texts):
    times, texts = zip(*timed_texts)
    concept_sets = text_to_concepts_spacy_batch(texts)
    cooccurences = []
    for time, concept_set in zip(times, concept_sets):
        for concept_1, concept_2 in product(concept_set, concept_set):
            if concept_1 != concept_2:
                cooccurences.append(
                    (time, concept_1, concept_2, 'coocurrence', 1)
                )
    return cooccurences


def time_text_to_coccur_rows(time, text, tags=None):
    '''
    :param time: timestamp string
    :param text: text document string
    :param tags: iterable of document tags (e.g. country of article)
    :return: list of tuples: (time, c1, c2, coocurrence, 1)
    '''
    concepts = set(text_to_concepts(text))
    if tags:
        concepts.update(tags)
    cooccurences = []
    for concept_1, concept_2 in product(concepts, concepts):
        if concept_1 != concept_2:
            cooccurences.append(
                (time, concept_1, concept_2, 'coocurrence', 1)
            )
    return cooccurences
