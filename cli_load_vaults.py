from obsidio import ObsidIO
from cfg import NwdTestConfig
from menus import SubMenu
from op_select_cfg_file import SelectCfgFileOp

class LoadVaultsMenu(SubMenu):
  def __init__(self, obio):
    self.obio = obio
    self._exit_after_selection = False

  def key(self):
    return "ldv"
  
  def exit_after_selection(self):
    return self._exit_after_selection
  
  def desc(self):
    return "Load Vaults"
  
  def get_ops(self):
    ops = []
    cfg_files = self.obio.get_cfg_files()
    if len(cfg_files) < 1:
      print("no files to list")
      print("files must start with Config prefix")
      print("if this is in error, check file names")
      print("for prefix: Config")
    else:
      key = 0
      for file in cfg_files:
        key = key + 1
        ops.append(SelectCfgFileOp(self, key, file))
    return ops
  
if __name__ == "__main__":
  tcfg = NwdTestConfig()
  obio = ObsidIO(tcfg)
  main = LoadVaultsMenu(obio)
  main.show_menu()