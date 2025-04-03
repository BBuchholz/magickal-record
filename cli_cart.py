from cartographer import Cartographer
from menus import (
  # LineOption,
  # Menu,
  SubMenu,
)
from op_list_cart_files import ListCartFilesOp

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
    return ops

if __name__ == "__main__":
  main = CartMenu()
  main.show_menu()