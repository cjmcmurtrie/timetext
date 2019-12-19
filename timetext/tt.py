from itertools import product
from collections.abc import Iterable
from timetext.db import DB
from timetext.parse import text_to_concepts_batch


class Timetext(object):

    def __init__(self, project_name):
        self.db = DB(project_name)

    def populate(self, times, texts, tags=None, mode='tokens'):
        if not tags:
            tags = [[]] * len(times)
        # relations = set()
        relations = time_text_to_coccur_batch(times, texts, tags, mode=mode)
        # if mode == 'tokens':
        #     for time, text, tags in zip(times, texts, tags):
        #         relations.update(time_text_to_coccur_rows(time, text))
        # elif mode == 'spacy':
        #     relations = time_text_to_coccur_batch(times, texts, tags)
        # elif mode == 'stopwords':
        #     pass
        self.db.insert_relations(relations)

    def relations(self, concepts, start_time=None, end_time=None):
        if isinstance(concepts, str):
            return self.db.get_concept_relations(concepts)
        elif isinstance(concepts, Iterable):
            return self.db.get_concept_relations_batch(concepts)

    def hops(self, concept, hops, start_time=None, end_time=None):
        # todo:
        # 1. time window querying
        concepts = {concept}
        hop_dict = dict()
        for hop in range(hops):
            times, related = zip(*self.relations(list(concepts)))
            novel = set(related)
            hop_dict[hop + 1] = novel - concepts
            concepts.update(novel)
        return hop_dict

    def paths(self, concept, hops, start_time=None, end_time=None):
        # todo: calculate hops as nested dicts to include paths.
        pass


def time_text_to_coccur_batch(times, texts, tags=None, mode='spacy'):
    concept_sets = text_to_concepts_batch(texts, mode)
    cooccurences = []
    for time, concept_set, tags in zip(times, concept_sets, tags):
        concept_set.update(set(tags))
        for concept_1, concept_2 in product(concept_set, concept_set):
            if concept_1 != concept_2:
                cooccurences.append(
                    (time, concept_1, concept_2, 'coocurrence', 1)
                )
    return cooccurences


# def time_text_to_coccur_rows(time, text, tags=None):
#     '''
#     :param time: timestamp string
#     :param text: text document string
#     :param tags: iterable of document tags (e.g. country of article)
#     :return: list of tuples: (time, c1, c2, coocurrence, 1)
#     '''
#     concepts = set(text_to_concepts(text))
#     if tags:
#         concepts.update(tags)
#     cooccurences = []
#     for concept_1, concept_2 in product(concepts, concepts):
#         if concept_1 != concept_2:
#             cooccurences.append(
#                 (time, concept_1, concept_2, 'coocurrence', 1)
#             )
#     return cooccurences


