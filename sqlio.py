from file_mgr import FileManager
from cfg import Config
from files import (
  get_sqlite3_files,
)

class SqlIO(FileManager):
  def __init__(self, cfg: Config):
    self.cfg = cfg

  def select_file(self, file_name):
    # TODO: connect to db and all that goes here
    db_version = self.get_current_db_version()


  def get_current_db_version(self):
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
    return "DB VERSIONING NOT YET IMPLEMENTED"

  def get_db_files(self):
    db_files = get_sqlite3_files(self.cfg.sqlite_folder())
    return db_files