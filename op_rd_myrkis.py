from menus import LineOption
from sqlio import SqlIO

class ReadMyrkis(LineOption):
  def __init__(self, sql: SqlIO):
    self.sql = sql

  def key(self):
    return "rdm"
  
  def desc(self):
    return "Read Myrkis"
  
  def run(self):
    if self.sql.table_exists("Myrki"):
      print("read table here")
    else:
      print("table Myrki not found")