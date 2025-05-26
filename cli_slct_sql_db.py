from sqlio import SqlIO
from menus import SubMenu
from cfg import NwdTestConfig

from op_select_file import SelectFileOp

class SelectSqliteDbFileMenu(SubMenu):
  def __init__(self, sql: SqlIO):
    self.sql = sql

  def key(self):
    return "sel"
  
  def exit_after_selection(self):
    return True
  
  def desc(self):
    return "Select Sqlite DB File"
  
  def get_ops(self):
    ops = []
    db_files = self.sql.get_db_files()
    if len(db_files) < 1:
      print("no files to list")
    else:
      key = 0
      for file in db_files:
        key += 1
        ops.append(SelectFileOp(self.sql, key, file))
    return ops

if __name__ == "__main__":
  tcfg = NwdTestConfig()
  sql = SqlIO(tcfg)
  main = SelectSqliteDbFileMenu(sql)
  main.show_menu()