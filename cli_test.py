from cfg import Config, NwdTestConfig
from cli_cart import CartMenu
from cartio import CartIO
from menus import SubMenu, LineOption

class TestMenu(SubMenu):
  def __init__(self, cart: CartIO):
    self.ops = []
    op = CartMenu(cart)
    self.add_op(op)

  def key(self):
    return "tst"
  
  def desc(self):
    return "Auxillary Test Operations Menu"
  
  def get_ops(self):
    return self.ops
  
  def add_op(self, op: LineOption):
    self.ops.append(op)
    
if __name__ == "__main__":
  tcfg = NwdTestConfig()
  cart = CartIO(tcfg)
  main = TestMenu(cart)
  main.show_menu()