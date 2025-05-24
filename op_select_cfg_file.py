from cartio import CartIO
from cfg import NwdTestConfig
from menus import LineOption

class SelectCfgFileOp(LineOption):
  def __init__(self, parent_menu, key, file_name):
    self.obio = parent_menu.obio
    self.parent_menu = parent_menu
    self.key_value = key
    self.file_name = file_name

  def key(self):
    return self.key_value

  def desc(self):
    return self.file_name

  def run(self):
    print("")
    print(f"selecting file: {self.file_name}")
    self.obio.select_cfg_file(self.file_name)
    print("")


