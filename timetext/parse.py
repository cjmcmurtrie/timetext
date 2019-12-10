import string


def tokenize(text, lowercase=False):
    if lowercase:
        text = text.lower()
    return text.translate(str.maketrans('', '', string.punctuation)).split()


def text_to_concepts(text):
    tokens = tokenize(text)
    concepts = tokens       # dummy procedure to be completed.
    return set(concepts)


def text_to_concepts_batch(texts):
    pass


def text_to_concepts_spacy(text):
    pass


def text_to_concepts_batch_spacy(texts):
    pass
