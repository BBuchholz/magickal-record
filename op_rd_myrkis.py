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
    myrkis = self.sql.select_myrkis()
    print(f"myrkis found: {myrkis}")