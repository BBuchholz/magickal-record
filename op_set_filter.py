from obsidio import ObsidIO
from cfg import NwdTestConfig
from menus import LineOption

class SetFileNameFilterOp(LineOption):
  def __init__(self, obio):
    self.obio = obio
    self.filter = ""

  def key(self):
    return "set"
  
  def desc(self):
    return "Set Obsidian FileName Filter"

  def run(self):
    print("")
    filter = input("enter filter: ")
    self.obio.file_filter = filter
    print(f"filter set to {self.obio.file_filter}")

if __name__ == "__main__":
  tcfg = NwdTestConfig()
  obio = ObsidIO(tcfg)
  main = SetFileNameFilterOp(obio)
  main.run()