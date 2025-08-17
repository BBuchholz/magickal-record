from obsidio import ObsidIO
from cfg import NwdTestConfig
from menus import LineOption

class ClearFileFilters(LineOption):
  def __init__(self, obio: ObsidIO):
    self.obio = obio
    self.filter = ""

  def key(self):
    return "clrff"
  
  def desc(self):
    return "Clear All Obsidian FileName Filters"

  def run(self):
    print("")
    print(f"current multi file filters: {self.obio.file_filters}")
    print(f"current single file filter: {self.obio.file_filter}")
    print("clearing filters...")
    self.obio.file_filters.clear()
    self.obio.file_filter = ""
    print("filters cleared.")
    print(f"current multi file filters: {self.obio.file_filters}")
    print(f"current single file filter: {self.obio.file_filter}")

if __name__ == "__main__":
  tcfg = NwdTestConfig()
  obio = ObsidIO(tcfg)
  obio.file_filter = "test"
  obio.file_filters.append("test2")
  obio.file_filters.append("test3")
  main = ClearFileFilters(obio)
  main.run()