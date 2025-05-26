from file_mgr import FileManager
from cfg import Config
from files import (
  get_sqlite3_files,
)

class SqlIO(FileManager):
  def __init__(self, cfg: Config):
    self.cfg = cfg

  def select_file(self, file_name):
    pass

  def get_db_files(self):
    db_files = get_sqlite3_files(self.cfg.sqlite_folder())
    return db_files