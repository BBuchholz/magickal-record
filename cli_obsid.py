from obsidio import ObsidIO
from menus import SubMenu
from op_imp_obo import ImportObsidianFilesMenu

class ObsidMenu(SubMenu):
  def __init__(self, config):
    self.obio = ObsidIO(config)

  def key(self):
    return "obo"
  
  def desc(self):
    return "Obsidian Integration Menu"
  
  def get_ops(self):
    ops = []
    ops.append(ImportObsidianFilesMenu(self.obio))
    return ops