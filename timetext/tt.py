from itertools import product
from collections import defaultdict
from timetext.db import DB
from timetext.parse import text_to_concepts, text_to_concepts_spacy_batch


class Timetext(object):

    def __init__(self, project_name):
        self.db = DB(project_name)

    def populate(self, relations):
        for relation in relations:
            self.db.insert_relation(relation)

    def parse_and_populate(self, times, texts, tags=None, mode='tokens'):
        if not tags:
            tags = [[]] * len(times)
        relations = set()
        if mode == 'tokens':
            for time, text, tags in zip(times, texts, tags):
                relations.update(time_text_to_coccur_rows(time, text))
        elif mode == 'spacy':
            relations = time_text_to_coccur_batch(times, texts, tags)
        self.db.insert_relations(relations)

    def relations(self, concept, start_time=None, end_time=None):
        return self.db.get_concept_relations(concept)

    def hops(self, concept, hops, start_time=None, end_time=None):
        # todo:
        # 1. time window querying
        # 2. optimise with batch querying executemany (currently one query per concept)
        concepts = {concept}
        hop_dict = dict()
        for hop in range(hops):
            novel = set()
            for concept in concepts:
                times, related = zip(*self.relations(concept))
                novel.update(related)
            hop_dict[hop + 1] = novel - concepts
            concepts.update(novel)
        return hop_dict


def time_text_to_coccur_batch(times, texts, tags=None):
    concept_sets = text_to_concepts_spacy_batch(texts)
    cooccurences = []
    for time, concept_set, tags in zip(times, concept_sets, tags):
        concept_set.update(set(tags))
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
