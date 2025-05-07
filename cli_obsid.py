from obsidio import ObsidIO
from cfg import NwdTestConfig
from menus import SubMenu
from op_imp_obo import ImportObsidianFilesMenu
from cli_load_vaults import LoadVaultsMenu
from op_dsp_vaults import DisplayVaultsOp
from op_create_aud_links import CreateAuditLinkagesFile
from op_create_myr_aud import CreateMyrkisAuditFile

class ObsidMenu(SubMenu):
  def __init__(self, config):
    self.obio = ObsidIO(config)

  def key(self):
    return "obo"
  
  def desc(self):
    return "Obsidian Integration Menu"
  
  def get_ops(self):
    ops = []
    ops.append(DisplayVaultsOp(self.obio))
    ops.append(LoadVaultsMenu(self.obio))
    ops.append(ImportObsidianFilesMenu(self.obio))
    ops.append(CreateAuditLinkagesFile(self.obio))
    ops.append(CreateMyrkisAuditFile(self.obio))
    # TODO: CREATE OP HERE to use audit_summary_report 
    # file from config and to create an MD file with a 
    # link to every file that has those myrkis anywhere 
    # in their name (can then copy this back into 
    # obsidian manually and it becomes a working list 
    # to cross reference all related files that have 
    # anything to do with a given card set as loaded and 
    # used to generate the audit summary report 
    # in the cart menu) SEARCH NAMES LIKE IMPORT DOES ABOVE
    return ops
  
if __name__ == "__main__":
  tcfg = NwdTestConfig()
  main = ObsidMenu(tcfg)
  main.show_menu()