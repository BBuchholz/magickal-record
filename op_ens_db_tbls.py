from menus import LineOption
from sqlio import SqlIO

class EnsureDbTablesOp(LineOption):
  def __init__(self, sql: SqlIO):
    self.sql = sql

  def key(self):
    return 'etb'
  
  def desc(self):
    return "Ensure Db Tables"

  def run(self):
    self.sql.ensure_all_tables()