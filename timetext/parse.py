import time
import spacy
from timetext.utils import tokenize, chunkdelimiters, chunkiter, gen_ngrams, STOP_WORDS


SPACY = spacy.load("en_core_web_sm", disable=['parser', 'tokenizer', 'ner', 'textcat'])


def text_to_concepts_batch(texts, mode):
    if mode == 'tokens':
        return text_to_concepts_tokens_batch(texts)
    elif mode == 'spacy':
        return text_to_concepts_spacy_batch(texts)
    elif mode == 'stopwords':
        return text_to_concepts_stopwords_batch(texts)


def text_to_concepts_tokens(text):
    tokens = tokenize(text)
    concepts = tokens       # dummy procedure to be completed.
    return set(concepts)


def text_to_concepts_tokens_batch(texts):
    results = []
    for text in texts:
        results.append(text_to_concepts_tokens(text))
    return results


def text_to_concepts_stopwords(text, ngram_range=2):
    tokens = tokenize(text, lowercase=True)
    chunks = chunkdelimiters(tokens, STOP_WORDS)
    ngrams = set()
    for chunk in chunks:
        for nglen in range(1, ngram_range + 1):
            ngrams.update(ng for ng in gen_ngrams(chunk, nglen))
    tostr = {' '.join(ngram) for ngram in ngrams}
    return tostr


def text_to_concepts_stopwords_batch(texts):
    results = []
    for text in texts:
        results.append(text_to_concepts_stopwords(text))
    return results


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
    noun_parts = {'NOUN', 'PROPN'}
    concept_pos = {'NOUN', 'PROPN', 'VERB', 'ADJ', 'ADV'}
    results = []
    for doc in SPACY.pipe(texts):
        if doc:
            tks, pos = zip(*[
                (tk.text, 'NOUN' if tk.pos_ in noun_parts else tk.pos_)
                for tk in doc
            ])
            poschunk = chunkiter(pos)
            ix = 0
            tks_chunks = []
            for chunk in poschunk:
                if any(pos in chunk for pos in concept_pos):
                    tks_chunks.append(' '.join(tks[ix: ix + len(chunk)]))
                ix += len(chunk)
            results.append(set(tks_chunks))
    return results
