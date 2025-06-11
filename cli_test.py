from cfg import Config, NwdTestConfig
from cli_cart import CartMenu
from cartio import CartIO
from mdio import MDIO
from menus import SubMenu, LineOption
from op_sug import SuggestionOp

class TestMenu(SubMenu):
  def __init__(self, tcfg: NwdTestConfig):
    self.ops = []
    
    # test menu instantiates its own 
    # test handlers that use test 
    # config, even from the main menu

    # CARTIO HANDLER
    cart = CartIO(tcfg)
    op = CartMenu(cart)
    self.add_op(op)

    # MDIO HANDLER
    mdio = MDIO(tcfg)
    op = SuggestionOp(mdio)
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
  # cart = CartIO(tcfg)
  # mdio = MDIO(tcfg)
  # main = TestMenu(cart, mdio)
  main = TestMenu(tcfg)
  main.show_menu()