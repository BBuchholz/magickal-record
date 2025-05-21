from obsidio import ObsidIO
from cfg import NwdTestConfig
from menus import SubMenu
from op_imp_obo import ImportObsidianFilesMenu
from cli_load_vaults import LoadVaultsMenu
from op_dsp_vaults import DisplayVaultsOp
from op_create_aud_links import CreateAuditLinkagesFile
from op_create_myr_aud import CreateMyrkisAuditFile
from op_launch_vault_gui import LaunchVaultBrowserGUI
from op_str_ver_vlt import StoreLastLoadedVaultAsDefault

class ObsidMenu(SubMenu):
  def __init__(self, obio: ObsidIO):
    self.obio = obio

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
    ops.append(LaunchVaultBrowserGUI(self.obio))
    ops.append(StoreLastLoadedVaultAsDefault(self.obio))
    return ops
  
if __name__ == "__main__":
  tcfg = NwdTestConfig()
  obio = ObsidIO(tcfg)
  main = ObsidMenu(obio)
  main.show_menu()