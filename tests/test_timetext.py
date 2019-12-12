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


def test_timetext_populate_1000():
    with open('data/1000.csv', 'r') as f:
        reader = csv.reader(f)
        relations = [(timestamp, text) for timestamp, text, metadata in reader][1:]
    f.close()
    tt = timetext('test_project')
    start = time.time()
    tt.parse_and_populate(relations)
    end = time.time()
    print('test: computed 1000 short documents in', end - start)
    assert end - start <= 0.2


if __name__ == '__main__':
    test_timetext_populate()
    test_timetext_populate_1000()
