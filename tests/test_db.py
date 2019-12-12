from timetext.db import DB, FETCH_QUERIES


def test_initialize_new_project():
    project_name = 'test_project'
    DB(project_name)


def test_insert_relation():
    '''
    Insert relation into
    '''
    project_name = 'test_project'
    tt = DB(project_name)
    relation = [
        '2003-01-01 00:24:52.158000+00:00',
        'this is a concept', 'this is a related concept',
        'co_occurrence', 1
    ]
    tt.insert_relation(relation)
    assert 'this is a concept' in tt.get_concept_relations('this is a concept')[0]


if __name__ == '__main__':
    test_initialize_new_project()
    test_insert_relation()
