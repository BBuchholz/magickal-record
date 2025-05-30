from sqlite3 import Cursor

class DbOne:
  # database definitions for version one
  def __init__(self):
    self.version = 1

  def create_table_db_meta(self, cursor):
    cursor.execute('''
      CREATE TABLE IF NOT EXISTS DbMeta (
        DbMetaKey TEXT NOT NULL UNIQUE,
        DbMetaValue TEXT,
        PRIMARY KEY(DbMetaKey)
      )
    ''')

  def insert_db_meta(self, cursor: Cursor, key, value):
    try:
      cursor.execute('''
        INSERT INTO DbMeta (DbMetaKey, DbMetaValue)
        VALUES (?, ?)
      ''', (key, value))
    except Exception as e:
      print("Exception inserting into db:")
      print(repr(e))
