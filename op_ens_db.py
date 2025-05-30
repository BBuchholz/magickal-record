from menus import LineOption
from sqlio import SqlIO

class EnsureDbFileOp(LineOption):
  def __init__(self, sql: SqlIO):
    self.sql = sql

  def key(self):
    return "edb"
  
  def desc(self):
    return "Ensure Db File"

  def run(self):
    fldr = self.sql.cfg.sqlite_folder()
    msg = f"This will check for a database "
    msg += f"with the name supplied. \n"
    msg += f"If the file does not exist one "
    msg += f"will be created in the "
    msg += f"folder {fldr}. \nIf you want a "
    msg += f"list of already created "
    msg += f"databases, use the select "
    msg += f"option. \nEntering a blank value "
    msg += f"for the name will cancel this "
    msg += f"operation. \nWhat database would "
    msg += f"you like to open?"
    name = input(msg)
    name = name.strip()
    if len(name) > 0:
      self.sql.create_db(name)
    else:
      print("no name given, aborting...")