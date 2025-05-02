from cfg import Config, NwdTestConfig
from obsidio import ObsidIO
from chronio import ChronIO
from op_gen_test_files import GenerateTestFiles
from menus import SubMenu

class TestMenu(SubMenu):
  def __init__(
      self,
      cfg: Config,
      obio: ObsidIO,
      chron: ChronIO):
    self.cfg = cfg
    self.obio = obio
    self.chron = chron

  def key(self):
    return "tst"
  
  def desc(self):
    return "Auxillary Test Operations Menu"
  
  def get_ops(self):
    ops = []
    ops.append(GenerateTestFiles(
      self.cfg,
      self.obio,
      self.chron))
    return ops
    
if __name__ == "__main__":
  tcfg = NwdTestConfig()
  obo = ObsidIO(tcfg)
  chron = ChronIO()
  main = TestMenu(tcfg, obo, chron)
  main.show_menu()