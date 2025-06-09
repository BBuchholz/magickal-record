from sqlio import SqlIO
from menus import SubMenu
from cfg import Config, NwdTestConfig
from cartio import CartIO

from cli_slct_sql_db import SelectSqliteDbFileMenu
from cli_cart import CartMenu
from op_ens_db_tbls import EnsureDbTablesOp
from op_ens_db import EnsureDbFileOp
from op_ins_carts import InsertSelectedCartFileIntoCurrentDb
from op_rd_myrkis import ReadMyrkis

class SqliteMenu(SubMenu):
  def __init__(self, cfg: Config):
    print(f"loading SqlIO configuration: {cfg.status()}")
    self.cfg = cfg
    self.sql = SqlIO(cfg)
    self.cart = CartIO(cfg)

  def key(self):
    return "sql"
  
  def desc(self):
    return "Sqlite Menu"
  
  def get_ops(self):
    ops = []
    ops.append(SelectSqliteDbFileMenu(self.sql))
    # TODO: implement these
    ops.append(EnsureDbTablesOp(self.sql))
    ops.append(EnsureDbFileOp(self.sql))
    ops.append(InsertSelectedCartFileIntoCurrentDb(self.sql, self.cart))
    ops.append(CartMenu(self.cart))
    ops.append(ReadMyrkis(self.sql))
    return ops
  
if __name__ == "__main__":
  tcfg = NwdTestConfig()
  main = SqliteMenu(tcfg)
  main.show_menu()