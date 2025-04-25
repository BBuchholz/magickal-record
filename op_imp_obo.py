from obsidio import ObsidIO
from cfg import TestingConfig
from menus import SubMenu

class ImportObsidianFilesMenu(SubMenu):
  def __init__(self, obio):
    self.obio = obio
    self.filter = ""

  def key(self):
    return "imp"
  
  def exit_after_selection(self):
    return True

  def desc(self):
    return "Import Obsidian Files"

  def get_ops(self):
    ops = []
    # TODO: add set filter op here, 
    # should be available in all menus, 
    # even if its already set, so it 
    # can be changed
    if len(self.filter) > 2 :
      filtered = self.obio.get_file_names(self.filter)
      if len(filtered) < 100:
        # TODO: add filtered filenames here
        print("add files goes here")
        # TODO: mimic cli_select_cart_file.py
      else:
        print("too many files selected, limit is 99")
        print("please change filter and try again")
    return ops
  

if __name__ == "__main__":
  tcfg = TestingConfig()
  obo = ObsidIO(tcfg)
  main = ImportObsidianFilesMenu(obo)
  main.show_menu()