from obsidio import ObsidIO
from menus import LineOption
from cfg import NwdTestConfig

class DisplayVaultsOp(LineOption):
  def __init__(self, obio):
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
    vaults = self.obio.loaded_vaults
    if len(vaults) < 1:
      print("no vaults are currently loaded")
      print("please use the load vaults op")
      print("to load vaults from config files")
    else:
      for vault in vaults:
        print(vault)


if __name__ == "__main__":
  tcfg = NwdTestConfig()
  obio = ObsidIO(tcfg)
  obio.load_vaults(tcfg.test_vault_config_file)
  main = DisplayVaultsOp(obio)
  main.run()
