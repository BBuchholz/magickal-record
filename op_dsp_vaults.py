from obsidio import ObsidIO
from menus import LineOption
from cfg import NwdTestConfig

class DisplayVaultsOp(LineOption):
  def __init__(self, obio: ObsidIO):
    self.obio = obio

  def key(self):
    return "dsp"

  def desc(self):
    msg = "display vault locations "
    msg += "currently loaded into the "
    msg += "Obsidian IO Handler (obsidio)"
    return msg

  def run(self):
    print("")
    if self.obio.loaded_vault is None:
      print("no vault is currently loaded")
      print("please use the load vaults op")
      print("to load vaults from config files")
    else:
      print(self.obio.loaded_vault)


if __name__ == "__main__":
  tcfg = NwdTestConfig()
  obio = ObsidIO(tcfg)
  obio.load_vaults(tcfg.test_vault_config_file())
  main = DisplayVaultsOp(obio)
  main.run()
