from files import (
  get_md_files,
  get_files,
  get_lines_from,
  get_filtered_md_files,
  get_multi_filter_md_files,
  get_prefixed_md_files,
  ensure_folder,
  write_lines,
  get_path_in_folder,
  path_exists,
)
from myr_file import MyrFile
from os import path
from cetar import CetAR
from cfg import Config
from chronio import ChronIO

class ObsidIO():
  """
  A class to handle Obsidian Input and Output

  Attributes:
    file_filter (str): used for single filter selections
    file_filters (list): used for Multi Filter selections
  """
  def __init__(self, cfg: Config):
    self._cfg = cfg
    self._loaded_vaults = []
    self._last_loaded_vault = None
    self.file_filter = ""
    self.file_filters = []

  @property
  def last_loaded_vault(self):
    return self._last_loaded_vault
  
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
        self._loaded_vaults.append(vault_address)
        print(f"vault address loaded for: {vault_address}")
        self._last_loaded_vault = vault_address
      else:
        print(f"vault address: {vault_address} not found...")
        print("skipping vault address, loading aborted")
  
  def load_vaults(self, md_file):
    print("multiple loaded vaults are supported")
    print("last loaded vault will be default")
    file_path = self._cfg.get_config_file(md_file)
    lines = get_lines_from(file_path)
    for line in lines:
      self.process_line(line)
    print(f"last loaded vault set to: {self._last_loaded_vault}")


  def get_cfg_files(self):
    folder = self._cfg.config_folder()
    cfg_files = get_md_files(folder, "Config")
    return cfg_files
  
  def list_obsidio_files(self):
    files_in_obsidio_fldr = []
    files_in_obsidio_fldr = get_files(self._cfg.obsidio_folder())
    return files_in_obsidio_fldr

  def get_src_md_files(self):
    folder = self._last_loaded_vault
    md_files = []
    if folder is None:
      print("Obsidio._last_loaded_vault not set, please load a vault and try again")
    elif path.exists(folder):
      md_files = get_filtered_md_files(folder, self.file_filter)
    return md_files
  
  def get_mf_src_md_files(self):
    folder = self._last_loaded_vault
    md_files = []
    if path.exists(folder):
      md_files = get_multi_filter_md_files(folder, self.file_filters)
    return md_files
  
  def get_src_md_file_path(self, fname_without_suffix):
    fldr = ""
    if not self.last_loaded_vault:
      raise Exception("vault not loaded")
    else:
      fldr = self.last_loaded_vault
    fname = fname_without_suffix + ".md"
    f_path = path.join(fldr, fname)
    return f_path
  
  def get_obsidio_file_path(self, file_name):
    return self._cfg.get_obsidio_file(file_name)
  
  def get_src_md_fnames_containing(self, myrkis):
    folder = self._last_loaded_vault
    md_files = []
    if path.exists(folder):
      md_files = get_multi_filter_md_files(folder, myrkis)
    return md_files
    
  def get_src_md_fnames_starting_with(self, prefixes, include_dash=False):
    folder = self._last_loaded_vault
    md_files = []
    if self._last_loaded_vault:
      if path.exists(folder):
        md_files = get_prefixed_md_files(folder, prefixes, include_dash)
    else:
      print("no vault loaded, aborting...")
    return md_files
  
  def obsidio_folder(self):
    return self._cfg.obsidio_folder()
  
  def create_vault_config_file(self, vault_name, vault_path):
    mf = MyrFile()
    mf.lines.append("vault: " + vault_path)
    file_name = "Config_" + vault_name + ".md"
    file_path = self._cfg.get_config_file(file_name)
    write_lines(file_path, mf.lines, True)
    print(f"file written: {file_path}")
    return file_path
  
  def create_cetar_file(self, cetar: CetAR):
    # mimic method: create_vault_config_file(vault_name, vault_path)
    mf = MyrFile()
    mf.lines.append("NOT IMPLEMENTED YET")
    chronio = ChronIO()
    timestamp = chronio.get_suffix()
    file_name = "CetAR_" + cetar.short_name + "_" + timestamp + ".md"
    file_path = self.get_obsidio_file_path(file_name)
    while path_exists(file_path):
      timestamp = chronio.get_suffix(timestamp)
      file_name = "CetAR_" + cetar.short_name + "_" + timestamp + ".md"
      file_path = self.get_obsidio_file_path(file_name)
    write_lines(file_path, mf.lines, True)
    print(f"file written: {file_path}")
    raise Exception(f"Not Implemented: write to file {file_path}")
    

  def ensure_folder(self, folder_path):
    ensure_folder(folder_path)
