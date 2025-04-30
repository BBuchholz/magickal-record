from files import (
  get_md_files,
  get_lines_from,
)
from os import path
from cfg import Config

class ObsidIO():
  def __init__(self, cfg: Config):
    self._cfg = cfg
    self._loaded_vaults = []

  @property
  def loaded_vaults(self):
    return self._loaded_vaults
  
  def select_file(self, md_file):
    file_path = self._cfg.get_obsidio_file(md_file)
    lines = get_lines_from(file_path)
    for line in lines:
      self.process_line(line)

  def select_cfg_file(self, md_file):
    file_path = self._cfg.get_config_file(md_file)
    lines = get_lines_from(file_path)
    success = False
    for line in lines:
      self.process_line(line)

  def process_line(self, line):
    if line.lower().startswith("vault: "):
      vault_address = line[7:]
      vault_address = path.expanduser(vault_address)
      if path.exists(vault_address):
        self._loaded_vaults.append(vault_address)
        print(f"vault address loaded for: {vault_address}")
      else:
        print(f"vault address: {vault_address} not found...")
        print("skipping vault address, loading aborted")
  
  def load_vaults(self, md_file):
    file_path = self._cfg.get_config_file(md_file)
    lines = get_lines_from(file_path)
    for line in lines:
      self.process_line(line)

  def get_cfg_files(self):
    folder = self._cfg.config_folder()
    cfg_files = get_md_files(folder, "Config")
    return cfg_files

