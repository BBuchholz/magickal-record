from cfg import Config
from os import path
from obsidio import ObsidIO
from cartreg import CartRegistry

class MyrkiRegistry:
  def __init__(self, cfg: Config):
    self.myrkis = []
    self.obio = ObsidIO(cfg)
    self.cartrg = CartRegistry(cfg)

  def load(self):
    # TODO: CartRegistry.load()
    self.cartrg.load()
    if len(self.cartrg.carts) < 0:
      print("no carts loaded for CartRegistry")
      print("no MyrKiS to search for, aborting...")
      return
    msg = "attempting to load MyrkiRegistry from "
    msg += "stored configuation"
    print(msg)
    # check if stored configuration exists
    verified_file = self.obio._cfg.verified_vault_file()
    if path.exists(verified_file):
      print("verified file found")
      # TODO: mirror CartRegistry.load() but check 
      # Obsidio verified vault for any file in 
      # MYRKI-SUFFIX format and also any MYRKI files
      # without the SUFFIX appended (just storing
      # the names for future usage so we can easily
      # retrieve a list) 
    else:
      print("verified file not found")
      msg = "autoloading is disabled until a verified "
      msg += "vault file is stored using the store "
      msg += "option in the obsidio ops menu (obo)"
      print(msg)
      