from cartio import CartIO
from menus import SubMenu

from op_select_file import SelectFileOp

class SelectCartFileMenu(SubMenu):
  def __init__(self, cart):
    self.cart = cart
  
  def key(self):
    return "select"
  
  def exit_after_selection(self):
    return True

  def desc(self):
    return "Select Cartographer File"

  def get_ops(self):
    ops = []
    cart_files = self.cart.get_cart_files()
    if len(cart_files) < 1:
      print("no files to list")
    else:
      key = 0
      for file in cart_files:
        key = key + 1
        ops.append(SelectFileOp(self.cart, key, file))
    return ops

if __name__ == "__main__":
  cart = CartIO()
  main = SelectCartFileMenu(cart)
  main.show_menu()
  
