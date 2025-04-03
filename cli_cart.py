from cartographer import Cartographer
from menus import (
  LineOption,
  Menu,
  SubMenu,
)

  
class ListCartFilesOp(LineOption):
  def __init__(self, cart):
    self.cart = cart
  def key(self):
    return "list"
  def desc(self):
    msg = "list valid cartographer files in "
    msg += "cartographer folder"
    return msg
  def run(self):
    print("these are the files found:")
    if len(self.cart.get_cart_files()) > 0:
      print("list files here")
    else:
      print("no files found")

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