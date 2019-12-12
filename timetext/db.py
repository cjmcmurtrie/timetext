import os
import sqlite3 as sql
from config import PROJECT_PATH


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
    """,
    'sql_insert_relations_batch': """
        
    """
}


FETCH_QUERIES = {
    'sql_concept_relations': """
        SELECT * FROM relation WHERE concept_1=?;
    """
}


class DB(object):

    def __init__(self, project_name):
        self.backend = 'sqlite'
        self.db_name = 'projects/{name}.db'.format(name=project_name)
        self.db_path = os.path.join(PROJECT_PATH, self.db_name)
        self._init()

    def _init(self):
        conn = sql.connect(self.db_path, timeout=10)
        cursor = conn.cursor()
        query = CREATE_TABLE_QUERIES['sql_create_relations_table']
        cursor.execute(query)
        conn.commit()
        conn.close()

    def get_concept_relations(self, concept, time_window=None):
        conn = sql.connect(self.db_path, timeout=10)
        cursor = conn.cursor()
        query = FETCH_QUERIES['sql_concept_relations']
        rows = cursor.execute(query, (concept, )).fetchall()
        conn.close()
        return rows

    def insert_relation(self, row):
        conn = sql.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute(INSERT_QUERIES['sql_insert_relation'], row)
        conn.commit()
        conn.close()

    def insert_relations(self, rows):
        conn = sql.connect(self.db_path)
        cursor = conn.cursor()
        cursor.executemany(INSERT_QUERIES['sql_insert_relation'], rows)
        conn.commit()
        conn.close()
