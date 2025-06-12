from file_mgr import FileManager
import sqlite3
from cfg import Config
from files import (
  get_sqlite3_files,
  get_path_in_folder,
)
from db_one import DbOne

class SqlIO(FileManager):
  def __init__(self, cfg: Config):
    self.cfg = cfg
    self.selected_db = None
    self.db_one = DbOne()

  def create_db(self, file_name: str):
    if not file_name.endswith(".sqlite3"):
      file_name = file_name + ".sqlite3"
    conn = self.open_connection(file_name)
    cursor = conn.cursor()
    self.db_one.ensure_table_db_meta(cursor)
    self.db_one.ensure_db_meta_values(cursor)
    conn.commit()
    conn.close()

  def open_connection(self, file_name=None):
    if file_name is not None:
      self.selected_db = file_name
    conn = None
    try:
      if self.selected_db is not None:
        s_fldr = self.cfg.sqlite_folder()
        fname = self.selected_db
        file_path = get_path_in_folder(s_fldr, fname)
        print("")
        print(f"attempting to connect to {file_path}")
        print("")
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
      try:
        cursor = conn.cursor()
        # TODO: connect to db and all that goes here
        metaData = self.get_db_meta(cursor)
        self.db_meta = metaData
      except Exception as e:
        print("Error getting db metadata")
        print("if this is a new database run etb option to ensure tables")
      finally:
        print("IMPLEMENTTHIS NEEDS TESTING")


  def get_db_meta(self, cursor: sqlite3.Cursor):
    return self.db_one.get_db_meta(cursor)
  #   version = None
  #   # TODO: check db_version goes here
  #   # to allow for this, each db should have 
  #   # a table called DbMeta that is just two 
  #   # columns "DbMetaKey" and "DbMetaValue", 
  #   # a key value store where we can store 
  #   # db information, then as we create 
  #   # different table definitions and revise 
  #   # them we can just increment the 
  #   # db version number and have different 
  #   # handlers for each version, so this 
  #   # method should check DbMeta for a key 
  #   # of "db_version" and should return 
  #   # that value here, going forward we can 
  #   # use that to load the proper sql scripts 
  #   # for any version we desire and will 
  #   # have ultimate flexibility with cowboy 
  #   # coding tables as inspiration strikes 
  #   # that we can clean up later, just moving 
  #   # things between DB files
  #   # We can even eventually write a script 
  #   # to include the expected version number
  #   # in the file name so when selecting we 
  #   # know which is the latest version
  #   cursor.execute("SELECT * FROM DbMeta")
  #   rows = cursor.fetchall()
  #   metaData = {}
  #   if len(rows) > 0:
  #     metaData = self.load_db_meta_from_rows(rows)
  #     print(f"metadata found: {metaData}")
  #   else:
  #     print("no db meta rows found")
  #   return metaData
  
  # def load_db_meta_from_rows(self, rows):
  #   metaData = {}
  #   for row in rows:
  #     if row['DbMetaKey'] == 'db_version':
  #       version = row['DbMetaValue']
  #       metaData['db_version'] = version
  #       print(f"found db_version: {version}")
  #     if row['DbMetaKey'] == 'tables_ensured_at':
  #       ensured = row['DbMetaValue']
  #       metaData['tables_ensured_at'] = ensured
  #       print(f"found tables_ensured_at: {ensured}")
  #   return metaData
    
  def select_myrkis(self):
    conn = self.open_connection()
    myrkis = {}
    if conn is not None:
      try:
        cursor = conn.cursor()
        # TODO: connect to db and all that goes here
        myrkis = self.db_one.select_myrkis(cursor)
      except Exception as e:
        print("Error selecting myrkis:")
        print(repr(e))
      finally:
        print("closing connection to db")
        conn.close()
        return myrkis
    
  def table_exists(self, table_name):
    return self.db_one.table_exists(table_name)
    

  def get_db_files(self):
    db_files = get_sqlite3_files(self.cfg.sqlite_folder())
    return db_files
  
  def ensure_all_tables(self):
    print("opening connection to db")
    conn = self.open_connection()
    if conn is not None:
      try:
        cursor = conn.cursor()
        # TODO: connect to db and all that goes here
        self.db_one.ensure_table_db_meta(cursor)
        self.db_one.ensure_db_meta_values(cursor)
        self.db_one.ensure_table_myrki(cursor)
      except Exception as e:
        print("Error ensuring tables:")
        print(repr(e))
      finally:
        print("committing changes to db")
        conn.commit()
        print("closing connection to db")
        conn.close()
        print("TABLES SHOULD BE ENSURED AFTER THIS POINT")
        