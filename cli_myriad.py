from mdio import MDIO
from cfg import NwdTestConfig, Config
from menus import SubMenu

class MyrMenu(SubMenu):
  def __init__(self, mdio: MDIO):
    self.mdio = mdio

  def key(self):
    return "myr"
  
  def desc(self):
    return "Myriad File Menu"
  
  def get_ops(self):
    ops = []
    return ops
  
if __name__ == "__main__":
  tcfg = NwdTestConfig()
  mdio = MDIO(tcfg)
  main = MyrMenu(mdio)
  main.show_menu()