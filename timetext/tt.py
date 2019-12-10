import sqlite3 as sql


class Timetext(object):

    def __init__(self, project_name):
        self.backend = 'sqlite'
        self.db_name = '../projects/{name}.db'.format(name=project_name)
        self.db = sql.connect(self.db_name)
        self._init()

    def _init(self):
        pass

    def populate(self, rows):
        pass

    def analyse(self, node, params):
        pass
