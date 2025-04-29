from obsidio import ObsidIO
from cfg import NwdTestConfig
from menus import SubMenu
from op_set_filter import SetFileNameFilterOp

class ImportObsidianFilesMenu(SubMenu):
  def __init__(self, obio):
    self.obio = obio
    self.obio.file_filter = ""

  def key(self):
    return "imp"
  
  def exit_after_selection(self):
    return False

  def desc(self):
    return "Import Obsidian Files"

  def get_ops(self):
    ops = []
    # TODO: add set filter op here, 
    # should be available in all menus, 
    # even if its already set, so it 
    # can be changed
    ops.append(SetFileNameFilterOp(self.obio))
    if len(self.obio.file_filter) > 2 :
      filtered = self.obio.get_file_names()
      if len(filtered) < 100:
        # TODO: add filtered filenames here
        print("add files goes here")
        # TODO: mimic cli_select_cart_file.py
      else:
        print("too many files selected, limit is 99")
        print("please change filter and try again")
    return ops
  

if __name__ == "__main__":
  tcfg = NwdTestConfig()
  obio = ObsidIO(tcfg)
  main = ImportObsidianFilesMenu(obio)
  main.show_menu()