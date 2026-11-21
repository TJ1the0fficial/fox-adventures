import sqlite3
from pathlib import Path

SRC = Path(__file__).resolve().parents[4]
DB_PATH = SRC / "databases"

DB_PATH.parent.mkdir(parents=True,exist_ok=True)

def search(database_withsuffix : str, table : str, coloumn : str, value):
    con = sqlite3.connect(database_withsuffix)
    cur = con.cursor()

    cur.execute(f"SELECT * FROM {table} WHERE {coloumn} = \'{value}\';")
    return_value = cur.fetchall()

    con.close()

    return return_value

# print(search("item_dictionary.db","items","name","dummy")[0])