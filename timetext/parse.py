import string
from itertools import product
import spacy


SPACY = spacy.load("en_core_web_sm", disable=['parser', 'tokenizer', 'ner', 'textcat'])


def tokenize(text, lowercase=False):
    if lowercase:
        text = text.lower()
    text = ''.join(c if c not in string.punctuation else ' ' for c in text)
    return text.split()


def text_to_concepts(text):
    tokens = tokenize(text)
    concepts = tokens       # dummy procedure to be completed.
    return set(concepts)


def text_to_concepts_batch(texts):
    pass


def text_to_concepts_spacy(text):
    doc = SPACY(text)
    tks = [tk.text for tk in doc]
    pos = ['NOUN' if tk.pos_ in ('NOUN', 'PROPN') else tk.pos_ for tk in doc]
    poschunk = chunkiter(pos)
    ix = 0
    tks_chunks = []
    for chunk in poschunk:
        if any(pos in chunk for pos in ('NOUN', 'VERB', 'ADJ', 'ADV')):
            tks_chunks.append(' '.join(tks[ix: ix+len(chunk)]))
        ix += len(chunk)
    return set(tks_chunks)


def text_to_concepts_spacy_batch(texts):
    # todo: tokenizer before does not seem to improve concept meaning.
    results = []
    for doc in SPACY.pipe(texts):
        tks = [tk.text for tk in doc]
        pos = ['NOUN' if tk.pos_ in ('NOUN', 'PROPN') else tk.pos_ for tk in doc]
        poschunk = chunkiter(pos)
        ix = 0
        tks_chunks = []
        for chunk in poschunk:
            if any(pos in chunk for pos in ('NOUN', 'VERB', 'ADJ', 'ADV')):
                tks_chunks.append(' '.join(tks[ix: ix + len(chunk)]))
            ix += len(chunk)
        results.append(set(tks_chunks))
    return results


def chunkiter(iterable):
    result = []
    group = []
    if iterable:
        prev = iterable[0]
        for e in iterable:
            if e == prev:
                group.append(e)
            else:
                result.append(group)
                group = [e]
            prev = e
        if len(group) == 1:
            result.append(group)
    return result
