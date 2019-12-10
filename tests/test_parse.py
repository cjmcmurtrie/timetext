import time
from timetext.parse import text_to_concepts


def test_text_to_concepts():
    text = '''
    Limalok is a guyot, an undersea volcanic mountain with a flat top, 
    in the southeastern Marshall Islands in the Pacific Ocean.
    '''
    concepts = text_to_concepts(text)
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
        text_to_concepts(text)
        times.append(time.time() - start)
    average_run = sum(times) / len(times)
    print('extracting concepts took', average_run, 'seconds per document')
    assert average_run < 0.01


if __name__ == '__main__':
    text = '''
    Limalok is a guyot, an undersea volcanic mountain with a flat top, 
    in the southeastern Marshall Islands in the Pacific Ocean.
    '''
    test_text_to_concepts()
    test_text_to_concepts_time()
