from cfg import TestingConfig

class ObsidIO():
  def __init__(self, cfg):
    self._cfg = cfg
    self._loaded_vaults = []

  @property
  def loaded_vaults(self):
    return self._loaded_vaults
  
  def load_vaults(self, cfg_file):
    pass

