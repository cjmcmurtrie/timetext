import time
from timetext.parse import tokenize, text_to_concepts_tokens, text_to_concepts_spacy, text_to_concepts_spacy_batch


def test_tokenize():
    text = '''
    Limalok is a guyot, an undersea volcanic mountain with a flat top, 
    in the southeastern Marshall Islands in the Pacific Ocean.
    '''
    tokens = tokenize(text)
    assert tokens == [
        'Limalok', 'is', 'a', 'guyot', 'an', 'undersea', 'volcanic', 'mountain', 'with', 'a', 'flat',
        'top', 'in', 'the', 'southeastern', 'Marshall', 'Islands', 'in', 'the', 'Pacific', 'Ocean'
    ]


def test_text_to_concepts():
    text = '''
    Limalok is a guyot, an undersea volcanic mountain with a flat top, 
    in the southeastern Marshall Islands in the Pacific Ocean.
    '''
    concepts = text_to_concepts_tokens(text)
    assert concepts == {
        'Limalok', 'is', 'a', 'guyot', 'an', 'undersea', 'volcanic', 'mountain', 'with', 'a', 'flat',
        'top', 'in', 'the', 'southeastern', 'Marshall', 'Islands', 'in', 'the', 'Pacific', 'Ocean'
    }


def test_text_to_concepts_time():
    '''
    Testing that 1000 short documents will parse in 0.01/document, implying capacity for 100k short documents
    per second or 6 million short documents per minute (assuming run-time scaling).
    '''
    text = '''
    Limalok is a guyot, an undersea volcanic mountain with a flat top, 
    in the southeastern Marshall Islands in the Pacific Ocean.
    '''
    times = []
    for _ in range(1000):
        start = time.time()
        text_to_concepts_tokens(text)
        times.append(time.time() - start)
    average_run = sum(times) / len(times)
    print('extracting concepts took', average_run, 'seconds per document')
    assert average_run < 0.01


def test_text_to_concepts_spacy():
    text = '''
    Limalok is a guyot, an undersea volcanic mountain with a flat top, 
    in the southeastern Marshall Islands in the Pacific Ocean.
    '''
    concepts = text_to_concepts_spacy(text)
    print(concepts)
    assert concepts == {
        'Limalok', 'Marshall Islands', 'undersea', 'volcanic',
        'Pacific Ocean', 'southeastern', 'top', 'flat', 'guyot', 'mountain'
    }


def test_text_to_concepts_spacy_time():
    text = '''
    Limalok is a guyot, an undersea volcanic mountain with a flat top, 
    in the southeastern Marshall Islands in the Pacific Ocean.
    '''
    times = []
    for _ in range(1000):
        start = time.time()
        text_to_concepts_spacy(text)
        times.append(time.time() - start)
    average_run = sum(times) / len(times)
    print('extracting concepts took', average_run, 'seconds per document')
    assert average_run < 0.01


def test_text_to_concepts_spacy_batch_time():
    text = '''
    Limalok is a guyot, an undersea volcanic mountain with a flat top, 
    in the southeastern Marshall Islands in the Pacific Ocean.
    '''
    texts = [text] * 1000
    start = time.time()
    text_to_concepts_spacy_batch(texts)
    end = time.time()
    print('extracting concepts took', (end - start) / 1000, 'seconds per document')
