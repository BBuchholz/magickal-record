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
        metaData = self.get_db_meta(cursor)
        self.db_meta = metaData
        print(f"successfully selected file: {file_name}")
      except Exception as e:
        print("Error getting db metadata")
        print("if this is a new database run etb option to ensure tables")
      finally:
        print(f"closing connection to: {file_name}")
        conn.commit()
        conn.close()
        print(f"closed connection to: {file_name}")


  def get_db_meta(self, cursor: sqlite3.Cursor):
    return self.db_one.get_db_meta(cursor)
    
  def select_myrkis(self):
    conn = self.open_connection()
    myrkis = []
    if conn is not None:
      try:
        cursor = conn.cursor()
        myrkis = self.db_one.select_myrkis(cursor)
      except Exception as e:
        print("Error selecting myrkis:")
        print(repr(e))
      finally:
        print("closing connection to db")
        conn.close()
        return myrkis
    
  def select_cards(self):
    conn = self.open_connection()
    cards = []
    if conn is not None:
      try:
        cursor = conn.cursor()
        cards = self.db_one.select_cards(cursor)
      except Exception as e:
        print("Error selecting cards:")
        print(repr(e))
      finally:
        print("closing connection to db")
        conn.close()
        return cards
      
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
        self.db_one.ensure_table_db_meta(cursor)
        self.db_one.ensure_db_meta_values(cursor)
        self.db_one.ensure_table_myrki(cursor)
        self.db_one.ensure_table_card(cursor)
        self.db_one.ensure_table_cet(cursor)
        self.db_one.ensure_table_collaboration(cursor)
        self.db_one.ensure_table_collab_member(cursor)
        self.db_one.ensure_table_source(cursor)
      except Exception as e:
        print("Error ensuring tables:")
        print(repr(e))
      finally:
        print("committing changes to db")
        conn.commit()
        print("closing connection to db")
        conn.close()
        print("TABLES SHOULD BE ENSURED AFTER THIS POINT")
        