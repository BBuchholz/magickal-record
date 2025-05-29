from file_mgr import FileManager
import sqlite3
from cfg import Config
from files import (
  get_sqlite3_files,
  get_path_in_folder,
)

class SqlIO(FileManager):
  def __init__(self, cfg: Config):
    self.cfg = cfg
    self.selected_db = None

  def open_connection(self):
    conn = None
    try:
      if self.selected_db is not None:
        s_fldr = self.cfg.sqlite_folder()
        fname = self.selected_db
        file_path = get_path_in_folder(s_fldr, fname)
        print(f"attempting to connect to {file_path}")
        conn = sqlite3.connect(file_path)
        conn.row_factory = sqlite3.Row
      else:
        print("no db file selected")
    except Exception as e:
      print("Exception opening connection to db")
      print(repr(e))
    finally:
      return conn

  def select_file(self, file_name):
    self.selected_db = file_name
    conn = self.open_connection()
    if conn is not None:
      cursor = conn.cursor()
      # TODO: connect to db and all that goes here
      metaData = self.get_db_meta(cursor)
      self.db_meta = metaData
    else:
      print("Error getting db metadata")


  def get_db_meta(self, cursor: sqlite3.Cursor):
    version = None
    # TODO: check db_version goes here
    # to allow for this, each db should have 
    # a table called DbMeta that is just two 
    # columns "DbMetaKey" and "DbMetaValue", 
    # a key value store where we can store 
    # db information, then as we create 
    # different table definitions and revise 
    # them we can just increment the 
    # db version number and have different 
    # handlers for each version, so this 
    # method should check DbMeta for a key 
    # of "db_version" and should return 
    # that value here, going forward we can 
    # use that to load the proper sql scripts 
    # for any version we desire and will 
    # have ultimate flexibility with cowboy 
    # coding tables as inspiration strikes 
    # that we can clean up later, just moving 
    # things between DB files
    # We can even eventually write a script 
    # to include the expected version number
    # in the file name so when selecting we 
    # know which is the latest version
    cursor.execute("SELECT * FROM DbMeta")
    rows = cursor.fetchall()
    metaData = {}
    if len(rows) > 0:
      metaData = self.load_db_meta_from_rows(rows)
      print(f"metadata found: {metaData}")
    else:
      print("no db meta rows found")
    return metaData
  
  def load_db_meta_from_rows(self, rows):
    metaData = {}
    for row in rows:
      if row['DbMetaKey'] == 'db_version':
        version = row['DbMetaValue']
        metaData['db_version'] = version
        print(f"found db_version: {version}")
      if row['DbMetaKey'] == 'tables_ensured_at':
        ensured = row['DbMetaValue']
        metaData['tables_ensured_at'] = ensured
        print(f"found tables_ensured_at: {ensured}")
    return metaData
    
    
    
    

  def get_db_files(self):
    db_files = get_sqlite3_files(self.cfg.sqlite_folder())
    return db_files