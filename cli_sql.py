from sqlio import SqlIO
from menus import SubMenu
from cfg import Config, NwdTestConfig

from cli_slct_sql_db import SelectSqliteDbFileMenu

class SqliteMenu(SubMenu):
  def __init__(self, cfg: Config):
    print(f"loading SqlIO configuration: {cfg.status()}")
    self.sql = SqlIO(cfg)

  def key(self):
    return "sql"
  
  def desc(self):
    return "Sqlite Menu"
  
  def get_ops(self):
    ops = []
    ops.append(SelectSqliteDbFileMenu(self.sql))
    return ops
  
if __name__ == "__main__":
  tcfg = NwdTestConfig()
  main = SqliteMenu(tcfg)
  main.show_menu()