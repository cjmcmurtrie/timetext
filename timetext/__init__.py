from timetext.tt import Timetext
"""
    timetext
    ~~~~~~~~
    Build and query a natural language graph database.

    :copyright: (c) 2019-2020 by Conan McMurtrie.
    :license: MIT, see LICENSE for more details.
"""


def timetext(project_name):
    return Timetext(project_name)


if __name__ == '__main__':
    from timetext import timetext
    tt = timetext('test_project')
    timestamped_texts = [
        ['2003-01-01', 'this is a document with a number of concepts'],
        ['2003-01-02', 'this is another  document with a number of different concepts']
    ]
    tt.populate(timestamped_texts)
