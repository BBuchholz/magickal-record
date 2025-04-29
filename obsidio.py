from files import (
  get_md_files,
  get_lines_from,
)

class ObsidIO():
  def __init__(self, cfg):
    self._cfg = cfg
    self._loaded_vaults = []

  @property
  def loaded_vaults(self):
    return self._loaded_vaults
  
  def load_vaults(self):
    for md_file in self.get_cfg_files():
      lines = get_lines_from(md_file)
      for line in lines:
        if line.lower().startswith("vault: "):
          vault_address = line[8:]
          self._loaded_vaults.append(vault_address)

  def get_cfg_files(self):
    folder = self._cfg.obsidio_cfg_folder
    cfg_files = get_md_files(folder)
    return cfg_files

