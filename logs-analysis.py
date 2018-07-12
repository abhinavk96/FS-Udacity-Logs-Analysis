import psycopg2

DB_NAME = "news"

def test_conn(name):
    db = psycopg2.connect(database=name)
    c = db.cursor()
    c.execute("SELECT * FROM pg_catalog.pg_tables;")
    # db.close()
    tables = c.fetchall()
    db.close()
    return tables

print(test_conn(DB_NAME))