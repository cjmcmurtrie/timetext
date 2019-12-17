import csv
import time
from timetext import timetext


def test_timetext_populate():
    tt = timetext('test_project')
    timestamped_texts = [
        ['2003-01-01', 'this is a document with a number of concepts'],
        ['2003-01-02', 'this is another  document with a number of different concepts']
    ]
    tt.parse_and_populate(timestamped_texts)


def get_1000_test_documents(test_file='data/1000.csv'):
    with open(test_file, 'r') as f:
        reader = csv.reader(f)
        time_texts = [(timestamp, text) for timestamp, text, metadata in reader][1:]
    f.close()
    return time_texts


def test_timetext_populate_1000_tokens(test_file='data/1000.csv'):
    time_texts = get_1000_test_documents()
    tt = timetext('test_project')
    start = time.time()
    tt.parse_and_populate(time_texts, mode='tokens')
    end = time.time()
    print('test: computed 1000 short documents in', end - start)
    assert end - start <= 0.2


def test_timetext_populate_1000_spacy(test_file='data/1000.csv'):
    time_texts = get_1000_test_documents()
    tt = timetext('test_project')
    start = time.time()
    tt.parse_and_populate(time_texts, mode='spacy')
    end = time.time()
    print('test: computed 1000 short documents in', end - start)
    assert end - start <= 0.6


if __name__ == '__main__':
    test_timetext_populate()
    # test_timetext_populate_1000_tokens()
    test_timetext_populate_1000_spacy()
