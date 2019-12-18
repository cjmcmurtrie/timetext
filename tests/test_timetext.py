import csv
import time
from timetext import timetext
from tests.config import PROJECT_NAME


def test_timetext_populate():
    tt = timetext(PROJECT_NAME)
    timestamped_texts = [
        ['2003-01-01', 'this is a document with a number of concepts'],
        ['2003-01-02', 'this is another  document with a number of different concepts']
    ]
    times, texts = zip(*timestamped_texts)
    tt.populate(times, texts)


def get_1000_test_documents(test_file='tests/data/1000.csv'):
    with open(test_file, 'r') as f:
        reader = csv.reader(f)
        time_texts = [(timestamp, text) for timestamp, text, metadata in reader][1:]
    f.close()
    return time_texts


def test_timetext_populate_1000_tokens(test_file='data/1000.csv'):
    times, texts = zip(*get_1000_test_documents())
    tags = [] * len(times)
    tt = timetext(PROJECT_NAME)
    start = time.time()
    tt.populate(times, texts, tags=tags, mode='tokens')
    end = time.time()
    print('test: computed 1000 short documents in', end - start)
    assert end - start <= 0.2


def test_timetext_populate_1000_spacy(test_file='data/1000.csv'):
    times, texts = zip(*get_1000_test_documents())
    tags = [] * len(times)
    tt = timetext(PROJECT_NAME)
    start = time.time()
    tt.populate(times, texts, tags=tags, mode='spacy')
    end = time.time()
    print('test: computed 1000 short documents in', end - start)
    assert end - start <= 0.6


def test_hops():
    tt = timetext(PROJECT_NAME)
    timestamped_texts = [
        ['2003-01-01', 'this is a text with a number of concepts'],
        ['2003-01-02', 'this is another  document with a number of different concepts']
    ]
    times, texts = zip(*timestamped_texts)
    tt.populate(times, texts)
    hops = tt.hops('text', 2)
    second_hop = hops[2]
    assert 'different' in second_hop
