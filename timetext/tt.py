from timetext.db import DB
from timetext.parse import time_text_to_coccur_rows


class Timetext(object):

    def __init__(self, project_name):
        self.db = DB(project_name)

    def populate(self, relations):
        for relation in relations:
            self.db.insert_relation(relation)

    def parse_and_populate(self, timed_texts):
        relations = set()
        for time, text in timed_texts:
            relations.update(time_text_to_coccur_rows(time, text))
        self.db.insert_relations(relations)

    def analyse(self, concept):
        pass
