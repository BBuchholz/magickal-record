from obsidio import ObsidIO
from cfg import NwdTestConfig
from menus import SubMenu
from op_set_filter import SetFileNameFilterOp
from op_copy_files import CopyFilesOp

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
      filtered = self.obio.get_src_md_files() 
      if len(filtered) < 100:
        print("the following files will be copied ")
        print("from the vault to the obsidio folder ")
        print("if you execute the copy command")
        for file in filtered:
          print(f"File: {file}")
        ops.append(CopyFilesOp(self.obio, filtered))
      else:
        print("too many files selected, limit is 99")
        print("please change filter and try again")
    return ops
  

if __name__ == "__main__":
  tcfg = NwdTestConfig()
  obio = ObsidIO(tcfg)
  obio.load_vaults(tcfg.test_vault_config_file())
  main = ImportObsidianFilesMenu(obio)
  main.show_menu()