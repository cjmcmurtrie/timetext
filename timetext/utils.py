import re


TOKENIZE_PATTERN = re.compile(r"[,.;@#?!&$<>:\'\"/\-\(\)]+\ *")


STOP_WORDS = {
    'i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're", "you've", "you'll", "you'd",
    'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', "she's", 'her', 'hers', 'herself',
    'it', "it's", 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom',
    'this', 'that', "that'll", 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has',
    'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until',
    'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before',
    'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again',
    'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few',
    'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very',
    's', 't', 'can', 'will', 'just', 'don', "don't", 'should', "should've", 'now', 'd', 'll', 'm', 'o', 're', 've',
    'y', 'ain', 'aren', "aren't", 'couldn', "couldn't", 'didn', "didn't", 'doesn', "doesn't", 'hadn', "hadn't", 'hasn',
    "hasn't", 'haven', "haven't", 'isn', "isn't", 'mightn', "mightn't", 'mustn', "mustn't", 'needn', "needn't",
    'shan', "shan't", 'shouldn', "shouldn't", 'wasn', "wasn't", 'weren', "weren't", 'won', "won't", 'wouldn',
    "wouldn't", 'many', 'few', 'several'
}


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
        result.append(group)
    return result


def chunkdelimiters(iterable, delimiters):
    result = []
    group = []
    if iterable:
        for e in iterable:
            if e not in delimiters:
                group.append(e)
            else:
                if group:
                    result.append(tuple(group))
                group = []
        result.append(tuple(group))
    return result


def tokenize(text, lowercase=False):
    if lowercase:
        text = text.lower()
    subpunct = TOKENIZE_PATTERN.sub(" ", text)
    return subpunct.split()


def gen_ngrams(iterable, n):
    return zip(*[iterable[i:] for i in range(n)])
