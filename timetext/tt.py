import sqlite3 as sql


CREATE_TABLE_QUERIES = {
    'sql_create_relations_table': """ 
            CREATE TABLE IF NOT EXISTS relation (
            id integer PRIMARY KEY,
            time timestamp,
            concept_1 text NOT NULL,
            concept_2 text NOT NULL,
            relation text NOT NULL,
            relation_value text
        );
    """,
    'sql_create_concepts_table': """
            CREATE TABLE IF NOT EXISTS concept (
            id integer PRIMARE KEY,
            time timestamp,
            concept text NOT NULL,
            property text,
            property_type text
        );
    """

}


INSERT_QUERIES = {
    'sql_insert_relation': """
        INSERT INTO relation(time, concept_1, concept_2, relation, relation_value)
        VALUES(?,?,?,?,?)
    """
}


FETCH_QUERIES = {
    'sql_concept_1_relations': """
        SELECT * FROM relation WHERE concept_1=?;
    """
}


class Timetext(object):

    def __init__(self, project_name):
        self.backend = 'sqlite'
        self.db_name = '../projects/{name}.db'.format(name=project_name)
        self.db = sql.connect(self.db_name)
        self._init()

    def _init(self):
        cursor = self.db.cursor()
        cursor.execute(CREATE_TABLE_QUERIES['sql_create_relations_table'])
        self.db.commit()

    def fetch(self, concept_1, time_window=None):
        cursor = self.db.cursor()
        query = FETCH_QUERIES['sql_concept_1_relations']
        rows = cursor.execute(query, (concept_1, )).fetchall()
        return rows

    def insert_relation(self, row):
        cursor = self.db.cursor()
        cursor.execute(INSERT_QUERIES['sql_insert_relation'], row)
        self.db.commit()

    def populate(self, rows):
        pass

    def analyse(self, node, params):
        pass
