from cartio import CartIO
from menus import (
  # LineOption,
  # Menu,
  SubMenu,
)
from op_list_cart_files import ListCartFilesOp
from op_list_myrkis import ListMyrkisOp
from cli_select_cart_file import SelectCartFileMenu
from op_list_related_myrkis import ListRelatedMyrkisOp
from op_audit_myrkis import AuditMyrkisOp
from op_audit_report import AudRepMenu
from cfg import Config, NwdTestConfig
from op_str_ver_cart import StoreSelectedCartFileAsVerifiedDefault
from op_clr_ver_cart import ClearSelectedVerifiedCartFiles
from op_lst_ver_cart import ListSelectedVerifiedCartFiles

class CartMenu(SubMenu):
  def __init__(self, cfg: Config):
    self.cart = CartIO(cfg)
  def key(self):
    return "cart"
  def desc(self):
    return "Cartographer menu"
  def get_ops(self):
    ops = []
    ops.append(ListCartFilesOp(self.cart))
    ops.append(ListMyrkisOp(self.cart))
    ops.append(ListRelatedMyrkisOp(self.cart))
    ops.append(AuditMyrkisOp(self.cart))
    ops.append(SelectCartFileMenu(self.cart))
    ops.append(AudRepMenu(self.cart))
    ops.append(StoreSelectedCartFileAsVerifiedDefault(self.cart))
    ops.append(ClearSelectedVerifiedCartFiles(self.cart))
    # TODO: implement
    # ops.append(ListSelectedVerifiedCartFiles(self.cart))
    return ops

if __name__ == "__main__":
  tcfg = NwdTestConfig()
  main = CartMenu(tcfg)
  main.show_menu()