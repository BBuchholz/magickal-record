"""
TODO: IMPLEMENT TODO items below 
COPIED VERBATIM FROM op_imp_obo.py


DONE: op_imp_obo.py should be copied to create 
op_mf_imp_obo.py -> Op Multi Filtered 
Imported Obsidian, 

DONE: can create a new version 
of method obo.get_src_md_files(self) to 
be obo.get_mf_src_md_files(self) 

  FIRST DONE: SetFileNameFilterOp needs to be 
  changed to call AddFileNameFilterOp and should 
  add to a separate list in OBIO to avoid breaking 
  currently working code (should have a separate 
  list of filters internally, we can refactor later,
  deprecating the single filter version, 
  if the new version becomes the exclusive one)

TODO: should have option to clear working directory
called ClearWorkingDirectoryOp

TODO: and can pass those filters to op_mf_imp_obo.py 
using a new method op_mf_imp_obo.add_filters(filters), 

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
from op_add_filter import AddFileNameFilterOp
from op_copy_files import CopyFilesOp
from op_clear_wd import ClearWorkingDirectoryOp
from op_clear_ff import ClearFileFilters
from op_gather_sl import GatherSeedLinks

class MultiFilterImportObsidianFilesMenu(SubMenu):
  def __init__(self, obio: ObsidIO):
    self.obio = obio
    self.obio.file_filters = []

  def key(self):
    return "imp"
  
  def exit_after_selection(self):
    return False

  def desc(self):
    return "Import Obsidian Files"

  def get_ops(self):
    ops = []
    ops.append(AddFileNameFilterOp(self.obio))
    ops.append(ClearWorkingDirectoryOp(self.obio))
    ops.append(GatherSeedLinks(self.obio))
    ops.append(ClearFileFilters(self.obio))
    if len(self.obio.file_filters) > 0 :
      filtered = self.obio.get_mf_src_md_files() 
      total = len(filtered)
      count = 0
      if total < 100:
        print("the following files will be copied ")
        print("from the vault to the obsidio folder ")
        print("if you execute the copy command")
        for file in filtered:
          count += 1
          print(f"File {count} of {total}: {file}")
        ops.append(CopyFilesOp(self.obio, filtered))
      else:
        print("too many files selected, limit is 99")
        print("please change filter and try again")
    return ops
  

if __name__ == "__main__":
  tcfg = NwdTestConfig()
  obio = ObsidIO(tcfg)
  obio.load_vaults(tcfg.test_vault_config_file())
  main = MultiFilterImportObsidianFilesMenu(obio)
  main.show_menu()