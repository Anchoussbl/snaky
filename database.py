import sqlite3
import contextlib
import os
# Scores:
# ==================================
# | Id       | Name     |  Score    |
# |----------|----------|-----------|
# | 1        | 'Player1'|    10     |
# ===================================

class DataBase:
    def __init__(self, name="test2.db"):
        self.filename = name
        self.insert_query = """INSERT INTO Scores (Name, Score)
                           VALUES (?, ?); """
        self.update_query = """UPDATE Scores 
                               SET Score=?
                               WHERE Name=?;
        """
        if not os.path.exists(self.filename):
            self.create()

    def create(self):
        create_table = """CREATE TABLE Scores (
                   id INTEGER PRIMARY KEY,
                   Name TEXT,
                   Score Integer
                   );
        """
        with contextlib.closing(sqlite3.connect(self.filename)) as con:
            with con:
                with contextlib.closing(con.cursor()) as cur:
                    cur.execute(create_table)
                    cur.execute(self.insert_query, ("Player1", 0))

    def load(self):
        result = {}
        with contextlib.closing(sqlite3.connect(self.filename)) as con:
            with con:
                with contextlib.closing(con.cursor()) as cur:
                    cur.execute('SELECT Name, Score FROM Scores WHERE Name="Player1";')
                    res = cur.fetchone() # -> ('Player1', 10)
                    result = {"Player1": res[1]}
        return result

    def store(self, values):
        data = (values["Player1"], "Player1")
        with contextlib.closing(sqlite3.connect(self.filename)) as con:
            with con:
                with contextlib.closing(con.cursor()) as cur:
                    cur.execute(self.update_query, data)
