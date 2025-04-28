from files import get_md_files

class ObsidIO():
  def __init__(self, cfg):
    self._cfg = cfg
    self._loaded_vaults = []

  @property
  def loaded_vaults(self):
    return self._loaded_vaults
  
  def load_vaults(self, cfg_file):
    pass

  def get_cfg_files(self):
    folder = self._cfg.obsidio_cfg_folder
    cfg_files = get_md_files(folder)
    return cfg_files

