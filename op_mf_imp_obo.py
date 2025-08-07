"""
TODO: IMPLEMENT TODO items below 
COPIED VERBATIM FROM op_imp_obo.py


TODO: op_imp_obo.py should be copied to create 
op_mf_imp_obo.py -> Op Multi Filtered 
Imported Obsidian, 

TODO: can create a new version 
of method obo.get_src_md_files(self) to 
be obo.get__mf_src_md_files(self, filters) 

TODO: and can pass those filters to op_mf_imp_obo.py 
during __init__, 

TODO: those filters will be all 
the file names from the audit report, 


TODO: convert this part into reasoning 
for documentation -> in this way, the 
working directory, obsidio, 
will have all the current copies of those 
files to work from and that's what we can 
copy into the Cet folders without altering 
the original obsidian garden at all 
(Cet folders are git tracked so we can 
freely work on those without fear cuz they 
can be rolled back to a previously 
committed version if need be)


"""

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