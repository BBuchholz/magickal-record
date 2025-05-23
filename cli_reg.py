from menus import SubMenu
from cfg import Config, NwdTestConfig
from myrreg import MyrkiRegistry
from op_reg_lcf import ListCartFileEntriesOp
from op_reg_lmk import ListMyrKisOp
from op_reg_lmi import ListMyrkiInstancesOp

class RegistryMenu(SubMenu):
  def __init__(self, cfg: Config):
    self.loaded = False
    self.myrreg = MyrkiRegistry(cfg)

  def key(self):
    return "reg"
  
  def desc(self):
    return "Card and Myrki Registry"
  
  def get_ops(self):
    if not self.loaded:
      print("loading myrki registry, this may take a moment")
      self.myrreg.load()
      self.loaded = True
    ops = []
    ops.append(ListCartFileEntriesOp(self.myrreg))
    ops.append(ListMyrKisOp(self.myrreg))
    ops.append(ListMyrkiInstancesOp(self.myrreg))
    return ops


if __name__ == "__main__":
  tcfg = NwdTestConfig()
  main = RegistryMenu(tcfg)
  main.show_menu()