import sqlite3
from contextlib import closing


def fetch(search_word, db_path='../db/data.db', table="synonyms", column="WORD"):
    with sqlite3.connect(db_path) as conn:
        with closing(conn.cursor()) as cursor:
            query = f"SELECT * FROM {table} WHERE {column} = ?"
            cursor.execute(query, (search_word,))
            return [dict(zip([desc[0] for desc in cursor.description], row)) for row in cursor.fetchall()]
