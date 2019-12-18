from timetext.db import DB, FETCH_QUERIES
from tests.config import PROJECT_NAME

def test_initialize_new_project():
    DB(PROJECT_NAME)


def test_insert_relation():
    '''
    Insert relation into
    '''
    tt = DB(PROJECT_NAME)
    relation = [
        '2003-01-01 00:24:52.158000+00:00',
        'this is a concept', 'this is a related concept',
        'co_occurrence', 1
    ]
    tt.insert_relation(relation)
    assert 'this is a related concept' in tt.get_concept_relations('this is a concept')[0]


def test_query_concept():
    tt = DB(PROJECT_NAME)
    relation = [
        '2003-01-01 00:24:52.158000+00:00',
        'this is a concept', 'this is a related concept',
        'co_occurrence', 1
    ]
    tt.insert_relation(relation)
    related_concepts = tt.get_concept_relations('this is a concept')
    times, concepts = zip(*related_concepts)
    assert 'this is a related concept' in concepts


def test_query_concepts_batch():
    tt = DB(PROJECT_NAME)
    relations = [
        [
            '2003-01-01 00:24:52.158000+00:00',
            'this is a concept', 'this is a related concept',
            'co_occurrence', 1
        ],
        [
            '2003-01-01 00:24:52.158000+00:00',
            'this is another concept', 'this is another related concept',
            'co_occurrence', 1
        ],
        [
            '2003-01-01 00:24:52.158000+00:00',
            'this is a third concept', 'this is a third related concept',
            'co_occurrence', 1
        ],
    ]
    tt.insert_relations(relations)
    related_concepts = tt.get_concept_relations_batch(
        ['this is a concept', 'this is another concept']
    )

