from cartio import Cartographer
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

class CartMenu(SubMenu):
  def __init__(self):
    self.cart = Cartographer()
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
    return ops

if __name__ == "__main__":
  main = CartMenu()
  main.show_menu()