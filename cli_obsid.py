from obsidio import ObsidIO
from menus import SubMenu
from op_imp_obo import ImportObsidianFilesMenu
from op_ld_vaults import LoadVaultsOp
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
    ops.append(LoadVaultsOp(self.obio))
    ops.append(ImportObsidianFilesMenu(self.obio))
    return ops
  
if __name__ == "__main__":
  main = ObsidMenu()
  main.show_menu()