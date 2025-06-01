from sqlite3 import Cursor
from chronio import ChronIO

class DbOne:
  # database definitions for version one
  def __init__(self):
    self.version = 1
    self.chron = ChronIO()

  def ensure_table_db_meta(self, cursor):
    cursor.execute('''
      CREATE TABLE IF NOT EXISTS DbMeta (
        DbMetaKey TEXT NOT NULL UNIQUE,
        DbMetaValue TEXT,
        PRIMARY KEY(DbMetaKey)
      )
    ''')

  def ensure_db_meta_values(self, cursor):
    print(f"checking current db metadata")
    current_meta = self.get_db_meta(cursor)
    print(f"current metadata is {current_meta}")
    key = 'db_version'
    if key not in current_meta:
      val = self.version
      print(f"key {key} not found, inserting")
      self.insert_db_meta(cursor, key, val)
      print(f"inserted value: {val} for key: {key}")
    else:
      val = current_meta[key]
      print(f"found existing value: {val} for key: {key}")
    key = 'db_ensured_at'
    if key not in current_meta:
      val = self.chron.get_timestamp()
      print(f"key {key} not found, inserting")
      self.insert_db_meta(cursor, key, val)
      print(f"inserted value: {val} for key: {key}")
    else:
      val = current_meta[key]
      print(f"found existing value: {val} for key: {key}")
      val = self.chron.get_timestamp()
      print(f"Updating db_ensured_at timestamp to {val}")
      self.update_db_meta(cursor, key, val)


  def get_db_meta(self, cursor: Cursor):
    version = None
    cursor.execute("SELECT * FROM DbMeta")
    rows = cursor.fetchall()
    metaData = {}
    if len(rows) > 0:
      metaData = self.load_db_meta_from_rows(rows)
      print(f"metadata found: {metaData}")
    else:
      print("no db meta rows found")
    return metaData

  def insert_db_meta(self, cursor: Cursor, key, value):
    try:
      cursor.execute('''
        INSERT INTO DbMeta (DbMetaKey, DbMetaValue)
        VALUES (?, ?)
      ''', (key, value))
    except Exception as e:
      print("Exception inserting into db:")
      print(repr(e))

  def update_db_meta(self, cursor: Cursor, key, val):
    query = '''
      UPDATE DbMeta
      SET DbMetaValue = ?
      WHERE DbMetaKey = ?
    '''
    cursor.execute(query, (val, key))

  def load_db_meta_from_rows(self, rows):
    metaData = {}
    for row in rows:
      if row['DbMetaKey'] == 'db_version':
        version = row['DbMetaValue']
        metaData['db_version'] = version
        print(f"found db_version: {version}")
      if row['DbMetaKey'] == 'db_ensured_at':
        ensured = row['DbMetaValue']
        metaData['db_ensured_at'] = ensured
        print(f"found db_ensured_at: {ensured}")
    return metaData