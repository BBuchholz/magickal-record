from obsidio import ObsidIO
from cfg import NwdTestConfig
from menus import SubMenu
from op_imp_obo import ImportObsidianFilesMenu
from cli_load_vaults import LoadVaultsMenu
from op_dsp_vaults import DisplayVaultsOp

class ObsidMenu(SubMenu):
  def __init__(self, config):
    self.obio = ObsidIO(config)

  def key(self):
    return "obo"
  
  def desc(self):
    return "Obsidian Integration Menu"
  
  def get_ops(self):
    ops = []
    ops.append(DisplayVaultsOp(self.obio))
    ops.append(LoadVaultsMenu(self.obio))
    ops.append(ImportObsidianFilesMenu(self.obio))
    return ops
  
if __name__ == "__main__":
  tcfg = NwdTestConfig()
  main = ObsidMenu(tcfg)
  main.show_menu()