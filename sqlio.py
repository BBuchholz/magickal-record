from file_mgr import FileManager
import sqlite3
from cfg import Config
from files import (
  get_sqlite3_files,
  get_path_in_folder,
)
from db_one import DbOne
from myrki_row_list import MyrkiRowList
from card_row_list import MyrkiInstanceRowList

class SqlIO(FileManager):
  def __init__(self, cfg: Config):
    self.cfg = cfg
    self.selected_db = None
    self.db = DbOne()

  def create_db(self, file_name: str):
    if not file_name.endswith(".sqlite3"):
      file_name = file_name + ".sqlite3"
    conn = self.open_connection(file_name)
    cursor = conn.cursor()
    self.db.ensure_table_db_meta(cursor)
    self.db.ensure_db_meta_values(cursor)
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

  def batch_insert_cards(self, cards):
    if self.selected_db is None:
      print("no db selected, exiting batch myrki insert")
      return
    else:
      file_name = self.selected_db
      conn = self.open_connection()
      if conn is not None:
        try:
          cursor = conn.cursor()
          for card in cards:
            print(f"inserting card: {card}")
            self.db.insert_myrki_instance(cursor, card)
          print(f"successfully selected file: {file_name}")
        except Exception as e:
          print("Error inserting card")
          print(repr(e))
        finally:
          print(f"closing connection to: {file_name}")
          conn.commit()
          conn.close()
          print(f"closed connection to: {file_name}")

  def batch_update_cards(self, cards):
    print("IMPLEMENT BATCH update HERE")

  def batch_insert_myrkis(self, myrkis):
    if self.selected_db is None:
      print("no db selected, exiting batch myrki insert")
      return
    else:
      file_name = self.selected_db
      conn = self.open_connection()
      if conn is not None:
        try:
          cursor = conn.cursor()
          for myrki in myrkis:
            print(f"inserting myrki: {myrki}")
            self.db.insert_myrki(cursor, myrki)
          print(f"successfully selected file: {file_name}")
        except Exception as e:
          print("Error inserting myrki")
          print(repr(e))
        finally:
          print(f"closing connection to: {file_name}")
          conn.commit()
          conn.close()
          print(f"closed connection to: {file_name}")
    

  def get_db_meta(self, cursor: sqlite3.Cursor):
    return self.db.get_db_meta(cursor)
    
  def select_myrkis(self) -> MyrkiRowList:
    conn = self.open_connection()
    myrkis = MyrkiRowList()
    if conn is not None:
      try:
        cursor = conn.cursor()
        myrkis = self.db.select_myrkis(cursor)
      except Exception as e:
        print("Error selecting myrkis:")
        print(repr(e))
      finally:
        print("closing connection to db")
        conn.close()
        return myrkis
    
  def select_myrki_instances(self) -> MyrkiInstanceRowList:
    conn = self.open_connection()
    cards = MyrkiInstanceRowList()
    if conn is not None:
      try:
        print(f"aquiring cursor")
        cursor = conn.cursor()
        cards = self.db.select_myrki_instances(cursor)
      except Exception as e:
        print("Error selecting cards:")
        print(repr(e))
      finally:
        print("closing connection to db")
        conn.close()
        return cards
      
  def table_exists(self, table_name):
    return self.db.table_exists(table_name)
    

  def get_db_files(self):
    db_files = get_sqlite3_files(self.cfg.sqlite_folder())
    return db_files
  
  def ensure_all_tables(self):
    print("opening connection to db")
    conn = self.open_connection()
    if conn is not None:
      try:
        cursor = conn.cursor()
        self.db.ensure_table_db_meta(cursor)
        self.db.ensure_db_meta_values(cursor)
        self.db.ensure_table_myrki(cursor)
        self.db.ensure_table_card(cursor)
        self.db.ensure_table_cet(cursor)
        self.db.ensure_table_collaboration(cursor)
        self.db.ensure_table_collab_member(cursor)
        self.db.ensure_table_source(cursor)
      except Exception as e:
        print("Error ensuring tables:")
        print(repr(e))
      finally:
        print("committing changes to db")
        conn.commit()
        print("closing connection to db")
        conn.close()
        print("TABLES SHOULD BE ENSURED AFTER THIS POINT")
        