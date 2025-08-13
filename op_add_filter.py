from obsidio import ObsidIO
from cfg import NwdTestConfig
from menus import LineOption

class AddFileNameFilterOp(LineOption):
  def __init__(self, obio: ObsidIO):
    self.obio = obio
    self.filter = ""

  def key(self):
    return "add"
  
  def desc(self):
    return "Add Obsidian FileName Filter"

  def run(self):
    print("")
    filter = input("enter filter: ")
    self.obio.file_filters.append(filter)
    print(f"current filters: {self.obio.file_filters}")

if __name__ == "__main__":
  tcfg = NwdTestConfig()
  obio = ObsidIO(tcfg)
  main = AddFileNameFilterOp(obio)
  main.run()