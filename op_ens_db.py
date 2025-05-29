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
    pass