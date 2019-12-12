import string
from itertools import product


def tokenize(text, lowercase=False):
    if lowercase:
        text = text.lower()
    return text.translate(str.maketrans('', '', string.punctuation)).split()


def text_to_concepts(text):
    tokens = tokenize(text)
    concepts = tokens       # dummy procedure to be completed.
    return set(concepts)


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


def text_to_concepts_batch(texts):
    pass


def text_to_concepts_spacy(text):
    pass


def text_to_concepts_batch_spacy(texts):
    pass
