import pathlib
import duckdb

DB_PATH = pathlib.Path(__file__).resolve().parent.parent / 'cities.ddb'


def test_cities_table_exists_and_has_rows():
    con = duckdb.connect(str(DB_PATH))
    tables = {row[0] for row in con.execute("PRAGMA show_tables").fetchall()}
    assert 'cities' in tables
    count = con.execute("SELECT COUNT(*) FROM cities").fetchone()[0]
    assert count > 0
