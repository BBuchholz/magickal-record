from files import (
  get_md_files,
  get_lines_from,
  get_filtered_md_files,
  get_multi_filter_md_files,
  get_prefixed_md_files,
  ensure_folder,
)
from os import path
from cfg import Config

class ObsidIO():
  def __init__(self, cfg: Config):
    self._cfg = cfg
    self._loaded_vault = None
    self.file_filter = ""

  @property
  def loaded_vault(self):
    return self._loaded_vault
  
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

  def fnames_to_wikilinks(self, fnames):
    wikilinks = []
    for fname in fnames:
      if fname.endswith(".md"):
        fname = fname.removesuffix(".md")
      link = "[[" + fname + "]]"
      if link not in wikilinks:
        wikilinks.append(link)
    return wikilinks

  def process_line(self, line):
    if line.lower().startswith("vault: "):
      vault_address = line[7:]
      vault_address = path.expanduser(vault_address)
      if path.exists(vault_address):
        self._loaded_vault = vault_address
        print(f"vault address loaded for: {vault_address}")
      else:
        print(f"vault address: {vault_address} not found...")
        print("skipping vault address, loading aborted")
  
  def load_vaults(self, md_file):
    print("currently only supports one loaded vault at a time")
    print("multiple lines defined as vault addresses will ")
    print("overwrite each other and only one will be loaded")
    file_path = self._cfg.get_config_file(md_file)
    lines = get_lines_from(file_path)
    for line in lines:
      self.process_line(line)

  def get_cfg_files(self):
    folder = self._cfg.config_folder()
    cfg_files = get_md_files(folder, "Config")
    return cfg_files

  def get_src_md_files(self):
    folder = self._loaded_vault
    md_files = []
    if path.exists(folder):
      md_files = get_filtered_md_files(folder, self.file_filter)
    return md_files
  
  def get_src_md_fnames_containing(self, myrkis):
    folder = self._loaded_vault
    md_files = []
    if path.exists(folder):
      md_files = get_multi_filter_md_files(folder, myrkis)
    return md_files
    
  def get_src_md_fnames_starting_with(self, prefixes, include_dash=False):
    folder = self._loaded_vault
    md_files = []
    if self._loaded_vault:
      if path.exists(folder):
        md_files = get_prefixed_md_files(folder, prefixes, include_dash)
    else:
      print("no vault loaded, aborting...")
    return md_files
  
  def obsidio_folder(self):
    return self._cfg.obsidio_folder()
  
  def create_vault_config(self, vault_name, vault_path):
    pass

  def ensure_folder(self, folder_path):
    ensure_folder(folder_path)
