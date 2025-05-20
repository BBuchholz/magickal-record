from cfg import Config
from os import path
from obsidio import ObsidIO

class MyrkiRegistry:
  def __init__(self, cfg: Config):
    self.myrkis = []
    self.obio = ObsidIO(cfg)

  def load(self, myrkis_to_look_for):
    # TODO: mirror CartRegistry.load()
    msg = "attempting to load MyrkiRegistry from "
    msg += "stored configuation"
    print(msg)
    # check if stored configuration exists
    verified_file = self.obio.cfg.verified_vault_file()
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
      msg += "cartographer file is stored using the "
      msg += "store option in the cart ops menu"
      print(msg)
      